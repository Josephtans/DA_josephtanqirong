#import unittest libray
import unittest
#import TASK5.py as prog so if there any changes to the file,i only need to change task5
from Project import TASK5 as prog


class Task8(unittest.TestCase):
    #function to test task5 url
    def test_EngineType(self):
        task5 = prog.TASK5
        #check the url of task5.py
        self.assertEqual(task5.url, "http://192.168.126.148/spicyx/")
if __name__ == '__main__':
    unittest.main()