import math
import numpy as np

# bezier_curve(xs,ys,num,b_xs,b_ys)
#xs表示原始数据
#n表示阶数
#k表示索引

def yuang(banjinX,banjinY,currX,currY,Ty=360,Xstep=5,er=2,Xv=0,Yv=0):
	#banjinX X轴半径和Y轴半径一样是椭圆
	#banjinY Y轴半径和X轴半径一样是圆
	#currX,currY显示偏移
	#Ty=360是圆
	
  plotPoints = []
  angle=[]
  #Ty=360
  for i in range(0,Ty,Xstep):
      if not Yv:
          y = int(math.sin(i / Ty *er* math.pi) * banjinY+currY )
      if Yv: y=i
      if not Xv:x=int(math.cos(i / Ty *er* math.pi) * banjinX+currX )
      if Xv: x=i
      plotPoints.append([x, y])
  angle=jiaodu(plotPoints)
   
  return plotPoints,angle
   
def jiaodu(plotPoints,ture1=1): 	
  angle=[]
  for i in range(len(plotPoints)-1):
  	x=plotPoints[i+1][0]-plotPoints[i][0]
  	y=plotPoints[i+1][1]-plotPoints[i][1]
  	z=math.atan2(y,x)
  	j=(-math.degrees(z))%360
  	angle.append(j)
  	#print(i,x,y,j)
  if ture1:
      i=len(plotPoints)-1
      x=plotPoints[i][0]-plotPoints[0][0]
      y=plotPoints[i][1]-plotPoints[0][1]
      z=math.atan2(y,x)
      j=(-math.degrees(z)+180)%360
      angle.append(j)
  if not ture1:
      i=len(plotPoints)-1
      x=plotPoints[i][0]-plotPoints[i-1][0]
      y=plotPoints[i][1]-plotPoints[i-1][1]
      z=math.atan2(y,x)
      j=(-math.degrees(z))%360
      j+=0
      angle.append(j)
  #print(i,x,y,j)
  
  return angle
  #返回plotPoints X，Y坐标轴
  #返回angle 角度



def one_bezier_curve(a,b,t):
    return (1-t)*a + t*b
 
#xs表示原始数据
#n表示阶数
#k表示索引
def n_bezier_curve(xs,n,k,t):
    if n == 1:
        return one_bezier_curve(xs[k],xs[k+1],t)
    else:
        return (1-t)*n_bezier_curve(xs,n-1,k,t) + t*n_bezier_curve(xs,n-1,k+1,t)
 
def bezier_curve(xs,ys,num,b_xs,b_ys):
    n = len(xs) - 1
    t_step = 1.0 / (num - 1)
    t = np.arange(0.0,1+t_step,t_step)
    for each in t:
        b_xs.append(n_bezier_curve(xs,n,0,each))
        b_ys.append(n_bezier_curve(ys,n,0,each))