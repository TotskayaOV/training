import argparse
import os
import logging
from collections import namedtuple


def parse_arguments():
    parser = argparse.ArgumentParser(description='Parse directory contents')
    parser.add_argument('directory', type=str, help='Path to the directory')
    return parser.parse_args()


def get_dir_content(directory):
    Entry = namedtuple('Entry', ['name', 'extension', 'is_dir', 'parent_directory'])
    entries = []
    for root, dirs, files in os.walk(directory):
        parent_directory = os.path.basename(os.path.normpath(root))
        for f in files:
            name, extension = os.path.splitext(f)
            entry = Entry(name=name, extension=extension, is_dir=False, parent_directory=parent_directory)
            entries.append(entry)
        for d in dirs:
            entry = Entry(name=d, extension='', is_dir=True, parent_directory=parent_directory)
            entries.append(entry)
    return entries


def save_entries_to_file(entries):
    with open('././directory_content.txt', 'w') as file:
        for entry in entries:
            line = f'Name: {entry.name}, ' \
                   f'Extension: {entry.extension}, ' \
                   f'Is Dir: {entry.is_dir}, ' \
                   f'Parent Directory: {entry.parent_directory}\n'
            file.write(line)


def setup_logging():
    logging.basicConfig(filename='././log.txt', level=logging.INFO, encoding='UTF-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')



if __name__ == '__main__':
    args = parse_arguments()
    directory = args.directory
    setup_logging()
    logging.info(f'Запуск анализа каталога: {directory}')
    entries = get_dir_content(directory)
    save_entries_to_file(entries)
    logging.info('Анализ каталога выполнен')
