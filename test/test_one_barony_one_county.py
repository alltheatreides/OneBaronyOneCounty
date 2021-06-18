import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from src.one_barony_one_county import one_barony_one_county


class TestOneBaronyOneCounty(unittest.TestCase):
    def setUp(self):
        if os.path.exists('data'):
            self.data_dir = 'data'
        elif os.path.exists(os.path.join('test', 'data')):
            self.data_dir = os.path.join('test', 'data')
        else:
            self.fail('Test data directory not found')
        outpur_dir = os.path.join(self.data_dir, 'output')
        if os.path.exists(outpur_dir):
            for file in os.listdir(outpur_dir):
                os.remove(os.path.join(outpur_dir, file))
        else:
            os.makedirs(outpur_dir)

    def test_one_barony_one_county(self):
        for filename in os.listdir(os.path.join(self.data_dir, 'input')):
            with self.subTest(filename=filename):
                output = os.path.join(self.data_dir, 'output', filename)
                one_barony_one_county(os.path.join(self.data_dir, 'input', filename), output)
                self.assertTrue(os.path.exists(output))
                with open(output, 'r') as f:
                    output_lines = f.readlines()
                with open(os.path.join(self.data_dir, 'expected_output', filename), 'r') as f:
                    expected_output_lines = f.readlines()
                for i in range(min(len(output_lines), len(expected_output_lines))):
                    self.assertEqual(output_lines[i].replace('\t', '').replace('\n', ''),
                                     expected_output_lines[i].replace('\t', '').replace('\n', ''),
                                     f'Issue line {i + 1}')


if __name__ == '__main__':
    unittest.main()