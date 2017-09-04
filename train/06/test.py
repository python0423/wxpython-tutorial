# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-09-04 20:34:20
# @Last Modified by:   admin
# @Last Modified time: 2017-09-04 20:49:09
import wx
class SketchWindow(wx.Window):
	"""窗口部件集"""
	def __init__(self, parent,ID):
		wx.Window.__init__(self, parent,ID)
		self.SetBackgroundColour("white")
		self.color="black"
		self.thickness=1

class SketchFrame(wx.Frame):
	"""docstring for SketchFrame"""
	def __init__(self, parent):
		wx.Frame.__init__(self,parent,-1,"sketch frame", size=(800,600))
		self.sketch=SketchWindow(self, -1)

if __name__ == '__main__':
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()