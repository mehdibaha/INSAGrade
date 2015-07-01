#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from statsbrowser import StatsBrowser
import matplotlib.pyplot as plt

##############
#DATA#
##############
# Stats for ventilation PC

targetURL = 'https://planete.insa-lyon.fr/uPortal/f/scol/normal/render.uP?pCt=scolarix-portlet.u22l1n13&pP_action=ventilation-pc'
username  = "embaha"
password  = "local22setting23"

statsBrowser = StatsBrowser()
statsBrowser.setTargetURL(targetURL)
statsBrowser.setUserAndPass(username, password)
statsVentil = zip(*statsBrowser.getResult())

# Sum of students
sumStudents = sum(statsVentil[0])

# Stats from Maurincomme
statsMaurin = []
subjects = []
for line in open("maur.txt", "r"):
    _list = line.split(" ")
    statsMaurin.append(int(float(_list[1].replace("\n", "")))*sumStudents/100) 
    subjects.append(_list[0])
##############

##############
#PLOTTING#
##############
fig = plt.figure()
ax = fig.add_subplot(111)

# Initial values
N = len(statsMaurin)
width = 0.35
ind = np.arange(N)*1.4
ys1 = statsVentil[0]
ys2 = statsVentil[1]
ys3 = statsMaurin

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

xTickMarks = subjects
ax.set_xticks(ind+2*width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)
plt.legend( (rect1[0], rect2[0], rect3[0]), ('1er Voeu', '2e Voeu', 'Disponibles') )

# Drawing, saving, shipping.
plt.show()
fig.savefig("figure1.png", dpi=300)