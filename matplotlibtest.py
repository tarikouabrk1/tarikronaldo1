import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,5))
plt.style.use('seaborn-v0_8-notebook')
x=np.linspace(0,20,100)
plt.plot(x,np.cos(x),'o--',color="red",lw=1,ms=5,label="shema")
plt.xlabel("temps")
plt.ylabel("abscisse")
plt.legend()
plt.show()
