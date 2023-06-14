day = "Thursday"
match day:
    case "Sunday"    : print("Take it easy")
    case "Monday"    : print("Go to work")
    case "Tuesday"   : print("Work + Hobbies")
    case "Wednesday" : print("Meetings")
    case "Thursday"  : print("Presentations")
    case "Friday"    : print("Interviews and party")
    case "Saturday"  : print("Time to do sports")

def greet(name=None):
    match name:
        # Check if name == None
        case None:
            print("Hello there")
        # Store name into some_name if it is not None
        case some_name:
            print(f"Hello {some_name}")
greet()       # Prints "Hello there"
greet("Jack") # Prints "Hello Jack"


coinflip = 4
match coinflip:
    case 1:
        print("Heads")
        exit()
    case 0:
        print("Tails")
    case _:
        print("Must be 0 or 1.")

# в этом случае проверяется только количество найденных элементов. Здесь мы использовали подстановку, чтобы убедиться, 
# что в кортеже есть два элемента, не заботясь об отдельных значениях элементов.
location = (0, 0)
match location:
    case(_,):
        print("1D location found")
    case(_, _):
        print("2D location found")
    case(_, _, _):
        print(("3D location found"))

# В качестве шаблонов выражения match-case можно использовать элементы перечислений (enumerations).
# Чтобы это продемонстрировать, давайте создадим класс перечисления Direction (унаследованный от класса Enum), 
# представляющий четыре основных направления на компасе.
# Далее создадим функцию handle_directions(), которая принимает элемент класса Direction в качестве входного аргумента. 
# Эта функция сопоставляет этот аргумент с одним из направлений из перечисления и реагирует соответствующим образом.
from enum import Enum
class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
def handle_directions(direction):
    match direction:
        case Direction.NORTH: print("Heading North")
        case Direction.EAST: print("Heading East")
        case Direction.SOUTH: print("Heading South")
        case Direction.WEST: print("Heading West")
handle_directions(Direction.NORTH)

# давайте проверим, является ли местоположение (переменная location) точкой 1D, 2D или 3D. 
# Кроме того, давайте будем сохранять значения координат в отдельных переменных в зависимости от количества измерений.
location = (1, 3)
match location:
    case x, :
        print(f"1D location found: ({x})")
    case x, y:
        print(f"2D location found: ({x}, {y})")
    case x, y, z:
        print((f"3D location found: ({x}, {y}, {z})"))
# Данный код сопоставляет переменную location, в которой сохранен некий кортеж с координатами, 
# с кортежами из одного, двух или трех элементов. А затем значения координат распаковываются в различные переменные.
# Если в кортеже больше значений, но важны только первые три, можно использовать оператор *.
# Допустим, есть кортеж с координатами, сохраненный в переменную location. И вдобавок в нем еще могут храниться 
# посторонние элементы. Чтобы отловить «лишние» элементы, воспользуемся оператором *:

location = (1, 3, 2, "a", "b", "c")
match location:
    case x, :
        print(f"1D location found: ({x})")
    case x, y:
        print(f"2D location found: ({x}, {y})")
    case x, y, z, *names:
        print((f"3D location found: ({x}, {y}, {z})"))
        print(f"Also, there was some extra data: {names}")

# В конструкции match-case можно сравнивать сразу несколько шаблонов.
# Для этого используется логический оператор |(или). Таким образом проверяется, соответствует ли 
# хотя бы один шаблон заданному значению.
# Например, давайте проверим, выходным или рабочим днем является день недели:

day = "Monday"
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Work")