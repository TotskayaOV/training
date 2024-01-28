import sys
import time
from multithr import multithreading
from multipr import multiprocess
from asynch import asynchrony


start_time = time.time()


if __name__ == "__main__":
    urls = sys.argv[1:]
    multithreading(urls)
    multiprocess(urls)
    asynchrony(urls)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    