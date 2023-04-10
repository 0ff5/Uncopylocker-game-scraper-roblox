Uncopylocked game scraper for Roblox is a Python script that searches for games containing a specified keyword and checks if they are uncopylocked. The script uses the requests and BeautifulSoup libraries to make requests to the Roblox API and parse HTML responses. It also uses the colorama library to add colored output to the console.

The script contains two functions. The first function, is_uncopylocked, takes a game URL as an argument and checks if the game is uncopylocked by looking for a specific HTML element. If the game is uncopylocked, the function saves the game URL to a text file called "UnG.txt" and prints a message to the console. If the game URL is already in the file, the function prints a message indicating that the game is already in the file.

The second function, search_games, takes a keyword as an argument and searches for games containing that keyword using the Roblox API. It then extracts the game URLs from the API response and returns them as a list.

The script uses a while loop to prompt the user to enter a keyword to search for uncopylocked games. It calls the search_games function to get a list of game URLs and then calls the is_uncopylocked function on each game URL to check if it is uncopylocked. The loop continues until the user enters "exit".
![Screenshot_1](https://user-images.githubusercontent.com/88597330/230805680-2ad5726a-6e9a-4ec3-8450-f1c91cae7a5c.png)
![Screenshot_2](https://user-images.githubusercontent.com/88597330/230805698-0ff02462-a79d-4229-bb0c-fe8c696ad6fd.png)
