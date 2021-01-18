def string_na_clean_list(string):
    txt = string.splitlines()
    t = []
    for i in txt:
        a = i.strip()
        if a is not '':
            t.append(i.strip())
    return t

def wyklucz_z_listy(set_ex, list_txt):
    return [i for i in list_txt if i not in set_ex or i not in list_txt]