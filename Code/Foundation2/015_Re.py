import re

txt = "The rain in Spain..."

# Return a list containing all ocurence of 'ai'
results = re.findall("ai", txt)
print(results)

# Return first occurance (of a white-space in this case)
results = re.search("\s", txt)
print(results.start())