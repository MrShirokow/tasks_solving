'''
                                                    Камень, ножницы, бумага
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. 
Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.
'''


data = {'камень': {'ножницы': 1, 'бумага': 0},
        'ножницы': {'бумага': 1, 'камень': 0},
        'бумага': {'камень': 1, 'ножницы': 0}}

timur_step, ruslan_step = (input() for _ in range(2))
result = data[timur_step].get(ruslan_step)
print('ничья' if result is None else ['Руслан', 'Тимур'][result])