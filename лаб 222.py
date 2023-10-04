def main():

    text = input("Введіть текст: ")
    words = text.split()
    word_count = len(words)
    char_count = 0
    for word in words:
        char_count += len(word)

    print("Кількість слів:", word_count)
    print("Кількість символів:", char_count)

if __name__ == "__main__":
    main()