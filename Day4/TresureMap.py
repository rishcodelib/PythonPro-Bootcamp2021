# Making it like a Martix Map

row0 = ["0","1" ,"2"]
row1 = ['_','_','_']
row2 = ['_','_','_']
row3 = ['_','_','_']

TresureMap = [row1,row2,row3]

print(f"  {row0} \n\n0 {row1}\n\n1 {row2}\n\n2 {row3}")

position = input("Where do you want to put the tresure? ")
h = int(position[0])
v= int(position[1])

TresureMap[h][v]="*"



print(f"  {row0} \n\n0 {row1}\n\n1 {row2}\n\n2 {row3}")
