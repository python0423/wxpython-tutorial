# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-26 09:51:32
# @Last Modified by:   admin
# @Last Modified time: 2017-08-26 10:41:27
import wx
class myframe(wx.Frame):
	"""docstring for myframe"""
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"hello",size=(1000,800))
class myapp(wx.App):
	"""docstring for myapp"""
	def OnExit(self):
		print "exit program"
		return 1
if __name__ == '__main__':
	app=myapp()
	frame=myframe()
	frame.Show()
	app.MainLoop()
		