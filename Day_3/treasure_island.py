'''This is treasure hunt game'''
# Import the questions, images and messages
import random
import asci
import qq
import msgs
print(asci.TREASURE)
# Welcome the user
print("Welcome to the FUN treasure hunt game")
print("You would need to answer correctly to advance")
print("Are you READY!!!")
# 2. Reveal to user the question and recieve answer to variable 'question'
for count in range(len(qq.Q1) + 1):
    w_display_msg = random.choice(msgs.WIN_MSG)
    question = input(f"{qq.Q1[count]} ").lower()
    if question == qq.A1[count]:
        print(w_display_msg)
    else:
        print(msgs.EXIT_MSG)
        break
