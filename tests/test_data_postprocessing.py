#Here's the unit test code for the given Python code:

import math
import unittest

class TestPredictionConversion(unittest.TestCase):
    
    def test_convert_predictions_to_list(self):
        predictions = [
            [torch.tensor([1.1])],
            [torch.tensor([2.2])],
            [torch.tensor([3.3])],
            [torch.tensor([4.4])],
            [torch.tensor([5.5])],
        ]
        expected = [[1.1], [2.2], [3.3], [4.4], [5.5]]
        self.assertEqual(convert_predictions_to_list(predictions), expected)

    def test_ceil_round_predictions(self):
        predictions = [
            [3.3, 4.4, 5.5],
            [6.6, 7.7, 8.8],
            [9.9, 10.1, 11.2],
            [12.3, 13.4, 14.5],
            [15.6, 16.7, 17.8],
        ]
        expected = [
            [3, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15],
            [17, 18, 19],
        ]
        self.assertEqual(ceil_round_predictions(predictions), expected)

if __name__ == '__main__':
    unittest.main()

#Note: You will need to import the 'torch' module before running this test code.