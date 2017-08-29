# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-22 21:42:10
# @Last Modified by:   admin
# @Last Modified time: 2017-08-29 22:05:08

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
import wx
import wx.grid
class LineupTable(wx.grid.PyGridTableBase):
	data=(("CF","Bob","Dernier"),("CF","Bob","Dernier"),
		("CF","Bob","Dernier"),("CF","Bob","Dernier"),
		("CF","Bob","Dernier"),("CF","Bob","Dernier"),
		("CF","Bob","Dernier"),("CF","Bob","Dernier"),("CF","Bob","Dernier"))
	colLalbls=("Last","First")
	def __init__(self):
		wx.grid.GridTableBase.__init__(self)
	def GetNumberRows(self):
		return len(self.data)
	def GetNumberCols(self):
		return len(self.data[0])-1
	def GetColLabelValue(self,col):
		return self.colLalbls[col]
	def GetRowLabelValue(self,row):
		return self.data[row][0]
	def IsEmptyCell(self,row,col):
		return False
	def GetValue(self,row,col):
		return self.data[row][col+1]
	def SetValue(self,row,col,value):
		pass


class SimpleGrid(wx.grid.Grid):
	"""docstring for SimpleGrid"""
	def __init__(self,parent):
		wx.grid.Grid.__init__(self, parent,-1)
		self.SetTable(LineupTable())
class TestFrame(wx.Frame):
	"""docstring for TestFrame"""
	def __init__(self, parent):
		wx.Frame.__init__(self, parent,-1,"a grid",size=(275,275))
		grid=SimpleGrid(self)
if __name__ == '__main__':
	app=wx.App()
	frame=TestFrame(None)
	frame.Show()
	app.MainLoop()

