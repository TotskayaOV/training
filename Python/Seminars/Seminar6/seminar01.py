def arifmetick(parse: list):
    while '*' in parse or '/' in parse:
        # result = (lambda pasre[i-1]: parse[i-1] * parse[i+1] for i in range(1, len(parse)) if parse[i] == '*')
        for i in range(1, len(parse)-1, 2):
            if parse[i] == '*':
                parse[i - 1] = float(parse.pop (i - 1)) * float(parse.pop (i))
                break
            elif parse[i] == '/':
                parse[i - 1] = float(parse.pop (i - 1)) / float(parse.pop (i))
                break
    while '+' in parse or '-' in parse:
        # result = (lambda pasre[i-1]: parse[i-1] * parse[i+1] for i in range(1, len(parse)) if parse[i] == '*')
        for i in range(1, len(parse)-1, 2):
            if parse[i] == '+':
                parse[i - 1] = float(parse.pop (i - 1)) + float(parse.pop (i))
                break
            elif parse[i] == '-':
                parse[i - 1] = float(parse.pop (i - 1)) - float(parse.pop (i))
                break
    return parse

# def brackets(parse: list):
#     while '(' in parse:
#         left = parse.index('(')
#         raght = parse.index(')')
#         if '(' in parse[left+1:raght]:
#             parse = brackets(parse[left+1:raght])
#         temp = arifmetick(parse[left+1:raght])
#         parse.insert(left, *temp)
#         del parse[left+1:raght+2]
#     return parse

user_input = input('Введите формулу: ')
num_str = ''
parse = user_input.replace('(', ' ( ').replace(')', ' ) ').replace('+', ' + ').replace('-', ' - ')\
                .replace('*', ' * ').replace('/', ' / ').split()
if '(' in parse:
    # while '(' in parse:
        left = parse.index('(')
        raght = parse.index(')')
        temp = arifmetick(parse[left+1:raght])
        parse.insert(left, *temp)
        del parse[left+1:raght+2]
parse = arifmetick(parse)    
try:
    num = int(*parse)
    print(*parse)
except:
    print(*parse)