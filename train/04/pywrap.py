# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-21 20:50:06
# @Last Modified by:   admin
# @Last Modified time: 2017-08-21 21:16:46

import os
import sys
import wx
from wx.py.crust import CrustFrame
def wrap(app):
	wx.InitAllImageHandlers()
	frame=CrustFrame()
	frame.SetSize(750, 525)
	frame.Show()
	frame.shell.interp.locals["app"]=app
	app.MainLoop()
def main(modulename=None):
	sys.path.insert(0, os.curdir)
	if not modulename:
		if len(sys.argv)<2:
			print "please specify a module name"
			raise SystemExit
		modulename=sys.argv[1]
		if modulename.endswith(".py"):
			modulename=modulename[:-3]
	module=__import__(modulename)
	# find app class
	App=None
	d=module.__dict__
	for item in d.keys():
		try:
			if issubclass(d[item],wx.App):
				App=d[item]
		except (NameError,TypeError):
			pass
	if App is None:
		print "no app class was found"
		raise SystemExit
	app=App()
	wrap(app)
if __name__ == '__main__':
	main()