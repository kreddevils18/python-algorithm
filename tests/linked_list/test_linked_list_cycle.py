import pytest

from src.linked_list.linked_list_cycle import LinkedListCycle


class TestLinkedListCycle:
    @pytest.mark.parametrize(
        "data, pos, expected",
        [
            ([3, 2, 0, -4], 1, True),
            ([1, 2], 0, True),
            ([1, 2], -1, False),
            ([[1], -1, False])
        ])
    def test_linked_list_cycle__ok(self, data, pos, expected):
        linked_list = LinkedListCycle(data, pos)
        actual = linked_list.has_cycle()

        assert actual == expected
