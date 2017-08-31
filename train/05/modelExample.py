# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-31 11:56:18
# @Last Modified by:   admin
# @Last Modified time: 2017-08-31 11:56:36
import wx
import abstractmodel
class SimpleName(abstractmodel.AbstractModel):
	"""自定义的模型类，它继承了抽象类"""
	def __init__(self, first="",last=""):
		abstractmodel.AbstractModel.__init__(self)
		# 使用set方法设置属性
		self.set(first,last)
	def set(self,first,last):
		# 这个方法做了两件事设置了属性，然后调用方法来处理
		self.first=first
		self.last=last
		self.update()
class ModelExample(wx.Frame):
	"""主框架"""
	def __init__(self, parent,id):
		wx.Frame.__init__(self, parent,id,"Flintstones",size=(640,200))
		panel=wx.Panel(self)
		panel.SetBackgroundColour("white")
		# 主框架绑定退出方法
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
		# 创建一个文本域
		self.textFields={}
		# 调用方法添加文本域属性
		self.createTextFields(panel)

		# 创建模型
		self.model=SimpleName()
		# 添加方法到容器中
		self.model.addListener(self.OnUpdate)

		# 调用方法创建按钮栏 
		self.createButtonBar(panel)

	def buttonData(self):
		# 返回按钮数据和绑定按钮的方法的二维列表
		return (("Fredify",self.OnFred),
			("Wilmafy",self.OnWilma),
			("Barnify",self.OnBarney),
			("Bettify",self.OnBerry))

	def createButtonBar(self,panel,yPos=0,xPos=0):
		# 迭代处理二维列表中的数据，发送元素的标签，处理器方法，位置
		for eachLabel,eachHandler in self.buttonData():
			pos=(xPos,yPos)
			button=self.buildoneButton(panel,eachLabel,eachHandler,pos)
			# 保证按钮的位置不会重叠，按钮依次排开
			xPos+=button.GetSize().width
	def buildoneButton(self,parent,label,handler,pos=(0,0)):
		# 之前重构代码见到的例子
		button=wx.Button(parent,-1,label,pos)
		self.Bind(wx.EVT_BUTTON,handler,button)
		return button

	def textFieldData(self):
		# 返回文本表头的名称和位置
		return (("First Name",(10,50)),("Last Name",(10,80)))
	def createTextFields(self,panel):
		# 迭代解析文本域，并交个下一个哥们处理
		for eachLabel,eachPos in self.textFieldData():
			self.createCaptionText(panel,eachLabel,eachPos)
	def createCaptionText(self,panel,label,pos):
		# 创建一个文本框和文本域
		static=wx.StaticText(panel,wx.NewId(),label,pos)
		static.SetBackgroundColour("white")
		textPos=(pos[0]+75,pos[1])
		self.textFields[label]=wx.TextCtrl(panel,wx.NewId(),"",
			size=(100,-1),pos=textPos,style=wx.TE_READONLY)
	def OnUpdate(self,model):
		# 在文本域上显示值，使用的实例对象是模型对象
		self.textFields["First Name"].SetValue(model.first)
		self.textFields["Last Name"].SetValue(model.last)

	# 响应按钮的处理器事件
	def OnFred(self,event):
		self.model.set("Fred", "Flintstone")
	def OnBarney(self,event):
		self.model.set("Barney", "Rubble")
	def OnWilma(self,event):
		self.model.set("Wilma", "Flintstone")
	def OnBerry(self,event):
		self.model.set("Berry", "Rubble")
	def OnCloseWindow(self,event):
		self.Destroy()

if __name__ == '__main__':
	app=wx.App()
	frame=ModelExample(parent=None,id=-1)
	frame.Show()
	app.MainLoop()