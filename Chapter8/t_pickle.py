# 직렬화

# 객체를 파일로 저장하는 것을 직렬화라고 한다. JSON과 같은 형식은 파이썬 프로그램에서 모든 데이터 타입을 직렬화하는 컨버터가 필요하다. 
# pickle : 바이너리 형식으로 된 객체를 저장하고 복원할 수 있는 모듈

# datetime을 JSON 변환 시 에러 -> pickle은 해결 가능

import pickle, datetime

now = datetime.datetime.now()
print(now)
date = pickle.dumps(now)
print(date) # 바이너리 형태로 바꿔버림. (직렬화)
pickled = pickle.loads(date) # 바이너리로 바뀐 값을 변환
print(pickled)


# pickle : 객체, 데이터를 파일로 저장 ( 모든 타입 가능 )