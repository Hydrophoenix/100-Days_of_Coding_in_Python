'''This program marks a spot with an "X"'''
row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]
Map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")
position = input("Where do you want to put the treasure?(NB: Use a two digit number, with each digit being between 0 and 2) ")
x = int(position[0])
y = int(position[1])
# check if the digits fall within 0 and 2
if x >= 0 or x <= 2:
    if y >= 0 or y <= 2:
# if yes insert 'X' in the appropriate place
        Map[x][y] = "X"
        print(f"{row_1}\n{row_2}\n{row_3}")
else:
    print("Can't find this location on the map!")
