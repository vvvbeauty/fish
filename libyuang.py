import math
def yuang(banjinX,banjinY,currX,currY,Ty=360,Xstep=5,er=2,Xv=0,Yv=0):
	#banjinX X轴半径和Y轴半径一样是椭圆
	#banjinY Y轴半径和X轴半径一样是圆
	#currX,currY显示偏移
	#Ty=360是圆
	
  plotPoints = []
  #Ty=360
  for i in range(0,Ty,Xstep):
      if not Yv:
          y = int(math.sin(i / Ty *er* math.pi) * banjinY+currY )
      if Yv: y=i
      if not Xv:x=int(math.cos(i / Ty *er* math.pi) * banjinX+currX )
      if Xv: x=i
      plotPoints.append([x, y])
  	
  angle=[]
  for i in range(len(plotPoints)-1):
  	x=plotPoints[i+1][0]-plotPoints[i][0]
  	y=plotPoints[i+1][1]-plotPoints[i][1]
  	z=math.atan2(y,x)
  	j=(-math.degrees(z))%360
  	angle.append(j)
  	#print(i,x,y,j)
  
  i=len(plotPoints)-1
  x=plotPoints[i][0]-plotPoints[0][0]
  y=plotPoints[i][1]-plotPoints[0][1]
  z=math.atan2(y,x)
  j=(-math.degrees(z)+180)%360
  angle.append(j)
  #print(i,x,y,j)
  
  return plotPoints,angle
  #返回plotPoints X，Y坐标轴
  #返回angle 角度