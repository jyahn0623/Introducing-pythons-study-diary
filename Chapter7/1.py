# 문자열 (Unicode), 바이트·바이트 배열(2진 데이터)

# python 2에서 바이트 배열 문자열 사용 -> python 3로 오면서 유니코드 사용

# 유니코드는 한 문자당 1~4바이트를 사용

# 1 바이트 : 아스키코드
# 2 바이트 : 라틴어
# 3 바이트 : 기본 다국어 평면의 나머지
# 4 바이트 : 아시아 언어 및 기호를 포함한 나머지

# UTF-8을 사용하면 인코딩 할 필요 없이 인생이 편해진다고 한다.



string = '안녕하세요, 만나서 반갑습니다.'
snowman = '\u2603'


ds = snowman.encode('utf-8')
# .encode() -> 바이트로 인코딩 하는 함수 
# params에 utf-8은 가변 길이 인코딩 방식

# .encode() 함수는 ascii 코드가 아닌 게 나오면 에러 발생 두 번째 인자에 다른 것을 취해 에러 해결 가능
# snowman.encode('ascii', 'ignore' or 'replace', 'backslashreplace', 'xmlcharrefreplace') 등 존재

# .decode() -> 바이트 문자열을 유니코드로 디코딩 가능
# 외부 소스(파일, db, 웹, 네트워크 api는 텍스트를 얻을 때마다 바이트 문자열로 인코딩 됨) 이것을 인코딩 과정을 거꾸로 하여 유니코드 문자열 획득 가능


zz = 'caf\u00e9'
print(zz) # 유니코드

pb = zz.encode('utf-8')  # 바이트 인코딩 시 caf\u00e9는 총 5바이트 할당 (c, a, f) 1바이트, \u00e9는 2 바이트
print(pb, type(pb))

print(pb.decode('ascii')) # 에러 발생, 0xc3, 0xa9는 아스키 코드 값이 아니기 때문에!
print(pb.decode('utf-8'))