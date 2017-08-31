# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-31 10:40:03
# @Last Modified by:   admin
# @Last Modified time: 2017-08-31 12:09:14
# 这是一个抽象类模型，用于更新视图数据
# 你可以把它作为自定义的模型类的父类
class AbstractModel(object):
	"""一个模型的抽象类"""
	def __init__(self):
		# 创建一个存放处理数据方法的容器
		self.listeners=[]
	def addListener(self,listenerFunc):
		# 添加方法到容器内
		self.listeners.append(listenerFunc)
	def removeListener(self,listenerFunc):
		# 删除指定方法
		self.listeners.remove(listenerFunc)
	def update(self):
		# 调用存放在容器中的方法来处理数据
		for eachFunc in self.listeners:
			eachFunc(self)
