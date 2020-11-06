"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
# Первый вариант предпочтительнее, т.к. сложность меньше
# Первый вариант: O(n)
def search_1(info):
    names = list(info.keys())       # O(n) + O(1) = O(n)
    profits = list(info.values())   # O(n) + O(1) = O(n)
    max_profit_companies = {}       # O(1)
    while len(max_profit_companies) < 3:    # O(1) - цикл всегда делает три прохода
        el = profits.index(max(profits))    # O(n)
        max_profit_companies[names[el]] = profits[el]   # O(1)
        names.pop(el), profits.pop(el)  # 2 * O(n)
    return max_profit_companies

# Второй вариант: O(N log N)
def search_2(info):
    new_lst = list(info.items())   # O(N) + O(1)
    new_lst.sort(key=lambda x: x[1]) # O(N logN)
    return new_lst[:3:-1] # O(N)

company_info = {'Рога': 500000, 'Копыта': 345000, 'Рога и Копыта': 800000, 'ПАО Газпром': 5000002,
    'ООО Ритейл': 1300000, 'ИП Заваркин': 180000, 'ПАО Лукойл': 5000001}

print(search_1(company_info))
print(search_2(company_info))