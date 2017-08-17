# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-17 22:00:31
# @Last Modified by:   admin
# @Last Modified time: 2017-08-17 22:08:03
import wx
class InsertFrame(wx.Frame):
	"""docstring for InsertFrame"""
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent,id,"frame with button ",size=(300,100))
		panel=wx.Panel(self,-1)
		button=wx.Button(panel,-1,"close",pos=(130,15),size=(40,40))
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
		self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)
	def OnCloseMe(self,event):
		self.Close(True)
	def OnCloseWindow(self,event):
		self.Destroy()

if __name__ == '__main__':
	app=wx.App()
	frame=InsertFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()