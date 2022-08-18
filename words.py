from random import randint

def secret_word(text):
    lenght = int(text)
    f = {
        3: "пес,лес,кот",
        4: "каша,мука,туча,галя",
        5: "арбуз,кувшин,антон",
        6: "каштан,стакан,матрац,кнопка"}
    words = f[lenght].split(",")
    temp = randint(0,len(words)-1)
    word = words[temp]
    return word


def word_processing(word, text):
    text = text.lower()
    text = [char for char in text]
    word = list(enumerate(char for char in word))
    bull = 0
    cow = 0
    st = 0
    match = ""
    for element in word:
        match_ind = 0
        for x in range (st,len(text)):
            if element[1] == text[x]:
                if element[0] != x:
                    match_ind = 1
                elif element[0] == x:
                        st=x+1
                        match_ind = 2
                if match_ind == 1: 
                    if not str(x) in match:
                        cow+=1
                        match += f"{x}"
                elif match_ind == 2: 
                    bull+=1
                    if str(x) in match: cow-=1              
    return[bull, cow]