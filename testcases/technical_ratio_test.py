# PyAlgoTrade
# 
# Copyright 2011 Gabriel Martin Becedillas Ruiz
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

import unittest
from pyalgotrade.technical import ratio
from pyalgotrade import dataseries

class TestCase(unittest.TestCase):
	def __buildRatio(self, values):
		return ratio.Ratio(dataseries.SequenceDataSeries(values))

	def testSimple(self):
		ratio = self.__buildRatio([1, 2, 1])
		self.assertTrue(ratio.getValueAbsolute(-1) == None)
		self.assertTrue(ratio[0] == None)
		self.assertTrue(ratio[1] == 1)
		self.assertTrue(ratio[2] == -0.5)
		with self.assertRaises(IndexError):
			ratio[3]

		self.assertTrue(ratio.getValue(1) == ratio[1])
		self.assertTrue(ratio.getValue() == ratio[2])

	def testNegativeValues(self):
		ratio = self.__buildRatio([-1, -2, -1])
		self.assertTrue(ratio.getValueAbsolute(-1) == None)
		self.assertTrue(ratio[0] == None)
		self.assertTrue(ratio[1] == -1)
		self.assertTrue(ratio[2] == 0.5)
		with self.assertRaises(IndexError):
			ratio[3]

		self.assertTrue(ratio.getValue(1) == ratio[1])
		self.assertTrue(ratio.getValue() == ratio[2])

def getTestCases():
	ret = []
	ret.append(TestCase("testSimple"))
	ret.append(TestCase("testNegativeValues"))
	return ret


