# python3

import sys


class Bracket:
    """Bracket class.

    It stores a bracket type which is one of [, (, { and position of the
    bracket in the string.
    """

    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, char):
        """Matches given character with the bracket's type."""

        if self.bracket_type == '[' and char == ']':
            return True
        if self.bracket_type == '{' and char == '}':
            return True
        if self.bracket_type == '(' and char == ')':
            return True
        return False


def checker(text):
    """Check balanced brackets.

    Given a text of opening and closing brackets, check whether it’s balanced.

    If the brackets are used correctly, return “Success” (without the quotes).
    Otherwise, output the 1-based index of the first unmatched closing bracket,
    and if there are no unmatched closing brackets, output the 1-based index of
    the first unmatched opening bracket.

    Samples:
    >>> checker("{[]}()")
    Success
    >>> # Explanation: Here there are 3 pairs of brackets, one of them is nested
    >>> # into another one, and the third one is separate from the first two.
    >>> checker("{[}")
    3
    >>> # Explanation: The bracket } is unmatched, because the last unmatched
    >>> # opening bracket before it is [ and not {. It is the first unmatched
    >>> # closing bracket, and our first priority is to output the first
    >>> # unmatched closing bracket, and its position is 3, so we output 3.
    >>> checker("foo(bar);")
    Success
    >>> # Explanation: All the brackets are matching, and all the other symbols
    >>> # can be ignored.
    >>> checker("foo(bar[i);")
    10
    >>> # Explanation: ) doesn’t match [, so ) is the first unmatched closing
    >>> # bracket, so we output its position, which is 10.
    """
    stack = []
    for index, char in enumerate(text, start=1):

        if char in ("[", "(", "{"):
            stack.append(Bracket(char, index))

        elif char in ("]", ")", "}"):
            if not stack:
                return index

            top = stack.pop()
            if not top.match(char):
                return index
    if stack:
        top = stack.pop()
        return top.position

    return "Success"


if __name__ == "__main__":
    text = sys.stdin.read().strip("\n")
    print(checker(text))
