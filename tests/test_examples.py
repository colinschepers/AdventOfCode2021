from typing import Sequence
from unittest import mock

import pytest

from utils import get_solution, get_input_from_file


solutions = {
    1: ['7', '5'],
    2: ['150', '900'],
    3: ['198', '230'],
    4: ['4512', '1924'],
    5: ['5', '12'],
    6: ['5934', '26984457539'],
    7: ['37', '168'],
    8: ['26', '61229'],
    9: ['15', '1134'],
    10: ['26397', '288957'],
    11: ['1656', '195'],
    12: ['10', '36'],
    13: ['17', '#####', '#...#', '#...#', '#...#', '#####'],
    14: ['1588', '2188189693529'],
    15: ['40', '315'],
    16: ['20', '1']
}

test_data = ((day, expected) for day, expected in solutions.items())


def get_input_example(day):
    return get_input_from_file(f"tests/examples/day{day:02d}.txt")


@pytest.mark.parametrize("day, expected", test_data)
def test_example_for_day(day: int, expected: Sequence[str]):
    with mock.patch('utils.get_input', get_input_example):
        assert get_solution(day) == list(expected)
