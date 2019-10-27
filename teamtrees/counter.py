import requests
import bs4


def get_trees_count(url="https://teamtrees.org/"):
    """
    Get the amount of trees planted
    :param url: Link to the TeamTrees website
    """
    resp = requests.get(url)
    assert resp.ok
    doc = bs4.BeautifulSoup(resp.text, features="html.parser")
    return int(doc.select_one("#totalTrees")["data-count"])
