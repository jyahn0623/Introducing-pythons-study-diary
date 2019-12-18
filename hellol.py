
a = 1

mast = 1 << 3

# 1000 
#  1이 1인가?

def updateBit(num, i, val):
    print( num | val << i )
    print( num & ~( 1<<i ) | (val << i))

updateBit(169, 3, 0)