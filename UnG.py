import concurrent.futures
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

init()

def is_uncopylocked(game_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    try:
        with requests.Session() as session:
            response = session.get(game_url, headers=headers)
            response.raise_for_status() # Raise an exception for any non-200 status codes
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[ERROR] Failed to get game info for game url {game_url}: {e}")
        return False

    soup = BeautifulSoup(response.content, 'lxml')
    game_context_menu_div = soup.find('div', {'id': 'game-context-menu'})
    if game_context_menu_div:
        print(Fore.GREEN + f"[SUCCESS] Found an uncopylocked game at: {game_url}")
        with open('UnG.txt', 'a+') as file:
            file.seek(0)
            if game_url in file.read():
                print(Fore.YELLOW + f"[INFO] Game {game_url} already in UnG.txt")
            else:
                file.write(f"{game_url} \n")
                print(Fore.BLUE + f"[INFO] Added game {game_url} to UnG.txt")
        return True
    else:
        print(Fore.YELLOW + f"[INFO] Game {game_url} is not uncopylocked")
        return False

def search_uncopylocked(keyword, start_row, max_rows):
    url = f'https://www.roblox.com/games/list-json?keyword={keyword}&startRows={start_row}&maxRows={max_rows}'

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(Fore.RED + f"[ERROR] Failed to search for games: {response.text}")
            return []

        response_json = response.json()
        game_urls = [game['GameDetailReferralUrl'] for game in response_json]

        for game_url in game_urls:
            is_uncopylocked(game_url)
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to search for games: {e}")
        return []

keyword = input("Enter a keyword to search for uncopylocked games (type 'exit' to quit): ")
while keyword != 'exit':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for start_row in range(0, 9800, 200):
            executor.submit(search_uncopylocked, keyword, start_row, 200)

    keyword = input("Enter a keyword to search for uncopylocked games (type 'exit' to quit): ")
