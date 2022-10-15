# Leetcode problem 21
from typing import Optional

from data_structures.linked_list import ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    sorted_list_sentinel: ListNode = ListNode(val=-1)
    curr_pos_sorted = sorted_list_sentinel

    while list1 and list2:

        if list1.val <= list2.val:
            curr_pos_sorted.next = list1
            list1 = list1.next_node
        else:
            curr_pos_sorted.next_node = list2
            list2 = list2.next_node

        curr_pos_sorted = curr_pos_sorted.next_node

    curr_pos_sorted.next_node = list1 if list1 else list2

    return sorted_list_sentinel.next_node

