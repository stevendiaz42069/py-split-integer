from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(8, 2)
    assert max(parts) - min(parts) <= 1
    assert sum(parts) == 8, "sum of parts must be equal to value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(8, 2)
    assert len(parts) == 2
    assert all(x == 8 // 2 for x in parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(8, 3)
    assert parts == sorted(parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert 0 in split_integer(3, 4)
