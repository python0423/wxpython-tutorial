# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-30 20:43:39
# @Last Modified by:   admin
# @Last Modified time: 2017-08-30 20:50:46
# 这是一个通用的处理二维列表的类
import wx
import wx.grid
class Genericatable(wx.grid.GridTableBase):
	"""docstring for Genericatable"""
	def __init__(self, data,rolLabels=None,colLabels=None):
		wx.grid.GridTableBase.__init__(self)
		# 收为己用
		self.data=data
		self.rolLabels=rolLabels
		self.colLabels=colLabels
	def GetNumberRows(self):
		return len(self.data)
	def GetNumberCols(self):
		return len(self.data[0])
	def GetColLabelValue(self,col):
		if self.colLabels:
			return self.colLabels[col]
	def GetRowLabelValue(self,row):
		if self.rolLabels:
			return self.rolLabels[row]
	def IsEmptyCell(self,row,col):
		return False
	def GetValue(self,row,col):
		return self.data[row][col]
	def SetValue(self,row,col,value):
		pass
		
