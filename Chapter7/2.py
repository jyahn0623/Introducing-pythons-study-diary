import re
# 정규 표현식

ss = re.match('Hello', 'Hello world')
#              매칭값       비교값

# 패턴을 컴파일 하고 매칭 하기   // 위와 동일한 방식
pss = re.compile('Hello')

# .group() 매치된 것들 찾기

# .saerch() : 첫 번째 일치하는 패턴 찾기
m = re.search('You', 'You are my you!')

# .findall() 모든 패턴 찾기

str1 = 'hello guys my name is ahnjuyoung'
a = re.findall('a', str1)

# .split() 패턴 나누기, .sub() 대체하기


'''
    . 하나의 문자
    ? 0 또는 1회
    * 0회 이상
    + 1회 이상 {1, }과 동일

    \d 숫자
    \D 비숫자
    \w 알파벳 문자, 숫자, 언더 스코어
    \W 비알파벳 문자
    \s 공백  (탭, 공백, )
    \S 비공백
    \b 단어 경계 
    \B 비단어 경계

    패턴 지정자
    abc - abc 매칭
    (abc|abd) - abc 또는 abd
    . \n을 제외한 모든 문자
    ^ 문자열의 시작
    $ 문자열의 끝
    {m, n} - m~n번
    [abc] - a 또는 b 또는 c
    [^abc] - a 또는 b 또는 c가 아님
'''

# 정규표현식은 아스키코드 외에 다른 것도 사용할 수 있다.
import string
testing = string.printable

rr = re.findall('\w', str1)


str2 = 'Testing is good paalace aa!'
zz = re.findall('a{0, 4}', str2)


# 이진 데이터 
# 이진 데이터를 다루기 위해서 엔디안(컴퓨터 프로세스가 데이터를 바이트로 나누는 방법), 정수에 대한 사인 비트 같은 개념을 알아야 한다.
'''
    바이트는 바이트의 튜플처럼 immutable
    바이트 배열은 mutable
'''

blist = [1, 2, 3, 40, 255] # 일반 리스트
byte_var = bytes(blist) # 불변
byte_arr = bytearray(blist) # 가변

# byte_var[1] = 3 # 에러 불변하기 때문
# byte_arr[1] = 3 # 에러 아님, 바뀜 바이트 값
print(blist, byte_var, byte_arr)

bytes_value = bytes(range(0, 255))
print(bytes_value) # 바이트도 출력할 수 있는 값은 아스키 코드를 사용해 출력한다.

