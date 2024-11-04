# Виконання домашнього завдання
## Завдання 1
У файлі **HW8_Task1.py** імплементував дві функції для рішення задачі зі з'єднанням кабелів: одну з використанням купи, іншу без використання купи.
На цьому прикладі можемо побачити різницю в ефективності обох підходів.

Для випадково згенерованого списку
```
Initial cabel lengths: [337, 732, 991, 977, 66]
```
Кроки об'єднання для функції без купи, та загальна вартість будуть виглядати наступним чином:
```
[337, 732, 991, 977, 66]
[991, 977, 66, 1069]
[66, 1069, 1968]
[1968, 1135]
Загальна вартійсть: 7275
```
Кроки об'єднання для функції з купою, та загальна вартість будуть виглядати наступним чином:
```
[66, 337, 991, 977, 732]
[403, 732, 991, 977]
[977, 991, 1135]
[1135, 1968]
Загальна вартійсть: 6609
```
## Завдання 2
У файлі **HW8_Task2.py**, згідно із завданням імплементував функцію **merge_k_lists(lists)**
```python
def merge_k_lists(lists):
    min_heap = []
    for lst in lists:
        for el in lst:
            heapq.heappush(min_heap, el)
    return heapq.nsmallest(len(min_heap), min_heap)
```
Враховуючи те, що функція **heapq.nsmallest(n, iterable)**, за умови що **n** більше або дорівнює розміру **iterable**, повертає просто результат виконання функції **sorted** на колекції, 
це рішення слід вважати просто демонстрацією ознайомлення з пакетом **heapq**. Альтернативно, повернення результату може виглядати так:
```python
return [heapq.heappop(min_heap) for _ in range(len(min_heap))]
```
