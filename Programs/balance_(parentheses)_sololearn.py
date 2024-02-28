"""Created on Sat Jul 24 01:21:36 2021

@author: Mohammad
"""


class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, item):
        self.item.insert(0, item)

    def pop(self):
        return self.item.pop(0)

    def printStack(self):
        print(self.item)


def isBalance(experssion):
    stack = Stack()
    for ch in experssion:
        if ch in ['(', '[', '{']:
            stack.push(ch)
        elif ch in [')', ']', '}']:
            index = [')', ']', '}'].index(ch)
            if not stack.isEmpty():
                if stack.item[0] == ['(', '[', '{'][index]:
                    stack.pop()
                else:
                    return False
            else:
                stack.push(ch)
        else:
            continue
    return stack.isEmpty()


print(isBalance(input()))
input('Press Enter to continue')
