def circle_area(w):
    area=w*w*3.14
    return area
def circle_circum(s):
    circum=s*2*3.14
    return circum

a=int(input('數字:'))
c=circle_area(a)
print("圓面積: ",c)

r= circle_circum(a)
print('圓周長',r)
