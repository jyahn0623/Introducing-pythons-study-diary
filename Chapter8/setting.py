# 설정 파일

# .ini, .cfg <- configparser 모듈을 통해 처리할 수 있다.

import configparser

cfg = configparser.ConfigParser()
cfg.read('./setting.ini')            # .cfg로 했지만 .ini로 바꾸어도 문제 없음

print(cfg['english'])                # section : english
print(cfg['english']['greeting'])    # hello

print(cfg['files']['home'])
print(cfg['files']['bin'])

# 설정 파일에
# 보간법을 사용하기 위해서 bin = %(home)'s'/bin s를 붙여야 함 몽미~


