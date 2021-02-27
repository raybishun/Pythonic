class Shortner:
    def __init__(self, items):
        self.original_items = items

    def print_original_items(self):
        print(self.original_items)

class ListAndCharShortner(Shortner):
    def print_shortned_items(self):
        print(self.original_items[0:3])

class DictionaryShortner(Shortner):
    def print_shortened_items(self):
        # original_items = {1: 'mike', 2: 'tom', 3: 'rebeca', 4: 'mike', 5: 'paul'}
        dict = self.original_items
        counter = 0
        result_dict = {}
        for(k, v) in dict.items():
            if(counter < 3):
                result_dict.update({k: v})
                counter += 1
        print(result_dict)



# Consumer Tests
# -----------------------------------------------------------------------------
# my_shortner = ListAndCharShortner("This is a sentence")
# my_shortner = ListAndCharShortner([1, 2, 3, 4, 5])
# my_shortner.print_shortned_items()
# my_shortner.print_original_items()

# my_shortner = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebeca', 4: 'mike', 5: 'paul'})
# my_shortner.print_original_items()
# my_shortner.print_shortened_items()