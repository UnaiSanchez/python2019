moves =[]
def move(origin, destination):
    moves.append([origin,destination])
def hanoi(num_of_disk, origin, temporary, destination):
    if num_of_disk == 0:
        pass
    else:
        hanoi(num_of_disk -1,origin,destination,temporary)
        move(origin,destination)
        hanoi(num_of_disk -1,temporary, origin, destination)  
hanoi(2, 0,1,2)
print(moves)