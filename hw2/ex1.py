import cfscrape
from bs4 import BeautifulSoup

# Використання cfscrape замість requests для обходу Cloudflare
scraper = cfscrape.create_scraper()
response = scraper.get('https://4pda.to/forum/index.php?showtopic=1086877')

# Перевіряємо статус запиту
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

    # Ваш код для парсингу коментарів
    comments = soup.find_all('table', class_='ipbtable')

    for comment in comments:
        post_body = comment.find('div', class_='postcolor')
        if post_body:
            comment_text = post_body.text.strip()
            print(comment_text)
else:
    print(f"Не вдалося отримати сторінку. Статус-код: {response.status_code}")


