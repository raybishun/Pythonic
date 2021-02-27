from objects.utils.utility_stuff import ListAndCharShortner, DictionaryShortner

my_shortner = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebeca', 4: 'mike', 5: 'paul'})
my_shortner.print_original_items()
my_shortner.print_shortened_items()