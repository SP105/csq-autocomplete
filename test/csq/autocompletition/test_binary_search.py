from unittest import TestCase

from csq.autocompletition.binary_search import find_ocurrence_binary_search
from csq.dictionaries.keywords import Keywords


class Test(TestCase):
    keywords_ = Keywords.list_
    keywords_.sort()

    def test_find_ocurrence_start_with_p(self):
        posibilities = find_ocurrence_binary_search('p', self.keywords_)
        self.assertListEqual(['pandora', 'paypal', 'pg&e', 'pinterest'], posibilities)

    def test_find_ocurrence_start_with_pr(self):
        posibilities = find_ocurrence_binary_search('pr', self.keywords_)
        self.assertListEqual(['press democrat', 'priceline', 'proactive', 'progenex'], posibilities)

    def test_find_ocurrence_start_with_pro(self):
        posibilities = find_ocurrence_binary_search('pro', self.keywords_)
        self.assertListEqual(['proactive', 'progenex', 'progeria', 'progesterone'], posibilities)

    def test_find_ocurrence_start_with_prog(self):
        posibilities = find_ocurrence_binary_search('prog', self.keywords_)
        self.assertListEqual(['progenex', 'progeria', 'progesterone'], posibilities)