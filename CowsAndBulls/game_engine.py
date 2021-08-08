from random import sample


class GameEngine:

    def __init__(self):
        self._holder = ()
        self._holder_number_user = []

    def guess_number(self):
        num = sample(range(0, 10), 5)
        if 0 == num[0]:
            value = num[1:]
        else:
            value = num[:4]
        self._holder = [char for char in value]

    def check_number(self, number):
        if len(str(number)) != 4:
            return 'Нужно 4х значное число, возможно у тебя 0 на первом месте) '
        set_number = set(str(number))
        if len(str(number)) != len(set_number):
            return 'Есть повторяющиеся числа '
        for x in str(number):
            if len(self._holder_number_user) == 4:
                self._holder_number_user.clear()
            self._holder_number_user.append(int(x))

    def animal_counter(self):
        cows = 0
        bulls = 0
        for i, value in enumerate(self._holder_number_user):
            if value == self._holder[i]:
                bulls += 1
            elif value in self._holder:
                cows += 1
        return cows, bulls

    def my_clear(self):
        del self._holder
        return self._holder_number_user.clear()
