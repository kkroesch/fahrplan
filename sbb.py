#!/usr/bin/env python3

# -*- coding: utf-8 -*-

""" Summarizes the next SBB connection between two stations using SBB OpenData API.
"""

import json
import argparse
import datetime
import dateutil.parser
import requests

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


def reformat_time(timestring):
	""" Format time from ISO datetime string. """
	return dateutil.parser.parse(timestring).strftime('%H:%M')


parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help="Increase output verbosity.", action="store_true")
parser.add_argument('depart', help="Departure station")
parser.add_argument('dest', help="Destination station")
parser.add_argument('-w', '--when', help="Departure time (defaults to now).")
arguments = parser.parse_args()

req = requests.get('http://transport.opendata.ch/v1/connections?from={}&to={}&limit=1'.format(arguments.depart, arguments.dest))
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
