# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-09-03 11:00:56
# @Last Modified by:   admin
# @Last Modified time: 2017-09-09 17:28:36
# 第一个程序 ，基本的静态文本控件
import wx
# 创建一个多行文本控件
class TextFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"text",size=(300,250))
		panel=wx.Panel(self,-1)
#====================================================================
		#创建上下箭头按钮
		# sc=wx.SpinCtrl(panel,-1,"",(30,20),(80,-1))
		# # 设置最大最小值范围，然后设置起始值
		# sc.SetRange(1,100)
		# sc.SetValue(5)
#====================================================================
		# 创建进度条
		# self.count=0
		# self.gauge=wx.Gauge(panel,-1,20,style=wx.GA_HORIZONTAL,validator=wx.DefaultValidator)
		# self.gauge.SetBezelFace(3)
		# self.gauge.SetShadowWidth(3)
		# self.Bind(wx.EVT_IDLE,self.Onidle)


	# def Onidle(self,event):
	# 	self.count=self.count+1
	# 	if self.count>=50:
	# 		self.count=0
	# 		self.gauge.SetValue(self.count)


#====================================================================
		# 创建一个复选框
		wx.CheckBox(panel,-1,u"马刺",pos=(20,20))
		wx.CheckBox(panel,-1,u"勇士",pos=(20,40))
		wx.CheckBox(panel,-1,u"火箭",pos=(20,60))
#====================================================================
		# 创建一个单选按钮
		wx.RadioButton(panel,-1,"allen",pos=(60,20))
		# style用来确定首选项
		wx.RadioButton(panel,-1,"bllen",pos=(60,40),style=wx.RB_GROUP)  
		wx.RadioButton(panel,-1,"cllen",pos=(60,60))

		# 创建一个单选框
		slist=["allen","bell","clver","david","ellen","frank","Green","Helen"]
		wx.RadioBox(panel,-1,"radiobox",(100,100),wx.DefaultSize,slist,2)
#====================================================================
		# 如何创建一个列表框
		wx.ListBox(panel,-1,(200,20),(80,120),slist,wx.LB_SINGLE)

		# 创建一个多选列表
		wx.ListBox(panel,-1,(200,200),(80,120),slist,wx.LB_MULTIPLE)
#====================================================================
		# 创建下拉形式的选择框
		wx.Choice(panel,-1,(185,308),choices=slist)




if __name__ == '__main__':
	app=wx.App()
	frame=TextFrame()
	frame.Show()
	app.MainLoop()
