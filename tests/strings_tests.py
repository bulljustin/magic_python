from nose.tools import *
from magic_python.strings import *

def setup():
	print("setup")

def teardown():
	print("teardown")

def test_file():
	assert(file.WRITE == 'w')
	assert(file.READ_ONLY == 'r')
	assert(file.APPEND == 'a')

