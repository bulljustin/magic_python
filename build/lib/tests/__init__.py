# from parent directory, run:
# nosetests -v
import os 
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#print(dir_path)
import sys
sys.path.insert(0, f"{dir_path}/magic_python")
