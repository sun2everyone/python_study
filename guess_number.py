# объявление функции
import random

def is_valid_int(input):
    if input.isdigit() and int(input)>0 and int(input)==float(input):
        return True
    else:
        return False

def is_valid(input, limit):
    if is_valid_int(input) and 1<=int(input)<=limit:
        return True
    else:
        return False

def check_bool(input):
    if input.lower()=='y':
        return 1
    elif input.lower()=='n':
        return 0
    else:
        return -1

def gen_random(n=100):
    return random.randint(1,n)

print('Добро пожаловать в числовую угадайку')
def get_value():
    n = input('Выберите верхнюю границу диапазона чисел:')
    while not is_valid_int(n):
        print('А может быть все-таки введем целое положительное число?')
        n = input('Выберите верхнюю границу диапазона чисел:')
    n = int(n)
    print('Отгадываем число от 1 до',n)
    return n

limit = get_value()
rnd=rnd = random.randint(1,limit)


count=0
while True:
    n = input('Введите целое число от 1 до '+str(limit)+' включительно:')
    if not is_valid(n, limit):
        print('А может быть все-таки введем целое число от 1 до ',limit,'?',sep='')
        continue
    else:
        n=int(n)
        count+=1
    if n>rnd:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif n<rnd:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем! Сделано попыток:',count)
        ans=-1
        while ans<0:
            ans=check_bool(input('Сыграть еще? y/n'))
        if not ans:
            break
        else:
            limit = get_value()
            rnd = random.randint(1, limit)
            count=0


print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
