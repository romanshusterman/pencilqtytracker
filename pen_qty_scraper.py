#!/usr/bin/env python
# coding: utf-8

# In[154]:


from selenium import webdriver
from bs4 import BeautifulSoup
import os
import datetime


# In[175]:


PATH_GD = '⁨Macintosh HD⁩/⁨Users⁩/romandavydov⁩/⁨Documents/chromedriver.exe⁩'


# In[176]:


driver = webdriver.Chrome(PATH_GD)


# In[177]:


website = driver.get('https://www.ilmakiage.co.il/mineral-lip-pencil-4043')


# In[178]:


for _ in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup1 = driver.page_source.encode("utf-8")

driver.close()


# In[179]:


soup = BeautifulSoup(soup1, 'lxml')


# In[180]:


try:
    soup.find('span', class_='qtyValidate_color', style='display: block;').contents[0] == 'הכמות המבוקשת אינה קיימת'
    qty_validate = soup.find('span', class_='qtyValidate_color', style='display: block;').contents[0]
    result = f'Ooops, the stock is empty ({qty_validate}). Open the app later to check quantity \n'
except AttributeError as err:
    result = "Tut sheli, it'shopping time, your favorite lip pencil is in stock \n https://www.ilmakiage.co.il/mineral-lip-pencil-4043 \n"


# In[190]:

current_time = datetime.datetime.now()
with open('Desktop/Masterschool/Selenium_Scraper_Lip_Pencil/rand2.txt', mode='a') as file:
    file.write(f"{current_time}, {result}")


# In[ ]:
import boto3
if result == "Tut sheli, it'shopping time, your favorite lip pencil is in stock \n https://www.ilmakiage.co.il/mineral-lip-pencil-4043 \n":
    ses_client = boto3.client("ses", region_name="ap-northeast-1")
    CHARSET = "UTF-8"

    response = ses_client.send_email(
    Destination={
            "ToAddresses": [
                "nogabrami@gmail.com",
            ],
        },
    Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": result,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Velvet pink color lip pencil is available",
            },
        },
    Source="shuster.landing@gmail.com",
    )




# In[ ]:





# In[ ]:
