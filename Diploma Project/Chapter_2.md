# Глава 2

## 2.1 Выбор формата данных для загрузки

Самые распространенные форматы выгрузки данных Excel и CSV. В случае с ботом главным ограничением является размер напрямую пересылаемого файла, поэтому предпочтительнее использовать файл CSV. CSV-файлы хранят данные в текстовом формате разделенные заданным разделителем (обычно запятой), файлы Excel хранят табличный формат данных. Помимо прочего  данные с расширением .csv для выгрузки как правило доступны на всех сервисах.  На уровне встроенного языка, Python содержит встроенную библиотеку для работы с CSV файлами, с помощью которой программисты могут без особого труда работать с файлами электронных таблиц CSV. Каждая новая запись в файле CSV начинается с новой строки. Формат файлов CSV можно легко экспортировать в электронные таблицы или базы данных.

Библиотека CSV
Эта библиотека является встроенной, и её не нужно дополнительно скачивать через систему управления пакетами pip. Эта библиотека является основной для работы с файлами CSV в Python. Она импортируется как обычные встроенные библиотеки:

Чтобы прочитать файл csv, необходимо создать объект reader:

`object = csv.reader(data, delimiter = ";")`

Объект reader имеет метод __next__(), и является итерируемым объектом.
Чтение файла будет происходить так:

```
import csv

with open("file.csv", encoding="utf-8") as file:

    csvfilereader = csv.reader(file, delimiter=";")
```

Конструкция with…as используется для того, чтобы быть уверенным, что файл будет корректно закрыт в случае если при выполнении программного кода произойдет непредвиденная ошибка.

Конструкция with…as используется для того, чтобы быть уверенным, что файл будет корректно закрыт в случае если при выполнении программного кода произойдет непредвиденная ошибка.

Стоит уделить внимание на то, что если перед чтением файла принудительно не установить правильную кодировку, в которой ранее файл был сохранен в нашем случае «UTF-8», то будет использоваться кодировка, определенная по умолчанию. Для windows это cp1251.

Встроенная библиотека работы с CSV позволяет использовать словари для работы с файлами. Для этого необходимо создать объект DictReader. С его помощью обращаться к элементам можно будет по имени столбцов, а не с помощью индексов.

При использовании DictReader в первой строке цикла будет содержаться не заголовок таблицы, а первая строка с данными. Поэтому для вывода заголовка используется условие i==0.

Для записи информации с CSV файл нужно использовать специальный объект writer.

 
`w = csv.writer(file, delimiter = "\t")`
Запись новой строки в файл осуществляется с помощью метода writerow(). Этот метод имеет следующий синтаксис:
 
`writerow("Имя", "Пол", "Возраст")`
Пример программы с использованием метода writerow():
```
import csv
 
with open("file.csv", mode="w", encoding='utf-8') as file:
 
    w = csv.writer(file, delimiter = ",", lineterminator="\r")
 
    w.writerow(["Имя", "Пол", "Возраст"])
 
    w.writerow(["Даша", "Женский", "7"])
 
    w.writerow(["Степа", "Мужской", "14"])
 
    w.writerow(["Иван", "Мужской", "16"])
```
 В метод writerow() необходимо передавать список, который в последствии будет записан в файл через симол-разделитель.

 Запись в файл также может быть осуществлена с помощью объекта DictWriter.

Метод DictWriter требует строгого указания параметра fieldnames. В качестве данных для записи используется словарь. Объект DictWriter также имеет еще один замечательный метод:

writerows(rows) – Записывает все элементы строк.

## 2.2. Библиотека Polars

Для работы с данными можно использовать только Python, но можно ускорить их обработку благодаря дополнительным билиотекам для работы с данными.
Наиболее часты выбором является Pandas. Но у Pandas есть ряд недостатков: 
1. потребление большого количества памяти
2. потребление большого объема оперативной памыти: память должна превышать объем данных в 5-10 раз
3. нет многопроцессорной поддержки
Поэтому в качестве обработки и анализа данных была выбрана билиотека Polars в качестве универсального инструмента для обработки небольших данных. Polars работает очень быстро и фактически является одним из наиболее эффективных доступных решений.

![Сравнение скорости работы распространенных билиотек с официального сайта Polars](./Images/polars.png)

Polars - это высокопроизводительная библиотека фреймов данных для работы со структурированными данными. Ядро написано на Rust, но библиотека доступна на Python, Rust и NodeJS. 
Её ключевыми функциями являются:
1. Скорость. Polars написан с нуля, разработан близко к машине и без внешних зависимостей.
2. Ввод и вывод дыннх.
3. Обрабатывает наборы данных, намного превышающие объем доступной оперативной памяти.
4. Оптимизация запросов для уменьшения ненужной работы / выделения памяти.
5. Многопоточность: Polars поддерживает преобразование данных с помощью своего потокового API вне основного потока. Позволяет обрабатывать результаты, не требуя одновременного хранения всех данных в памяти
6. Многопроцессорность: Polars распределяет рабочую нагрузку между доступными ядрами процессора без какой-либо дополнительной настройки.
7. Механизм векторных запросов: Polars использует Apache Arrow, столбчатый формат данных, для обработки ваших запросов векторным способом. Он использует SIMD для оптимизации использования ЦП.

Для установки Polars используется стандартная команды:

`pip install polars`




Как таковое Polars имеет большое значение для:

Уменьшите количество избыточных копий.
Эффективно просматривайте кэш памяти.
Сведите к минимуму конфликты при параллелизме.
Обрабатывайте данные порциями.
Повторно используйте выделенную память.