import glob
import re
import matplotlib.pyplot as plt

loss=[]
for file_name in glob.glob("../*"):
    if file_name[3:10]=='weights':
        file_name=re.findall(r"\d+\.?\d*", file_name)
        loss.append(float(file_name[1]))
loss=sorted(loss,reverse=True)
plt.plot(loss)
plt.xlabel("epoch time")
plt.ylabel("loss")
plt.show()