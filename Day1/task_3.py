import bs4

""" Open and get text from file """
with open("./Day1/index.html", "r") as html_file:
      html = bs4.BeautifulSoup(html_file.read(), "html.parser")

""" Find text """
p = html.find("p").getText()
title = html.find("title").getText()

""" Print it """
print(title)
print(p)