import math
import matplotlib.pyplot as plt

theta = math.radians(60)

PointX = []
PointY = []

def addplt(point):
    PointX.append(point[0])
    PointY.append(point[1])


def koch_curve(n,p1,p2):
    print(n,p1,p2)
    if n==0:
        return
    else:
        
        sx=(2*p1[0]+p2[0])/3
        sy=(2*p1[1]+p2[1])/3
        tx=(p1[0]+2*p2[0])/3
        ty=(p1[1]+2*p2[1])/3

        ux = (tx - sx)*math.cos(theta) - (ty - sy)*math.sin(theta) + sx
        uy = (tx - sx)*math.sin(theta) + (ty - sy)*math.cos(theta) + sy

        s=[sx,sy]
        t=[tx,ty]
        u=[ux,uy]

        koch_curve(n-1, p1, s)
        print(s)
        addplt(s)
        
        koch_curve(n-1, s, u)
        print(u)
        addplt(u)

        koch_curve(n-1, u, t)
        print(t)        
        addplt(t)

        koch_curve(n-1, t, p2)

    return



if __name__=='__main__':
    p1=[0,0]
    p2=[100,0]
    n=3


    print(p1)
    addplt(p1)

    koch_curve(n,p1,p2)

    print(p2)
    addplt(p2)
        
    # グラフ描写
    plt.plot(PointX,PointY)
    plt.xlim([0,100])
    plt.ylim([0,100])

    plt.show()
    