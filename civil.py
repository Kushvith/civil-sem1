import time
are = []
sumx = []
sumy = []
def rect(a,b,c = 0, d=0):
   
    
    area = a*b
    are.append(area) 
    x = float((a/2))+c
    sumx.append(x) 
    y= float((b/2))+d
    return f'the area of recatangle is {area} x is {x} and y is {y}'

def triangle(a, b, c=0, d=0):
    area = a*b/2
    are.append(area)
    x = a/3+c
    sumx.append(x)
    y= b/3+d
    sumy.append(y)
    return f'the area of triangle is {area} x is {x} and y is {y}'

def circle(a, c=0, d=0):
    area = 3.14*a*a
    are.append(area)
    x = a
    sumx.append(x)
    y= a
    sumy.append(y)
    return f'the area of circle is {area} x is {x} and y is {y}'

def semicircle(a, c=0, d=0):
    area = 3.14*a*a/2
    are.append(area)
    x = float(4*a/(3*3.14)) 
    sumx.append(x)
    y= a*4/3*3.14
    sumy.append(y)
    return f'the area of semicircle is {area} x is {x} and y is {y}'

def quadcircle(a, c=0, d=0):
    area = 3.14*a*a/4
    are.append(area)
    x = 4*a/3*3.14
    sumx.append(x)
    y= a*4/3*3.14
    sumy.append(y)
    return f'the area of quadcircle is {area} x is {x} and y is {y}'

def areaval(are):
    sum = 0
    for a in range(0,len(are)):
        print(f'£area {sum + are[a]}')

def xval(are, x):
    d=[] 
    sum = 0
    for a,b in zip(are, x):
        c = a*b
        d.append(c)
    for e in range(0,len(d)):
        return f'the £ax is {sum+d[e]}'
def yval(are, x):
    d=[] 
    sum = 0
    for a,b in zip(are, x):
        c = a*b
        d.append(c)
    for e in range(0,len(d)):
        return f'the £ax is {sum+d[e]}' 
i= 10
while(i>0):
    print(''' 
       enter only numbers for excution
    ''') 
    print("'1' recatangle") 
    print("'2' triangle 📐")
    print("'3' circle ⭕") 
    print("'4' semicircle")
    print("'5' quadcircle")
    print("'q' exit the program😁")
    
    inputs = input('enter the values 📖')
    
    if(inputs =='1'):
        a = float(input('enter the width')) 
        b= float(input('enter the heigth')) 
        c = float(input('extra distance from x axis')) 
        d = float(input('extra distance wrt y axis')) 
        print(rect(a, b, c, d))
    elif(inputs =='2'):
        a = float(input('enter the width')) 
        b= float(input('enter the heigth')) 
        c = float(input('extra distance from x axis')) 
        d = float(input('extra distance wrt y axis')) 
        print(triangle(a, b, c, d)) 
    
    elif(inputs =='3'):
        a = float(input('enter the width')) 
       
        c = float(input('extra distance from x axis')) 
        d = float(input('extra distance wrt y axis')) 
        print(circle(a, c, d)) 
    
    elif(inputs =='4'):
        a = float(input('enter the width')) 
       
        c = float(input('extra distance from x axis')) 
        d = float(input('extra distance wrt y axis')) 
        print(semicircle(a, c, d)) 
    elif(inputs =='5'):
        a = float(input('enter the width')) 
       
        c = float(input('extra distance from x axis')) 
        d = float(input('extra distance wrt y axis')) 
        print(quadcircle(a, c, d)) 
    elif(inputs == 'q'):
        break
    else:
        print("invalid input 😘") 
    
    
    
else:
    print("error 😡 please 🙏 contact developer kushvith") 

areaval(are)
print(xval(are, sumx)) 
print(xval(are, sumy)) 
print("enjoyed developed by kushvith") 
print("copyright 2021-2022😛😛") 
