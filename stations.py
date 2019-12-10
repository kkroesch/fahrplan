#!/usr/bin/env python3

# -*- coding: utf-8 -*-

""" Searches for station IDs using SBB OpenData API.
"""

import json
import argparse
import requests

icons = {
	"train": "",
	"bus": "ﲞ",
	"tram": "館",
	"pedestrian": "",
	None: "ﴤ",
}

parser = argparse.ArgumentParser()
parser.add_argument('station', type=str)
parser.add_argument('-v', '--verbose', help="Increase output verbosity.", action="store_true")
arguments = parser.parse_args()

req = requests.get('http://transport.opendata.ch/v1/locations?query=' + arguments.station)
station_list = req.json()

for station in station_list['stations']:
	print(f"{icons[station['icon']]} {station['id']}  {station['name']}")
