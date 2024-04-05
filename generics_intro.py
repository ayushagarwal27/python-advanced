from typing import Generic, TypeVar

V = TypeVar('V')
T = TypeVar('T')


class Pair(Generic[V]):
    def __init__(self, left: V, right: T):
        self.left = left
        self.right = right

    def get_right(self) -> T:
        return self.right


def main():
    pair = Pair('Hello', 45)
    print(pair.left)


if __name__ == '__main__':
    main()
