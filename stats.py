def get_total_words(text):
    return len(text.split())

def get_character_count(text):
    character_output = {}
    for i in text:
        lowercase_character = i.lower()
        if lowercase_character in character_output:
            character_output[lowercase_character] += 1
        else:
            character_output[lowercase_character] = 1
    return character_output

def sort_key(count):
    return count["num"]

def get_sorted_dictionary(input_dictionary):    
    list_of_dictionaries = []

    for key, value in input_dictionary.items():
        small_dictionary = {"char": key, "num": value}
        list_of_dictionaries.append(small_dictionary)
    
    list_of_dictionaries.sort(reverse=True, key=sort_key)
    return list_of_dictionaries







