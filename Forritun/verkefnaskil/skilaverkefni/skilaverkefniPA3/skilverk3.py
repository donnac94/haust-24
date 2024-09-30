def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("File not found!")
        return None

def write_file(filename, words):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')
    print("File written!")

def print_word_by_line(words, line_number):
    if line_number.isdigit() and 1 <= int(line_number) <= len(words):
        print(words[int(line_number) - 1])
    else:
        print("Invalid line number!")

def search_words(words, search_str):
    results = [word for word in words if word.startswith(search_str)]
    if results:
        for word in results:
            print(word)
    else:
        print("No words found starting with", search_str)

def append_word(words, word):
    words.append(word)
    print(f'Appended word: {word}')

def main():
    filename = input("Enter filename: ")
    words = read_file(filename)
    
    if words is None:
        return
    
    while True:
        action = input("Enter action: ").strip()
        
        if action.startswith('l/'):
            line_number = action[2:]
            print_word_by_line(words, line_number)
        
        elif action.startswith('s/'):
            search_str = action[2:]
            search_words(words, search_str)
        
        elif action.startswith('a/'):
            word = action[2:]
            append_word(words, word)
        
        elif action == 'w':
            write_file(filename, words)
        
        elif action == 'q':
            break
        
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()