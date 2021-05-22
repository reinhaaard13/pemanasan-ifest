def main():
    number_list = input().split()
    even_list = [int(x) for x in number_list if int(x)%2 == 0]
    odd_list = [int(x) for x in number_list if int(x)%2 != 0]

    even_list.sort()
    odd_list.sort()

    if len(even_list) >= len(odd_list):
        print([x for x in list_mix(even_list, odd_list)])

def list_mix(first_list, second_list):
    mixed_list = []
    while first_list:
        try:
            mixed_list.append(first_list.pop(0))
            mixed_list.append(second_list.pop(0))
        except IndexError:
            break
    return mixed_list

if __name__ == "__main__":
    main()