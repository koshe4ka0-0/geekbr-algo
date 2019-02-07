#Закодируйте любую строку из трех слов по алгоритму Хаффмана
from collections import Counter, deque

class MyNode:
    def __init__(self, value, right = None, left = None):
        self.value = value
        self.right = right
        self.left = left


def search(bin_tree, number, path = ''):
    if bin_tree.value == number:
        return f'{path}'
    elif number < bin_tree.value and bin_tree.left is not None:
        return search(bin_tree.left, number, path=f'{path}0')
    elif number > bin_tree.value and bin_tree.right is not None:
        return search(bin_tree.right, number, path=f'{path}1')
    
    return f'Число {number} в дереве не найдено'

# = Counter(input("Введите строку из трех слов: "))
s = Counter('beep boop beer!')
alf = set(s)

def func(count):
    lst = deque(s.most_common()[:-(len(count) + 1):-1])
    count = dict(count)

    value = lst[0][1] + lst[1][1]
    left = lst[0][0]
    right = lst[1][0]

    lst.popleft()
    count.pop(left)
    lst.popleft()
    count.pop(right)

    count = Counter(count)
    count[MyNode(value, right, left)] = value 
    return count

while len(s) > 1:
    s = func(s)
s = s.popitem()
s = s[0]
dic = {}

for i in alf:
    dic[i] = search(s, 2)

print(dic)




