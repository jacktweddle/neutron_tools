import unittest
from unittest.mock import patch, mock_open
import mcnp_analysis as ma
import mcnp_output_reader as mor


class normalise_test_case(unittest.TestCase):
    """ tests normalise function"""

    def test_norm_nice_data(self):
        data = [1, 2, 3, 4]
        self.assertEqual(ma.normalise(data, 10), [10, 20, 30, 40])
        self.assertEqual(ma.normalise(data, 1), data)
        result = ma.normalise(data, 0.1)
        self.assertAlmostEqual(result[0], 0.1, 7)
        self.assertAlmostEqual(result[1], 0.2, 7)
        self.assertAlmostEqual(result[2], 0.3, 7)
        self.assertAlmostEqual(result[3], 0.4, 7)


class calc_absolute_err_test(unittest.TestCase):
    """ test for absolute error calculation function"""

    def test_abs_err_calc(self):
        err = [1, 0.5, 0.1]
        res = [1, 1, 1]
        self.assertEqual(ma.calc_err_abs(res, err), [1, 0.5, 0.1])


class calc_bin_width_test(unittest.TestCase):
    """ test for bin width calculation function"""

    def test_bin_widths(self):
        bins = [1, 1.5, 1.6]
        self.assertEqual(len(ma.calc_bin_width(bins)), 3)


class calc_bin_mid_test(unittest.TestCase):
    """ test for bin width calculation function"""

    def test_bin_mids(self):
        bins = [1, 3, 5]
        self.assertEqual(len(ma.calc_mid_points(bins)), 2)
        self.assertEqual(ma.calc_mid_points(bins), [2, 4])


class csv_test_case(unittest.TestCase):
    """ tests write_lines function"""

    def test_write_csv(self):
        open_mock = mock_open()
        single = mor.read_output_file("test_output/singles.io")
        for tn in single.tally_data:
            if tn.number == 4:
                data = tn
        with patch("neut_utilities.open", open_mock, create=True):
            ma.csv_out(data, "output.txt")

        open_mock.assert_called_with("output.txt", "w")


if __name__ == '__main__':
    unittest.main()
