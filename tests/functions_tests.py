from nose.tools import *
from magic_python.functions import *

def setup():
	print("setup")

def teardown():
	print("teardown")

def test_length():
	test_string = "this string is 33 characters long"
	len1 = length(test_string)
	len2 = len(test_string)
	assert(len1==len2)
