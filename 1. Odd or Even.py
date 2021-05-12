# Date: 12 May 2021
# Author: Nathaniel Fernandes
# Description: When run, the user is asked to enter a number and we'll calculate if it's odd or even!
# Difficulty: 1/10

want_to_play = input("Howdy! Do you want to play a game (Y/N): ")

while want_to_play in ("Y", "y", "yes", "yup"):
    num = int(input("Pick a positive number and I'll tell you if it's odd or even: "))
    is_even = "even" if abs(num) % 2 == 0 else "odd"

    print("%d is %s" % (num, is_even))
    want_to_play = input("Do you want to play again?: ")


# Learned
# 1. input returns a string, so coerce to int before do any calculations! (Line 4y)
# 2. The ternary operator:  [on_true] if (condition) else [on_false]
# 3. String formatting with the % sign
