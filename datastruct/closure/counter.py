def counter():
    count = [0];
    def instance():
        count[0] += 1
        return count[0]
    return instance

if __name__ == '__main__':
    counter1 = counter()
    counter2 = counter()
    print counter1()
    print counter1()
    print counter1()
    print counter2()
    print counter2()
    print counter2()
    print counter2()
    print counter2()
    print counter1()