import threading
import time
import requests
import os


threads = []
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
            tread = threading.Thread(target=print, args=(file_name, count_words(file_name)))
            threads.append(tread)
            tread.start()

if __name__ == '__main__':

    count_directory('C:/Users/ASUS/Documents/Projeckt/123/Flask')
    for thread in threads:
        thread.join()
    print(f"Downloaded {time.time()} in {time.time()-start_time:.2f} seconds")

