from inspect import isgeneratorfunction 

def numList(max): 
    n = 1
    while n <= max: 
        yield n 
        n = n + 1
def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return
def main():
    print isgeneratorfunction(numList) 
    for num in numList(10):
        print num

    for content in read_file('../README.md'):
        print content

if __name__ == "__main__":
    main()
