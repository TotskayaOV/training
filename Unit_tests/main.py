# from Vehicle import Car, Motorcycle
#
#
# obj_1 = Car('BMW', 'x5', 2005)
# print(obj_1.get_speed())
# obj_1.testdrive()
# print(obj_1.get_speed())
# print(obj_1)
# motorcycle = Motorcycle('Lebedev Motors', 'Ataman', 2008)
# print(motorcycle)
input_list = [1,2,'aasf','1','123',123]
output_list = [x for x in input_list if isinstance(x, int|float)]
print(output_list)
# Домашнее задание к семинару №2 JUnit:
# 1. Настроить новый проект:
#  a). Нужно создать новый проект, со следующей структурой классов (3 отдельных класса):
#
#
#  b). Настроить тестовую среду
#      (создать тестовый класс VehicleTest, пометить папку как Test sources (зеленая папка),
#      импортировать необходимые для тестов библиотеки (JUnit, assertJ - все что было на семинаре))
#  c). Написать следующие тесты:
#      - проверка того, что экземпляр объекта Car также является экземпляром транспортного средства; (instanceof)
#      - проверка того, объект Car создается с 4-мя колесами
#      - проверка того, объект Motorcycle создается с 2-мя колесами
#      - проверка того, объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
#      - проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
#      - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта) машина
#      останавливается (speed = 0)
#      - проверить, что в режиме парковки (сначала testDrive, потом park  т.е эмуляция движения транспорта) мотоцикл
#      останавливается (speed = 0)