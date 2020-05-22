size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Linh and these are my sheep sizes","\n",size)

print('\n',"Now my biggest sheep has size", max(size), "let's shear it")

size[size.index(300)] = 8
print('\n',"After sheering, here is my flock",'\n',size)

new_size = []
for i in range(len(size)):
    newsize = size[i] + 50
    new_size.append(newsize)
print('\n',"One month has passed, now here is my flock",'\n',new_size)

