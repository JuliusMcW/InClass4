
import unittest
import palindrome
import pytest


class Tester(unittest.TestCase):
    def test_pal1(self):
        result = palindrome.pal("Johnny")
        self.assertEqual(result,True)
    def test_pal2(self):
        result = palindrome.pal("JohhoJ")
        self.assertEqual(result,False)
    def test_pal3(self):
        result = palindrome.pal(" ")
        self.assertEqual(result,True)



def test_palpt1():
	assert palindrome.pal("Johhoj")

def test_palpt2():
	assert palindrome.pal("johhoj")

def test_palpt3():
	assert palindrome.pal(1234)
