# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-22 20:38:57
# @Last Modified by:   admin
# @Last Modified time: 2017-08-24 22:00:29

# 1.一个重构的例子，这个例子的代码结构性很差,作为原型
import wx
class RefactorExample(wx.Frame):
	"""继承父框架"""
	def __init__(self, parent,id):
		wx.Frame.__init__(self, parent,id,"refactor example",size=(340,200))
		panel=wx.Panel(self,-1)
		panel.SetBackgroundColour("Green")
		# create first button
		prevButton=wx.Button(panel,-1,"<<PREV",pos=(80,0))
		# bind first button
		self.Bind(wx.EVT_BUTTON,self.OnPrev,prevButton)
		# create second button
		nextButton=wx.Button(panel,-1,"NEXT>>",pos=(160,0))
		# bind second button
		self.Bind(wx.EVT_BUTTON,self.OnNext,nextButton)
		# bind a close method
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)

		# create a menubar
		menuBar=wx.MenuBar()
		# create a menu
		menu1=wx.Menu()
		# add a open item
		openMenuItem=menu1.Append(-1, "&Open", "Copy in status bar")
		# bind a menu event for 'open' item
		self.Bind(wx.EVT_MENU,self.OnOpen,openMenuItem)
		# add a exit item
		qutiMenuItem=menu1.Append(-1, "&Quit", "Quit")
		# bind closewindow method
		self.Bind(wx.EVT_MENU,self.OnCloseWindow,qutiMenuItem)
		# add menu items to menubar
		menuBar.Append(menu1,"&File")
		# create second menu object
		menu2=wx.Menu()
		# create copy ,cut,paste item,add them to menu2
		copyItem=menu2.Append(-1, "&Copy", "Copy")
		self.Bind(wx.EVT_MENU,self.OnCopy,copyItem)
		cutItem=menu2.Append(-1, "&Cut", "Cut")
		self.Bind(wx.EVT_MENU,self.OnCut,cutItem)
		pasteItem=menu2.Append(-1, "&Paste", "Paste")
		self.Bind(wx.EVT_MENU,self.OnPaste,pasteItem)
		# add menu2 to menubar
		menuBar.Append(menu2,"&Edit")
		# ????
		self.SetMenuBar(menuBar)

		# ????
		static=wx.StaticText(panel,wx.NewId(),"first name",pos=(10,50))
		static.SetBackgroundColour("White")
		text=wx.TextCtrl(panel,wx.NewId(),"",size=(100,-1),pos=(80,50))
		static2=wx.StaticText(panel,wx.NewId(),"last name",pos=(10,80))
		static2.SetBackgroundColour("White")
		text2=wx.TextCtrl(panel,wx.NewId(),"",size=(100,-1),pos=(80,80))

		firstButton=wx.Button(panel,-1,"FIRST")
		self.Bind(wx.EVT_BUTTON,self.OnFirst,firstButton)

		menu2.AppendSeparator()
		optItem=menu2.Append(-1, "&Options...", "display options")
		self.Bind(wx.EVT_MENU,self.OnOptions,optItem)
		lastButton=wx.Button(panel,-1,"LAST",pos=(240,0))
		self.Bind(wx.EVT_BUTTON,self.OnLast,lastButton)

	def OnPrev(self,event):
		pass
	def OnNext(self,event):
		pass
	def OnLast(self,event):
		pass
	def OnFirst(self,event):
		pass
	def OnOpen(self,event):
		pass
	def OnCopy(self,event):
		pass
	def OnCut(self,event):
		pass
	def OnPaste(self,event):
		pass
	def OnOptions(self,event):
		pass
	def OnPrev(self,event):
		pass

	def OnCloseWindow(self,event):
		self.Destroy()
if __name__ == '__main__':
	app=wx.App()
	frame=RefactorExample(parent=None, id=-1)
	frame.Show()
	app.MainLoop()



# 2. 重构代码，把按钮和绑定按钮作为单独方法
def createbuttonbar(self):
	firstbutton=wx.Button(panel,-1,"FIRST")
	self.Bind(wx.EVT_BUTTON,self.OnFirst,firstbutton)
	prevbutton=wx.Button(panel,-1,"<<PREV",pos=(80,0))
	self.Bind(wx.EVT_BUTTON,self.OnPrev,prevbutton)
	nextbutton=wx.Button(panel,-1,"NEXT>>",pos=(160,0))
	self.Bind(wx.EVT_BUTTON,self.OnNext,nextbutton,pos=(200,0))
	lastbutton=wx.Button(panel,-1,"LAST")
	self.Bind(wx.EVT_BUTTON,self.OnLast,lastbutton)
''' note: 像上面这样把代码分离出来，就会看出有规律可寻，其实只是名称不同，但做了同样的事情
	像这样的代码就需要被重构，因为它在重复做一件事，通过寻找规律，编写一个公用的方法，可以适用
	于所有这样的按钮的绑定
'''

# 3.再次重构代码，让代码具有公用性
def createButtonBar(self,panel):
	'''这个方法用来创建按钮基本属性，然后调用按钮的具体方法，传递具体的按钮属性 '''
	self.buildOneButton(panel,"First",self.OnFirst,(80,0))
	self.buildOneButton(panel,"<<PREV",self.OnPrev,(160,0))
	self.buildOneButton(panel,"NEXT>>",self.OnNext,(160,0))
	self.buildOneButton(panel,"Last",self.OnLast,(240,0))

def buildOneButton(self,parent,label,handler,pos=(0,0)):
	''' 这个方法用来创建具体的按钮，得到具体的属性值'''
	button=wx.Button(parent,id,label,pos)
	# 绑定按钮的事件处理器
	self.Bind(wx.EVT_BUTTON,handler,button)
	return button

# 4.第三次重构，分离数据的创建，把按钮名称和事件处理器放在一个容器内
# 按钮位置可以自动判断，确保新添加的按钮会被放在合适的位置
# 因为数据会被分离出去，所以方法变成了公用的，在以后的项目中可以重用代码
def buttonData(self):
	# 把名称和处理器方法放在一个元祖中，以元祖对的形式
	return (("First",self.OnFirst),("<<PREV",self.OnPrev),("NEXT>>",self.OnNext),("Last",self.OnLast))

def createButtonBar(self,panel,yPos=0):
	xPos=0
	for eachLabel,eachHandler in self.buttonData():
		pos=(xPos,yPos)
		button=self.buildOneButton(panel,eachLabel,eachHandler,pos)
		# 确保按钮的横坐标能被放在正确的位置
		xPos+=button.GetSize().width
def buildOneButton(self,parent,label,handler,pos=(0,0)):
	button=wx.Button(parent,-1,label,pos)
	self.Bind(wx.EVT_BUTTON,handler,button)
	return button


# 第四次重构，把上面所有的改动进行整理，完整的程序如下
import wx
class RefactorExample(wx.Frame):
	"""docstring for RefactorExample"""
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,"Refactor Example",size=(340,200))
		panel=wx.Panel(self,-1)
		panel.SetBackgroundColour("White")
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
		# 下面是简化后的代码
		self.createMenuBar()
		self.createButtonBar(panel)
		self.createTextFields(panel)
	def menuData(self):
		return (("&File",("&Open","open in status bar",self.OnOpen),("&Quit","Quit",self.OnCloseWindow)),
			("&Edit",
			("&Copy","Copy",self.OnCopy),
				("C&ut","cut",self.OnCut),
				("&Paste","paste",self.OnPaste),
				("","",""),
				("&Options...","DisplayOptions",self.OnOptions)
				))
	def createMenuBar(self):
		menuBar=wx.MenuBar()
		for eachMenuData in self.menuData():
			menuLabel=eachMenuData[0]
			menuItems=eachMenuData[1:]
			menuBar.Append(self.createMenu(menuItems),menuLabel)
		self.SetMenuBar(menuBar)

	def createMenu(self,menuData):
		menu=wx.Menu()
		for eachLabel,eachStatus,eachHandler in menuData:
			if not eachLabel:
				menu.AppendSeparator()
				continue
			menuItem=menu.Append(-1, eachLabel,eachStatus)
			self.Bind(wx.EVT_MENU,eachHandler,menuItem)
		return menu
	def buttonData(self):
		# 把名称和处理器方法放在一个元祖中，以元祖对的形式
		return (("First",self.OnFirst),("<<PREV",self.OnPrev),("NEXT>>",self.OnNext),("Last",self.OnLast))

	def createButtonBar(self,panel,yPos=0):
		xPos=0
		for eachLabel,eachHandler in self.buttonData():
			pos=(xPos,yPos)
			button=self.buildOneButton(panel,eachLabel,eachHandler,pos)
			# 确保按钮的横坐标能被放在正确的位置
			xPos+=button.GetSize().width
	def buildOneButton(self,parent,label,handler,pos=(0,0)):
		button=wx.Button(parent,-1,label,pos)
		self.Bind(wx.EVT_BUTTON,handler,button)
		return button

	def textFieldData(self):
		return (("first name",(10,50)),("last name",(10,80)))
	def createTextFields(self,panel):
		for eachLabel,eachPos in self.textFieldData():
			self.createCaptionedText(panel,eachLabel,eachPos)
	def createCaptionedText(self,panel,label,pos):
		static=wx.StaticText(panel,wx.NewId(),label,pos)
		static.SetBackgroundColour("white")
		textPos=(pos[0]+75,pos[1])
		wx.TextCtrl(panel,wx.NewId(),"",size=(100,-1),pos=textPos)
		def OnPrev(self,event):
			pass
		def OnNext(self,event):
			pass
		def OnLast(self,event):
			pass
		def OnFirst(self,event):
			pass
		def OnOpen(self,event):
			pass
		def OnCopy(self,event):
			pass
		def OnCut(self,event):
			pass
		def OnPaste(self,event):
			pass
		def OnOptions(self,event):
			pass
		def OnPrev(self,event):
			pass

		def OnCloseWindow(self,event):
			self.Destroy()
if __name__ == '__main__':
	app=wx.App()
	frame=RefactorExample(parent=None, id=-1)
	frame.Show()
	app.MainLoop()




		

