def main():
    def sort_on(dict):
        return dict["count"]

    frank_contents = get_text("books/frankenstein.txt")
    char_dict = count_chars(frank_contents)
    alpha_count_arr = get_alpha_count_arr(char_dict)
    print(alpha_count_arr)
    alpha_count_arr.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankentein.txt ---")
    print(f"{count_words(frank_contents)} words found in the document\n")

    for char in alpha_count_arr:
        print(f"The '{char['letter']}' character was found {char['count']} times")

    print("--- End report ---")


def get_alpha_count_arr(char_dict):
    res_arr = []
    for key in char_dict:
        if key.isalpha():
            res_arr.append({"letter": key, "count": char_dict[key]})
    
    return res_arr


def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    res_dict = {}
    for c in text:
        c = c.lower()
        if c in res_dict:
            res_dict[c] += 1
        else:
            res_dict[c] = 1
    
    return res_dict

main()