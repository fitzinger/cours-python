#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process weather forecast json files to plot the time evolution of temperature
"""

import urllib.request
import json
import matplotlib.pyplot as plt
import numpy as np
import sys

URL_PREFIX = "http://www.prevision-meteo.ch/services/json/"


class City():
    """Loads a json dictionary downloaded from city name
    and provide a method to search for day temperature"""

    def __init__(self, city_name):
        """Loads city json dict"""
        jsonfile_url = URL_PREFIX + city_name
        self.legend = city_name
        self.json = self._get_json(jsonfile_url)

    def _get_json(self, jsonfile_url):
        """Download json file from URL and return a python dict"""
        f = urllib.request.urlopen(jsonfile_url)  # open url
        json_dict = json.loads(f.read().decode('utf8'))
        if 'errors' in json_dict:
            error = json_dict['errors'][0]
            msg = "Error for {} (code: {})\n{}\n{}" \
                  .format(self.legend, error['code'], error['text'],
                          error['description'])
            sys.exit(msg)
        else:
            return json_dict

    def get_temperature(self, day_key):
        """store hour and temperature in numpy arrays for given day_key"""
        day = self.json[day_key]
        day_hd = day['hourly_data']  # point to hourly data
        tempe = [[int(hour[:-3]), data['TMP2m']] for hour, data in
                 day_hd.items()]  # Create a list of [hour, temperature]
        tempe.sort()  # Sort temperatures according to the hour of day
        # Create numpy array and transpose list of (hour, tempe)
        t = np.array(tempe).transpose()
        self.hour = t[0]
        self.temperature = t[1]


class Location(City):
    """Loads a json dictionary downloaded from geographic coordinates"""

    def __init__(self, lat, lng):

        jsonfile_url = "{}lat={}lng={}".format(URL_PREFIX, lat, lng)
        self.legend = "lat={}, lng={}".format(lat, lng)
        self.json = self._get_json(jsonfile_url)


def plot_day_temperature(*cities, day_number=0):
    """Plot temperature vs hour for an arbitrary number of cities at given
    day_number (0: today, 1: tomorrow, etc.)"""

    day_key = 'fcst_day_{}'.format(day_number)
    day = cities[0].json[day_key]

    fig = plt.figure()  # initialize figure
    title = "{} {}".format(day['day_long'], day['date'])
    fig.suptitle(title, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)  # initialize a plot area
    fig.subplots_adjust(top=0.85)
    ax.set_title('Evolution horaire')
    ax.set_xlabel('Temps [h]')
    ax.set_ylabel('Température [deg. C]')

    for city in cities:
        city.get_temperature(day_key)
        ax.plot(city.hour, city.temperature, label=city.legend)

    ax.legend()  # Add legend to plot
    plt.show()  # Ensure figure is shown


if __name__ == '__main__':
    # This block is not executed if this file is imported as a module

    # Instanciate City and Location objects:
    toulouse = City('Toulouse')
    paris = City('Paris')
    strasbourg = City('Strasbourg')
    trou_perdu = Location(lat=45.32, lng=10)
    # Plot temperature evolution of all these objects on the same graph
    plot_day_temperature(toulouse, paris, strasbourg, trou_perdu, day_number=0)
