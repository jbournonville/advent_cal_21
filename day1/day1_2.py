
if __name__ == '__main__':

    content = open('input.txt', "r").readlines()

    increase_count = 0

    for i in range(0, len(content)):

        firstBatch = content[i: i + 3]
        secondBatch = content[i + 1: i + 4]

        if sum(map(int, firstBatch)) < sum(map(int, secondBatch)):
            increase_count += 1

    print(increase_count)
