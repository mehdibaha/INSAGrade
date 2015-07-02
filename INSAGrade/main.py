#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
from sbbrowser import SubjectsBrowser
from grades import GradeCalculator, Grade
from functools import partial

targetURL = 'http://cipcnet.insa-lyon.fr/scol/cours_eleve'

# Main graphical interface
class INSAGrade(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, style=wx.DEFAULT_FRAME_STYLE,
            title="Login", size=(375, 625))

        self.panelLogin = PanelLogin(self)
        self.panelGrades  = PanelGrades(self)
        self.panelGrades.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panelLogin, 1, wx.EXPAND)
        self.sizer.Add(self.panelGrades, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.Centre()
        self.Show()

# Shows input to enter school's credentials
class PanelLogin(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.initUi()

    def initUi(self):
        center = 110
        st_w = wx.StaticText(self, pos=(center, 10), label='Enter your INSA credentials :')
        self.tc_u = wx.TextCtrl(self, pos=(center, 40), size=(150,25))
        self.tc_p = wx.TextCtrl(self, pos=(center, 70), size=(150, 25), style=wx.TE_PASSWORD)
        self.tc_u.SetHint("Your username")
        self.tc_p.SetHint("Your password")
        self.tc_u.SetLabelText("embaha")
        self.tc_p.SetLabelText("local22setting23")
        self.b_va = wx.Button(self, pos=(center, 110), label='Connect', size=(150, 25))
        self.b_va.Bind(wx.EVT_BUTTON, self.showPanelGrades)

    def showPanelGrades(self, event):
        self.parent.SetTitle("Grades")
        self.parent.panelLogin.Hide()
        self.parent.panelGrades.initUI(self.tc_u.GetValue(), self.tc_p.GetValue())
        self.parent.panelGrades.Show()
        self.parent.Layout()

# Shows list of subjects and grade inputs
class PanelGrades(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.mainList = []

    def initUI(self, username, password):
        try:
            if(username != "" and password != ""):
                subjectsBrowser = SubjectsBrowser(targetURL, username, password)
                subjects = subjectsBrowser.getResult()
                for i,s in enumerate(subjects): # DO LIT OF TEXTCTRL
                    subjectName, subjectCoeff = s[0], s[1]
                    wx.StaticText(self, pos=(20, 20+30*i), label=subjectName)
                    tc = wx.TextCtrl(self, pos=(265, 20+30*i), size=(80,25))
                    self.mainList.append([ tc, subjectCoeff ])
                self.bva = wx.Button(self, pos=(120, 30+30*len(subjects)), label='Calculate grade', size=(150, 25))
                self.bva.Bind(wx.EVT_BUTTON, self.calculateGrade)
            else: # Empty username or password
                wx.MessageBox('Please enter a valid username/password', 'Info', wx.OK | wx.ICON_INFORMATION)
                self.showPanelLogin()
        except AttributeError: # Wrong username or password
            wx.MessageBox('Wrong username/password', 'Info', wx.OK | wx.ICON_INFORMATION)
            self.showPanelLogin()

    # Calculates final grade on button click
    def calculateGrade(self, event):
        valuesList = [(ml[0].GetValue(), ml[1]) for ml in self.mainList] # gettings values list from inputs
        gradesList  = [(float(ml[0]),float(ml[1])) for ml in valuesList if ml[0]] # converting to grades list
        gradeCalculator = GradeCalculator()
        gradeCalculator.setGradesList(gradesList)
        wx.MessageBox(str(gradeCalculator.getFinalGrade()), 'Your grade', wx.OK | wx.ICON_INFORMATION)

    def showPanelLogin(self):
        self.parent.SetTitle("Login")
        self.parent.panelGrades.Hide()
        self.parent.panelLogin.Show()
        self.parent.Layout()

if __name__ == '__main__':
    app = wx.App()
    frame = INSAGrade()
    frame.Show()
    app.MainLoop()