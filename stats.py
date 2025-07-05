def sort_on(items):
    return items["num"]

def get_num_cha(text):
    result = {}
    for c in text:
        cha = c.lower()
        if cha.isalpha() != True:
            pass
        elif cha in result:
            result[cha] += 1
        else:
            result[cha] = 1
    new_result = []
    for key in result:
        new_result.append({"char": key, "num": result[key]})
    new_result.sort(reverse=True, key=sort_on)
    return new_result

def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        cha_list = get_num_cha(file_contents)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for cha in cha_list:
            print(f"{cha["char"]}: {cha["num"]}")
        print("============= END ===============")

