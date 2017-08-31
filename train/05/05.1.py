# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-22 21:42:10
# @Last Modified by:   admin
# @Last Modified time: 2017-08-31 11:56:40

# 5.2 使用grid控件，非模型方法
# import wx
# import wx.grid
# class SimpleGrid(wx.grid.Grid):
# 	"""docstring for SimpleGrid"""
# 	def __init__(self,parent):
# 		wx.grid.Grid.__init__(self, parent,-1)
# 		# 创建行和列数，9行2列
# 		self.CreateGrid(9, 2)
# 		# 创建第一个列的表头和第二列的表头
# 		self.SetColLabelValue(0,"First")
# 		self.SetColLabelValue(1,"Last")
# 		# 第一行的表头
# 		self.SetRowLabelValue(0,"CF")
# 		# 开始存放表格数据，从第一行第一列开始，然后是第一行第二列
# 		self.SetCellValue(0, 0,"Bob")
# 		self.SetCellValue(0, 1,"Dernier")
# 		# 第二行的表头
# 		self.SetRowLabelValue(1,"2B")
# 		self.SetCellValue(1, 0,"Ryne")
# 		self.SetCellValue(1, 1,"Sandberg")
# 		# 第三行的表头
# 		self.SetRowLabelValue(2,"LF")
# 		self.SetCellValue(2, 0,"Gary")
# 		self.SetCellValue(2, 1,"Matthews")
# 		# 第四行的表头
# 		self.SetRowLabelValue(3,"2B")
# 		self.SetCellValue(3, 0,"Ryne")
# 		self.SetCellValue(3, 1,"Sandberg")
# 		# 第五行的表头
# 		self.SetRowLabelValue(4,"2B")
# 		self.SetCellValue(4, 0,"Ryne")
# 		self.SetCellValue(4, 1,"Sandberg")
# 		# 第六行的表头
# 		self.SetRowLabelValue(5,"2B")
# 		self.SetCellValue(5, 0,"Ryne")
# 		self.SetCellValue(5, 1,"Sandberg")
# 		# 第七行的表头
# 		self.SetRowLabelValue(6,"2B")
# 		self.SetCellValue(6, 0,"Ryne")
# 		self.SetCellValue(6, 1,"Sandberg")
# 		# 第八行的表头
# 		self.SetRowLabelValue(7,"2B")
# 		self.SetCellValue(7, 0,"Ryne")
# 		self.SetCellValue(7, 1,"Sandberg")
# 		# 第九行的表头
# 		self.SetRowLabelValue(8,"2B")
# 		self.SetCellValue(8, 0,"Ryne")
# 		self.SetCellValue(8, 1,"Sandberg")

# class TestFrame(wx.Frame):
# 	"""docstring for TestFrame"""
# 	def __init__(self, parent):
# 		wx.Frame.__init__(self, parent,-1,"a grid",size=(275,275))
# 		grid=SimpleGrid(self)
		
# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=TestFrame(None)
# 	frame.Show()
# 	app.MainLoop()

# 2. 使用PyGridTableBase来生成一个表
# 这个程序无法正确运行，可能是gridtablebase类的问题
# import wx
# import wx.grid
# class LineupTable(wx.grid.GridTableBase):
# 	data=(("CF","Bob","Dernier"),("CF","Bob","Dernier"),
# 		("CF","Bob","Dernier"),("CF","Bob","Dernier"),
# 		("CF","Bob","Dernier"),("CF","Bob","Dernier"),
# 		("CF","Bob","Dernier"),("CF","Bob","Dernier"),("CF","Bob","Dernier"))
# 	colLabels=("Last","First")
# 	def __init__(self):
# 		wx.grid.GridTableBase.__init__(self)
# 	# 返回表中的行数
# 	def GetNumberRows(self):
# 		return len(self.data)
# 	# 返回表中的列数，不包含CF列
# 	def GetNumberCols(self):
# 		return len(self.data[0])-1
# 	# 获取列的表头
# 	def GetColLabelValue(self,col):
# 		return self.colLabels[col]
# 	# 获取行的表头
# 	def GetRowLabelValue(self,row):
# 		return self.data[row][0]
# 	# 判断单元格中的数据是否为空
# 	def IsEmptyCell(self,row,col):
# 		return False
# 	# 获取单元格中的数据
# 	def GetValue(self,row,col):
# 		return self.data[row][col+1]
# 	# 设置单元格的数据
# 	def SetValue(self,row,col,value):
# 		pass
# class SimpleGrid(wx.grid.Grid):
# 	"""docstring for SimpleGrid"""
# 	def __init__(self,parent):
# 		wx.grid.Grid.__init__(self, parent,-1)
# 		self.SetTable(LineupTable())
# class TestFrame(wx.Frame):
# 	"""docstring for TestFrame"""
# 	def __init__(self, parent):
# 		wx.Frame.__init__(self, parent,-1,"a grid",size=(275,275))
# 		grid=SimpleGrid(self)
# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=TestFrame(None)
# 	frame.Show()
# 	app.MainLoop()


# 3.使用外部generictable来分离模型代码
# import wx
# import wx.grid
# import generictable
# data=(("bob","dernier"),("bob","dernier"),
# 	("bob","dernier"),("bob","dernier"),
# 	("bob","dernier"),("bob","dernier"),
# 	("bob","dernier"),("bob","dernier"),
# 	("bob","dernier"),)
# colLabels=("Last","Fast")
# rowLabels=("CF","2B","LF","1B","RF","3B","C",
# 	"SS","P")

# class SimpleGrid(wx.grid.Grid):
# 	"""docstring for SimpleGrid"""
# 	def __init__(self,parent):
# 		wx.grid.Grid.__init__(self, parent,-1)
# 		tableBase=generictable.Genericatable(data,rowLabels,colLabels)
# 		self.SetTable(tableBase)
# class TestFrame(wx.Frame):
# 	"""docstring for TestFrame"""
# 	def __init__(self, parent):
# 		wx.Frame.__init__(self, parent,-1,"a grid",size=(275,275))
# 		grid=SimpleGrid(self)
# if __name__ == '__main__':
# 	app=wx.App()
# 	frame=TestFrame(None)
# 	frame.Show()
# 	app.MainLoop()

# 第四个例子，展示了简单的MVC模式思想
# 按钮控制器的方法引起模型的变化
# 模型被分离出去，单独处理数据，模型提供了一个接口，让视图可以显示数据；
# 模型中的更新导致文本域的改变；

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