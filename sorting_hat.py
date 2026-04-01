Q1='Do you like Dawn or Dusk?\n 1) Dawn \n 2) Dusk'
print(Q1)
answear1=int(input('Enter your answear (1-2):'))
Q2="When I’m dead, I want people to remember me as:\n 1) The Good \n 2) The Great\n 3) The Wise\n 4) The Bold"
print(Q2)
answear2=int(input('Enter your answear (1-4):'))
Q3="Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum"
print(Q3)
answear3=int(input('Enter your answear (1-4):'))
G=0
S=0
H=0
R=0
if answear1==1:
    G+=1
    R+=1
elif answear1==2:
    S+=1
    H=+1
else:
    print('Wrong input')
if answear2==1:
    H+=2
elif answear2==2:
    S+=2
elif answear2==3:
    R+=2
elif answear2==4:
    G+=2
else: 
    print('Wrong input')
if answear3==1:
    S+=4
elif answear3==2:
    H+=4
elif answear3==3:
    R+=4
elif answear3==4:
    G+=4 
else:
    print('Wrong input')
print(f'Your house score is: {G} for Gryffindor, {S} for Slytherin, {H} for Hufflepuff, {R} for Ravenclaw')
house={'Gryffindor': G, 'Hufflepuff': H, 'Slytherin':S, 'Ravenclaw':R}
winner=max(house, key=house.get)
print(f'Congrats, you are a {winner}')