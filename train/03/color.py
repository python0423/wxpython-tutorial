# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-28 21:21:51
# @Last Modified by:   admin
# @Last Modified time: 2017-08-28 21:53:47
import wx,time
# 点击按钮，画布开始变颜色，每三秒变一种颜色
class myframe(wx.Frame):
	"""docstring for myframe"""
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,"hello,color",size=(400,400))
		self.panel=wx.Panel(self,-1,pos=(100,100),size=(100,100))
		self.button=wx.Button(self,-1,"click",pos=(150,10),size=(50,25))
		self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
	def OnClick(self,event):
		for x in ["Green","Red","black"]:
			print x
			time.sleep(1)
			self.panel.SetBackgroundColour(x)
			self.panel.Refresh()
				
		
if __name__ == '__main__':
	app=wx.App()
	frame=myframe(parent=None,id=-1)
	frame.Show()
	app.MainLoop()