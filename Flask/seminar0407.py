import numpy as np
import threading
from multiprocessing import Process
import time
import asyncio


arr = np.random.randint(1, 101, 1000000)

threads = []
processing = []
result = 0
result_mp = 0

def sum_array(arr_slice):
    global result
    result += sum(arr_slice)

def sum_array_mp(arr_slice):
    global result_mp
    result_mp += sum(arr_slice)



def multithreading(arr):
    num_threads = 4
    slice_size = len(arr) // num_threads

    for i in range(num_threads):
        start = i * slice_size
        end = (i + 1) * slice_size if i < num_threads - 1 else len(arr)
        thread = threading.Thread(target=sum_array, args=(arr[start:end],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def multiprocessing_sum(arr):
    num_process = 4
    slice_size = len(arr) // num_process

    for i in range(num_process):
        start = i * slice_size
        end = (i + 1) * slice_size if i < num_process - 1 else len(arr)
        process = Process(target=sum_array_mp, args=(arr[start:end],))
        processing.append(process)
        process.start()
    for process in processing:
        process.join()


async def asynchrony():
    start_time = time.time()
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, sum_array, arr)
    return result


if __name__ == '__main__':
    start_time = time.time()
    multithreading(arr)
    print(f"Многопоточность. Сумма элементов массива: {result}, "
          f"время выполнения: {time.time() - start_time:.5f} секунд")
    start_time = time.time()
    result = multiprocessing_sum(arr)
    print(f"Многопроцессорность. Сумма элементов массива: {result_mp}, "
          f"время выполнения: {time.time() - start_time:.5f} секунд")
    result = asyncio.run(asynchrony())
    print(
        f"Сумма элементов массива (асинхронность): {result}, время выполнения: {time.time() - start_time:.5f} секунд")
