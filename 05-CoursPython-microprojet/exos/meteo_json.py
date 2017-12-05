#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process a weather forecast json file to plot the time evolution of today's
temperature in Strasbourg
"""

import urllib.request, urllib.error, urllib.parse
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

jsonfile_url = "http://www.prevision-meteo.ch/services/json/Strasbourg"

f = urllib.request.urlopen(jsonfile_url)  # open url
json = json.loads(f.read().decode('utf8'))  # Read JSON file

day = json['fcst_day_0']  # point the current day data
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
title = "{} {}".format(day['day_long'], day['date'])
fig.suptitle(title, fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)  # initialise a plot area
fig.subplots_adjust(top=0.85)
ax.set_title('Day temperature')
ax.set_xlabel('Time [h]')
ax.set_ylabel('Temperature [deg. C]')

ax.plot(t[0], t[1])  # plot t[1] (tempe) as a function of t[0] (hour)

# Add meteo icon to plot
icon = urllib.request.urlopen(day['icon_big'])  # Open weather icon

axicon = fig.add_axes([0.8, 0.8, 0.15, 0.15])
img = mpimg.imread(icon)  # initialise image
axicon.set_xticks([])  # Remove axes ticks
axicon.set_yticks([])
axicon.imshow(img)  # trigger the image show

plt.show()
