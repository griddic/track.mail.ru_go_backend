import os
import pytest

from entry_task.count_lines import count_lines_in_file


@pytest.mark.parametrize(("file_path", 'lines_amount'), [
    ("1.txt", 1),
    ("10.txt", 10),
    ("empty_tail.txt", 10),
    ("empty_head.txt", 10),
    ("100.txt", 100),
    ("666.txt", 666)
])
@pytest.mark.parametrize("buffer", [1, 5, 7, 100, None])
def test_counter(file_path, lines_amount, buffer):
    file_path = os.path.join("files", file_path)
    counted_lines_amount = count_lines_in_file(file_path, buffer=buffer) if buffer is not None else count_lines_in_file(
        file_path)
    assert counted_lines_amount == lines_amount
