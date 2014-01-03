def contains(array, e):
    for i in range(0,len(array)):
        if array[i] == e:
            return True

    return False

def count(enc):
    unique = []
    unique.append(enc[0])
    count = []
    count.append(1)
    for i in range(1,len(enc)):
        if contains(unique, enc[i]):
            count[unique.index(enc[i])] += 1
        else:
            unique.append(enc[i])
            count.append(1)

    return count

def main():
    message = open('encrypted_message.txt', 'r')
    enc = []
    for line in message:
        enc.append(line)
    message.close()

    enc_count = []
    enc_count = count(enc)
    print(len(enc_count))
if __name__ == '__main__':
    main()
