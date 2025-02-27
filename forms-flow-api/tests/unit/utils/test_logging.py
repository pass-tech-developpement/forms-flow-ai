"""Tests to assure the logging utilities.

Test-Suite to ensure that the logging setup is working as expected.
"""

import os

from formsflow_api.utils.logging import setup_logging


def test_logging_with_missing_file(capsys):
    """Assert that a message is sent to STDERR when the configuration doesn't exist."""
    file_path = None
    setup_logging(file_path)  # important to do this first

    captured = capsys.readouterr()

    assert captured.err.startswith("Unable to configure logging")
