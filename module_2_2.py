first = int(input('Введите первое число:'))
second = int(input('Ведите второе чмсло:'))
third = int(input('ведите третье число:'))
if first == second == third:
    print('3')
elif first != second and second == third or first == second and second != third or first != third and second == third or first == third and second != third:
    print('2')
elif first != second != third:
    print('0')