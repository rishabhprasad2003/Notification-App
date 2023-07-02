import random

# Unicode characters \u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518
#                       ●      ┌      ─      ┐      │      └     ┘


dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

num_of_dice = int(input("Enter the number of dice to roll: "))
dice_nums = []

for dice in range(num_of_dice):
    dice_nums.append(random.randint(1,6))


# to get all the dice in different rows
# for i in range(num_of_dice):
#     for j in dice_art.get(dice_nums[i]):
#         print(j)

# to get all the dice in a single row
for line in range(5):
    for die in dice_nums:
        print(dice_art.get(die)[line],end=" ")
    print()

print(f"Total: {sum(dice_nums)}")


