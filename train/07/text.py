# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-09-11 20:46:30
# @Last Modified by:   admin
# @Last Modified time: 2017-09-11 21:47:13

# 基本文本框
import wx
import time
class TextFrame(wx.Frame):
	"""继承父框架"""
	def __init__(self,parent):
		wx.Frame.__init__(self,parent,-1,"text frame",size=(500,200),pos=(100,50))
		panel=wx.Panel(self,-1)
		panel.SetBackgroundColour("red")
		text_nc=wx.StaticText(panel,-1,"Spurs",pos=(20,80),size=(150,50))
		text_black=wx.StaticText(panel,-1,"Heat",style=wx.ALIGN_LEFT,pos=(10,20),size=(80,20))
		text_blue=wx.StaticText(panel,-1,"Warriors",pos=(20,40),size=(80,20),style=wx.ALIGN_CENTER)
		text_white=wx.StaticText(panel,-1,"Rocket",pos=(20,60),size=(80,20),style=wx.ALIGN_RIGHT)
		
		# 指定前景色和背景色,前景色就是字体颜色
		text_black.SetBackgroundColour("black")
		text_black.SetForegroundColour("green")
		text_blue.SetBackgroundColour("blue")
		text_white.SetBackgroundColour("white")

		# 下面的文本框将使用标准黑客界面打印文本
		text_hack=wx.StaticText(panel,-1,"hack text,this is a new world ,new stage, and new age",pos=(50,30))
		text_hack.SetForegroundColour("green")
		text_hack.SetBackgroundColour("black")

		# 设置字体
		font_hack=wx.Font(20,wx.DECORATIVE,wx.ITALIC,wx.NORMAL,underline=True)
		text_hack.SetFont(font_hack)



if __name__ == '__main__':
	app=wx.App()
	frame=TextFrame(None)
	frame.Show()
	app.MainLoop()