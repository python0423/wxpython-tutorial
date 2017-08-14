# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-14 21:10:10
# @Last Modified by:   admin
# @Last Modified time: 2017-08-14 21:29:43
# 图像处理
import wx
class Frame(wx.Frame):
	"""docstring for Frame"""
	# 增加了一个图像参数image,在实例化时会被提供
	def __init__(self, image,parent=None,id=-1,pos=wx.DefaultPosition,title="hello,wxpython"):
		# 显示图像，创建一个位图对象temp
		temp=image.ConvertToBitmap()
		# size是获取图像的宽度和高度，然后传递给wx.frame，以便适用框架的宽度和高度
		size=temp.GetWidth(),temp.GetHeight()
		f_size=(800,600)
		wx.Frame.__init__(self,parent,id,title,pos,f_size)
		# 把temp这个位图对象传递给bitmap,以显示这个图像
		self.bmp=wx.StaticBitmap(parent=self,bitmap=temp)
class App(wx.App):
	"""docstring for App"""
	def OnInit(self):
		image=wx.Image("wx.jpg",wx.BITMAP_TYPE_JPEG)
		self.frame=Frame(image)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True
def main():
	app=App()
	app.MainLoop()
if __name__ == '__main__':
	main()
		