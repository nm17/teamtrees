import bs4
import pandas as pd
import pytz
import requests
import datetime


def _get_donations(top, url="https://teamtrees.org/"):
    resp = requests.get(url)
    assert resp.ok
    doc = bs4.BeautifulSoup(resp.text, features="html.parser")
    df = pd.DataFrame(columns=["Name", "DateTime", "Amount", "Message"])
    for el in doc.select(
        "{} > div".format("#top-donations" if top else "#recent-donations")
    ):
        date = el.select_one("p:nth-child(2) > span:nth-child(3)").text
        date = datetime.datetime.fromisoformat(date[: date.find(".")])
        date = pytz.utc.localize(date)
        df = df.append(
            {
                "Name": el.select_one("p:nth-child(2) > strong:nth-child(1)").text,
                "DateTime": date,
                "Amount": int(
                    el.select_one("p:nth-child(2) > span:nth-child(2)")
                    .text.split()[0]
                    .replace(",", "")
                ),
                "Message": el.select_one("p:nth-child(2) > span:nth-child(4)").text,
            },
            ignore_index=True,
        )
    return df


def get_top_donations(url="https://teamtrees.org/"):
    return _get_donations(True, url)


def get_recent_donations(url="https://teamtrees.org/"):
    return _get_donations(False, url)
