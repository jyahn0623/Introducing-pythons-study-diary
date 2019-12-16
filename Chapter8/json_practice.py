import json

# 데이터 -> JSON 문자열로 인코딩 (dumps)
# JSON 문자열 -> 데이터로 디코딩 (loads)
ANJUYOUNG = {
                "이름" : "안주영",
                "나이" : 25,
                "취미" : {
                            "취미 1" : "농구",
                            "취미 2" : "축구"
                        }
            }   

# dict을 json으로
ajy = json.dumps(ANJUYOUNG, ensure_ascii=False)

# str을 json으로
json_ajy = json.loads(ajy)


# 날짜 타입의 경우 표준 JSON에서 지원하지 않는 형태
import datetime

now = datetime.datetime.now()
# json.dumps(now) # TypeError: Object of type datetime is not JSON serializable 에러 발생

# datetime 객체를 문자열과 epoch 값이 같이 있는 JSON이 이해할 수 있는 타입으로 변환하면 된다.
d = json.dumps(str(now))
print(d)

from time import mktime
now_epoch = int(mktime(now.timetuple()))
# 312123 형태로 나옴
json.dumps(now_epoch)



# YAML도 있지만 아직까지 파이썬 표준 라이브러리는 없는 상태.