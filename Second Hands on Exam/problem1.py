class FlamesGame:

  def __init__(self, name1, name2):
    self.name1 = name1.lower().replace(" ", "")
    self.name2 = name2.lower().replace(" ", "")
    self.flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]

  def remove_common_letters(self):
    list1 = list(self.name1)
    list2 = list(self.name2)

    for char in self.name1:
      
      if char in list2:
       list1.remove(char)
       list2.remove(char)

    return len(list1) + len(list2)


  def get_result(self):
    count = self.remove_common_letters()

    if count == 0:

     return "Not compatible! Single forever </3"


    flames_list = self.flames.copy()

    idx = 0

    while len(flames_list) > 1:
     idx = (idx + count - 1) % len(flames_list)
     flames_list.pop(idx)

    return flames_list[0]


if __name__ == "__main__":

  n1 = input("Enter your name: ")
  n2 = input("Your crush name: ")
  
  game = FlamesGame(n1, n2,)
  print("Result:", game.get_result())