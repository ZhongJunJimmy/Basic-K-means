import numpy as np
import matplotlib.pyplot as plt

#clustering by Vertical bisector
def VerticalBisector(parameter,groupPoint):
	m=-1/(parameter[1][1]-parameter[0][1]/parameter[1][0]-parameter[0][0])
	center=[((parameter[1][0]+parameter[0][0])/2),((parameter[1][1]+parameter[0][1])/2)]
	k=center[1]-m*center[0]
	count=0

	Group1=[]
	Group2=[]
	for index in groupPoint:
		if(groupPoint[count,0]*m-groupPoint[count,1]+k>0):
			Group1.append([groupPoint[count,0],groupPoint[count,1]])
		elif (groupPoint[count,0]*m-groupPoint[count,1]+k<0):
			Group2.append([groupPoint[count,0],groupPoint[count,1]])
		count+=1
	
	Point=[]
	Point.append(newPoint(Group1))
	Point.append(newPoint(Group2))

	return Point
	
#calculator two point's distance by Euler's formula
def Euler(groupPoint,parameter):
	dis=np.sqrt(pow((parameter[0]-groupPoint[0]),2)+pow((parameter[1]-groupPoint[1]),2))
	return dis

#clustering by Euler's formula
def GroupingEuler(kPoint,parameter):
	Group1=[]
	Group2=[]
	count=0
	for index in parameter:
		if(Euler(index,kPoint[0])<Euler(index,kPoint[1])):
			Group1.append(index)
		else:
			Group2.append(index)
		count+=1

	point=[]
	point.append(newPoint(Group1))
	point.append(newPoint(Group2))
	point.append(Group1)
	point.append(Group2)
	return point

#calculator centroid points
def newPoint(parameter):
	count=0
	X=0
	Y=0
	for index in parameter:
		X+=parameter[count][0]
		Y+=parameter[count][1]
		count+=1
	point=[X/count,Y/count]
	return point


#main program
groupPoint = np.random.rand(100,2)
prePoint=[[0.1,0.1],[0.2,0.2]]

result=VerticalBisector(prePoint,groupPoint)
newPoint2=GroupingEuler(result,groupPoint)

kPoint=[]
kPoint.append(newPoint2[0])
kPoint.append(newPoint2[1])
newkPoint3=GroupingEuler(kPoint,groupPoint)


while Euler(kPoint[0],newkPoint3[0])!=0:
	kPoint=[]
	kPoint.append(newkPoint3[0])
	kPoint.append(newkPoint3[1])
	newkPoint3=GroupingEuler(kPoint,groupPoint)

#print result list
#print(newkPoint3)

#draw result fig 
fig = plt.figure(1)
plt.ion()
for gr in newkPoint3[2]:
	plt.scatter(gr[0],gr[1],s=50,c="red")
for gr in newkPoint3[3]:
	plt.scatter(gr[0],gr[1],s=50,c="blue")
plt.scatter(newkPoint3[0][0],newkPoint3[0][1],s=60,c="black")
plt.scatter(newkPoint3[1][0],newkPoint3[1][1],s=60,c="black")
plt.show(1)
plt.ioff()
