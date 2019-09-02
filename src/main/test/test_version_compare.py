import unittest.mock
from compare_versions import VersionCompare, InvalidVersionFormatError


class TestVersionCompare(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_version_compare_equal(self):
        version_string_a = '1.2.1.1'
        version_string_b = '1.2.1.1'
        version_compare = VersionCompare()
        version_a_list, version_b_list = version_compare.get_version_string_as_list(version_string_a, version_string_b)
        return_version_string = version_compare.compare_versions_input(version_a_list, version_b_list)
        self.assertEqual('EQ', return_version_string)

    def test_version_compare_equal_trail_zero(self):
        version_string_a = '1.2.1.1'
        version_string_b = '1.2.1.1.0'
        version_compare = VersionCompare()
        version_a_list, version_b_list = version_compare.get_version_string_as_list(version_string_a, version_string_b)
        return_version_string = version_compare.compare_versions_input(version_a_list, version_b_list)
        self.assertEqual('EQ', return_version_string)

    def test_version_compare_greater(self):
        version_string_a = '1.3.2.1'
        version_string_b = '1.3.2.1.3'
        version_compare = VersionCompare()
        version_a_list, version_b_list = version_compare.get_version_string_as_list(version_string_a, version_string_b)
        return_version_string = version_compare.compare_versions_input(version_a_list, version_b_list)
        self.assertEqual('1.3.2.1.3', return_version_string)

    def test_version_compare_error(self):
        version_string_a = '1.3.2.'
        version_string_b = '1.3.2.1.3'
        version_compare = VersionCompare()
        version_a_list, version_b_list = version_compare.get_version_string_as_list(version_string_a, version_string_b)
        with self.assertRaises(InvalidVersionFormatError):
            version_compare.compare_versions_input(version_a_list, version_b_list)
