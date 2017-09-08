# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-09-03 11:00:56
# @Last Modified by:   admin
# @Last Modified time: 2017-09-04 20:45:18
# 本章讲述静态文本控件

# 第一个程序 ，基本的静态文本控件
import wx
# class StaticTextFrame(wx.Frame):
# 	"""静态文本属性及样式"""
# 	def __init__(self):
# 		wx.Frame.__init__(self,None,-1,"statictext",size=(400,300))
# 		panel=wx.Panel(self,-1)
# 	# 创建一个基本的静态文本
# 		wx.StaticText(panel,-1,"this is an example of static text",(100,10))

# 	# 指定了前景色和背景色的文本
# 		rev=wx.StaticText(panel,-1,"static text with colors",(100,300))
# 		rev.SetForegroundColour("green")
# 		rev.SetBackgroundColour("black")

# 	# 指定居中对齐的文本
# 		center=wx.StaticText(panel,-1,"",(100,50),(160,-1),wx.ALIGN_CENTER)
# 		center.SetForegroundColour("green")
# 		center.SetBackgroundColour("black")

# 	# 指定新的字体的文本
# 		str="you could change font"
# 		text=wx.StaticText(panel,-1,str,(20,100))
# 		font=wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
# 		text.SetFont(font)

# 	# 显示多行对齐文本
# 		wx.StaticText(panel,-1,"hello,world\n like a align grazing at us \n"" so there is something viable",
# 		(220,150),style=wx.ALIGN_RIGHT)

# class Myclass(wx.Frame):
# 	"""静态文本控件"""
# 	def __init__(self):
# 		wx.Frame.__init__(self, None,-1,"静态文本窗口",size=(500,500))
# 		panel=wx.Panel(self,-1)
# 		# 创建简单静态文本
# 		# wx.StaticText(panel,-1,"马刺今年夺冠",(100,100),(200,250),wx.ALIGN_CENTER)
# 		# wx.StaticText(panel,-1,u"勇士今年夺冠",(201,10),(150,200),wx.ALIGN_LEFT)
# 		# wx.StaticText(panel,-1,u"骑士今年夺冠",(301,30),(100,200),wx.ALIGN_RIGHT)

# 		# 创建带颜色的文本
# 		rev=wx.StaticText(panel,-1,"马刺今年夺冠",(100,100),(200,250),wx.ALIGN_CENTER)
# 		rev.SetForegroundColour("green")
# 		rev.SetBackgroundColour("black")
# 		cev=wx.StaticText(panel,-1,"勇士今年夺冠",(200,200),(310,360),wx.ALIGN_CENTER)
# 		cev.SetForegroundColour("green")
# 		cev.SetBackgroundColour("black")

# 		# 创建多行文本
# 		tev=wx.StaticText(self,-1,"勇士今年夺冠\n马刺今年夺冠\n骑士今年夺冠",(100,60),(500,200),wx.ALIGN_CENTER)
# 		tev.SetForegroundColour("green")
# 		tev.SetBackgroundColour("black")


# 第二个程序，用户输入文本
# class TextFrame(wx.Frame):
# 	"""用户输入控件"""
# 	def __init__(self):
# 		wx.Frame.__init__(self,None,-1,"文本输入控件",size=(300,100))
# 		panel=wx.Panel(self,-1)
# 		# 用户输入框
# 		text=wx.StaticText(panel,-1,"用户名输入",size=(175,-1))
# 		user=wx.TextCtrl(panel,-1,"input something",size=(175,-1),style=wx.TE_CENTER)
# 		user.SetInsertionPoint(0)
# 		# 密码输入框
# 		text_passwd=wx.StaticText(panel,-1,"password")
# 		passwd=wx.TextCtrl(panel,-1,"input password",size=(175,-1),style=wx.TE_PASSWORD)
# 		sizer=wx.FlexGridSizer(cols=1,hgap=6, vgap=6)
# 		sizer.AddMany([text,user,passwd,text_passwd])
# 		panel.SetSizer(sizer)





if __name__ == '__main__':
	app=wx.App()
	# frame=StaticTextFrame()
	# frame=Myclass()
	frame=TextFrame()
	frame.Show()
	app.MainLoop()
