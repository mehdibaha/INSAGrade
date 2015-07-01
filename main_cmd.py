#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sbbrowser import SubjectsBrowser
from grades import GradeCalculator, Grade

# Command line tool to calculate your grades

subjectsBrowser = SubjectsBrowser()
subjectsBrowser.setUserAndPass(raw_input("Username? "), raw_input("Password? "))
subjects = subjectsBrowser.getSubjects()

gradeCalculator = GradeCalculator()

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
	gradeCalculator.addGrade(Grade(subjectGrade, subjectCoeff))
print "Your grade : " + str(gradeCalculator.getFinalGrade())