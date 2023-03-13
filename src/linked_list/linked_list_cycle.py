from typing import Optional, List, Any

from dataclasses import dataclass


@dataclass
class Node:
    data: int = None
    next: Optional[Any] = None


class LinkedListCycle:
    head = None
    tail = None

    def __init__(self, data: List[int], pos: int) -> None:
        """
        Initial linked list
        :param data:
        """
        node_list = []
        for item in data:
            node_list.append(self.push(item))

        self.print_list()
        if pos < 0:
            return

        self.tail.next = node_list[pos]

    def push(self, data) -> Node:
        """
        Function to insert a new node at the tail
        :param data:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        return node

    def print_list(self):
        """
        Print linked list
        """
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def has_cycle(self) -> bool:
        """
        Check linked list has cycle
        :return: bool
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
