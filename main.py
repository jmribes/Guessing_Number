from game_data import data
from art import logo
from art import vs
import random

A = random.choice(data)
B = random.choice(data)

print(logo)
score = 0
game_continue = True

while game_continue:
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}\n")
  
  election = input("Who has more followers? Type 'A' or 'B': \n")
  if A['follower_count'] > B['follower_count']:
    if election == "A":
      game_continue = True
      score += 1
      print (f"you win, {A['name']} has {A['follower_count']} millions of followers, while {B['name']} has {B['follower_count']} millions of followers\n Score: {score}")
    else:
      game_continue = False
      print(f"you lose, {A['name']} has {A['follower_count']}  millions of followers, while {B['name']} has {B['follower_count']} millions of followers\n Final Score: {score}")
  
  else:
    if election == "A":
      game_continue = False
      print(f"you lose, {A['name']} has {A['follower_count']}  millions of followers, while {B['name']} has {B['follower_count']} millions of followers\n Final Score: {score}")
    else:
      game_continue = True
      score +=1
      print (f"you win, {A['name']} has {A['follower_count']} millions of followers, while {B['name']} has {B['follower_count']} millions of followers\n Score: {score}")

  if game_continue:
    if election == "A":
      pass
    else:
      A = B
    B = random.choice(data)
