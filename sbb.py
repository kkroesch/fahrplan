#!/usr/bin/env python3

# -*- coding: utf-8 -*-

""" Searches for station IDs using SBB OpenData API.
"""

import json
import argparse
import requests
import dateutil.parser

icons = {
    "train": "",
    "bus": "ﲞ",
    "tram": "館",
    "pedestrian": "",
    None: "ﴤ",
}

def reformat_time(timestring):
    """ Format time from ISO datetime string. """
    return dateutil.parser.parse(timestring).strftime('%H:%M')


class Colors:
    """ Colors for console putput as ANSI code.
        Example usage:
            exit(Colors.ERROR.format('Error: API token not given.'))
            print(Colors.OKGREEN.format("All went fine.")
    """
    HEADER = '\033[95m{}\033[0m'
    OKBLUE = '\033[94m{}\033[0m'
    OKGREEN = '\033[92m{}\033[0m'
    ERROR = '\033[91m{}\033[0m'
    WARNING = '\033[93m{}\033[0m'
    FAIL = '\033[91m{}\033[0m'
    BOLD = '\033[1m{}\033[0m'
    UNDERLINE = '\033[4m{}\033[0m'
    ENDC = '\033[0m'


class FindAction(argparse.Action):
    """
        Find a station ID for given (partial) name.
    """
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(FindAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        req = requests.get('http://transport.opendata.ch/v1/locations?query=' + values)
        station_list = req.json()

        for station in station_list['stations']:
            station['id'] = (station['id'] or "-"*7)
            print(f"{icons[station['icon']]} {station['id']}  {station['name']}")


class ConnectAction(argparse.Action):
    """
        Retrieves the connection for two given station IDs.
    """
    def __init__(self, option_strings, dest, nargs='+', **kwargs):
        super(ConnectAction, self).__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        req = requests.get('http://transport.opendata.ch/v1/connections?from={}&to={}&limit=1'.format(values[0], values[1]))
        fahrplan = req.json()

        for conn in fahrplan['connections']:
            title = "Von {} Nach {}".format(conn['from']['station']['name'], conn['to']['station']['name'])
            print(Colors.BOLD.format(title))

            for section in conn['sections']:
                if section['journey'] is None:
                    continue

                print("Mit {} von {} um {} nach {} ({} an: {}).".format(
                    Colors.ERROR.format(section['journey']['name']), 
                    section['departure']['station']['name'], 
                    reformat_time(section['departure']['departure']), 
                    section['journey']['to'],
                    section['arrival']['station']['name'],
                    reformat_time(section['arrival']['arrival']),
                ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrieve SBB connections.')
    parser.add_argument('-v', '--verbose', 
            help="Increase output verbosity.", action="store_true")

    subparsers = parser.add_subparsers(title='sub-commands')
    parser_find = subparsers.add_parser('id', help='Find station ID for (partial) name.')
    parser_find.add_argument('part', type=str, action=FindAction, help='A station name.')

    parser_connect = subparsers.add_parser('conn', help='Find connection between two station IDs.')
    parser_connect.add_argument('stations', action=ConnectAction, nargs='+', help="Waypoints")
    parser_connect.add_argument('-w', '--when', help="Departure time (defaults to now).")

    arguments = parser.parse_args()
