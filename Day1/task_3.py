import re

# -- Open and get text from file --
html_file = open("./Day1/index.html", "r")
html = html_file.read()
html_file.close()

# -- Find text -- 
text = "My super text"
list_1 = re.findall(text, html)
print(list1)
