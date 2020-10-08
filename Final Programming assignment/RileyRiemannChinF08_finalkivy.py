#Making block eleven or accordion

import RileyRiemannChinF08_final as r 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

deck = r.Deck() # creating a deck of cards

class ImageButton(ButtonBehavior,Image):
  def __init__(self,**kwargs):
    super(ImageButton,self).__init__(**kwargs)
    self.value_suit = None
  

class MyButton(Button):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.size = (50,50)
    self.valign = 'middle'
    self.halign = 'center'
    self.padding = (20,20)


class accordiun(App):
  def build(self):
    self.root= BoxLayout(orientation = 'vertical')
    self.reset = 0
    self.state = 0 #game state to check whether options are valid or not 
    #0 is not started
    #1 is when cards are generated
    #2 is when player starts adding to the pile
    
    top_layout = BoxLayout(orientation = 'horizontal')
    self.main_label = Label(text = 'Welcome to Accordion!',font_size = 20)
    top_layout.add_widget(self.main_label)

    button_grid = GridLayout(cols = 1, rows = 3,row_default_height=40)
    button_confirm = MyButton(text= 'Confirm',pos = (100,100),on_press = self.validate)
    button_cancel = MyButton(text = 'Cancel', pos = (200,200), on_press = self.remove_options)
    button_reset = MyButton(text = 'Reset game',on_press = self.generate_cards)
    button_grid.add_widget(button_confirm)
    button_grid.add_widget(button_cancel)
    button_grid.add_widget(button_reset)
    top_layout.add_widget(button_grid)

    self.root.add_widget(top_layout)

    self.generate_cards(button_reset) #button reset is the self


    return self.root

  def generate_cards(self,instance):
    self.state = 1
    if self.reset > 0:
      self.root.remove_widget(self.GL1)
      self.main_label.text = "Welcome to Accordion!"
    self.reset += 1
    deck = r.Deck()
    self.GL1 = GridLayout(cols = 13, rows = 4,spacing = 5)
    pic_file = '.jpg'

    self.button_list = []
    self.overall_list = []
    accordion_list = []
    sublist = []
    for i in range(52):
      button = ImageButton()
      card = str(deck.drawCard())
      print(card)

      if 'Spades' in card:
        pic_file = 'S' + pic_file
      elif 'Hearts' in card:
        pic_file = 'H' + pic_file
      elif ' Clubs' in card:
        pic_file = 'C' + pic_file
      elif 'Diamonds' in card:
        pic_file = 'D' + pic_file
      
      if 'Ace' in card:
        pic_file = 'A' + pic_file
      elif '2' in card:
        pic_file = '2' + pic_file
      elif '3' in card:
        pic_file = '3' + pic_file
      elif '4' in card:
        pic_file = '4' + pic_file
      elif '5' in card:
        pic_file = '5' + pic_file
      elif '6' in card:
        pic_file = '6' + pic_file
      elif '7' in card:
        pic_file = '7' + pic_file
      elif '8' in card:
        pic_file = '8' + pic_file
      elif '9' in card:
        pic_file = '9' + pic_file
      elif '10' in card:
        pic_file = 'T' + pic_file
      elif 'Jack' in card:
        pic_file = 'J' + pic_file
      elif 'Queen' in card:
        pic_file = 'Q' + pic_file
      elif 'King' in card:
        pic_file = 'K' + pic_file

      button.bind(on_press = self.on_press)

      button.source = pic_file
      button.value_suit = pic_file.strip('.jpg')
      self.overall_list.append(button.value_suit)
      sublist.append(button.value_suit)
      if len(sublist) == 13:
        accordion_list.append(sublist)
        sublist = []

      self.button_list.append(button)
      self.GL1.add_widget(button)
      pic_file = '.jpg'

    self.accordion_list = accordion_list
    print(self.overall_list)
    print(self.accordion_list)
    self.root.add_widget(self.GL1)

  def on_press(self,instance): #when a card is pressed, do a thing
    if self.state == 1: #game started, player has clicked on a card
      self.main_label.text = instance.value_suit + ","
      self.state = 2
    elif self.state == 2: #game is ongoing, with player adding more cards to the pile
      if instance.value_suit not in self.main_label.text:
        self.main_label.text += instance.value_suit + ","
      else:
        pass

  def remove_options(self,instance): #when cancel is pressed remove all options
    self.state == 1
    # try:
    #   self.main_label.text = ''
    # except:
    #   pass
    self.main_label.text = ''
  def validate(self,instance): #player confirms his move
    splitted_list = self.main_label.text.split(',')
    splitted_list.pop()
    print(splitted_list)
    if len(splitted_list) <= 1:
      self.state = 1
    else:
      suit_check = 0
      value_check = 0

      is_in_same_row = False
      is_in_same_suit = False
      is_in_same_value = False

      same_row = []
      first_suit = splitted_list[0][1]
      first_value = splitted_list[0][0]


      for i in splitted_list: #check if in the same row
        for j in range(len(self.accordion_list)):
          if i in self.accordion_list[j]:
            same_row.append(j)
      same_row = list(set(same_row))
      if len(same_row) == 1:
        is_in_same_row = True
      else:
        self.main_label.text = "Not all are in the same row!"

      if splitted_list[1][0] == first_value:
        value_check = 1
      elif splitted_list[1][1] == first_suit:
        suit_check = 1


      for i in range(len(splitted_list)): #checks for same suit or same value
        print("suit", splitted_list[i][1], "value", splitted_list[i][0])
        if suit_check == 1:
          if splitted_list[i][1] == first_suit:
            if i == len(splitted_list) - 1:
              is_in_same_suit = True
          else:
            self.main_label.text = "Invalid combination!"
            break
        elif value_check == 1:
          if splitted_list[i][0] == first_value:
            if i == len(splitted_list) - 1:
              is_in_same_value = True
          else:
            self.main_label.text = "Invalid combination"
            break
        else:
          self.main_label.text = "Invalid combination!"
          break

      print(is_in_same_value,is_in_same_suit,is_in_same_row)
      if is_in_same_row == True and (is_in_same_suit == True or is_in_same_value == True):
        self.main_label.text = ""
        for i in splitted_list[1:]: #remove the other elements in the list.
          self.overall_list.remove(i)
          for j in self.button_list:
            if j.value_suit == i:
              self.GL1.remove_widget(j)

        self.accordion_list = []
        sublist = []
        for i in self.overall_list:
          sublist.append(i)
          if len(sublist) == 13:
            self.accordion_list.append(sublist)
            sublist = []
        if len(sublist) > 0:
          self.accordion_list.append(sublist)

      print(self.overall_list,'\n',self.accordion_list)
      
      if len(self.overall_list) == 1:
        self.main_label.text = "Congratulations you won the game!" 


      self.state = 1

accordiun().run()