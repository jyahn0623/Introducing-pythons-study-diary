# 1
'''
class Thing(object):
    pass

ex = Thing()
'''

#2
'''
class Thing2(object):
    def __init__(self):
        self.letters = 'abc'

ex = Thing2().letters
print(ex)
'''

#3 위와 동일
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


a = Element('안주영', '아펠리오스', '1')
el_dict = {'name' : '안재영', 'symbol' : '베인', 'number' : 20}
b = Element(**el_dict)
print(**el_dict)