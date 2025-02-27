def get_wordcount(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    words = text.lower()
    for char in words:
        if char in char_dict:
            char_dict[char] += 1
        else: 
            char_dict[char] = 1
    return char_dict

def sort_on(dict_item):
    char = list(dict_item.keys())[0]
    return dict_item[char]
        
def sort_dict(dict):
    list_raw = []
    for key, value in dict.items():
        paired_dict = {key: value}
        if key.isalpha():
            list_raw.append(paired_dict)
    list_raw.sort(key=sort_on, reverse=True)
    return list_raw
    
