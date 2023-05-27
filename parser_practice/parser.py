import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://kaktus.media/'
HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
	}

@csrf_exempt
def get_html(url, params = ''):
	req = requests.get(url, headers = HEADERS)
	return req

@csrf_exempt
def get_data(html):
	soup = BS(html, 'html.parser')
	items = soup.find_all('div', class_ = "ArticleItem--data ArticleItem--data--withImage")
	kaktus_news = []
	
	for item in items:
		kaktus_news.append(
				{
					'img': URL + item.find('img', class_='ArticleItem--image-img ls-is-cached lazyloaded').get('src'),
					'title': URL + item.find('a', class_='ArticleItem--name').get_text(),
					'time': item.find('div', class_='ArticleItem--time').get_text()
					}
				)
	return kaktus_news

@csrf_exempt
def parser():
	html = get_html(URL)
	if html.status_code == 200:
		kaktus_news_1 = []
		for page in range(0, 1):
			html = get_html(f'https://kaktus.media/?lable=8&date=2022-12-06&order=time', params = page)
			kaktus_news_1.extend(get_data(html.text))
		return kaktus_news_1
	else:
		raise Exception('error in parser func...')

	
	