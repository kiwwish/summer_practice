from bs4 import BeautifulSoup
import requests

link = input("Вставте ссылку на исполнителя в сервисе 'Яндекс-Музыка': ")
try:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    artist = soup.find("h1", class_="page-artist__title typo-h1 typo-h1_big").text
    print(f"10 самых популярных треков исполнителя {artist}: ")
    tracks = soup.find_all("a", class_="d-track__title deco-link deco-link_stronger")
    n = 1
    for track in tracks[:10]:
        print(f"{n}. {track.text}")
        n = n + 1
except (requests.exceptions.MissingSchema,
        requests.exceptions.InvalidURL,
        requests.exceptions.InvalidSchema):
    print("Неверная ссылка! Попробуйте еще раз.")