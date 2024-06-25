import unittest
import dnf


class TestDNF(unittest.TestCase):

    def test_3_element_sort_1(self):
        expected_output = [0, 1, 2]
        input_array = [0, 1, 2]

        output = dnf.sort_dfa(input_array)
        self.assertEqual(expected_output, output)

    def test_3_element_sort_2(self):
        expected_output = [0, 1, 2]
        input_array = [2, 1, 0]

        output = dnf.sort_dfa(input_array)
        self.assertEqual(expected_output, output)

    def test_3_element_sort_3(self):
        expected_output = [0, 1, 2]
        input_array = [1, 2, 0]

        output = dnf.sort_dfa(input_array)
        self.assertEqual(expected_output, output)

    def test_3_element_sort_4(self):
        expected_output = [0, 0, 0]
        input_array = [0, 0, 0]

        output = dnf.sort_dfa(input_array)
        self.assertEqual(expected_output, output)

    def test_3_element_sort_5(self):
        expected_output = [1, 1, 1]
        input_array = [1, 1, 1]

        output = dnf.sort_dfa(input_array)
        self.assertEqual(expected_output, output)

    def test_3_element_sort_6(self):
        expected_output = [2, 2, 2]
        input_array = [2, 2, 2]

        output = dnf.sort_dfa(input_array)
        self.assertEqual(expected_output, output)

    def test_positive_sort(self):
        expected_output = [0, 0, 0, 1, 1, 1, 2, 2]
        input_array = [2, 1, 0, 2, 0, 1, 0, 1]

        output = dnf.sort_dfa(input_array)
        self.assertEqual(expected_output, output)


if __name__ == '__main__':
    unittest.main()
