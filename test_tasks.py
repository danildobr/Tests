import pytest
from tasks_1_2_3 import FlatIterator, solution, vote

def generate_data_solution():
    yield 1, 8, 15, (-3.0, -5.0)
    yield 1, -13, 12, (12.0, 1.0)
    yield -4, 28, -49, 3.5
    yield 1, 1, 1, 'корней нет'
    
@pytest.mark.parametrize('a,b,c,expected', generate_data_solution())
def test_solution_discriminant(a, b, c, expected):
    assert solution(a, b, c) == expected
    
####################################################################################
def generate_data_vote():
    yield [], None
    yield [1, 1, 1, 2, 3], 1
    yield [10, 10, 10, 10], 10
    yield [0, 2, 7, 8], 0
    yield [-8, -8, 3, 51], -8

@pytest.mark.parametrize('list_vote, expected', generate_data_vote())
def test_vote(list_vote, expected):
    assert vote(list_vote) == expected

####################################################################################
class TestFlatIterator:
    def setup_method(self):
        self.lists_1 = [['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],[1, 2, None]]
       
        self.lists_2 = [[['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]]
        
    def test_flatiterator_1(self):
        iterator = FlatIterator(self.lists_1)
        assert list(iterator) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    
    def test_flatiterator_2(self):
        iterator = FlatIterator(self.lists_2)
        assert list(iterator) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
        
    def test_empty_lists(self):
        assert list(FlatIterator([])) == []
        assert list(FlatIterator([[], [[]]])) == []
    
    
    