import sys
import os
import json
from dotenv import load_dotenv
import requests
load_dotenv()
from bs4 import BeautifulSoup

def getGraphQlData(site_endpoint):
  
    query = """{"query":"query GetPostsEdges { documents(first: 2000) {   edges {     node {       id       title       date       content     }   } }}","variables":{}}
"""
    # headers = [{'Content-Type: application/json'}, {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}]
    headers={"Content-Type": "application/json",
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
             } 
    r = requests.post(site_endpoint, data=query, headers=headers)
  
    data =  json.loads(r.text)
    j_Object = data['data']['documents']['edges']
    for edges in j_Object:
     title = edges['node']['title']
     fileName = title.replace(" ","_").replace("?","")
     content=BeautifulSoup(edges['node']['content'],features="html.parser")
     f = open("docs/"+fileName.replace(" ","_")+".txt", "w+")
     f.write(title +"\n\n ")
     f.write(content.get_text())
     f.close()
    return r
    # print("ok")