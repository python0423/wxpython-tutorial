# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-14 21:01:58
# @Last Modified by:   admin
# @Last Modified time: 2017-08-14 21:10:03

import wx
# 使用frame类来做，比之前的放在一起做更好，因为可以增加更多的关于框架的功能
class Frame(wx.Frame):
	pass

class App(wx.App):
	"""docstring for App"""
	def OnInit(self):
		# 把对frame实例的引用作为应用程序实例的一个属性，而frame的类的定义则放在外部
		self.frame=Frame(parent=None,title="spare")
		self.frame.Show()
		# settopwindow()方法用来说明哪一个框架是顶级窗口，程序可以创建多个窗口，但必有一个是顶级窗口
		self.SetTopWindow(self.frame)
		return True
if __name__ == '__main__':
	app=App()
	app.MainLoop()

		