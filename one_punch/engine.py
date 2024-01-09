import requests
from bs4 import BeautifulSoup

class TestEngine:
	def __init__(self, keyword):
		self.keyword = keyword
		self.data = []

	def create_data(self) -> None:
		rank = 1
		for item in self.keyword:
			rank += 1
			name = item + "name"
			price = item + "price"
			thumb = item + "thumb"
			img_url = item + "img_url"
			# self.data.append([name, price, img_url, rank])
			self.data.append({"name": name, "price": price, "img_url": img_url, "rank": rank})


class Engine:
	pass


class CoupangEngine:
	def __init__(self, keyword):
		self.headers = {
			'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
		}
		self.cookie = {
			"a": "b"
		}
		self.keyword = keyword
		self.base_url = "https://www.coupang.com/np/search?component=&q="
		self.url = self.base_url + self.keyword
		self.data = []
		self.status = None

	def get_data(self):
		response = requests.get(self.url, timeout=5, headers=self.headers, cookies=self.cookie)
		html = response.text
		status = response.status_code
		self.status = status
		soup = BeautifulSoup(html, 'html.parser')
		items = soup.select("[class=search-product]")
		return items

	def create_data(self) -> None:
		items = self.get_data()
		rank = 1
		for item in items:
			name = item.select_one(".name").text
			price = item.select_one(".price-value").text
			thumb = item.select_one(".search-product-wrap-img")
			if thumb.get("data-img-src"):
				img_url = f"http:{thumb.get('data-img-src')}"
			else:
				img_url = f"http:{thumb.get('src')}"
			# self.data.append([name, price, img_url, rank])
			self.data.append({"name": name, "price": price, "img_url": img_url, "rank": rank})
			rank += 1


class NaverEngine:
	pass


class DanawaEngine:
	pass


class EstreetEngine:
	pass






