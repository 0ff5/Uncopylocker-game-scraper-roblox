import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

# Initialize colorama module
init()

# Function to check if a game is uncopylocked
def is_uncopylocked(game_id):
    url = f'https://www.roblox.com/games/{game_id}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    # Make a request to the game page
    response = requests.get(url, headers=headers)

    # If the request fails, return False
    if response.status_code != 200:
        print(Fore.RED + f"[ERROR] Failed to get game info for game id {game_id}: {response.text}")
        return False

    # Check if the game is uncopylocked
    soup = BeautifulSoup(response.text, 'html.parser')
    game_context_menu_div = soup.find('div', {'id': 'game-context-menu'})
    if game_context_menu_div:
        print(Fore.GREEN + f"[SUCCESS] Found an uncopylocked game at: {url}")
        with open('UnGames.txt', 'a') as file:
            file.write(f"{url}\n")
        return True
    else:
        print(Fore.YELLOW + f"[INFO] Game {game_id} is not uncopylocked")
        return False

# Function to search for games with a keyword
def search_games(keyword):
    url = f'https://www.roblox.com/games/list-json?keyword={keyword}&startRows=0&maxRows=100'

    # Make a request to the API to search for games
    response = requests.get(url)

    # If the request fails, return an empty list
    if response.status_code != 200:
        print(Fore.RED + f"[ERROR] Failed to search for games: {response.text}")
        return []

    # Get the response JSON
    response_json = response.json()

    # Extract the game IDs from the response
    game_ids = [game['PlaceID'] for game in response_json]

    return game_ids

# Example usage of the functions
while True:
    keyword = input("Enter a keyword to search for uncopylocked games (type 'exit' to quit): ")
    if keyword == 'exit':
        break

    game_ids = search_games(keyword)
    for game_id in game_ids:
        is_uncopylocked(game_id)
