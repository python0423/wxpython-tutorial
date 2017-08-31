# -*- coding: utf-8 -*-
# @Author: admin
# @Date:   2017-08-31 11:54:15
# @Last Modified by:   admin
# @Last Modified time: 2017-08-31 12:08:14
# 第一个例子，展示了如何使用unittest模块进行测试
# 测试的用例是05.1中的第四个例子
import unittest
import modelExample
import wx
class TestExample(unittest.TestCase):
	"""创建一个测试实例"""
	def setUp(self):
		# 为测试进行配置
		self.app=wx.App()
		self.frame=modelExample.ModelExample(parent=None,id=-1 )
	def tearDown(self):
		# 测试之后的清除工作
		self.frame.Destroy()
	def testModel(self):
		# 创建一个测试
		self.frame.OnBarney(None)
		# 对于失败的断言
		self.assertEqual("Barney", self.frame.model.first,
			msg="First is wrong")
		self.assertEqual("Rubble", self.frame.model.last)
def suite():
	suite=unittest.makeSuite(TestExample,"test")
	return suite

if __name__ == '__main__':
	# 开始测试
	unittest.main(defaultTest="suite")