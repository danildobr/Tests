# Задание «Квадратное уравнение»
# нахождение корней дискриминанта
import math

def discriminant(a, b, c):
    return b ** 2 - 4 * a * c  

def solution(a, b, c):
    if discriminant(a, b, c) > 0:
        root_1 = (- b + math.sqrt(discriminant(a, b, c))) / (2 * a)
        root_2 = (- b - math.sqrt(discriminant(a, b, c))) / (2 * a)
        return root_1, root_2
    
    elif discriminant(a, b, c) == 0:
        return ((- b / (2 * a)))
    
    else:
        return ('корней нет')
#########################################################
# Задание «Голосование»
# Условие задачи
# Нужно реализовать функцию, принимающую список чисел. Вывести число, которое встречается чаще всего. 
# Максимальное число голосов всегда уникально.
# В результате корректного выполнения задания будет выведен следующий результат:

def vote(list_vote):
    dict_vote = {}
    for el in list_vote:
        if el in dict_vote:
            dict_vote[el] += 1
        else:
            dict_vote[el] = 1
                       
    maxi = 0
    max_vote = None
    for key, volu in dict_vote.items():
        if volu > maxi:
            maxi = volu
            max_vote = key         
        
    return max_vote
#########################################################
# «Iterators»

class FlatIterator:
    def __init__(self, lists_1):
        self.lists_1 = lists_1
    
    def __iter__(self):
        self.el = self.get_el_list(self.lists_1)
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.el):
            raise StopIteration
        return self.el[self.cursor]
    
    def get_el_list(self, lists_1):
        result = []
        for el in lists_1:
            if not isinstance(el, list):
                result.append(el)
            else:
                result.extend(self.get_el_list(el))
        return result
