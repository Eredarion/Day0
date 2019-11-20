import bs4

# -- Open and get text from file --
html_file = open("./Day1/index.html", "r")
html = bs4.BeautifulSoup(html_file.read(), "html.parser")
html_file.close()

# -- Find text --
p = html.find("p").getText()
title = html.find('title').getText()

print(title)
print(p)