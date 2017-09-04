# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-09-03 11:00:56
# @Last Modified by:   admin
# @Last Modified time: 2017-09-04 20:45:18
# 本章介绍一些基本组件

# 第一个程序，基于设备上下文来画一幅画
import wx
# 窗口部件集
class SketchWindow(wx.Window):
	"""窗口部件集"""
	def __init__(self, parent,ID):
		wx.Window.__init__(self, parent,ID)
		self.SetBackgroundColour("white")
		self.color="black"
		self.thickness=1
		# 创建一个pen画笔对象
		self.pen=wx.Pen(self.color,self.thickness,
			wx.SOLID)
		self.lines=[]
		self.curLine=[]
		self.pos=(0,0)
		self.InitBuffer()

		# 连接事件
		self.Bind(wx.EVT_LEFT_DOWN,self.OnLeftDown)
		self.Bind(wx.EVT_LEFT_UP,self.OnLeftUp)
		self.Bind(wx.EVT_MOTION,self.OnMotion)
		self.Bind(wx.EVT_SIZE,self.OnSize)
		self.Bind(wx.EVT_IDLE,self.OnIdle)
		self.Bind(wx.EVT_PAINT,self.OnPaint)
	def InitBuffer(self):
		size=self.GetClientSize()
		# 创建一个缓存的设备上下文
		self.buffer=wx.Bitmap(size.width,size.height)
		dc=wx.BufferedDC(None,self.buffer)
		#使用设备上下文
		dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		dc.Clear()
		self.DrawLines(dc)
		self.reInitBuffer=False

	def GetLinesData(self):
		return self.lines[:]

	def SetLinesData(self,lines):
		self.lines=lines[:]
		self.InitBuffer()
		self.Refresh()

	def OnLeftDown(self,event):
		self.curLine=[]
		# 得到鼠标位置
		self.pos=event.GetPosition()
		# 捕获鼠标
		self.CaptureMouse()

	def OnLeftUp(self,event):
		if self.HasCapture():
			self.lines.append((self.color,self.thickness,
				self.curLine))
			self.curLine=[]
			# 释放鼠标
			self.ReleaseMouse()

	def OnMotion(self,event):
		# 判断是否在拖动
		if event.Dragging() and event.LeftIsDown:
			# 创建另一个上下文
			dc=wx.BufferedDC(wx.ClientDC(self),self.buffer)
			self.drawMotion(dc,event)
		event.Skip()

	# 绘画到设备上下文
	def drawMotion(self,dc,event):
		dc.SetPen(self.pen)
		newPos=event.GetPosition()
		coords=self.pos+newPos
		self.curLine.append(coords)
		dc.DrawLine(*coords)
		self.pos=newPos

	def OnSize(self,event):
		self.reInitBuffer=True

	def OnIdle(self,event):
		if self.reInitBuffer:
			self.InitBuffer()
			self.Refresh(False)
	
	def OnPaint(self,event):
		dc=wx.BufferedPaintDC(self, self.buffer)

	# 绘制所有线条
	def DrawLines(self,dc):
		for colour,thickness in self.lines:
			pen=wx.Pen(colour,thickness,wx.SOLID)
			dc.SetPen(pen)
			for coords in line:
				dc.DrawLine(*coords)

	def SetColor(self,color):
		self.color=color
		self.pen=wx.Pen(self.color,self.thickness,wx.SOLID)

	def SetThickness(self,num):
		self.thickness=num
		self.pen=wx.Pen(self.color,self.thickness,wx.SOLID)



# 框架集
class SketchFrame(wx.Frame):
	"""框架"""
	def __init__(self, parent):
		wx.Frame.__init__(self, parent,-1,"sketch frame"
			,size=(800,600))
		self.sketch=SketchWindow(self,-1)
		


# 主程序
if __name__ == '__main__':
	app=wx.App()
	frame=SketchFrame(None)
	frame.Show()
	app.MainLoop()