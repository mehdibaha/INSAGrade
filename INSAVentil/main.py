#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from statsbrowser import StatsBrowser
import matplotlib.pyplot as plt
import urllib2, urllib, base64
import datetime, time

# Stats from Maurincomme
def getMaurin():
    statsMaurin = []
    subjects = []
    for line in open("maur.txt", "r"):
        _list = line.split(" ")
        statsMaurin.append(float(_list[1].replace("\n", "")))
        subjects.append(_list[0])
    return subjects, statsMaurin

def processMaurin(statsMaurin, sumStudents):
    return [int(s*sumStudents/100) for s in statsMaurin]

def updateFigure(statsVentil, statsMaurin):
    ys1 = statsVentil[0]
    ys2 = statsVentil[1]
    ys3 = processMaurin(statsMaurin, sum(statsVentil[0]))

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
    ax.set_title('Distribution des places dans les departements')
    ax.set_ylabel('Nb de Places')
    # TickMarks
    xTickMarks = subjects
    ax.set_xticks(ind+2*width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=45, fontsize=10)
    # Drawing, saving, shipping.
    plt.legend( (rect1[0], rect2[0], rect3[0]), ('1er Voeu', '2e Voeu', 'Disponibles') )
    fig.savefig("figure.png", dpi=100)
    plt.close(fig)

def sendImage():
    with open("figure.png", "rb") as image_file:
        figure = base64.b64encode(image_file.read())
    data = urllib.urlencode({'image' : figure, 'time' : str(int(time.time()))})
    req = urllib2.Request(apiURL, data)
    urllib2.urlopen(req)

def periodicTask(lastsStats, statsMaurin):
    statsVentil = zip(*statsBrowser.getResult())
    if(lastStats != statsVentil):
        print "Begin drawing at " + str(datetime.datetime.now())
        updateFigure(statsVentil, statsMaurin)
        sendImage()
        print "Send drawing at " + str(datetime.datetime.now())
    else:
        print "RAS"
    return statsVentil

# Init everythang
targetURL = 'https://planete.insa-lyon.fr/uPortal/f/scol/normal/render.uP?pCt=scolarix-portlet.u22l1n13&pP_action=ventilation-pc'
apiURL = "http://burnd.cles-facil.fr/insa/ventil.php"
username  = raw_input("username? ")
password  = raw_input("password? ")
statsBrowser = StatsBrowser(targetURL, username, password)
subjects, statsMaurin = getMaurin()
lastStats = []

while True:
    lastStats = periodicTask(lastStats, statsMaurin)
    time.sleep(3)



