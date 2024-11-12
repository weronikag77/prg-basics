#Write a program that prints a popular computer games, each game name on a separate line. 
#Use the while statement. 

computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
computer_games.sort()
n = 0
while n < len(computer_games):
    print(f"{n+1}. {computer_games[n]}")
    n += 1
