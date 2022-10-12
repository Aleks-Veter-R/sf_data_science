"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 100) # загадываем число
left_predict_number = 0
right_predict_number = 100

# количество попыток
count = 0

while True:
    count+=1
    
    if count == 1:
        predict_number = int(
            input(
                "Угадай число от {} до {}: ".format(
                    left_predict_number,
                    right_predict_number
                )
            )
        )
    else:
        predict_number = int(
            input(
                "Искомое число лежит в интервале от {} до {}: ".format(
                    left_predict_number,
                    right_predict_number
                )
            )
        )

    if predict_number > number:
        print(
            'Число должно быть больше {}, но меньше {}!'.format(
                left_predict_number,
                predict_number
            )
        )
        
        right_predict_number = predict_number

    elif predict_number < number:
        print(
            'Число должно быть больше {}, но меньше {}!'.format(
                predict_number,
                right_predict_number,
            )
        )
        
        left_predict_number = predict_number
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла
