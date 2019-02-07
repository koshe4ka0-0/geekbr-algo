from binarytree import tree, bst

class MyNode:
    def __init__(self, value, right = None, left = None):
        self.value = value
        self.right = right
        self.left = left

#a = tree(height=3, is_perfect=True)
#print(a)
#b = bst(height=3, is_perfect=True)
#print(b)

bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input("Введите число для поиска: "))

def search(bin_tree, number, path = ''):
    if bin_tree.value == number:
        return f'Число {number} находится по следующему пути: \n Корень {path}'
    if number < bin_tree.value and bin_tree.left is not None:
        return search(bin_tree.left, number, path=f'{path}\n Шаг влево')
    if number > bin_tree.value and bin_tree.right is not None:
        return search(bin_tree.right, number, path=f'{path}\n Шаг вправо')
    
    return f'Число {number} в дереве не найдено'


print(search(bt, num))
