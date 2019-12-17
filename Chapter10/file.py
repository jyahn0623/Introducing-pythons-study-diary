# 10장은 시스템
# 생성하기 : open()
import os

with open('./test.txt', 'wt') as f:
    f.write('test')

# exists() 존재여부 확인
print(os.path.exists('./test.txt'))  # true
print(os.path.exists('./test1.txt'))  # false

# isfile(파일인지) 타입 확인, isdir(디렉터리인지), isabs(절대 경로인지)
print(os.path.isfile('./test.txt'))
print(os.path.isfile('./test1.txt'))

# copy() 복사하기
import shutil
shutil.copy('./test.txt', './test_copied.txt')

# rename() 이름 변경
os.rename('./test_copied.txt', 'ni_hao.txt')

# link(), symlink() 심볼릭 링크
# pass unix

# chmod(), chown() 파일 소유권 바꾸기
# pass unix

# abspath() 절대 경로 얻기 
print(os.path.abspath('./test.txt'))

# realpath() 심벌릭 링크 경로 얻기
# unix

# remove() 삭제하기
if os.path.exists('./ni_hao.txt'):
    os.remove('./ni_hao.txt')