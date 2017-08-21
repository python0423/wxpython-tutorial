# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-21 20:46:28
# @Last Modified by:   admin
# @Last Modified time: 2017-08-21 20:48:20
import wx
class Frame(wx.Frame):
	"""docstring for Frame"""
	pass
class App(wx.App):
	"""docstring for App"""
	def OnInit(self):
		self.frame=Frame(parent=None,id=-1,title="spare")
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True
if __name__ == '__main__':
	app=App()
	app.MainLoop()
	
