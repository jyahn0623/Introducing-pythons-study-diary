# 객체는 함수와 데이터로 구성

'''
· 클래스
class Person():
    def __init__(self, name, *args, **kwargs):
        self.name = name


ajy = Person('안주영') 
print(ajy.name)

'''

'''
setter, getter
class A:
    def __init__(self, age):
        self.__age = age
 

    @property
    def age(self):
        return self.__age * 10 # getter, setter를 데코레이터로 구현한 것, 마음대로 가지고 쓸 수 있다.

    @age.setter
    def age(self, _age):
        self.__age = _age


o_A = A(20)
print(o_A.age)
o_A.age = 30
print(o_A.age)
'''

# 클래스 정의에서 메소드의 첫 번째 인자가 self라면 인스턴스 메서드, 이 메서드를 호출할 때 객체를 전달
# 클래스 메서드는 클래스 전체에 영향을 끼친다. @classmethod 데커레이터가 있다면 클래스 메소드
# 클메는 첫 번째 매개변수는 (클래스 자신)을 가진다.
# 정적 메소드는 @staticmethod를 가지고, 정적 메소드를 사용 시 객체를 만들어 호출할 필요가 없이 클래스 네임.메소드로 실행할 수 있다.

'''
class A():
    count = 0
    def __init__(self):
        A.count += 1 # 클래스 변수
    
    def exclaim(self):
        print('hi! hi!')
    
    @classmethod
    def kids(cls):
        print(cls.count)

e_A = A()
b_A = A()

e_A.kids()
b_A.kids()
'''

# 덕 타이핑의 개념
'''
class A:
    def hello(self):
        print('hello')

class B:
    def hello(self):
        print('Ni hao')

class C:
    def hello(self):
        print('안녕하세요.')

def hello(cls):
    cls.hello()

a = A()
b = B()
c = C()

a.hello()
b.hello()
c.hello()
'''

# 산술/비교 연산자를 재정의할 수 있다.
# eq, gt, ne, gt, lt, lte, gte, add, sub, mul, mod 등.
'''
class A:
    def __init__(self, word):
        self.word = word

    def __eq__(self, word2):
        return self.word == word2.word


a = A('hi')
b = A('hi')

print(a == b)
'''


# repr() vs str()
# str()은 print()의 내용 좌우, repr()은 A = person()있을 때 A만 했을 때 인터프리터에서의 내용 좌우

# 컴포지션, 어그리게이션
'''
class Person:
    def __init__(self, mouth, nose):
        self.mouth = mouth
        self.nose = nose

    def tellInfomation(self):
        print('my Nose is', self.mouth.cm, 'my Mouth is', self.nose.cm)
class Nose:
    def __init__(self, cm):
        self.cm = cm

class Mouth:
    def __init__(self, cm):
        self.cm = cm

n = Nose(10)
m = Mouth(10)

a = Person(n, m) # 사람은 코와 입을 가지기 때문에 별도의 객체로 만들어 할당
a.tellInfomation()
'''