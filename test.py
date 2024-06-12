import time
from datetime import datetime


def read_file(file_name: str):
    time.sleep(3)
    with open(file_name) as f:
        data = f.read()
        print(f"{file_name} => {data}")


def main():
    files = ["data/data_1.txt", "data/data_2.txt"]
    for file in files:
        read_file(file)


if __name__ == "__main__":
    print(datetime.now())
    main()
    print(datetime.now())
