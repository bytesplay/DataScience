#Игра: Угадай число.
import random

def predict_function(number):
    """Функция угадывает число, основываясь на сравнении его с подаваемым
    агрументом n и возвращает количество попыток для достижения цели.
    Args:
        number (int): число, которое необходимо угадать
    """
    #Задаем начальный и конечный интервал поиска
    start = 1
    end = 100
    iteration = 0
    while True:
        iteration += 1
        prediction = round((end + start)/2) #Предполагаемое число - середина интервала поиска
        if prediction > number:
            end = prediction
        elif prediction < number:
            start = prediction
        else:
            # print(f"Загаданное число {prediction} найдено за {iteration} шагов")
            break
    return iteration

def middle(function, runs=1000):
    """Функция считает средний результат выполнения функции,
    передаваемой аргументом, при выполнении runs раз

    Args:
        function (function): _description_
        runs (int, optional): _description_. Defaults to 1000.
    """
    result = 0
    for i in range(runs):
        number = random.randint(1, 100) #Загадываем число от 1 до 100
        result += predict_function(number)
    middle_result = round(result/runs)
    print("Среднее количество попыток:", middle_result)

middle(predict_function)
