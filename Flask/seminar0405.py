from multiprocessing import Process, Pool
import time
import requests
import os


processing = []
start_time = time.time()

file_name = ''

def count_words(file_name):
    with open(file_name, 'r', encoding='UTF-8') as f:
        text = f.read()
        words = text.split()
        return len(words)

def count_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_name = os.path.join(root, file)
            process = Process(target=print, args=(file_name, count_words(file_name)))
            processing.append(process)
            process.start()


if __name__ == '__main__':
    count_directory('C:/Users/ASUS/Documents/Projeckt/123/Flask')
    for process in processing:
        process.join()
    print(f"Downloaded {time.time()} in {time.time() - start_time:.2f} seconds")
