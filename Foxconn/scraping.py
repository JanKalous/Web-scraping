from selenium import webdriver
import pandas as pd
import numpy as np
import os.path, time
website = r"https://www.contextures.com/xlsampledata01.html"
path = r"C:\Users\hkalo\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(website)

rows = driver.find_elements_by_tag_name('tr')

order_date = []
region = []
rep = []
item = []
units = []
unit_cost = []
total = []

for row in rows:
    order = (row.find_element_by_xpath('./td[1]').text)
    order_date.append(order)
    regi = (row.find_element_by_xpath('./td[2]').text)
    region.append(regi)
    repp = (row.find_element_by_xpath('./td[3]').text)
    rep.append(repp)
    it = (row.find_element_by_xpath('./td[4]').text)
    item.append(it)
    un = (row.find_element_by_xpath('./td[5]').text)
    units.append(un)
    unco = (row.find_element_by_xpath('./td[6]').text)
    unit_cost.append(unco)
    tot = (row.find_element_by_xpath('./td[7]').text)
    total.append(tot)
    print(tot)
driver.quit()
df = pd.DataFrame({"OrderDate": order_date, "Region": region, "Rep": rep, "Item": item, "Units": units, "UnitsCost":unit_cost, "Total": total})

df.drop(0, inplace=True)
df['Discount'] = np.where(df['Region']== 'Central', 0.23, 0.12)

df["Units_int"] = df["Units"].astype("int")
df["UnitCost_int"] = df["UnitsCost"].astype("float")
df['ExtraDiscount'] = np.where((df['Region']== 'East') & (df["Units_int"] > 50),7.2,0)
df['FinalDiscount'] = (df['Units_int'] * df['Discount']) + df['ExtraDiscount']
df['FinalPrice'] = (df['Units_int'] * df['UnitCost_int']) - df['FinalDiscount']
df['CreationDate'] = time.ctime(os.path.getctime(r'C:\Users\hkalo\naucse-python\Foxconn'))
df.to_csv("datafox.csv", index=False)
print(df)