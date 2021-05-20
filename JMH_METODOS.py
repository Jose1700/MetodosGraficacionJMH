##PARTE DE CORRER AL FINAL DEL CODIGO
#JOSE MARTINEZ HERNANDEZ 19/05/2021
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

def Bresenhams(x1, y1, x2, y2):   
    plt.xlim([x1-5, x2+5])
    plt.ylim([y1-5, y2+5])
    plt.title('METODO BRESENHAMS')
    x=x1
    y=y1
    dx = x2 -x1
    dy = y2 -y1
    p= 2*dy-x
    
    print('x  y')
    while x <= x2:
        print(x, ' ', y)   
        rect1 = matplotlib.patches.Rectangle((x, y),1, 1,linewidth=1, edgecolor='b', facecolor='none')
        ax.add_patch(rect1)
        x+=1
        if p<0:
            p=p+2 * dy
        else: 
            p= p + (2*dy) - (2*dx)
            y+=1
       
        
        
    plt.show()       

def DDA(x1, y1, x2, y2):   
    plt.xlim([x1-2, x2+2])
    plt.ylim([y1-2, y2+2])
    plt.title('METODO DDA')
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    if dx > dy:
        steps = dx
    else: 
        steps = dy

    xInc = round((dx/steps), 2)
    yInc = round((dy/steps), 2)
    print('x  y')   

    for i in range(0, steps+1):
        rect1 = matplotlib.patches.Rectangle((round(x1), round(y1)),1, 1,linewidth=1, edgecolor='b', facecolor='none')
        ax.add_patch(rect1)
        x1 += xInc 
        y1 += yInc 
        print (round(x1), '  ', round(y1))  
    plt.show()

    
x1 = int(input("Ingresa x1: "))    
y1 = int(input("Ingresa y1: "))    
x2 = int(input("Ingresa x2: "))    
y2 = int(input("Ingresa y2: "))    


#Aqui solo se descomenta el método que se quiera usas
#Nota no se puden los dos juntos
Bresenhams(x1, y1, x2, y2)
#DDA(x1, y1, x2, y2)