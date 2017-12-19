#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process weather forecast json files to plot the time evolution of temperature
"""

import urllib.request
import json
import matplotlib.pyplot as plt
import sys

URL_PREFIX = "http://www.prevision-meteo.ch/services/json/"


class City():
    """Loads a json dictionary downloaded from city name
    and provide a method to search for day temperature"""

    def __init__(self, city_name):
        """Loads city json dict"""
        # TODO: From city name, build jsonfile URL
        # TODO: Call _get_json() to store city dictionary
        # --- Your code here ---

        self.legend = city_name

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
        """return hour and temperature as numpy arrays for given day_key"""
        # TODO: From day_key ('fcst_day_X'), extract time and temperature data
        # to build the two 1D numpy arrays self.hour and self.temperature
        # --- Your code here ---

        pass


def plot_day_temperature(*cities, day_number=0):
    """Plot temperature vs hour for an arbitrary number of cities at given
    day_number (0: today, 1: tomorrow, etc.)"""

    fig = plt.figure()  # initialize figure

    # TODO: Build a day_key string from day_number in order to get day
    # dictionary
    # --- Your code here ---

    # TODO: Uncomment above when the above is ready
    # day = cities[0].json[day_key]
    # title = "{} {}".format(day['day_long'], day['date'])
    # fig.suptitle(title, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)  # initialize a plot area
    fig.subplots_adjust(top=0.85)
    ax.set_title('Evolution horaire')
    ax.set_xlabel('Temps [h]')
    ax.set_ylabel('Température [deg. C]')

    # TODO: loop over cities in order to:
    # 1. get hour and temperature for given city
    # 2. plot hour and temperature on ax for given city
    #    (use fonction ax.plot() with "label=" argument)
    # --- Your code here ---

    ax.legend()  # Add legend to plot
    plt.show()  # Ensure figure is shown


if __name__ == '__main__':
    # This block is not executed if this file is imported as a module

    # Instanciate City object:
    toulouse = City('Toulouse')
    paris = City('Paris')
    strasbourg = City('Strasbourg')
    # Plot temperature evolution of all these objects on the same graph
    plot_day_temperature(toulouse, paris, strasbourg, day_number=0)
