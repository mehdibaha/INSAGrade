#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sbbrowser import SubjectsBrowser
from grades import GradeCalculator, Grade

# Command line tool to calculate your grades
myGradeCalculator = GradeCalculator()
mySubjectsBrowser = SubjectsBrowser()

try:
	subjects = mySubjectsBrowser.getSubjects()
	for s in subjects:
		subjectName = s[0]
		subjectCoeff = float(s[1])
		while True:
			try:
				subjectGrade = float(raw_input(subjectName + "? "))
			except ValueError:
				print("Wa baraka")
				continue
			break
		newGrade = Grade(subjectGrade, subjectCoeff)
		myGradeCalculator.addGrade(newGrade)
	print "Your grade : " + str(myGradeCalculator.getFinalGrade())
except AttributeError:
	print "Wrong username & password."