import matplotlib.pyplot as plt


x = []
y = []

for i in range(5):
    
    data1 = input("X axis : ")
    data2 = input("Y axis : ")
    x.append(data1)
    y.append(data2)
    
    # Display the plot for 10 seconds
    plt.show(block=False)
    plt.pause(10)
    plt.close()