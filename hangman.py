import random
word_list=[
    'мама',
    'папа',
    'мыло',
    'рама',
    'авокадо',
    'ерунда',
    'параллелепипед'
    'синхрофазотрон'
]

def get_word(lst):
    return random.choice(lst).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word=word.upper()
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    if len(word)>=6: #упрощаем, открывая первую и последнюю буквы
        word_completion=word[0]+word_completion[1:]
        word_completion=word_completion[:-1]+word[-1]
    while tries>0 and not guessed:
        print(display_hangman(tries))
        print('Слово:')
        print(word_completion)
        char = input('Введите букву или слово целиком: ') or '.'
        while not char.isalpha():
            print('Ввод некорректный, попробуйте еще раз!')
            char = input('Введите букву или слово целиком: ')
        char=char.upper()
        if len(char)==1 and char in guessed_letters:
            print('Вы уже вводили букву',char)
            continue
        else:
            guessed_letters.append(char)
        if len(char)>1 and char in guessed_words:
            print('Вы уже вводили слово', char)
            continue
        else:
            guessed_words.append(char)
        if not char in word:
            tries-=1
        else:
            if len(char)>1 and char == word:
                guessed=True
            elif len(char)==1:
                for i in range(len(word)):
                    if word[i]==char:
                        word_completion=word_completion[:i]+char+word_completion[i+1:]
        if word_completion==word:
            guessed=True
    print('Загаданное слово: ',word)
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Удачи в следующий раз!')

def check_bool(input):
    if input.lower()=='y':
        return 1
    elif input.lower()=='n':
        return 0
    else:
        return -1

########################################
print('Давайте играть в угадайку слов!')
pl = -1
while pl<0:
    pl=check_bool(input('Сыграем? y/n: '))
    if pl==1:
        play(get_word(word_list))
        pl=-1
