import csv
# csv


# _f = csv.writer(open('./test.csv', 'wt', newline=''))

# _list = [
#             ['안주영', 25],
#             ['안재영', 20],
#             ['안상문', 52],
#             ['고영임', 49]
#         ]

# for l in _list:    # 한 라인씩 할 수도 있지만.
#     print(l)

# _f.writerows(_list) # 한 번에 넣어버린다.

# 읽기
with open('./test.csv', 'rt') as f:
    reader = csv.reader(f)
    _read_list = [ r for r in reader ]
print(_read_list)

# 리스트 형태가 아닌 dict 형태로 ([[], []]가 아닌  [{}, {}]) 받아보자
# DictReader() 함수 사용, 자연스레 DictWriter()는 dict으로 csv 파일을 쓸 수 있겠다 생각할 수 있음.

with open('./test.csv', 'r') as f:
    cin = csv.DictReader(f, fieldnames=['이름', '나이'])
    _dict_data = [ r for r in cin ]

for obj in _dict_data:
    print(obj['이름'], obj['나이']) # OrderedDict 반환, 일반 dict처럼 사용 가능



with open('./test1.csv', 'wt') as wf:
    test_dict = [
                    {'이름' : '안주영', '나이' : 25},
                    {'이름' : '안주영', '나이' : 25},
                    {'이름' : '안주영', '나이' : 25},
                    {'이름' : '안주영', '나이' : 25}
                ]
    
    fw = csv.DictWriter(wf, fieldnames=['이름', '나이']) # fieldsname과 키 값이 다르면 에러 발생
    fw.writeheader() # fieldsnames을 기준으로 헤더를 쓴다.
    fw.writerows(test_dict)

# 다시 읽어본다.
with open('./test1.csv', 'r') as f:
    reader = csv.DictReader(f) # 헤더가 있는 경우, 즉 첫 번째 라인은 fieldsnames의 값으로 임명된다.
    _data = [ r for r in reader ]
