import requests
from bs4 import BeautifulSoup


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
		self.data = []
		rank = 1
		for item in items:
			rank += 1
			name = item.select_one(".name").text
			price = item.select_one(".price-value").text
			thumb = item.select_one(".search-product-wrap-img")
			if thumb.get("data-img-src"):
				img_url = f"http:{thumb.get('data-img-src')}"
			else:
				img_url = f"http:{thumb.get('src')}"

			# self.data.append([name, price, img_url, rank])
			self.data.append([name])


class NaverEngine:
	pass


class DanawaEngine:
	pass


class EstreetEngine:
	pass






