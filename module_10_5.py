import time
from multiprocessing import Pool
from datetime import timedelta

def read_info(name):
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            # Обработка строки (если необходимо)
            line = line.strip()

if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    linear_duration = timedelta(seconds=end_time - start_time)
    print(f'Время выполнения линейного вызова: {linear_duration}')

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    multiprocessing_duration = timedelta(seconds=end_time - start_time)
    print(f'Время выполнения многопроцессного вызова: {multiprocessing_duration}')