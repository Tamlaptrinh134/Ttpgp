import matplotlib.pyplot as plt
#from matplotlib.figure
import numpy as np

def item_scatter(event):
	if event.artist.axes is not None:
		index = event.ind[0]
		print(datas_out[index])

size = 20

datas_x = list(range(size)) * size
datas_y = [i for i in range(size) for _ in range(size)]
datas_z = np.random.random(size**2).tolist()

datas_z_og = datas_z.copy()

datas_out = [0] * size ** 2

datas_scan_y_z = []

for k in range(size):
	datas_scan_y_z.append(size * k - 0)
print(datas_z)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection = "3d")
size_read = size
size_read_bf = 0

line_2 = ax.scatter(datas_x, datas_y, datas_z, c = datas_z, cmap = 'gist_earth', marker = "o")
#line_og = ax.scatter(datas_x, datas_y, datas_z, color = "#e3dfde", marker = ".")
line, = ax.plot(datas_x[size_read_bf:size_read], datas_y[size_read_bf:size_read], datas_z[size_read_bf:size_read], marker = ".", color = 'red')
liney, = ax.plot(list(map(lambda x:datas_x[x], datas_scan_y_z)), list(map(lambda x:datas_y[x], datas_scan_y_z)), list(map(lambda x:datas_z[x], datas_scan_y_z)), marker = ".", color = 'green')
fig.colorbar(line_2)
fig.canvas.mpl_connect('pick_event', item_scatter)
line_2.set_picker(True)
ax.set_xlabel('Chiều dài ( m )')
ax.set_ylabel('Chiều rộng ( m )')
ax.set_zlabel('Chiều cao ( m )')

speed = 0.2
flatness_scan = 3 #*fns
corner_point = 2

p = 0

for a in range(flatness_scan * size):
	print(f"Info [{a}]: Is working! -> {round(a / (flatness_scan * size) * 100, 1)}%")
	line.set_xdata(datas_x[size_read_bf:size_read])
	line.set_ydata(datas_y[size_read_bf:size_read])
	line.set_3d_properties(datas_z[size_read_bf:size_read]) 
	liney.set_xdata(list(map(lambda x:datas_x[x], datas_scan_y_z)))
	liney.set_ydata(list(map(lambda x:datas_y[x], datas_scan_y_z)))
	liney.set_3d_properties(list(map(lambda x:datas_z[x], datas_scan_y_z))) 
	line_2._offsets3d = (datas_x, datas_y, datas_z)
	line_2.set_array(datas_z)
	plt.pause(speed)
	plt.draw()
	for i in range(len(datas_z[size_read_bf:size_read]) - corner_point):
		fist_num = datas_z[size_read_bf:size_read][i]
		end_num = datas_z[size_read_bf:size_read][i+corner_point]

		average = (fist_num + end_num) / 2

		datas_z.pop(round(i+size_read_bf))
		datas_z.insert(round(i+size_read_bf), average)
		datas_z.pop(round(i+size_read_bf+corner_point/2))
		datas_z.insert(round(i+size_read_bf+corner_point/2), average)
		datas_z.pop(round(i+size_read_bf+corner_point))
		datas_z.insert(round(i+size_read_bf+corner_point), average)
	
	datas_scan_y_z.clear()
	
	for i in range(size):
		fist_num = datas_z[size * i + p]
		if size * (i + 2) + p < size**2:
			end_num = datas_z[size * (i + 2) + p]

			average = (fist_num + end_num) / 2
			datas_z.pop(size * i + p)
			datas_z.insert(size * i + p, average)
			datas_z.pop(size * (i + 1) + p)
			datas_z.insert(size * (i + 1) + p, average)
			datas_z.pop(size * (i + 2) + p)
			datas_z.insert(size * (i + 2) + p, average)

		datas_scan_y_z.append(size * i + p)

	if size_read == len(datas_x):
		size_read_bf = 0
		size_read = size
	else:
		size_read_bf += size
		size_read += size
	
	if p == size - 1:
		p = 0
	else:
		p += 1

print(f"Info [{a}]: End work! -> 100%")
#print(datas_out)


datas_out.clear()
for i in range(size ** 2):
	datas_out.append(datas_z[i] - datas_z_og[i])
plt.show()