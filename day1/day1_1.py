if __name__ == '__main__':

    f = open("input.txt", 'r')
    content = f.read().split("\n")
    content.remove("")

    increase_count = 0
    last_value = 0

    for i in content:
        if last_value != 0 and int(i) > last_value:
            increase_count = increase_count + 1

        last_value = int(i)
    print(increase_count)
