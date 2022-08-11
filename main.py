from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
os.system("cls")
import time
product="3080"
old_url=f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={product}&_sacat=0&rt=nc&LH_ItemCondition=1000%7C1500"
new_url=None
names=[]
prices=[]
conditions=[]
links=[]
countries=[]
while True:
    try:
        if old_url != new_url:
            if new_url is not None:
                old_url = new_url
            time.sleep(5)
            result=requests.get(old_url).text
            doc=BeautifulSoup(result,"html.parser")
            tbody=doc.find(class_="srp-results srp-list clearfix")
            items=tbody.find_all(class_="s-item s-item__pl-on-bottom s-item--watch-at-corner")
            for item in items:
                try:
                    href=item.find('a',class_="s-item__link")
                    name=href.text
                    link=href['href']
                    price=item.find('span',class_="s-item__price").text
                    condition=item.find('span',class_="SECONDARY_INFO").text
                    country=item.find('span',class_="s-item__location s-item__itemLocation").text.strip('from ')
                except:
                    pass
                names.append(name)
                prices.append(price)
                conditions.append(condition)
                links.append(link)
                countries.append(country)
            new_url=tbody.find('a',class_="pagination__next icon-link")
            new_url=new_url['href']
            print('done')
        else:
            break
    except:
        pass
to_dic={"Name":names,"Price":prices,"Condition":conditions,"Contry":countries,"Links":links}
df = pd.DataFrame(to_dic)
df.to_excel(f"{product}.xlsx")
print("completed data scraping check now")