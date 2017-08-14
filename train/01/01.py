# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-14 20:30:18
# @Last Modified by:   admin
# @Last Modified time: 2017-08-14 20:40:46

# wxpython 第一章
import wx
class MyFrame(wx.Frame):
	"""docstring for MyFrame"""
	def __init__(self):
		wx.Frame.__init__(self, None,-1,"My Frame", size=(300,300))
		panel=wx.Panel(self,-1)
		panel.Bind(wx.EVT_MOTION,self.OnMove)
		wx.StaticText(panel,-1,"pos:",pos=(10,12))
		self.posCtrl=wx.TextCtrl(panel,-1,"",pos=(40,10))
	def OnMove(self,event):
		pos=event.GetPosition()
		self.posCtrl.SetValue("%s,%s" %(pos.x,pos.y))
		
		

if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=MyFrame()
	frame.Show(True)
	app.MainLoop()