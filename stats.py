def counting_words(txt):
    
    new = []
    new = txt.split()

    return len(new)

def counting_each_character(txt):

    dict_text = list(txt.lower())
    new_dict = {}

    for l in dict_text:
        #new_dict[l] = new_dict[l] + 1
        if l not in new_dict:
            new_dict[l] = 1
        else:
            new_dict[l] = new_dict[l] + 1
    
    return new_dict

def sort_on(items):

    return items["num"]

def sorting(txt):

    new_list = []

    for l in txt:

        #print(f"its {l} and {txt[l]}")
        ltr = {}
        if l != " ":
            ltr["letter"] = l
            ltr["num"] = txt[l]
            new_list.append(ltr)

    #print(new_list.sort(reverse = True))
    
    new_list.sort(reverse=True, key=sort_on)

    return new_list



