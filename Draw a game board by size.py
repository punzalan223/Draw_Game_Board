
top_size = int(input("Enter the size: "))
print('x ',end='')
middle_size = int(input(""))
print(top_size,'x',middle_size)
top = ' --- '
middle = '|   |'
board_top_size = top * top_size
board_middle_size = middle * top_size
print(board_top_size)
print(board_middle_size)
print(board_top_size)
for i in range(middle_size-1):
    print(board_top_size)
    print(board_middle_size)
    print(board_top_size)