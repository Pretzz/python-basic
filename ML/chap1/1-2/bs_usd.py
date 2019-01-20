from bs4 import BeautifulSoup
import urllib.request as req


url = "https://finance.naver.com/marketindex/"

req = req.urlopen(url)

soup = BeautifulSoup(req, "html.parser")

usd = soup.select_one("#exchangeList").select_one("a.usd")
value = usd.select_one("span.value").string
print(value)