"""Created on Sat Jul 24 01:21:36 2021

@author: Mohammad
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)


def isBalance(experssion: str) -> bool:
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in experssion:
        if ch in ['(', '[', '{']:
            stack.push(ch)
        elif ch in [')', ']', '}']:
            if stack.isEmpty() or stack.pop() != matching[ch]:
                return False
    return stack.isEmpty()


print(isBalance(input()))

# Edited on Tue Nov 03 16:23:00 2026
