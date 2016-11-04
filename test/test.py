#!/usr/bin/env python

# -*- coding: utf-8 -*-

""" Summarizes the next SBB connection between two stations using SBB OpenData API.
"""

import json
import argparse
import datetime
import dateutil.parser
import requests

from ansi import Colors


def reformat_time(timestring):
	""" Format time from ISO datetime string. """
	return dateutil.parser.parse(timestring).strftime('%H:%M')


parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help="Increase output verbosity.", action="store_true")
parser.add_argument('-f', '--depart', help="Departure station")
parser.add_argument('-t', '--dest', help="Destination station")
parser.add_argument('-w', '--when', help="Departure time (defaults to now).")
arguments = parser.parse_args()

print(arguments.depart, arguments.dest, arguments.when)

with open('test/sample.json', 'r') as fp:
	fahrplan = json.load(fp)

for conn in fahrplan['connections']:
	title = "Von {} Nach {}".format(conn['from']['station']['name'], conn['to']['station']['name'])
	print(Colors.BOLD.format(title))

	for section in conn['sections']:
		print("Mit {} von {} um {} nach {} ({} an: {}).".format(
			Colors.ERROR.format(section['journey']['name']), 
			section['departure']['station']['name'], 
			reformat_time(section['departure']['departure']), 
			section['journey']['to'],
			section['arrival']['station']['name'],
			reformat_time(section['arrival']['arrival']),
		))
