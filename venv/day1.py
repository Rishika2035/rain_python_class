from collections import Counter

text= "Python is an amazing programming language. Python is fun to learn and powerful to use."

words= text.lower().split()
word_count= Counter(words)

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

#Queue
from queue import Queue
task_queue = Queue()
tasks= ["Task 1: Clean the room", "Task 2: Write python code", "Task 3: Read a book"]
for task in tasks:
    task_queue.put(task)

print("Processing tasks:")
while not task_queue.empty():
    print(task_queue.get())

#deque
from collections import deque
import random
#initialize deck of cards
deck= deque([f"{value} of {suit}" for value in
             ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
              for suit in ["Hearts", "Diaomnds", "Clubs", "Spades"]])
#Shuffle the deck
random.shuffle(deck)

#Players and their hands
player1=[]
player2=[]

#Draw 3 cards for each player
for _ in range(3):
    player1.append(deck.popleft())
    player2.append(deck.popleft())

#Display players hands
print("Player 1's Hand:")
print(player1)
print("\nPlayer 2's Hand:")
print(player2)

#grocery list organizer
from collections import Counter
from queue import Queue 
grocery_items={
    "1: Sugar", "2:Rice", "3:Honey", "4:Meat", "5: Vegetables", "6:Fruits", "7:Juice", "8:Bread", "9:Honey", "10:Juice" }
item_count=Counter(grocery_items)
print("Number of groceries:")
for item, count in item_count.items():
    print(f"{item}:{count}")
item_queue= Queue()
for item in grocery_items:
    item_queue.put(grocery_items)
print("Processing items:")
while not item_queue.empty():
    print(item_queue.get())