#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process weather forecast json files to plot the time evolution of temperature
"""

import meteo_heritage as mc
import argparse

URL_PREFIX = "https://www.prevision-meteo.ch/services/json/"


def get_args():
    """Handle command-line arguments"""

    parser = argparse.ArgumentParser(description='Plot temperature forecast.')
    parser.add_argument('-d', '--day', metavar='INTEGER', default=0, type=int,
                        help='day for the weather forecast (0 to 4)')
    parser.add_argument('--city', metavar='STRING', nargs='*',
                        help='city for which to get the weather forecast')
    parser.add_argument('--location', metavar='lat long', nargs=2,
                        help='latitude and longitude')
    parser.add_argument('--here', default=False, action='store_true',
                        help='use current location')
    return parser.parse_args()


if __name__ == '__main__':
    # This block is not executed if this file is imported as a module
    args = get_args()

    cities = []
    if args.city:
        cities = [mc.City(city_name) for city_name in args.city]

    if args.location:
        location = mc.Location(lat=args.location[0], lng=args.location[1])
        cities.append(location)

    if args.here:
        cities.append(mc.Here())

    if not cities:
        city_name = input("Enter city:\n")
        cities = (mc.City(city_name),)

    mc.plot_day_temperature(*cities, day_number=args.day)
