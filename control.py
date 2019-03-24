#1. if문

#if문 기본
number = 1 #true

if number == 1:
    print('number는 True입니다.')
else:
    print('number는 False입니다.')

#비교연산자와 논리연산자
number1 = 100
number2 = 200
number3 = 300
number4 = 400

a = number1 > number2   #이거슨 거짓
b = number3 < number4   #이거슨 참

if a:
    print('True')
else:
    print('False')

if a and b:     #둘 중 하나라도 거짓이면 False
    print('True')
else:
    print('False')

#x in list
list = ['a', 'b']

if 'a' in list:
    print('a가 있습니다.')
else:
    if 'b' in list:
        print('b가 있습니다.')
    else:
        print('a와 b가 모두 없습니다.')

#elif
if 'a' in list:
    print('a가 있습니다.')
elif 'b' in list:       #else: 하고 if <조건문>: 이 부분을 그냥 elif <조건문>으로 변경.
    print('b가 있습니다.')
else:
    print('a와 b가 모두 없습니다.')

#pass
list = ['a', 'b']

if 'a' in list:
    pass
else:
    print('a가 없습니다.')

#한줄로 만들기
if 'a' in list:
    print("있습니다.")
    print("진짜 있습니다.")
else:
    print('없습니다.!')

# 세미콜론 사용
if 'a' in list: print("있습니다."); print("진짜 있습니다.")
else: print('없습니다.!')

#2. while문

#기본 예시
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#포매팅
#숫자형
print('오늘은 12월 %d일 이다.' %27) 
day = 28
print('오늘은 12월 %d일이다.' %day) 
#문자형
print('%s은 %s를 배우고 있습니다.' %('오늘', 'python')) 
subject = '창업'
print('오늘은 %s를 배우고 있습니다.' %subject)
#혼합
print('%s는 %d월 %d일 입니다.' %('내일', 12, 27))

#break & continue
# 1부터 5까지 출력해보세요
num1 = 0
while num1 < 10:
    num1 += 1
    print(num1)
    if num1 ==5:
        break

#1부터 10까지 숫자 중 홀수를 출력해보세요
num2 = 0
while num2 < 10:
    num2 += 1
    if num2 % 2 == 0 :
        continue
    print(num2)

#3. for문
#예제 1
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

#예제 2
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#break & continue
# 1부터 5까지 출력해보세요
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in list1:
    print(i)
    if i == 5:
        break

#1부터 10까지 숫자 중 홀수를 출력해보세요
list2 = [1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if i % 2 ==0:
        continue
    print(i)

#range
a = range(0,10)
print(a[9])
a = range(0,10,1)
print(a[9])
a = range(0,10,2)
print(a[1])

#range 사용 : 1부터 5까지 출력해보세요
for i in range(0,11):
    print(i)
    if i ==5:
        break

#List Comprehension
#기본
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

#리스트 내포 이용
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

#[1,2,3,4] 중에서 짝수인 2와 4에만 3을 곱하여 담고 싶다면 if 문을 사용!
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)






























#연습문제2
#shirt

#연습문제3 
i = 0
while True:
    i += 1  
    if i > 4: break  
    print ('*' * i) 

#연습문제4 #7
moeum = "aeiou"
count = 0
word = "mutzangesazachurum"
for a in word:
    if a in moeum:
        count+= 1
print(count)