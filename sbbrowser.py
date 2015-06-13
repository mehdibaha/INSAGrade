#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
from getpass import getpass

class SubjectsBrowser(object):
	"""docstring for SubjectsBrowser"""

	def __init__(self, username, password):
		super(SubjectsBrowser, self).__init__()
		self._subjects = ()
		self._loginURL = 'https://login.insa-lyon.fr/cas/login'
		self._subjectsURL = 'http://cipcnet.insa-lyon.fr/scol/cours_eleve'
		self._browser = mechanize.Browser()
		self._username = username
		self._password = password

	def login(self):
		self._browser.open(self._loginURL)
		self._browser.select_form(nr=0)
		self._browser.form['username'] = self._username
		self._browser.form['password'] = self._password
		self._browser.submit()

	def listFromHtml(self, result):
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

	def retrieveSubjects(self):
		self.login()
		self._browser.open(self._subjectsURL)
		result = self._browser.response().read().decode('ascii', 'ignore') # Decoding result (to unicode)
		self._subjects = self.listFromHtml(result)

	def getSubjects(self):
		self.retrieveSubjects()
		return self._subjects