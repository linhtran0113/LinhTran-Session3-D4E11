size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Linh and here is my flock","\n",size,'\n')


month1_size = []
for i1 in range(len(size)):
    month1size = size[i1] + 50
    month1_size.append(month1size)
print("MONTH 1:", '\n', "One month has passed, now here is my flock", '\n', month1_size)
print('Now my biggest sheep has size', max(month1_size), "let's shear it")

month1_size[month1_size.index(max(month1_size))] = 8
print("After shearing, here is my flock","\n",month1_size,'\n')


month2_size = []
for i2 in range(len(size)):
    month2size = month1_size[i2] + 50
    month2_size.append(month2size)
print("MONTH 2:", '\n', "One month has passed, now here is my flock", '\n', month2_size)
print('Now my biggest sheep has size', max(month2_size), "let's shear it")

month2_size[month2_size.index(max(month2_size))] = 8
print("After shearing, here is my flock","\n",month2_size,'\n')


month3_size = []
for i3 in range(len(size)):
    month3size = month2_size[i3] + 50
    month3_size.append(month3size)
print("MONTH 3:", '\n', "One month has passed, now here is my flock", '\n', month3_size)
print('Now my biggest sheep has size', max(month3_size), "let's shear it")

month3_size[month3_size.index(max(month3_size))] = 8
print("After shearing, here is my flock","\n",month3_size)