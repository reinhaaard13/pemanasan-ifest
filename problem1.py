import sys

def count(jp,ranges):
    for i in range(jp):
        count = 0
        start_range = int(ranges[i][0])
        end_range = int(ranges[i][1])

        for y in range(start_range,end_range,1):
            if str(y)[-1] == '3' or str(y)[-1] == '4':
                count += 1
        print(count)

def main():
    jp = int(input())
    ranges = []
    for _ in range(jp):
        inp = sys.stdin.readline().rstrip('\n')
        ranges.append(inp.split())
    count(jp,ranges)

if __name__ == "__main__":
    main()