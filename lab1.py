# -*- coding: utf-8 -*
"""
Скрипт lab1 принимает файл с перечислением N цифр и сумму S, которую нужно получить арифмитическими действиями "+" и "-" . 
В результате выводит в файл полученное равенство с расставленными знаками
Формат входных данных: N X1 X2 ... XN S
Формат выходныъ данных: X1 +/- X2 +/- ... +/- XN = S
"""
from typing import Union

def findSolution(numbers: list,targetSum: int,expression: str, index = 0,currentSum = 0) -> Union[str,None]:
    """
    Основная функция рекурсивного поиска решений 
    
    :param 
    numbers(list): Входное значение с массивом из N чисел
    targetSum(int): Входное константное значение S, число, которое стремится получить выходная программа
    expression(str): Переменное значение текущего выражения чисел
    index(int): Входное значение, определяющее индекс числа из numbers(list)
    currentSum(int): Значение текущего выражение expression(str)

    :return 
    expression(str)|(None): Возращает строковое зачение выражения чисел, если оно равно targetSum(int), а иначе None
    """   
    # Если подошли к концу проверяем уравнение на соответствия условию
    if index == len(numbers):
        if currentSum == targetSum: return expression
        return None
    currentNumber = numbers[index]
    # Разбиваем на два случая рекурсию: + и - и идем глубже
    result = findSolution(
        numbers,
        targetSum,
        str(expression)+"+"+str(currentNumber),
        index+1,
        currentSum+currentNumber
    )
    if result: return result
    result = findSolution(
        numbers,
        targetSum,
        str(expression)+"-"+str(currentNumber),
        index+1,
        currentSum-currentNumber
    )
    if result: return result
    return None

def solveExp(fileAdressInput: str,fileOutput: str):
    """
    Вспомогательная функция для операций с файлами. 
    Выводит результат в отдельны файл, либо пишет 'no solution'
    
    :param 
    fileAdressInput(str): Входное значение с адрессом входного файла
    fileOutput(str): Входное значение с адрессом выходного файла

    :return 
    (None)
    """   
    with open(fileAdressInput,"r") as file:
        fileString = list(map(int,file.readline().split()))
        N = fileString[0]
        numbersArray = fileString[1:N+1]
        targetSum = int(fileString[N+1])
        result = findSolution(numbersArray,targetSum,numbersArray[0])
        with open(fileOutput,"w") as output:
            if result: output.write(result + "=" + str(targetSum))
            else: output.write('no solution')

if __name__ == "__main__":
    solveExp('input.txt', 'output.txt')