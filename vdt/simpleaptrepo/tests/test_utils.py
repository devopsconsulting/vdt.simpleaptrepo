import unittest

import vdt.simpleaptrepo.utils as utils


def mock_dist_osx():
    return ('Mac OSX', '10.10.5', 'Yosemity')


def mock_dist_ubuntu():
    return ('Ubuntu', '12.04', 'precise')


def mock_dist_debian():
    return ('debian', '8.6', '')


class TestUtils(unittest.TestCase):

    def test_platform_is_debian(self):
        utils.platform.dist = mock_dist_osx
        self.assertFalse(utils.platform_is_debian())

        utils.platform.dist = mock_dist_ubuntu
        self.assertTrue(utils.platform_is_debian())

        utils.platform.dist = mock_dist_debian
        self.assertTrue(utils.platform_is_debian())
