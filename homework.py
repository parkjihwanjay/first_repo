연습문제 1
list_1 = ['Life', 'is', 'too', 'short']
print(" ".join(list_1))

연습문제 2
i=1
while(i<5):
    print("*"*i)
    i += 1

연습문제 3
count = 0
str_1 = "mutzangesazachurum"
for i in str_1:
    if i in 'aeiou':
        count += 1
print(count)
list1=[1,2,3]
print([i for i in list1])

과제 1-1
i=0
sum = 0
while(i<1001):
    i+=1
    if i%3 == 0:
        sum += i

print(sum)

#과제 1-2
i=10
while(i>0):
    print("*"*i)
    i -= 1

과제 1-3
sum =0
A=[20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
while len(A)>0 :
    if A[-1] >= 50:
        sum += A[-1]
    A.pop()
print(sum)

#과제 2-1
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

과제 2-2
sum = 0
A =[70,60,55,75,95,90,80,80,85,100]
for i in A:
    sum += i
print(sum/len(A))

과제 2-3
nubmers=[1,2,3,4,5]
result = [num*2 for num in nubmers if num%2 == 1]
print(result)
