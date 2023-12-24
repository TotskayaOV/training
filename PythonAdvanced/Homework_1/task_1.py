START_POINT = 2
STOP_POINT = 11
TABLE_HEADER = 'Таблица умножения'
COLUMNS_NUM = 4

def four_columns(start_num=START_POINT):
    result_str = ''
    for i in range(START_POINT, STOP_POINT):
        cnt = 0
        while cnt < COLUMNS_NUM:
            result_str += f'{start_num + cnt} * {i} = {i * (start_num + cnt)}\t\t'
            cnt += 1
        print(result_str)
        result_str = ''

print(f'\n{TABLE_HEADER:^58}\n')
four_columns()
print()
four_columns(start_num=START_POINT + COLUMNS_NUM)
