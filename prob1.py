import sys

def count(ranges):
    count = 0
    start_range = int(ranges[0])
    end_range = int(ranges[1])

    for y in range(start_range,end_range,1):
        if str(y)[-1] == '3' or str(y)[-1] == '4':
            count += 1
    return count

def main():
    jp = int(input())
    ranges = []
    for _ in range(jp):
        inp = sys.stdin.readline().rstrip('\n')
        ranges.append(inp)

    for rng in ranges:
        print(count(rng.split()))

if __name__ == "__main__":
    main()