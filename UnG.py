import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

init()

# Function to check if a game is uncopylocked
def is_uncopylocked(game_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    response = requests.get(game_url, headers=headers)

    if response.status_code != 200:
        print(Fore.RED + f"[ERROR] Failed to get game info for game url {game_url}: {response.text}")
        return False

    soup = BeautifulSoup(response.text, 'html.parser')
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

# Function to search for games with a keyword
def search_games(keyword):
    url = f'https://www.roblox.com/games/list-json?keyword={keyword}&startRows=0&maxRows=150'


    response = requests.get(url)

    if response.status_code != 200:
        print(Fore.RED + f"[ERROR] Failed to search for games: {response.text}")
        return []

    response_json = response.json()
    game_urls = [game['GameDetailReferralUrl'] for game in response_json]

    return game_urls

while True:
    keyword = input("Enter a keyword to search for uncopylocked games (type 'exit' to quit): ")
    if keyword == 'exit':
        break

    game_urls = search_games(keyword)
    for game_url in game_urls:
        is_uncopylocked(game_url)
