# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""

import sys
import urllib.request
from bs4 import BeautifulSoup

url = sys.argv[1]
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

def get_tags(html):
    return [meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"})]

def get_title(html):
    return soup.find("title").text.strip()
