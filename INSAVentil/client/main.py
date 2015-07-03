#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from statsbrowser import StatsBrowser
import matplotlib.pyplot as plt
import urllib2, urllib, base64
import datetime, time

# Parse stats from Official Note from School about available seats in each departments
def getMaurin():
    statsMaurin = []
    subjects = []
    for line in open("maur.txt", "r"):
        _list = line.split(" ")
        statsMaurin.append(float(_list[1].replace("\n", "")))
        subjects.append(_list[0])
    return subjects, statsMaurin

# Process said stats with sum of students taken into account
def processMaurin(statsMaurin, sumStudents):
    return [int(s*sumStudents/100) for s in statsMaurin]

def updateFigure(statsVentil, statsMaurin):
    ys1 = statsVentil[0] # 1st vow
    ys2 = statsVentil[1] # 2nd vow
    ys3 = processMaurin(statsMaurin, sum(statsVentil[0])) # Places available

    # Initial values for plotting
    N = len(statsMaurin)
    width = 0.35
    ind = np.arange(N)*1.4

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Drawing bars
    rect1 = ax.bar(ind, ys1, width, color="#f1595f", alpha=1)
    rect2 = ax.bar(ind+width, ys2, width, color="#f1595f", alpha=0.5)
    rect3 = ax.bar(ind+2*width, ys3, width, color="#599ad3", alpha=1)
    # Plot limits
    ax.set_xlim(-width, len(ind)*1.4)
    ax.set_ylim([0, 140])
    # Title, labels, tickmarks
    ax.set_title('Places distribution in INSA departments')
    ax.set_ylabel('No of Places')
    # TickMarks
    xTickMarks = subjects
    ax.set_xticks(ind+2*width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)
    # Drawing, saving, shipping.
    plt.legend( (rect1[0], rect2[0], rect3[0]), ('1st Vow', '2nd Vow', 'Available') )
    figTime = str(int(time.time()))
    fig.savefig("figure_" + figTime + ".png", dpi=100)
    plt.close(fig)
    return figTime

# Encode image and send it to php server
def sendImage(figTime, key):
    with open("figure_" + figTime + ".png", "rb") as image_file:
        figure = base64.b64encode(image_file.read())
    data = urllib.urlencode({'API_KEY' : key, 'image' : figure, 'time' : str(int(time.time()))})
    req = urllib2.Request(apiURL, data)
    urllib2.urlopen(req)

# Check for data and send it to server if it's new
def periodicTask(lastsStats, statsMaurin, key):
    statsVentil = zip(*statsBrowser.getResult())
    if(lastStats != statsVentil):
        print "Begin drawing at " + str(datetime.datetime.now())
        figTime = updateFigure(statsVentil, statsMaurin)
        sendImage(figTime, key)
        print "Send drawing at " + str(datetime.datetime.now())
        print ""
    return statsVentil

# Init everythang
targetURL = 'https://planete.insa-lyon.fr/uPortal/f/scol/normal/render.uP?pCt=scolarix-portlet.u22l1n13&pP_action=ventilation-pc'
apiURL = "http://burnd.cles-facil.fr/insa/ventil.php"
username  = "USERNAME"
password  = "PASSWORD"
application_key = "API_KEY"
statsBrowser = StatsBrowser(targetURL, username, password)
subjects, statsMaurin = getMaurin()
lastStats = []

# Main loop
while True:
    lastStats = periodicTask(lastStats, statsMaurin, application_key)
    time.sleep(3)



