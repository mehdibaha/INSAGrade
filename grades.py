#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

# Calculates grade either by adding the Grade object one by one,
# or by giving a list of the form : [(grade0, coeff0), (...,...)]
class Grade(object):
	"""docstring for Grade"""
	def __init__(self, grade, coeff):
		super(Grade, self).__init__()
		self._grade = grade
		self._coeff = coeff

class GradeCalculator(object):
	"""docstring for GradeCalculator"""
	def __init__(self):
		super(GradeCalculator, self).__init__()
	def __init__(self, gradesList):
		super(GradeCalculator, self).__init__()
		self._gradesSum = 0
		self._coeffsSum = 0
		if(len(gradesList) > 0):
			self._gradesSum  = sum([g*c for (g,c) in gradesList])
			self._coeffsSum  = sum(zip(*gradesList)[1])
	def addGrade(self, grade):
		self._coeffsSum += grade._coeff
		self._gradesSum += grade._grade*grade._coeff
	def getFinalGrade(self):
		if self._coeffsSum != 0:
			return self._gradesSum/self._coeffsSum
		else:
			return 0