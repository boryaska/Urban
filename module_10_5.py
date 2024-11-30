from multiprocessing import Pool
import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            if line.strip() == '':
                break
            all_data.append(line.strip())
    return all_data        

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = time.time()
    for file in filenames:
        read_info(file)
    end = time.time()
    print(f'{end-start} (линейный)')

    start_time = time.time()
    with Pool(4) as p:
        res = p.map(read_info, filenames)
    end_time = time.time()

    print(f'{end_time-start_time} (многопроцессорный)')
    
    