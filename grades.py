#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

class Grade(object):
	"""docstring for Grade"""
	_grade = 0 # TE REMOOOOVE !!!!!
	_coeff = 0
	def __init__(self, grade, coeff):
		super(Grade, self).__init__()
		self._grade = grade
		self._coeff = coeff

class GradeCalculator(object):
	"""docstring for GradeCalculator"""
	def __init__(self):
		super(GradeCalculator, self).__init__()
	def __init__(self, mainList):
		super(GradeCalculator, self).__init__()
		self._gradesSum = 0
		self._coeffsSum = 0
		if(len(mainList) > 0):
			# LIST [(gradei, coeffi), (...,...)]
			self._gradesSum  = sum([g*c for (g,c) in mainList])
			self._coeffsSum  = sum(zip(*mainList)[1])
	def addGrade(self, grade):
		self._coeffsSum += grade._coeff
		self._gradesSum += grade._grade*grade._coeff
	def getFinalGrade(self):
		if self._coeffsSum != 0:
			return self._gradesSum/self._coeffsSum
		else:
			return 0