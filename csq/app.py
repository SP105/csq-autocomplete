from csq.AbstractClass import AbstractClass
from csq.autocompletition.binary_search import find_ocurrence_binary_search
from csq.autocompletition.simple_variants import find_ocurrence_in_any_part, find_ocurrence_start_with
from csq.dictionaries.keywords import Keywords, WikiWords


class App(AbstractClass):
    def __init__(self):
        super().__init__()
        self.keywords = Keywords.list_
        self.autocomplete = None

    @staticmethod
    def _get_function(val: int):
        return {
            1: find_ocurrence_start_with,
            2: find_ocurrence_in_any_part,
            3: find_ocurrence_binary_search,
        }.get(val)

    def select_autcomplente_function(self):
        while True:
            try:
                print("Please select on of:")
                print("[1] - Match the start of the keyword")
                print("[2] - Match any portion of the keyword")
                print("[3] - Match the start of the keyword (binary search)")
                val = int(input())
                if val not in [1, 2, 3]:
                    raise ValueError
                self.autocomplete = self._get_function(val)
            except ValueError:
                print("Sorry, that was not an option.", end='\n\n')
                continue
            else:
                break

    def run(self):
        print("Press Ctrl-C to terminate the program")
        self.select_autcomplente_function()
        self.choose_keywords()
        self.keywords.sort()

        try:
            while True:
                input_str = input("Please enter a string:\n").lower()
                words = self.autocomplete(input_=input_str,
                                          keywords=self.keywords)

                print("The posibilities founds are:", end='\n')
                print(words, end='\n\n')
        except KeyboardInterrupt:
            print("**************")
            print("Procces finish")
            print("**************")

    def choose_keywords(self):
        while True:
            try:
                print("Do you want to use the WikiWords dataset?")
                print("[1] - Yes")
                print("[2] - No")
                val = int(input())
                if val not in [1, 2]:
                    raise ValueError
                self.keywords = WikiWords().list_ if val == 1 else self.keywords
            except ValueError:
                print("Sorry, that was not an option.", end='\n\n')
                continue
            else:
                break
