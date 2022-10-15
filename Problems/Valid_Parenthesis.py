# Leetcode problem 20

brackets_dict: dict = {'(': ')', '{': '}', '[': ']'}
from Data_Structures.Stack import Stack


def isValid(s: str) -> bool:
    brackets_stack: Stack = Stack()

    for bracket in s:
        if bracket in brackets_dict.keys():
            brackets_stack.push(bracket)

        elif bracket in brackets_dict.values():
            top = brackets_stack.pop()
            if (top is None) or (brackets_dict[top] != bracket):
                return False

    return brackets_stack.empty()


class Solution:
    pass
