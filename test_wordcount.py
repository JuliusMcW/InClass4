import unittest
import wordcount
import pytest
class Tester(unittest.TestCase):
    def test_wc1(self):
        result = wordcount.count("This test will pass")
        self.assertEqual(result,4)
    def test_wc2(self):
        result = wordcount.count("This test will fail")
        self.assertEqual(result,3)
    def test_wc3(self):
        result = wordcount.count("Pass?")
        self.assertEqual(result,1)
def test_wcpt1():
	assert wordcount.count(1234)==1
def test_wcpt2():
	assert wordcount.count("Johnny")==1
def test_wcpt3():
	assert wordcount.count(" ")==0
