import unittest
from typing import List
from data_structures.linked_list import ListNode, array_to_linked_list, linked_list_to_array
from problems.merge_two_sorted_lists import merge_two_lists


class MyTestCase(unittest.TestCase):
    def test_array_to_linked_list_to_array(self):
        arr: List = []
        # arrange
        linked_list: ListNode = array_to_linked_list(arr)

        # act
        new_arr: List = linked_list_to_array(linked_list)

        # assert
        self.assertEqual(arr, new_arr)

    def test_happy_merge(self):
        # arrange:
        list1: ListNode = array_to_linked_list([1,2,4])
        list2: ListNode = array_to_linked_list([1,3,4])

        # act:
        new_sorted_list: ListNode = merge_two_lists(list1, list2)
        new_sorted_array: List = linked_list_to_array(new_sorted_list)

        # assert:
        self.assertEqual([1,1,2,3,4,4], new_sorted_array)  # add assertion here


if __name__ == '__main__':
    unittest.main()
