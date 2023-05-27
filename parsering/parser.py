import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'http://www.manascinema.com'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

@csrf_exempt
def get_html(url, params=''):
	req = requests.get(url, headers = HEADERS)
	return req

@csrf_exempt
def get_data(html):
	soup = BS(html, 'html.parser')
	items = soup.find_all('div', class_="short_movie_info")
	manas_film = []
	
	for item in items:
		manas_film.append(
				{
					'title': URL + item.find('a').get('href'),
					'title_text': item.find('div', class_='m_title').get_text(),
					'img': URL + item.find('div', class_='m_thumb').find('img').get('scr')
					}
				)
	return manas_film

@csrf_exempt
def parser():
	html = get_html(URL)
	if html.status_code == 200:
		manas_film_1 = []
		for page in range(0,1):
			html = get_html(f'http://www.manascinema.com/movies', params=page)
			manas_film_1.extend(get_data(html.text))
		return manas_film_1
	else:
		raise Exception('error in parser func...')
	