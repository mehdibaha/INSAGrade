#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mechanize
from bs4 import BeautifulSoup

loginURL = 'https://login.insa-lyon.fr/cas/login'

# Base class for retrieving info from website
class BaseBrowser(object):
    def __init__(self):
        self._subjects = ()
        self._loginURL = loginURL
        self._browser = mechanize.Browser()
        self._browser.set_handle_robots(False)

    # Sets loginURL and finalURL
    def setTargetURL(self, targetURL):
        self._targetURL = targetURL

    # Sets username and password to login
    def setUserAndPass(self, username, password):
        self._username = username
        self._password = password

    # Login with username and password to website
    def login(self):
        self._browser.open(self._loginURL)
        self._browser.select_form(nr=0)
        self._browser.form['username'] = self._username
        self._browser.form['password'] = self._password
        self._browser.submit()

    # Login, browse, then gets result
    def getResult(self):
        self.login()
        self._browser.open(self._targetURL)
        result = self._browser.response().read().decode('ascii', 'ignore') # Decoding result (to unicode)
        return self.resultFromHtml(result)

    # Parse html to get result
    def resultFromHtml(self, result):
        raise NotImplementedError("resultFromHtml() in BaseBrowser is not implemented")