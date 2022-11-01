import pytest


class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __get_item(self, index):
        if index:
            temp = self.top
            while index:
                if temp.next is None:
                    raise IndexError
                temp = temp.next
                index -= 1
            return temp
        else:
            if self.top:
                return self.top
            else:
                raise IndexError

    def push_back(self, obj):
        if self.top:
            last = self.__get_item(self._length - 1)
            last.next = obj
        else:
            self.top = obj
        self._length += 1

    def push_front(self, obj):
        if self.top:
            obj.next = self.top
            self.top = obj
        else:
            self.top = obj
        self._length += 1

    def __getitem__(self, item):
        return self.__get_item(item).data

    def __setitem__(self, key, data):
        self.__get_item(key).data = data

    def __len__(self):
        return self._length

    def __iter__(self):
        for i in range(self._length):
            yield self.__get_item(i)


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


def push_back(stack: Stack, obj: StackObj):
    """ Add StackObj to the end. """
    stack._length += 1
    if not stack.top:
        return _push_back_in_empty_stack(stack, obj)
    _push_back_in_filled_stack(stack, obj)  # 1+ nodes in stack


def get_node(stack: Stack, key: int) -> StackObj:
    node = stack.top
    for _ in range(key):
        node = node.next
    return node


def _push_back_in_empty_stack(stack: Stack, obj: StackObj):
    if stack.top is None:  # empty stack
        stack.top = obj


def _push_back_in_filled_stack(stack: Stack, obj: StackObj):
    current_node = stack.top  # not empty stack
    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = obj


@pytest.fixture
def stack():
    stack = Stack()
    return stack


@pytest.fixture
def stack_obj():
    stack_obj = StackObj('some data')
    return stack_obj


@pytest.mark.parametrize('index, stack_size', (
        (0, 1),
        (0, 10),
        (1, 2),
        (1, 10),
        (2, 10),
        (4, 10),
        (6, 10),
))
def test_stack_setitem_in_long_stack(stack, stack_obj, index, stack_size):
    for i in range(stack_size):
        push_back(stack, StackObj(str(i)))
    stack[index] = stack_obj.data
    assert get_node(stack, index).data == stack_obj.data
