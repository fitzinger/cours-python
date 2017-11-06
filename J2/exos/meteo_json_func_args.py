#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process a weather forecast json file to plot the time evolution of temperature
of a given day in a given city
"""

import argparse
import urllib.request
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def get_city_json(city_name):
    """Return a meteo json dictionary corresponding to city"""

    jsonfile_url = "http://www.prevision-meteo.ch/services/json/"\
                   + city_name
    f = urllib.request.urlopen(jsonfile_url)  # open url
    city_json = json.loads(f.read().decode('utf8'))
    if 'errors' in city_json:
        print("{} n'existe pas dans la base. Essayez un autre nom."
              .format(city_name))
        return None
    else:
        return city_json


def plot_day_tempe(city_json, day_key):
    """Plot Temperature vs hour from a json dictionary for a given day_key"""

    city_name = city_json['city_info']['name']
    day = city_json[day_key]
    day_hd = day['hourly_data']  # point to hourly data

    # Get tempe = [[h1, T1], [h2, T2], ...] list
    # where h1 is the time in hour and T2 is the temperature in deg. C
    tempe = []
    for hour, data in day_hd.items():
        # get first part of time in "00H00" format and remove "H00"
        # get temperature at 2m above ground 'TMP2m'
        tempe.append([int(hour[:-3]), data['TMP2m']])
    # Alternative form using list comprehension:
    # tempe = [[int(hour[:-3]), data['TMP2m']] for hour, data in day_hd.iteritems()]

    tempe.sort()  # Sort temperatures according to the hour of day
    t = np.array(tempe).transpose()  # Transpose list of (hour, tempe)

    # Plot T = T(hour)
    fig = plt.figure()  # initialise figure
    title = "{} {} à {}".format(day['day_long'], day['date'], city_name)
    fig.suptitle(title, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)  # initialise a plot area
    fig.subplots_adjust(top=0.85)
    ax.set_title('Evolution horaire')
    ax.set_xlabel('Temps [h]')
    ax.set_ylabel('Température [deg. C]')

    ax.plot(t[0], t[1])  # plot t[1] (tempe) as a function of t[0] (hour)

    # Add meteo icon to plot
    icon = urllib.request.urlopen(day['icon_big'])  # Open weather icon

    axicon = fig.add_axes([0.8, 0.8, 0.15, 0.15])
    img = mpimg.imread(icon)  # initialise image
    axicon.set_xticks([])  # Remove axes ticks
    axicon.set_yticks([])
    axicon.imshow(img)  # trigger the image show
    plt.show()  # trigger the figure show


def do_argparse():
    """Handle command-line arguments"""

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-d', '--day', metavar='INTEGER', default=0, type=int,
                        help='day for the weather forecast (0 to 4)')
    parser.add_argument('villes', metavar='STRING', nargs='*',
                        help='city for which to get the weather forecast')
    return parser.parse_args()

if __name__ == '__main__':
    # This block is not executed if this file is imported as a module
    args = do_argparse()
    if args.villes:
        cities = [get_city_json(c) for c in args.villes if c]
    else:
        city = None
        while city is None:  # Infinite loop to handle city name input
            city = get_city_json(input("Entrer la ville :\n"))
        cities = [city]

    for city_json in cities:
        plot_day_tempe(city_json, 'fcst_day_' + str(args.day))  # plot day temperature evolution
