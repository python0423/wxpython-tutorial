# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-14 20:30:18
# @Last Modified by:   admin
# @Last Modified time: 2017-08-26 08:35:49

# wxpython 第一章

# 它用来显示一个鼠标位置的窗口
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
	app=wx.App()
	frame=MyFrame()
	frame.Show(True)
	app.MainLoop()


