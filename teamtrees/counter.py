import requests
import bs4


def get_trees_count():
    resp = requests.get("https://teamtrees.org")
    assert resp.ok
    doc = bs4.BeautifulSoup(resp.text)
    return int(doc.select_one("#totalTrees")["data-count"])
