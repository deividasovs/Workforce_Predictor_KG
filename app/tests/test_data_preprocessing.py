
import pandas as pd
import unittest

from app.data_preprocessing import pre_process_data

class TestPreProcessData(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({
            'Timestamp': ['2021-01-01 00:00:00', '2021-01-01 01:00:00', '2021-01-01 02:00:00', '2021-01-01 03:00:00'],
            'transaction_count': [20, 20, 24, 26],
            'workforce_type_1': [2.1, 2.4, 2.3, 2.4],
            'workforce_type_2': [1.1, 2.2, 3.3, 4.4],
            'workforce_type_3': [1.0, 2.0, 3.0, 4.0],
            'workforce_type_4': [0.1, 0.2, 0.3, 0.4]
        })

    def test_pre_process_data_with_dataframe(self):
        expected_output = self.test_data.assign(
            time_idx=[0, 1, 2, 3],
            constant_group='group_1',
            year=[2021, 2021, 2021, 2021],
            month=[1, 1, 1, 1],
            day=[1, 1, 1, 1],
            hour=[0, 1, 2, 3]
        ).drop(columns=['Timestamp'])

        output = pre_process_data(self.test_data)

        pd.testing.assert_frame_equal(output, expected_output)

if __name__ == '__main__':
    unittest.main()
