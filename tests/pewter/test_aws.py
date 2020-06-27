import os

import pytest

import pewter.aws as aws


def test_create_key_pair(mocker):
    # mocks
    mock_ec2 = mocker.Mock()
    key_material = "key_material"
    mock_ec2.create_key_pair.return_value = {"KeyMaterial": key_material}
    mock_log = mocker.patch("pewter.aws.log")
    mock_os_open = mocker.patch("pewter.aws.os.open")
    mock_os_open_return_value = mocker.Mock()
    mock_os_open.return_value = mock_os_open_return_value
    mock_os_write = mocker.patch("pewter.aws.os.write")
    mock_os_close = mocker.patch("pewter.aws.os.close")

    # logic
    key_name = "key_name"
    path = "path"
    aws.create_key_pair(key_name, path, mock_ec2)

    # assertions
    mock_ec2.create_key_pair.assert_called_with(KeyName=key_name)
    assert mock_log.data.call_count == 2
    mock_os_open.assert_called_with(
        path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode=0o400
    )
    mock_os_write.assert_called_with(
        mock_os_open_return_value, str.encode(key_material)
    )
    mock_os_close.assert_called_with(mock_os_open_return_value)
