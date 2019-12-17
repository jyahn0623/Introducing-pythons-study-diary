# 디렉터리 다루기
import os
# mkdir()
if not os.path.exists('nest_dir'): # 파일도 되고, 디렉터리도 되네.
    os.mkdir('nest_dir')

# rmdir()
if os.path.exists('nest_dir') and os.path.isdir('nest_dir'):
    os.rmdir('nest_dir')

# 콘텐츠 나열하기 : listdir() // 디렉터리 안 파일 등 나열
print(os.listdir('../Chapter10')) # Chapter10 안에 있는 모든 파일/디렉터리가 나열됨

# 응용 가능
for a in os.listdir('../Chapter10'):
    # 문자열로 반환
    print(os.path.isdir(a))

# 현재 디렉터리 바꾸기 chdir()
os.chdir('hello') # hello 디렉터리로 이동
print(os.listdir('.'))

# 일치하는 파일 나열하기 : glob()
# regex가 아닌 유닉스 쉘 규칙을 사용하여 일치하는 파일이나 디렉터리의 이름 검색
# *, ?, [abc], [!abc]
import glob
print(glob.glob('d*')) # d로 시작하는 파일/디렉터리 검색 가능


