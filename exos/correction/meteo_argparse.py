#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process weather forecast json files to plot the time evolution of temperature
"""

import meteo_city as mc
import argparse

URL_PREFIX = "http://www.prevision-meteo.ch/services/json/"


def do_argparse():
    """Handle command-line arguments"""

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-d', '--day', metavar='INTEGER', default=0, type=int,
                        help='day for the weather forecast (0 to 4)')
    parser.add_argument('city', metavar='STRING', nargs='*',
                        help='city for which to get the weather forecast')
    return parser.parse_args()

if __name__ == '__main__':
    # This block is not executed if this file is imported as a module
    args = do_argparse()

    if args.city:
        cities = [mc.City(city_name) for city_name in args.city]
    else:
        city_name = input("Enter city:\n")
        cities = (mc.City(city_name),)

    mc.plot_day_temperature(*cities, day_number=args.day)
