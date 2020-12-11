import requests
import bs4
import re


url = input("Enter The Url : ")
file_name = input("Enter File : ")


if url == '':
       print("Please Enter Url")

elif file_name == '':
       print("Enter File Name")

elif re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', url):
      
       res = requests.get(url)
       html = bs4.BeautifulSoup(res.text, "html.parser")
       html.prettify()
       links = html.select("a")
       
       for link in links:
              data = link.get("href")
              
              f = open(file_name+'.txt', 'a+')
              file = f" \n Link : {data}"
              f.write(file)


else:
       print("InValid url")

