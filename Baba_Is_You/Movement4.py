import copy
def up(shot):
	dic=grammar3(shot)
	for dicitem in dic.items():
		if dicitem[1].issuperset({"you"})==True:
			for dirobjs in shot.dir_objects.items():
				if dirobjs[0]==dicitem[0]:
					for dirobjpos in dirobjs[1]:
						result=push2(shot,dirobjpos[0],dirobjpos[1]-1,"u",dic)
						if result==False:
							continue
						else:
							shot=result
							dirobjpos[1]-=1
			for objs in shot.objects.items():
				if objs[0]==dicitem[0]:
					for objpos in objs[1]:
						result=push2(shot,objpos[0],objpos[1]-1,"u",dic)
						if result==False:
							continue
						else:
							shot=result
							objpos[1]-=1
	shot=grammar4(shot)
	dic=grammar3(shot)
	if win3(shot,dic)==True:
		shot.win=True
	return shot

def down(shot):
	dic=grammar3(shot)
	for dicitem in dic.items():
		if dicitem[1].issuperset({"you"})==True:
			for dirobjs in shot.dir_objects.items():
				if dirobjs[0]==dicitem[0]:
					for dirobjpos in dirobjs[1]:
						result=push2(shot,dirobjpos[0],dirobjpos[1]+1,"d",dic)
						if result==False:
							continue
						else:
							shot=result
							dirobjpos[1]+=1
			for objs in shot.objects.items():
				if objs[0]==dicitem[0]:
					for objpos in objs[1]:
						result=push2(shot,objpos[0],objpos[1]+1,"d",dic)
						if result==False:
							continue
						else:
							shot=result
							objpos[1]+=1
	shot=grammar4(shot)
	dic=grammar3(shot)
	if win3(shot,dic)==True:
		shot.win=True
	return shot

def left(shot):
	dic=grammar3(shot)
	for dicitem in dic.items():
		if dicitem[1].issuperset({"you"})==True:
			for dirobjs in shot.dir_objects.items():
				if dirobjs[0]==dicitem[0]:
					for dirobjpos in dirobjs[1]:
						result=push2(shot,dirobjpos[0]-1,dirobjpos[1],"l",dic)
						if result==False:
							continue
						else:
							shot=result
							dirobjpos[0]-=1
			for objs in shot.objects.items():
				if objs[0]==dicitem[0]:
					for objpos in objs[1]:
						result=push2(shot,objpos[0]-1,objpos[1],"l",dic)
						if result==False:
							continue
						else:
							shot=result
							objpos[0]-=1
	shot=grammar4(shot)
	dic=grammar3(shot)
	if win3(shot,dic)==True:
		shot.win=True
	return shot

def right(shot):
	dic=grammar3(shot)
	for dicitem in dic.items():
		if dicitem[1].issuperset({"you"})==True:
			for dirobjs in shot.dir_objects.items():
				if dirobjs[0]==dicitem[0]:
					for dirobjpos in dirobjs[1]:
						result=push2(shot,dirobjpos[0]+1,dirobjpos[1],"r",dic)
						if result==False:
							continue
						else:
							shot=result
							dirobjpos[0]+=1
			for objs in shot.objects.items():
				if objs[0]==dicitem[0]:
					for objpos in objs[1]:
						result=push2(shot,objpos[0]+1,objpos[1],"r",dic)
						if result==False:
							continue
						else:
							shot=result
							objpos[0]+=1
	shot=grammar4(shot)
	dic=grammar3(shot)
	if win3(shot,dic)==True:
		shot.win=True
	return shot

def push2(shot,x,y,direction,dic):
	if 0<=x<=shot.width-1 and 0<=y<=shot.height-1:
		for objs in shot.objects.items():
			i=0
			while i<len(objs[1]):
				if x==objs[1][i][0] and y==objs[1][i][1]:
					if objs[0][:5]=="text_":
						if direction=="u":
							shot=push2(shot,x,y-1,direction,dic)
						if direction=="d":
							shot=push2(shot,x,y+1,direction,dic)
						if direction=="l":
							shot=push2(shot,x-1,y,direction,dic)
						if direction=="r":
							shot=push2(shot,x+1,y,direction,dic)
						if shot==False:
							return False
						else:
							if direction=="u":
								shot.objects[objs[0]][i][1]-=1
							if direction=="d":
								shot.objects[objs[0]][i][1]+=1
							if direction=="l":
								shot.objects[objs[0]][i][0]-=1
							if direction=="r":
								shot.objects[objs[0]][i][0]+=1
							return shot
					elif (objs[0] in dic.keys()) and dic[objs[0]].issuperset({"stop"})==True:
						return False
				i+=1
		for dirobjs in shot.dir_objects.items():
			i=0
			while i<len(dirobjs[1]):
				if x==dirobjs[1][i][0] and y==dirobjs[1][i][1]:
					if dirobjs[0][:5]=="text_":
						if direction=="u":
							shot=push2(shot,x,y-1,direction,dic)
						if direction=="d":
							shot=push2(shot,x,y+1,direction,dic)
						if direction=="l":
							shot=push2(shot,x-1,y,direction,dic)
						if direction=="r":
							shot=push2(shot,x+1,y,direction,dic)
						if shot==False:
							return False
						else:
							if direction=="u":
								shot.dir_objects[dirobjs[0]][i][1]-=1
							if direction=="d":
								shot.dir_objects[dirobjs[0]][i][1]+=1
							if direction=="l":
								shot.dir_objects[dirobjs[0]][i][0]-=1
							if direction=="r":
								shot.dir_objects[dirobjs[0]][i][0]+=1
							return shot
					elif (dirobjs[0] in dic.keys()) and dic[dirobjs[0]].issuperset({"stop"})==True:
						return False
				i+=1
		return shot
	else:
		return False
def grammar3(shot):
	dic={}
	for ispos in shot.objects["text_is"]:
		boolean1=False
		for babapos in shot.objects["text_baba"]:
			if babapos==[ispos[0],ispos[1]-1]:
				boolean1=True
				thing="baba"
		for wallpos in shot.objects["text_wall"]:
			if wallpos==[ispos[0],ispos[1]-1]:
				boolean1=True
				thing="wall"
		for flagpos in shot.objects["text_flag"]:
			if flagpos==[ispos[0],ispos[1]-1]:
				boolean1=True
				thing="flag"
		boolean2=False
		for youpos in shot.objects["text_you"]:
			if youpos==[ispos[0],ispos[1]+1]:
				boolean2=True
				attri="you"
		for stoppos in shot.objects["text_stop"]:
			if stoppos==[ispos[0],ispos[1]+1]:
				boolean2=True
				attri="stop"
		for winpos in shot.objects["text_win"]:
			if winpos==[ispos[0],ispos[1]+1]:
				boolean2=True
				attri="win"
		if boolean1==True and boolean2==True:
			if thing in dic.keys():
				dic[thing].add(attri)
			else:
				dic[thing]={attri}
		boolean1=False
		for babapos in shot.objects["text_baba"]:
			if babapos==[ispos[0]-1,ispos[1]]:
				boolean1=True
				thing="baba"
		for wallpos in shot.objects["text_wall"]:
			if wallpos==[ispos[0]-1,ispos[1]]:
				boolean1=True
				thing="wall"
		for flagpos in shot.objects["text_flag"]:
			if flagpos==[ispos[0]-1,ispos[1]]:
				boolean1=True
				thing="flag"
		boolean2=False
		for youpos in shot.objects["text_you"]:
			if youpos==[ispos[0]+1,ispos[1]]:
				boolean2=True
				attri="you"
		for stoppos in shot.objects["text_stop"]:
			if stoppos==[ispos[0]+1,ispos[1]]:
				boolean2=True
				attri="stop"
		for winpos in shot.objects["text_win"]:
			if winpos==[ispos[0]+1,ispos[1]]:
				boolean2=True
				attri="win"
		if boolean1==True and boolean2==True:
			if thing in dic.keys():
				dic[thing].add(attri)
			else:
				dic[thing]={attri}
	return dic
def win3(shot,dic):
	youset=set()
	winset=set()
	for dicitem in dic.items():
		if dicitem[1].issuperset({"you"}):
			if dicitem[0] in shot.dir_objects.keys():
				i=0
				while i<len(shot.dir_objects[dicitem[0]]):
					youset.add((shot.dir_objects[dicitem[0]][i][0],shot.dir_objects[dicitem[0]][i][1]))
					i+=1
			if dicitem[0] in shot.objects.keys():
				i=0
				while i<len(shot.objects[dicitem[0]]):
					youset.add((shot.objects[dicitem[0]][i][0],shot.objects[dicitem[0]][i][1]))
					i+=1
		if dicitem[1].issuperset({"win"}):
			if dicitem[0] in shot.dir_objects.keys():
				i=0
				while i<len(shot.dir_objects[dicitem[0]]):
					winset.add((shot.dir_objects[dicitem[0]][i][0],shot.dir_objects[dicitem[0]][i][1]))
					i+=1
			if dicitem[0] in shot.objects.keys():
				i=0
				while i<len(shot.objects[dicitem[0]]):
					winset.add((shot.objects[dicitem[0]][i][0],shot.objects[dicitem[0]][i][1]))
					i+=1
	if youset.intersection(winset)==set():
		return False
	else:
		return True
def grammar4(shot):
	dic={}
	for ispos in shot.objects["text_is"]:
		boolean1=False
		for babapos in shot.objects["text_baba"]:
			if babapos==[ispos[0],ispos[1]-1]:
				boolean1=True
				thing="baba"
		for wallpos in shot.objects["text_wall"]:
			if wallpos==[ispos[0],ispos[1]-1]:
				boolean1=True
				thing="wall"
		for flagpos in shot.objects["text_flag"]:
			if flagpos==[ispos[0],ispos[1]-1]:
				boolean1=True
				thing="flag"
		boolean2=False
		for babapos in shot.objects["text_baba"]:
			if babapos==[ispos[0],ispos[1]+1]:
				boolean2=True
				attri="baba"
		for wallpos in shot.objects["text_wall"]:
			if wallpos==[ispos[0],ispos[1]+1]:
				boolean2=True
				attri="wall"
		for flagpos in shot.objects["text_flag"]:
			if flagpos==[ispos[0],ispos[1]+1]:
				boolean2=True
				attri="flag"
		if boolean1==True and boolean2==True:
			if thing in dic.keys():
				dic[thing].add(attri)
			else:
				dic[thing]={attri}
		boolean1=False
		for babapos in shot.objects["text_baba"]:
			if babapos==[ispos[0]-1,ispos[1]]:
				boolean1=True
				thing="baba"
		for wallpos in shot.objects["text_wall"]:
			if wallpos==[ispos[0]-1,ispos[1]]:
				boolean1=True
				thing="wall"
		for flagpos in shot.objects["text_flag"]:
			if flagpos==[ispos[0]-1,ispos[1]]:
				boolean1=True
				thing="flag"
		boolean2=False
		for babapos in shot.objects["text_baba"]:
			if babapos==[ispos[0]+1,ispos[1]]:
				boolean2=True
				attri="baba"
		for wallpos in shot.objects["text_wall"]:
			if wallpos==[ispos[0]+1,ispos[1]]:
				boolean2=True
				attri="wall"
		for flagpos in shot.objects["text_flag"]:
			if flagpos==[ispos[0]+1,ispos[1]]:
				boolean2=True
				attri="flag"
		if boolean1==True and boolean2==True:
			if thing in dic.keys():
				dic[thing].add(attri)
			else:
				dic[thing]={attri}
	shot=change4(shot,"baba",dic)
	shot=change4(shot,"wall",dic)
	shot=change4(shot,"flag",dic)
	return shot
def change4(shot,thing,dic):
	if thing in dic.keys():
		for attri in dic[thing]:
			if thing in shot.dir_objects.keys():
				if attri in shot.dir_objects.keys():
					for dirobjpos in shot.dir_objects[thing]:
						shot.dir_objects[attri].append(dirobjpos)
				else:
					for dirobjpos in shot.dir_objects[thing]:
						shot.objects[attri].append(dirobjpos)
				shot.dir_objects[thing].clear()
			else:
				if attri in shot.dir_objects.keys():
					for objpos in shot.objects[thing]:
						shot.dir_objects[attri].append(objpos)
				else:
					for objpos in shot.objects[thing]:
						shot.objects[attri].append(objpos)
				shot.objects[thing].clear()
			return change4(shot,attri,dic)
	else:
		return shot