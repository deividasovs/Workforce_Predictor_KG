import torch

import unittest

from app.data_postprocessing import convert_predictions_to_list, ceil_round_predictions

class TestPredictionConversion(unittest.TestCase):
    
    def test_convert_predictions_to_list(self):
        predictions = [
            [torch.Tensor([1.1])],
            [torch.Tensor([2.2])],
            [torch.Tensor([3.3])],
            [torch.Tensor([4.4])],
            [torch.Tensor([5.5])],
        ]
        expected = [[1.1], [2.2], [3.3], [4.4], [5.5]]
        self.assertEqual(convert_predictions_to_list(predictions), expected)

    def test_ceil_round_predictions(self):
        predictions = [
            [3.3, 4.4, 5.5],
            [6.6, 7.7, 8.8],
        ]
        expected = [
            [3, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(ceil_round_predictions(predictions), expected)

if __name__ == '__main__':
    unittest.main()