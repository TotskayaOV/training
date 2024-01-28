import requests
from datetime import datetime
from multiprocessing import Process, Pool
import time


processes = []
start_time = time.time()


def download_image(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + str(datetime.now().timestamp()) + '.png'
    with open(filename, "wb") as f:
        f.write(response.content)
        print(f"Downloaded {url} in {time.time()-start_time:.2f} seconds")


def multiprocessing(urls):
    for url in urls:
        process = Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


if __name__ == '__main__':
    urls = ['https://avatars.mds.yandex.net/i?id=be0194f08f8302cc7c1c55d836b3465fbb08e5f6-12645377-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=26eef3948c699b5b1000dc9e1bb2f068db1ddf4d-10995124-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=5928f2b58c6f204d0e0c3a5c41c07e136f6d2cea-12544737-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=ae55f3cacaf3431753bccf7e3a863987f45ee0f4-10807079-images-thumbs&n=13',
            'https://avatars.mds.yandex.net/i?id=acf92da9844f00928e2390fc14cae357a52b07bf-11481522-images-thumbs&n=13'
            ]
    multiprocessing(urls)
