# 1
import unicodedata
mystery = '\U0001f4a9'
#print(mystery, unicodedata.name(mystery))

# 2
pop_bytes = mystery.encode('utf-8')
#print(pop_bytes)

# 3
pop_string = pop_bytes.decode('utf-8')
#print(pop_string, pop_string==mystery)

# 4
a = '''
    Hi my name is {name} what is your name?
'''
#print(a.format(name='안주영'))
#print(a.format(**{'name' : '안주영'}))


# 5
foam = \
'''
We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon.
'''


import re
p = re.compile('c[\w]*')
#print(p.findall(foam))

# r로 끝나는 단어
#print(re.findall('.*.r', foam))

# a, e, i, o, u 가 세 번 연속으로 나오는 단어
print(re.findall('.*[aeiou]{3}.*', foam))
