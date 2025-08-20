# iterable -> __iter__ -> iterator objects       iterable to protokół
# iterator -> co musi miec protokół iteratora? __iter__ & __next__ -> item | StopIteration
from typing import Iterator


numbers = [1,2,3,4,5]

iterator = iter(numbers) # wywołuje __iter__ i zwraca iterator obj.

# for number in iterator:
#     print(number)
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) wyrzuci błąd StopIteration

class Range: # moja pierwsza klasa, która spełnia dwa protokoły naraz :D:D;D
    def __init__(self, start: int, stop: int | None = None, step: int =1, /) -> None:
        if stop is None:
            stop = start
            start = 0

        self.start = start
        self.stop = stop
        self.step = step

        self.item = start
        self. counter = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.counter >= (self. stop - self.start) // self.step:
            raise StopIteration("Something is yes no")

        result = self.item

        self.counter += 1
        self.item += self.step

        return result

r1 = Range(0, 5, )
it = iter(r1)
# print(r1 is it) # True bo __new__ zwraca to samo co __iter__
#
# print(next(r1)) # moge użyć r1 bo to to samo co iter(r1)
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))



class Odd:
    def __init__(self, iterable):
        self.iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.iterable):
            raise StopIteration('Yolo')

        for item in self.iterable[self._index]:
            if self._index % 2 == 0:
                self._index += 1
                return item
            else:
                self._index += 1


class Iterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Odd(self.data)


for element in Iterable([1, 2, 3, 4, 5, 6]):
     print(element)





