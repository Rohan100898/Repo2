import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("D:\Sample Directory\kf3d8.csv")

x = data['SLV']
y = data['SHV']
z = data['LNV']

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')  # Create a 3D subplot
ax.scatter(x, y, z, c = 'red', marker='o')  # Plot the data

ax.set_xlabel('SLV Axis Label')
ax.set_ylabel('SHV Axis Label')
ax.set_zlabel('LNV Axis Label')
plt.title('3D Scatter Plot')
plt.show()