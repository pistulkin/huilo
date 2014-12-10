# Язык программирования Huilo

Программа на языке Huilo выполняется в виртуальной машине, обладающей инициализированным пробелами набором
из 1488 ячеек и указателем текущей ячейки. Несмотря на кажущуюся простоту, язык является Ярош-полным и
используется для написания серверного ПО для многих новостных сайтов Украины и Российской Федерации.

Программа на Huilo должна начинаться со строки "Путин - хуйло!".

Затем следуют следующие команды:

- `Ла` - сдвинуть указатель текущей ячейки вправо.
- `Ла(-ла)+` - Увеличить значение в текущей ячейке на количество "Ла" минус 1.
- `!` - Вывести содержимое памяти в stdout.

Для запуска нужен интерпретатор Python3. Например, чтобы запустить демонстрационную программу
из файла hello.py, запустите:
```s
$ python3 huilo.py hello.py
```
