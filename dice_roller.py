import random
def main():
  dice_rolls = 2
  dice_sum = 0
  for turn in range(dice_rolls):
    roll = random.randint(1,6)
    dice_sum+=roll
    print(f'You rolled a {roll}')
  print(f"total sum {dice_sum}")
if __name__== "__main__":
  main()
