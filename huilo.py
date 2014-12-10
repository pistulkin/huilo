import sys
import re


DEBUG = False


class Machine:
    ALPHABET = ' АБВГҐДЕЄЖЗИIЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ.,!?:"@$'
    MEMLEN = 14

    def __init__(self):
        self.memory = []
        self.ptr = 0
        self.clear()

    def clear(self):
        self.memory = [0] * self.MEMLEN
        self.ptr = 0

    def incr(self, n):
        if DEBUG: print('INCR(%d)' % n)
        self.memory[self.ptr] += int(n)
        self.fwd()

    def fwd(self):
        if DEBUG: print('FWD')
        self.ptr += 1
        self.ptr %= self.MEMLEN

    def out(self):
        if DEBUG: print('OUT')
        if DEBUG: print(self.memory)
        human = ''.join([self.ALPHABET[i] for i in self.memory]).strip()
        print(human)


def run(source):
    sig = 'путин - хуйло!'
    machine = Machine()

    with open(source) as fh:
        line = fh.readline().strip().lower()
        if line != sig:
            raise Exception('Программа должна начинаться со строчки "Путин - хуйло!"')

        linecnt = 1
        for line in fh:
            linecnt += 1
            line = line.strip().lower()
            if line == '' or line[0] == '#':
                continue

            for command in line.split(' '):
                if command[-1] == '!':
                    flush = True
                    command = command[:-1]
                else:
                    flush = False

                if command == '':
                    pass

                elif command == 'ла':
                    machine.fwd()

                elif command == '!':
                    machine.out()

                elif re.match('^ла(-ла)+$', command):
                    n = (len(command) + 1) / 3 - 1
                    machine.incr(n)

                else:
                    raise Exception('Синтаксическая ошибка в команде "%s" в строке %d' % (command, linecnt))

                if flush:
                    machine.out()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Интерпретатор языка Huilo.\nДля запуска программы на языке Huilo, передайте имя файла в первом параметре.')
        exit()

    run(sys.argv[1])
