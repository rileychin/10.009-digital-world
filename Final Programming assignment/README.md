# *Digital World final programming assignment, accordiun*

## Done By:
* Riley Riemann Chin F08 1004147


### Table of contents
*Introduction
*Prerequisites
*How to run
*How to play
*My Code
*Acknowledgements
*Link to video 


# Introduction 
Welcome to my final digital world assignment README. This file will cover all the basics and need-to-knows
of my game. The game is called accordiun, it is loosely based on the popular card game accordion, with a slight 
twist of my own. This game is a single player game, and is run on a kivy window. 


## Prerequisites
You will need the following to run the game:
*Python3
*Kivy 
*A copy of my final assignment code contained in a .rar file


### How to run
*Download the .rar file, and run the file "RileyRiemannChinF08_finalkivy.py" it will automatically open and display a kivy window. 


#### How to play
*A deck of 52 cards will be shuffled and split into 4 rows and 13 columns. The objective of the game is to stack all the cards into one pile.
But you can only stack cards that are in the same row, and they must either be in the same suit, or same value. A simple game but it is much easier
said than done. You can stack multiple cards together(e.g more than 2 cards) if they all follow the same suit or value. For example,
in Row 1, there is a 6 hearts, 6 diamonds and 6 clubs. The first card you click will be the stacked card, and the rest will be stacked below it. 
So once you click confirm, you will have 6 hearts, and the 6 diamonds and 6 clubs will be removed from the grid, and the first 2 cards of Row 2 will
move up to Row 1.


#### My Code
# Part 1, The deck (found in RileyRiemannChinF08_final.py)
*The deck of cards was created seperately from the game, in an earlier attempt to recreate another card game. I reused the same code to generate the deck
of cards by importing the classes used. To create a card, I used a class called Card, that was initialized to have a suit and value as its attribute. 
I then created a Deck class, which had a method called create_deck such that it would generate 52 cards from Ace to King and from the 4 suits available. 
I then had an in built shuffle function that was able to shuffle the deck of cards by creating a new list and adding cards at random positions using 
.insert() function, and then assigning 

# Part 2, The game(found in RileyRiemannChinF08_finalkivy.py)
*The main game is found in a kivy class called accordiun, which inherits attributes from the App class. The main functionalities are found in the build(self) method.
The root widget is in a boxlayout format. There is 2 components that make up the display, the top component and the bottom component. The top component 
is a box layout with a horizontal orientation, with a main label on the left and 3 buttons on the right. The 3 buttons are namely "Confirm", "Cancel", "Reset Game"

**The confirm button is to confirm a user's actions when he has selected the cards. It is binded to an event method called "validate", this validate method confirms the 
user's actions and ensures the rules of the game are met before he can advance to his next move. 
The cancel button is to cancel a user's actions, this is just shown from the erasing of everything from the main label.
The reset game button is an option for a user to restart a new game. the new game will have a different shuffled deck 
and is used more or less if the player cannot find any more moves to advance and win the game. 

***The bottom component on the kivy application consists of images that are actually buttons. They are called ImageButton inherited from the ButtonBehaviour and Image class
such that it has an image and acts like button. The layout consists of a GridLayout with 4 rows and 13 columns. Each cell is populated with an ImageButton and corresponds 
to a certain card in the deck of cards. The images are downloaded online and are used in this application. 

****When a user clicks on a card, the main label will update its text with a shorthand notation for the card's value and its suit. For example, if its a King of Hearts it will
display "KH", additional clicks on the same card will not be added to main label as there is a check done using a simple form of state management. The game starts at state 1, 
then transitions to state 2 when a user clicks on a card. The next time the user clicks on the same card, there will be a checking to condition to check if the card's 
shorthand notation is already inside the main label, so it will not add it again. 

*****When a user confirms his choice and clicks confirm, the program will check if the cards selected are of valid combination(same suit, same value, same row). 
It does this by already having a pre exisiting list with sublists in to show the index(i.e row and column) of each card. The program will loop through the list 
and find the corresponding cards. It will then check the cards for the same row condition by just checking if its in the same sublist. Then it will check the 
same suit condition by checking the second letter of the shorthand notation. Subsequently it checks the same value by checking the first letter of the shorthand notation
If the same row condition is satisfied, and either the same suit or same value condition is satisfied, it will remove the cards from the grid and from the list itself. 



#####Acknowledgements
*Libraries used. 
-kivy
-random

###### Link to video
* https://youtu.be/pw3EzTHtiPY



 