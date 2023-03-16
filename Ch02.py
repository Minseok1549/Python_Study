# Sequence
# 2.1 내장 시퀀스
# 컨테이너 시퀀스 : (1) 서로 다른 자료형 (2) 객체에 대한 참조 (3) list, tuple, collections, deque
# 균일 시퀀스 : (1) 단 하나의 자료형 (2) 객체에 대한 참조 대신 자신의 메모리 공간에 각 항목의 값 (3) str, bytes, bytearray, memoryview, array.array

# 2.2 지능형 리스트와 제너레이터 표현식

symbols = '$%^&'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

codes = [ord(symbol) for symbol in symbols]

# 2.2.2 지능형 리스트와 map() / filter() 비교
symbols = '$%^&'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 63]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 63, map(ord, symbols)))
print(beyond_ascii)

# 다른 생성자에 전달할 리스트를 통째로 만들지 않고 반복자 프로토콜을(iterator protocol)을 이용해서 항목을 하나씩 생성하는
# 제너레이터 표현식은 메모리를 더 적게 사용함
symbols = '$%^&'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

import array

a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)

# 데카르트곱을 지능형 리스트와 제너레이터 표현식으로 각각 표현
# 제너레이터 표현식을 사용하면 한번에 한 항목만 생성할 수 있도록 for 루프에 데이터를 전달하기 때문에 모든 항목이 메모리에 생성되지 않음
colors = ['red', 'yellow']
sizes = ['S', 'L']
tshirts = [(color, size) for size in sizes for color in colors]

for tshirt in (f'{color} {size}' for size in sizes for color in colors):
    print(tshirt)

# 2.3 튜플은 단순한 불변 리스트가 아니다.
# 위치나 원소가 바뀌지 않는 불변성으로 인해 레코드로서 사용도 가능함

# array 는 list 보다 훨씬 빠른 속도를 제공한다.
# 다만 모든 타입의 객체를 담을 수 있는 list 보다
# array 는 unicode 만을 내부에 담도록 강제 받는 것으로 보임

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
# h short int 로 선언 후 B unsigned char 로 형변환 후 값을 바꾸면 다음과 같이 변함
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
memv_oct.tolist()

memv_oct[5] = 4
print(numbers)