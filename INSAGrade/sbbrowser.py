#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,inspect
sys.path.insert(0,'..')
from basebrowser import BaseBrowser
from bs4 import BeautifulSoup

# Retrieves departments stats from the school's website
class SubjectsBrowser(BaseBrowser):
	# Parse html to get subjects lists
	def resultFromHtml(self, result):
		data = []
		soup = BeautifulSoup(result)
		table = soup.find('table', attrs={'class':'listing'})
		rows = table.find_all('tr')
		for row in rows:
			cols = row.find_all('td')
			if len(cols) != 0: # No empty columns.
				cols = [ele for ele in [cols[0], cols[2]]] # Filtering columns
				cols = [ele.text.strip() for ele in cols] # Gets text, and strips it
				cols = [ele.encode('ascii') for ele in cols] # Encoding columns (to string)
				data.append([ele for ele in [cols[0], cols[1]] if ele]) # No empty elements.
		return tuple(data)