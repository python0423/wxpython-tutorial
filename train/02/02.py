# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-15 20:43:05
# @Last Modified by:   admin
# @Last Modified time: 2017-08-15 21:57:25

# 允许重定向
import sys,wx
class Frame(wx.Frame):
	"""docstring for Frame"""
	def __init__(self, parent,id,title):
		print "frame.__init__"
		wx.Frame.__init__(self,parent,id,title)
		
class App(wx.App):
	# 如果redirect为真， 则重定向到框架，否则，定向到控制台;
	# 如果重定向为真，那filename也可以被指定，可以重定向到一个文件而不是一个框架
	def __init__(self,redirect=True,filename="02.txt"):
		print "App_init_" # 在控制台输出
		wx.App.__init__(self,redirect,filename)
	def OnInit(self):
		# 从这里开始，生命周期开始
		print "Oninit"  
		self.frame=Frame(parent=None,id=-1,title="starutup")
		self.frame.Show()
		self.SetTopWindow(self.frame)
		print >> sys.stderr,"a pretend error"
		return True
	def OnExit(self):
		# 从这里，生命周期结束
		print "Onexit"
		

if __name__ == '__main__':
		# 如果redirect为真， 则重定向到框架，否则，定向到控制台;
		app=App(redirect=True)	
		print "before mainloop"
		app.MainLoop()
		print "after mainloop"