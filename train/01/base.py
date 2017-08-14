# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-14 20:43:00
# @Last Modified by:   admin
# @Last Modified time: 2017-08-14 21:31:01
# 这个程序会讲解使用wxpython的五个必要步骤
# 步骤一：导入wx模块，这会导入所有wx的应用包，类
# 导入顺序很重要，必须先导入wx，然后再导入wx中的其他所需要的包
import wx

# 步骤二：子类化应用程序类，继承一个wx中的类，通过使用wx.app来实现
class App(wx.App):
	"""docstring for App"""
	# 步骤三：定义应用程序的初始化方法，一般的，wxpython程序
	# 需要一个frame框架对象和一个application对象。frame对象一般在oninit中定义
	# show()方法用来显示框架或者隐藏，通过指定布尔值来确定。frame.show()===frame.hide(false)
	# wx.Frame(x1,x2,x3)有三个参数，仅仅第一个是必须的，其他是默认的
	# 记住：如果使用init方法，要记得继承wx.App()的init方法，如果没有继承，oninit方法也不会得到调用
	# 如果没有重写init方法，将自动继承父类的init。
	'''
	class myapp(wx.App):
		def __init__(self):
			wx.App.__init__(self)
	'''
	def OnInit(self):
		frame=wx.Frame(parent=None,title="Bare")
		frame.Show()
		return True
# 步骤四：创建一个app实例，并调用主循环方法
# wx主要用来响应鼠标和键盘事件，当一个应用程序的所有框架都关闭时，
# mainloop()方法将返回且程序退出
app=App()
app.MainLoop()
		

