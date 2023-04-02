import matplotlib.pyplot as plt
x = [2000,2005,2010,2015,2020]


plt.subplot(2,2,1)
y = [2,4,7,5,6]
plt.plot(x,y, color="r", label="Benz")
plt.grid(True)
#plt.title("Benz")
plt.ylabel("Benz", color="r")

plt.subplot(2,2,2)
y = [5,6,8,4,7]
plt.plot(x,y, color="b", label="BMW")
plt.grid(True)
#plt.title("BMW")
plt.ylabel("BMW", color="b")

plt.subplot(2,2,3)
y = [2,1,3,7,3]
plt.plot(x,y, color="g", label="Ford")
plt.grid(True)
#plt.title("Ford")
plt.ylabel("Ford", color="g")

plt.subplot(2,2,4)
y = [7,8,6,9,6]
plt.plot(x,y, color="y", label="Audi")
plt.grid(True)
#plt.title("Audi")
plt.ylabel("Audi", color="y")

plt.show()
