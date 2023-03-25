
import pandas as pd
import unittest

class TestPreProcessData(unittest.TestCase):
    def setUp(self):
        # create test data
        self.test_data = pd.DataFrame({
            'Timestamp': ['2021-01-01 00:00:00', '2021-01-01 01:00:00', '2021-01-01 02:00:00', '2021-01-01 03:00:00'],
            'transaction_count': [100, 200, 300, 400],
            'workforce_type_1': ['10', '20', '30', '40'],
            'workforce_type_2': [1.1, 2.2, 3.3, 4.4],
            'workforce_type_3': [1.0, 2.0, 3.0, 4.0],
            'workforce_type_4': [0.1, 0.2, 0.3, 0.4]
        })

    def test_pre_process_data_with_csv_path(self):
        # arrange
        csv_path = 'test_data.csv'
        self.test_data.to_csv(csv_path, index=False)

        expected_output = self.test_data.assign(
            time_idx=[0, 1, 2, 3],
            constant_group='group_1',
            year=[2021, 2021, 2021, 2021],
            month=[1, 1, 1, 1],
            day=[1, 1, 1, 1],
            hour=[0, 1, 2, 3]
        ).drop(columns=['Timestamp'])

        # act
        output = pre_process_data(csv_path)

        # assert
        pd.testing.assert_frame_equal(output, expected_output)

    def test_pre_process_data_with_dataframe(self):
        # arrange
        expected_output = self.test_data.assign(
            time_idx=[0, 1, 2, 3],
            constant_group='group_1',
            year=[2021, 2021, 2021, 2021],
            month=[1, 1, 1, 1],
            day=[1, 1, 1, 1],
            hour=[0, 1, 2, 3]
        ).drop(columns=['Timestamp'])

        # act
        output = pre_process_data(self.test_data)

        # assert
        pd.testing.assert_frame_equal(output, expected_output)


if __name__ == '__main__':
    unittest.main()
