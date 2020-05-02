import pandas as pd
f = open("text.txt","r")
#g = open("text2.txt","w")
y = []
c = 0

for x in f.readlines():
  x = x.replace("\n",'')
  y.append(x)
  #g.write("Open-ended\t%s")
print(y)
f.close()
#g.close()
