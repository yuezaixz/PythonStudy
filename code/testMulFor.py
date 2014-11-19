def main():
    print [ str(x)+str(y)+str(z) for x in range(1,10) for y in range(0,10) for z in range(1,10) if x == z ]
if __name__ == "__main__":
    main()