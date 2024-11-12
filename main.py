
def main():
    book_path = 'books/frankenstein.txt'
    file_contents = get_book_text(book_path)
    wc = word_count(file_contents)
    cc = char_count(file_contents)
    report = sort_char_count(cc)
    print(f'Report on {book_path}')
    print(f'Document contains {wc} words\n')
    for char_dict in report:
        alpha = char_dict["char"]
        count = char_dict["count"]
        print(f'The "{alpha}" character appeared {count} times')



def word_count(book_as_string):
    words = book_as_string.split()
    return len(words)

def char_count(book_as_string):
    # lowercase and split into chars
    lowered_str = book_as_string.lower()
    char_dict = {}
    for char in list(lowered_str):
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict['count']

def sort_char_count(char_dict):
    char_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            char_list.append({"char": key, "count": value})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

if __name__ == "__main__":
    main()