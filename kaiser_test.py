import unittest
from kaiser import Kaiser

class TestOrderCancellation(unittest.TestCase):
    def test_order_cancellation_1(self):
        kaiser = Kaiser()
        list = [3,2,3,1,5]
        self.assertListEqual(kaiser.order_cancellation(list, 2), [2])
        
    def test_order_cancellation_2(self):
        kaiser = Kaiser()
        list = [3,2,3,1,5]
        self.assertListEqual(kaiser.order_cancellation(list, 7), [5,2])
        
    def test_order_cancellation_3(self):
        kaiser = Kaiser()
        list = [5,2,7,2]
        self.assertListEqual(kaiser.order_cancellation(list, 3), [2,2])
        
    def test_order_cancellation_4(self):
        kaiser = Kaiser()
        list = [1, 5, 5, 97, 20, 83, 29, 12, 8, 2,41, 4, 36, 7, 8, 15, 23, 31, 90,15, 7, 9, 6, 16, 12, 15, 13, 19,20, 15, 15, 9, 9, 9, 9, 19, 100,2, 4, 8, 18, 10, 7, 17, 3, 33, 23]
        self.assertListEqual(kaiser.order_cancellation(list, 15), [15])
        
    def test_order_cancellation_5(self):
        kaiser = Kaiser()
        list = [1, 5, 5, 97, 20, 83, 29, 12, 8, 2,41, 4, 36, 7, 8, 15, 23, 31, 90,15, 7, 9, 6, 16, 12, 15, 13, 19,20, 15, 15, 9, 9, 9, 9, 19, 100,2, 4, 8, 18, 10, 7, 17, 3, 33, 23]
        self.assertListEqual(kaiser.order_cancellation(list, 375), [100,97,90,83,5])
        
if __name__ == "__main__":
    unittest.main()