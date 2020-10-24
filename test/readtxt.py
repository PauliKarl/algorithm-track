inplist = {'Hips':[],'Peivis':[],'spine0':[]}

with open("./input.txt",'r') as f:
    for line in f.readlines():
        line  = list(line.split(","))
        inplist.append(line)

print(inplist)