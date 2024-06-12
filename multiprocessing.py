import time
import multiprocessing
from datetime import datetime


def write_file(file_path: str, data: str):
    time.sleep(3)
    with open(file_path, 'r+') as file:
        file.write(data)
        print(f"data written to {file_path}\n")


def main():
    file_path1 = 'data/data_1.txt'
    file_path2 = 'data/data_2.txt'
    data = ' hello teacher'
    data = 'my name is Zoirjon'

    process1 = multiprocessing.Process(target=write_file, args=(file_path1,)),
    process1 = multiprocessing.Process(target=write_file, args=(file_path2,)),

    process1.start()
    process2.start()

    process1.join()
    process2.join()


if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())
