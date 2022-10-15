from typing import List


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def array_to_linked_list(arr: List) -> ListNode:
    """
    :param arr: list of any type
    :return: ListNode (=head) if arr is not empty
            None o.w
    """
    sentinel: ListNode = ListNode()
    prev_node = sentinel
    for cell in arr:
        new_node: ListNode = ListNode(val=cell)
        prev_node.next_node = new_node
        prev_node = new_node
    return sentinel.next_node


def linked_list_to_array(head: ListNode) -> List:
    new_list: List = list()
    curr_node: ListNode = head
    while curr_node is not None:
        new_list.append(curr_node.val)
        curr_node = curr_node.next_node
    return new_list
