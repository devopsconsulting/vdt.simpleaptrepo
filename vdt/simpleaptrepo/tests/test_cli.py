import unittest

from click.testing import CliRunner

import mock

from vdt.simpleaptrepo import cli


def mock_check_output(*args, **kwargs):
    return ""


class TestCLI(unittest.TestCase):

    @mock.patch('subprocess.check_output', side_effect=mock_check_output)
    def test_create_gpg_key(self, mock_check_output):
        runner = CliRunner()
        result = runner.invoke(cli.create_key)
        # command should be run without error
        self.assertEqual(result.exit_code, 0)
        # and our mock functions should have been called
        self.assertTrue(mock_check_output.called)
