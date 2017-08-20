# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-17 22:00:31
# @Last Modified by:   admin
# @Last Modified time: 2017-08-20 21:12:28

# 1.指定source和不指定的效果
# import wx
# class InsertFrame(wx.Frame):
# 	"""docstring for InsertFrame"""
# 	def __init__(self,parent,id):
# 		wx.Frame.__init__(self, parent,id,"frame with button ",size=(300,100))
# 		panel=wx.Panel(self,-1)
# 		button=wx.Button(panel,-1,"close",pos=(130,15),size=(40,40))
# 		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
# 		self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)
# 	def OnCloseMe(self,event):
# 		self.Close(True)
# 	def OnCloseWindow(self,event):
# 		self.Destroy()

# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=InsertFrame(parent=None,id=-1)
# 	frame.Show()
# 	app.MainLoop()


# 2.使用source来指定触发的窗口部件，即使是框架也可以指定
# import wx
# class MenuEventFrame(wx.Frame):
# 	def __init__(self,parent,id):
# 		wx.Frame.__init__(self, parent,id,"Menus",size=(300,200))
# 		# 创建菜单栏
# 		menuBar=wx.MenuBar()
# 		# 创建菜单
# 		menu1=wx.Menu()
# 		# 把菜单添加到菜单栏中,菜单名字是File
# 		menuBar.Append(menu1,"&File")
# 		# 添加菜单项
# 		menuItem=menu1.Append(-1, "&Exit")
# 		self.SetMenuBar(menuBar)
# 		# 绑定菜单项事件到指定的处理器上，并把菜单项作为source的值
# 		self.Bind(wx.EVT_MENU,self.OnCloseMe,menuItem)
# 	def OnCloseMe(self,event):
# 		self.Close(True)

# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=MenuEventFrame(parent=None, id=-1)
# 	frame.Show()
# 	app.MainLoop()

# 3.这个程序将会说明事件处理的过程
# import wx
# class MouseFrame(wx.Frame):
# 	def __init__(self,parent,id):
# 		wx.Frame.__init__(self, parent,id,"frame with button",size=(300,300))
# 		self.panel=wx.Panel(self)
# 		self.button=wx.Button(self.panel,label="not ever",pos=(100,45))
# 		# 这里使用source绑定了按钮
# 		self.Bind(wx.EVT_BUTTON,self.OnButtonClick,self.button)
# 		self.button.Bind(wx.EVT_ENTER_WINDOW,self.OnEnterWindow)
# 		self.button.Bind(wx.EVT_LEAVE_WINDOW,self.OnLeaveWindow)
# 	def OnButtonClick(self,event):
# 		self.panel.SetBackgroundColour("Green")
# 		self.panel.Refresh()
# 	def OnEnterWindow(self,event):
# 		self.button.SetLabel("over me!!")
# 		event.Skip()
# 	def OnLeaveWindow(self,event):
# 		self.button.SetLabel("not over me")
# 		event.Skip()

# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=MouseFrame(parent=None,id=-1)
# 	frame.Show()
# 	app.MainLoop()


# 4.skip方法的使用
import wx
class DoubleFrame(wx.Frame):
	"""docstring for DoubleFrame"""
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent,id,"doubleframe",size=(300,100))
		self.panel=wx.Panel(self,-1)
		self.button=wx.Button(self.panel,-1,"click me",pos=(100,15))
		self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
		self.button.Bind(wx.EVT_LEFT_DOWN,self.OnMouseDown)
	# 当按钮被按下时，背景色变化，但不一定是鼠标左击事件
	def OnClick(self,event):
		self.panel.SetBackgroundColour("Green")
		self.panel.Refresh()
	def OnMouseDown(self,event):
		self.SetLabel("again!")
		# 这里使用skip确保能在鼠标点击后颜色变了，同时标题也出现
		# skip函数用来维持处理器的等待状态，以监听其他操作，当鼠标左键被释放，则触发wx.EVT_BUTTON事件
		event.Skip()

		

if __name__ == '__main__':
	app=wx.App()
	frame=DoubleFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()