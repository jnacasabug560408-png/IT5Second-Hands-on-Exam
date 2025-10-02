import random
class LotteryGame:

  def __init__(self):
    self.winning_numbers = set(random.sample(range(1, 61), 6))

  def play(self, player_numbers):
    if len(player_numbers) != 6:

      return "Invalid input! Must choose 6 numbers."

    player_numbers = set(player_numbers)

    matches = len(self.winning_numbers & player_numbers)


    if matches == 6:
     prize = 1_000_000

    else:
      prize = matches * 1000


    return {

      "Winning Numbers": self.winning_numbers,

      "Player Numbers": player_numbers,

      "Matches": matches,

      "Prize": f"₱{prize:,}"

    }



if __name__ == "__main__":
  print("Enter 6 unique numbers (1–60):")
  numbers = []

  while len(numbers) < 6:

    try:
      n = int(input(f"Number {len(numbers)+1}: "))

      if 1 <= n <= 60 and n not in numbers:
        numbers.append(n)

      else:
        print("Invalid or duplicate number. Try again.")

    except ValueError:
      print("Enter a valid number.")


  game = LotteryGame()
  result = game.play(numbers)


  print("\n--- Lottery Results ---")
  for k, v in result.items():

    print(f"{k}: {v}")