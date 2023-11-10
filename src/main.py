#   bnk-web-scaping

import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os

r = requests.get("https://www.bnk48.com/index.php?page=members")
soup = BeautifulSoup(r.text, "lxml")

detail = soup.find("div", {"class": "boxMembersClass"})
div_tags = detail.find_all("div")
URL = "https://www.bnk48.com/"

for div_tag in div_tags:
    try:
        url = div_tag.find("div")["style"]
        url_sub = re.split("url\\(", url)
        url_sub = url_sub = re.split("\\);", url_sub[1])
        url_image = URL + url_sub[0]

        mem_name = div_tag.find("div", {"class": "boxnameMem"})
        info_personal = mem_name.text.split()
        print(info_personal[:], url_image, end="\n")
        full_filename = os.path.join("./src/source_images", info_personal[0] + ".png")
        print("foll_filename", info_personal[0])
        urllib.request.urlretrieve(url_image, full_filename)
    except Exception as e:
        pass
