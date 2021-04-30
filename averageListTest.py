import unittest
import averageList
import math

class testCaseVolume(unittest.TestCase):
    def test_average(self):
        arr = [10, 20, 30, 40, 50]
        result = averageList.calcAverage(arr)
        self.assertEqual(result, 30)

        arr = [0, 10, 20, 30, 40]
        result = averageList.calcAverage(arr)
        self.assertEqual(result, 20)


        arry = [-10, 0, 10, 20, 30]
        result = averageList.calcAverage(arr)
        self.assertEqual(result, 10)
        
if __name__ == '__main__':
    unittest.main()