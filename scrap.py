import bs4
import requests

print("################# All Header finder from wikipedia page #####################"+"\n\n\n")

print("Please enter article name for wikipedia :")
url="https://en.wikipedia.org/wiki/"+input()


res=requests.get(url)
soup=bs4.BeautifulSoup(res.text,'html.parser')
print("\nList of Headers:-")
allHeading=soup.select('.mw-headline')
for head in soup.findAll('span',{'class':'mw-headline'}):
	print("   ->"+head.text)
# print (allHeading)