# print all the even numbers till n where n is a integer
n = int(input("Enter the number till you want the even "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

count = 0
for i in range(1, n+1):
    if i % 2 == 0:
        count += 1

print("The count is ",count)

i = 1
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1



evenum = []
for i in range(1, n+1):
    if i%2==0:
        evenum.append(i)

print(type(evenum))
print(evenum)

print(evenum[0])
print(evenum[3])
print(evenum[-1])

# list can be of mixed data types
list1 = [1, 'ritu', 3.9, 'C']
print(list1)
list1.insert(0, 'priya') # position and item
print(list1)