def count_words():
    # Open file
    file = open('jocker.txt', 'r')
    string = file.read()


    # Split text by space

    for word in string.split(" "):
        print("The {1} and {1}".format(word, len(word)))


if __name__ == "__main__":
    count_words()
