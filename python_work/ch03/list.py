
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())

# Index Positions Start at 0, Not 1
print(bicycles[1])
print(bicycles[3])

# Using Individual Values from a List
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print(bicycles[-1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 修改元素 'honda' 为 'ducati'
motorcycles[0] = 'ducati'
print(motorcycles)
# 在列表末尾添加新元素 'honda'
motorcycles.append('honda')
print(motorcycles)

# Inserting Elements into a List
motorcycles.insert(0, 'honda')
print(motorcycles)

# Removing Elements from a List
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(motorcycles)

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removing an Item by Value
motorcycles.remove('yamaha')
print(motorcycles)