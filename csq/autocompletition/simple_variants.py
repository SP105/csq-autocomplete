"""
This are the straightforward solutions in Python because it use native functionality
of the language. The problem is that this solution always has a constant run time of O(n)
because needs to scan all the keywords.
"""


def find_ocurrence_in_any_part(input_: str, keywords: list) -> list:
    """
    Find the first 4 ocurrence of the input in any part of the word for the keywords list.

    :param input_: (str) input from console
    :param keywords: (list) keywords to search the input
    :return: (list) 4 or less posibilities found.
    """

    posibilities = [word for word in keywords if input_ in word]
    posibilities.sort()

    return posibilities[:4]


def find_ocurrence_start_with(input_: str, keywords: list) -> list:
    """
    Find the first 4 ocurrence of the input in the start of the words for the keywords list

    :param input_: (str) input from console
    :param keywords: (list) keywords to search the input
    :return: (list) 4 or less posibilities found.
    """

    posibilities = [word for word in keywords if word.startswith(input_)]
    posibilities.sort()

    return posibilities[:4]
