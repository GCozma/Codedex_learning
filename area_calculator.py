import math
print('==================\nArea Calculator 📐\n==================')
menu='1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit'
print(menu)
select=int(input('Which schape:'))
if select==3:
    side=int(input('Insert side:'))
    area=side**2
    print(f'Area of the square is: {area}')
elif select==2:
    lenght=int(input('Insert lenght:'))
    width=int(input('Insert widht:'))
    area=lenght*width
    print(f'Area of the rectangle is: {area}')
elif select==1:
    height=int(input('Insert the height:'))
    base=int(input('Insert the base:'))
    area=(height*base)/2
    print(f'Area of the triangle is: {area}')
elif select==4:
    radius=int(input('Inser the radius:'))
    area=math.pi*radius**2
    print(f'Area of the circle is: {area}')
else:
    print('Closing the menu, see you next time :)')

