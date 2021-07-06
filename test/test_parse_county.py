import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from src.one_barony_one_county import parse_county


class TestParseCounty(unittest.TestCase):
    def test_cultural_names_no_copy(self):
        input_lines = [
            'c_middlesex = {\n',
            '\n\tb_london = {\n',
            '\t\tcultural_names = {\n',
            '\t\t\tfrench = cn_londres\n',
            '\t\t}\n',
            '\t}\n',
            '}\n']
        new_lines, i = parse_county(input_lines, 0, set())
        self.assertEqual(i, 6)
        self.assertEqual(new_lines, input_lines)

    def test_cultural_names_duplicates(self):
        input_lines = [
            'c_london = {\n',
            '\tcultural_names = {\n',
            '\t\tfrench = cn_londres\n',
            '\t}\n',
            '\n\tb_london = {\n',
            '\t\tcultural_names = {\n',
            '\t\t\tfrench = cn_londres\n',
            '\t\t}\n',
            '\t}\n',
            '}\n']
        new_lines, i = parse_county(input_lines, 0, set())
        self.assertEqual(i, 9)
        self.assertEqual(new_lines, input_lines)

    def test_cultural_names_copy(self):
        input_lines = [
            'c_london = {\n',
            '\n\tb_london = {\n',
            '\t\tcultural_names = {\n',
            '\t\t\tfrench = cn_londres\n',
            '\t\t}\n',
            '\t}\n',
            '}\n']
        new_lines, i = parse_county(input_lines, 0, set())
        self.assertEqual(i, 6)
        expected_lines = [
            'c_london = {\n',
            '\tcultural_names = {\n',
            '\t\tfrench = cn_londres\n',
            '\t}\n',
            '\n\tb_london = {\n',
            '\t\tcultural_names = {\n',
            '\t\t\tfrench = cn_londres\n',
            '\t\t}\n',
            '\t}\n',
            '}\n']
        self.assertEqual(new_lines, expected_lines)



if __name__ == '__main__':
    unittest.main()