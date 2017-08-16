# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-15 20:43:05
# @Last Modified by:   admin
# @Last Modified time: 2017-08-16 21:38:07

# 允许重定向
# import sys,wx
# class Frame(wx.Frame):
# 	"""docstring for Frame"""
# 	def __init__(self, parent,id,title):
# 		print "frame.__init__"
# 		wx.Frame.__init__(self,parent,id,title)
		
# class App(wx.App):
# 	# 如果redirect为真， 则重定向到框架，否则，定向到控制台;
# 	# 如果重定向为真，那filename也可以被指定，可以重定向到一个文件而不是一个框架
# 	def __init__(self,redirect=True,filename="02.txt"):
# 		print "App_init_" # 在控制台输出
# 		wx.App.__init__(self,redirect,filename)
# 	def OnInit(self):
# 		# 从这里开始，生命周期开始
# 		print "Oninit"  
# 		self.frame=Frame(parent=None,id=-1,title="starutup")
# 		self.frame.Show()
# 		self.SetTopWindow(self.frame)
# 		print >> sys.stderr,"a pretend error"
# 		return True
# 	def OnExit(self):
# 		# 从这里，生命周期结束
# 		print "Onexit"
		

# if __name__ == '__main__':
# 		# 如果redirect为真， 则重定向到框架，否则，定向到控制台;
# 		app=App(redirect=True)	
# 		print "before mainloop"
# 		app.MainLoop()
# 		print "after mainloop"


# 2.给框架增加一个窗口部件
# import wx
# class InsertFrame(wx.Frame):
# 	"""docstring for InsertFrame"""
# 	def __init__(self,parent,id):
# 		wx.Frame.__init__(self, parent,id,"frame with button ",size=(300,100))
# 		panel=wx.Panel(self)
# 		button=wx.Button(panel,label="close",pos=(125,10),size=(50,50))
# 		# 绑定按钮的单击事件
# 		self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)
# 		# 绑定窗口的关闭事件
# 		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
# 	def OnCloseMe(self,event):
# 		self.Close(True)
	
# 	def OnCloseWindow(self,event):
# 		self.Destroy()

# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=InsertFrame(parent=None,id=-1)
# 	frame.Show()
# 	app.MainLoop()



# 3.给框架增加一个菜单栏，工具栏和状态栏
# import wx
# # import images
# class ToolbarFrame(wx.Frame):
# 	"""docstring for ToolbarFrame"""
# 	def __init__(self,parent,id):
# 		wx.Frame.__init__(self, parent,id,"toolbar",size=(300,200))
# 		panel=wx.Panel(self)
# 		panel.SetBackgroundColour("Red")
# 		# 创建状态栏,显示在底部，宽度和框架相同，高度自定义
# 		statusbar=self.CreateStatusBar()
# 		# 创建工具栏
# 		toolbar=self.CreateToolBar()
# 		# 添加一个工具栏，参数为：id，位图，短的帮助文本，显示在状态栏的长帮助文本。
# 		# toolbar.AddSimpleTool(wx.NewId(),images.getNewBitmap(),"new","long help for new")
# 		# 使用realize来显示工具栏，必须
# 		toolbar.Realize()

# 		#创建菜单栏
# 		menubar=wx.MenuBar()
# 		# 创建两个菜单
# 		menu1=wx.Menu()
# 		menu2=wx.Menu()
# 		# 把菜单一添加到菜单栏中,它重新定义append,是首字母大写的
# 		menubar.Append(menu1,"&File")
# 		# 给菜单二增加几个项目
# 		menu2.Append(wx.NewId(),"&Copy","copy in status bar")
# 		menu2.Append(wx.NewId(), "C&ut", "")
# 		menu2.Append(wx.NewId(),"&options","display options")
# 		# 把菜单二添加进去
# 		menubar.Append(menu2,"&Edit")
# 		# 把菜单栏放在框架上
# 		self.SetMenuBar(menubar)

# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=ToolbarFrame(parent=None,id=-1)
# 	frame.Show()
# 	app.MainLoop()


# 消息对话框
import wx
class InsertFrame(wx.Frame):
	"""docstring for InsertFrame"""
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent,id,"frame with button ",size=(300,100))
		dlg=wx.MessageDialog(None, "so you love python ?", "title", wx.YES_NO|wx.ICON_QUESTION)
		result=dlg.ShowModal()
		dlg.Destroy()

if __name__ == '__main__':
	app=wx.App()
	frame=InsertFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()