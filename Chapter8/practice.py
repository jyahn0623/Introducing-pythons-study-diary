# 1
test1 = 'This is a test of the emergency text system'
with open('./test.txt', 'w') as f:
    f.write(test1)

# 2
with open('./test.txt', 'r') as f:
    test2 = f.readline()    

print(test1==test2)

# 3
import csv
# txt = [
#             ['author', 'book'],
#             ['J R R Tolkien', 'The Hobbit'],
#             ['Lynne Truss', '"Eats, Shoots & Leaves"']
#         ]

# with open('./books.csv', 'w', newline="") as f:
#     w = csv.writer(f)
#     w.writerows(txt)


# 4
with open('./books.csv', 'r') as f:
    r = csv.DictReader(f)
    books = [ a for a in r ]  # 첫 행은 기본으로 헤더

for book in books:
    print(book['author'], '*'*10,  book['book'])
