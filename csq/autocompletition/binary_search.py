"""
    This is an implementation of the binarysearch algorithms for the list of keywords wich has a time complexity of
    average O(log(n)). Since is not only a traditional binary search (sinche the input witch is the one
    we are looking for can be in many keywords), we need to add a time of k witch are the amounts words that start with
    input. So the average will be O(log(n + k))
"""


def find_ocurrence_binary_search(input_: str, keywords: list) -> list:
    """
    Find the first 4 ocurrence of the input in the start of the word for the keywords list

    :param input_:
    :param keywords:
    :return:
    """

    low = 0
    high = len(keywords) - 1
    posibilities = []
    index = None

    while low <= high:
        index = (low + high) // 2
        key = keywords[index]
        if key.startswith(input_):
            break
        if key < input_:
            low = index + 1
        elif key > input_:
            high = index - 1

    if index is not None and low < high:
        while index >= 0 and keywords[index].startswith(input_):
            index = index - 1
        index = index + 1

        while keywords[index].startswith(input_) and len(posibilities) <= 4:
            posibilities.append(keywords[index])
            index = index + 1

    return posibilities[:4]
