import unittest

from click.testing import CliRunner

import mock

from vdt.simpleaptrepo import cli

GPG_KEY_OUTPUT = """GPG OUTPUT
Key created (see above for the hash)
Now add a repository with the 'create-repo' command
"""

GPG_KEY_ERROR = """Usage: create-gpg-key [OPTIONS]

Error: GPG ERROR
"""


class TestCLI(unittest.TestCase):

    @mock.patch('subprocess.check_output', return_value="GPG OUTPUT")
    def test_create_gpg_key(self, mock_subprocess):
        runner = CliRunner()
        result = runner.invoke(cli.create_key)

        # command should be run without error
        self.assertEqual(result.exit_code, 0)
        # and our mock functions should have been called
        self.assertTrue(mock_subprocess.called)
        # click's output should be captured correctly
        self.assertEqual(result.output, GPG_KEY_OUTPUT)

    @mock.patch('subprocess.check_output', side_effect=ValueError('GPG ERROR'))
    def test_create_gpg_key_exception(self, mock_subprocess):
        runner = CliRunner()
        result = runner.invoke(cli.create_key)

        # command should raise an error
        self.assertEqual(result.exit_code, 2)
        # and our mock functions should have been called
        self.assertTrue(mock_subprocess.called)
        # click's output should be captured correctly
        self.assertEqual(result.output, GPG_KEY_ERROR)
