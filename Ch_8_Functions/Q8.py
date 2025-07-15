# Write a python function to remove a given word from a list ad strip it at the same time.

def remove_word_part(words, part_to_remove):
    new_list = []

    for w in words:
        w = w.strip()  # remove spaces
        if part_to_remove not in w:  # if the part is NOT in the word
            new_list.append(w)

    return new_list

words = ["  apple", "banana ", " mango", "grape", " pineapple", " orange "]
part_to_remove = "an"

result = remove_word_part(words, part_to_remove)

print("Cleaned list:", result)
