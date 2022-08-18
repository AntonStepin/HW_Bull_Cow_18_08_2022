from random import randint

from words import *

global game
game = False
global word
word = ""
global length
length = 0

def start (update, context):
    global game
    game = False
    global word
    word = ""
    global length
    length = 0
    context.bot.send_message(update.effective_chat.id, "Привет, хочешь поиграть в игру: Быки и коровы?")

def main (update, context):
    text = update.message.text
    global game
    global word
    global length
    if game == False and text == 'да':
        game = True
        context.bot.send_message(update.effective_chat.id, "Супер, тогда введи сколько букв должно быть в загаданном слове (цифру от 3 до 6)")
        return game
    elif game == False and text != 'да':
       context.bot.send_message(update.effective_chat.id, "Тогда в другой раз") 
    if game == True and length == 0:
        if text.isdigit() and int(text) >=3 and int(text) <= 6:
            length = int(text)
            word = secret_word(text)
            print(word)
            context.bot.send_message(update.effective_chat.id, f"Теперь введи слово из {length} букв")
            return int(length)
        else:
            context.bot.send_message(update.effective_chat.id, "Некорректный ввод")   
    if game == True and not word == "":
        if len(text) == length and word != text:
            context.bot.send_message(update.effective_chat.id, f"Быков - {word_processing(word, text)[0]} и коров - {word_processing(word, text)[1]}")
        elif word == text:
            context.bot.send_message(update.effective_chat.id, "Ты выиграл!!!!!")
            game == False
            return start(update, context)
        else:
            context.bot.send_message(update.effective_chat.id, "Чего то не то написал)))")
            









