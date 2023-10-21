from pathlib import Path


def rename_files(count_num: int, suffix_file: str, save_out_name: list, finally_name='', dir_name=False):
    dir_path = Path.cwd()
    if dir_name:
        dir_path = dir_path / dir_name
    cnt = 1
    for obj in dir_path.iterdir():
        if obj.suffix == suffix_file:
            old_name = obj.stem
            new_name = ''
            start_name = 0 if len(old_name) < save_out_name[0] else save_out_name[0]
            len_name = (len(old_name) - 1) if len(old_name) < save_out_name[1] else save_out_name[1]
            for i in range(start_name, len_name):
                new_name += old_name[i]
            number_name = str(cnt) if len(str(cnt)) > count_num else ('0' * (count_num-len(str(cnt))) + str(cnt))
            new_name += finally_name + number_name + suffix_file
            obj.rename(dir_path / new_name)
            cnt += 1


if __name__ == '__main__':
    rename_files(3, '.txt', [1, 3], 'check', 'bin')
