import unittest
from unittest import TestCase
from csq.dictionaries.keywords import Keywords

from csq.autocompletition.simple_variants import find_ocurrence_start_with, find_ocurrence_in_any_part


class Test(TestCase):
    keywords_ = Keywords.list_

    def test_find_ocurrence_start_with_p(self):
        posibilities = find_ocurrence_start_with('p', self.keywords_)
        self.assertListEqual(['pandora', 'paypal', 'pg&e', 'pinterest'], posibilities)

    def test_find_ocurrence_start_with_pr(self):
        posibilities = find_ocurrence_start_with('pr', self.keywords_)
        self.assertListEqual(['press democrat', 'priceline', 'proactive', 'progenex'], posibilities)

    def test_find_ocurrence_start_with_pro(self):
        posibilities = find_ocurrence_start_with('pro', self.keywords_)
        self.assertListEqual(['proactive', 'progenex', 'progeria', 'progesterone'], posibilities)

    def test_find_ocurrence_start_with_prog(self):
        posibilities = find_ocurrence_start_with('prog', self.keywords_)
        self.assertListEqual(['progenex', 'progeria', 'progesterone'], posibilities)

    @unittest.expectedFailure
    def test_find_ocurrence_start_with_PROG(self):
        posibilities = find_ocurrence_start_with('PROG', self.keywords_)
        self.assertListEqual(['progenex', 'progeria', 'progesterone'], posibilities)

    def test_find_ocurrence_in_any_part_a(self):
        posibilities = find_ocurrence_in_any_part('a', self.keywords_)
        self.assertListEqual(['bank', 'kayak', 'pandora', 'paypal'], posibilities)

    def test_find_ocurrence_in_any_part_b(self):
        posibilities = find_ocurrence_in_any_part('b', self.keywords_)
        self.assertListEqual(['bank', 'reprobe'], posibilities)

    def test_find_ocurrence_in_any_part_c(self):
        posibilities = find_ocurrence_in_any_part('c', self.keywords_)
        self.assertListEqual(['press democrat', 'priceline', 'proactive', 'project free tv'], posibilities)
