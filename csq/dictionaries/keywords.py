from dataclasses import dataclass

from csq.AbstractClass import AbstractClass


@dataclass
class Keywords(AbstractClass):
    list_ = ['project runway', 'pinterest', 'river', 'kayak',
             'progenex', 'progeria', 'pg&e', 'project free tv',
             'bank', 'proactive', 'progesterone', 'press democrat',
             'priceline', 'pandora', 'reprobe', 'paypal', ]


@dataclass
class WikiWords(AbstractClass):
    list_ = []

    def __init__(self):
        super().__init__()
        self.list_ = self._load_file('../data/WikiWords_FirstMillion_Refined_V6.csv')
        self.list_.sort()
