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
		wx.Frame.__init__(self,parent,-1,"text frame",size=(600,400),pos=(100,50))
		panel=wx.Panel(self,-1)
		panel.SetBackgroundColour("Aquamarine")
#=======================================================================
		# 创建单行文本
		# text_nc=wx.StaticText(panel,-1,"Spurs",pos=(20,80),size=(150,50))
		# text_black=wx.StaticText(panel,-1,"Heat",style=wx.ALIGN_LEFT,pos=(10,20),size=(80,20))
		# text_blue=wx.StaticText(panel,-1,"Warriors",pos=(20,40),size=(80,20),style=wx.ALIGN_CENTER)
		# text_white=wx.StaticText(panel,-1,"Rocket",pos=(20,60),size=(80,20),style=wx.ALIGN_RIGHT)
		
		# 指定前景色和背景色,前景色就是字体颜色
		# text_black.SetBackgroundColour("black")
		# text_black.SetForegroundColour("green")
		# text_blue.SetBackgroundColour("blue")
		# text_white.SetBackgroundColour("white")

		# 下面的文本框将使用标准黑客界面打印文本
		text_hack=wx.StaticText(panel,-1,u"开始游戏",pos=(50,30))
		text_hack.SetForegroundColour("Coral")
		text_hack.SetBackgroundColour("black")
		text_hackone=wx.StaticText(panel,-1,u"继续游戏",pos=(50,60))
		text_hackone.SetForegroundColour("Coral")
		text_hackone.SetBackgroundColour("black")
		text_hacktwo=wx.StaticText(panel,-1,u"结束游戏",pos=(50,100))
		text_hacktwo.SetForegroundColour("Coral")
		text_hacktwo.SetBackgroundColour("black")
#========================================================================
		# 创建多行文本
		# mul_text=wx.TextCtrl(panel,-1,"richtext\n""other text\n""third text",pos=(60,120),style=wx.TE_MULTILINE)
		# # 设置多行文本的背景色
		# mul_text.SetForegroundColour("green")
		# mul_text.SetBackgroundColour("black")
		# 创建一个丰富文本行
		# mulcolor_text=wx.TextCtrl(panel,-1,'''richtext\nhello,world\nhello,python\nhello,this is a national\n but you know, nation is the country, the age, the mind, \n please do not destory this nation,and 
		# 	and so \n do not force your mind to this country\n is that ok? ''',pos=(60,100),
		# 	style=wx.TE_MULTILINE|wx.TE_RICH2)
		# mulcolor_text.SetForegroundColour("green")
		# mulcolor_text.SetBackgroundColour("black")


#============================================================================
		# 设置字体
		# font_hack=wx.Font(20,wx.DECORATIVE,wx.ITALIC,wx.NORMAL,underline=True)
		# text_hack.SetFont(font_hack)
		# # 另一种风格的字体
		# font_roman=wx.Font(25,wx.ROMAN,wx.SLANT,wx.BOLD)
		# text_hackone.SetFont(font_roman)
		# # 另一种风格的字体
		# font_huawen=wx.Font(30,wx.DEFAULT,wx.NORMAL,wx.LIGHT,faceName=u'华文彩云')
		# text_hacktwo.SetFont(font_huawen)
		# 打印系统所有可用的字体
		# e=wx.FontEnumerator()
		# e.EnumerateFacenames()
		# fontList=e.GetFacenames()
		# for x in fontList:
		# 	print x
		# 不同字体的多行风格
		# mulfont_text=wx.TextCtrl(panel,-1,"the first line\n the second line\n the third line\n",pos=
		# 	(300,60),size=(320,200),style=wx.TE_MULTILINE|wx.TE_RICH2)
		# mulfont_text.SetFont(font_huawen)

#============================================================================
		# 使用按钮
		self.button_one=wx.Button(panel,-1,"click me",pos=(100,45))
		self.Bind(wx.EVT_BUTTON,self.OnClick_one,self.button_one)
		# setdefault设置按钮为对话框的默认按钮
		self.button_one.SetDefault()

		# 另一个按钮
		self.button_two=wx.Button(panel,-1,"click two",pos=(100,70))
		self.button_two.Bind(wx.EVT_BUTTON,self.OnClick_two,self.button_two)
		self.button_two.SetDefault()
		# 创建位图按钮，先创建一个位图，然后创建一个按钮；
		bmp=wx.Image("bit.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
		self.button_bitmap=wx.BitmapButton(panel,-1,bmp,pos=(100,90))
		self.Bind(wx.EVT_BUTTON,self.OnClick_bit,self.button_bitmap)
		# 创建另一个位图按钮
		bmp_one=wx.Image("bitone.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
		self.buttonbit_one=wx.BitmapButton(panel,-1,bmp_one,pos=(200,90))
		self.Bind(wx.EVT_BUTTON,self.OnClick_bit,self.buttonbit_one)
		# 第三个不同图像的位图按钮
		bmp_two=wx.Image("bittwo.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
		self.buttonbit_two=wx.BitmapButton(panel,-1,bmp_two,pos=(300,90),style=0)
		self.Bind(wx.EVT_BUTTON,self.OnClick_bit,self.buttonbit_two)

		# 创建通用按钮

	def OnClick_one(self,event):
		self.button_one.SetLabel(u"点击")
	def OnClick_two(self,event):
		self.button_two.SetLabel(u"点击一下")
	def OnClick_bit(self,event):
		self.Destroy()



if __name__ == '__main__':
	app=wx.App()
	frame=TextFrame(None)
	frame.Show()
	app.MainLoop()