import re

print("\nPut 'cancel' at any input to quit the program.")

word_of_day = input("Enter daily wordle answer: ")

while True:
    if word_of_day == "cancel":
        quit()
    if len(word_of_day) != 5 or not bool(re.match('^[abcdefghijklmnopqrstuvwxyz]+$', word_of_day)):
        print("Invalid word input, needs to be 5 letters no capitals.")
    else:
        break

word = []
word_letters = []

def Check(type, id):
    if type == "#":
        if word[id] in word_letters:
            return True
        else:
            return False
    else:
        if word[id] not in word_letters:
            return True
        else:
            return False

loop = 0
while True:
    while True:
        if loop == 0:
            art = input("Enter line here (# for green/yellow, _ for a grey space): ")
        else:
            art = input("Enter line here: ")
        
        if art == "cancel":
            quit()
        if len(art) != 5 or not bool(re.match('^[#_]+$', art)):
            print("Invalid line input, only # and _")
            break

        max_words = input("Maximum amount of words given (no input is 20): ")
        if max_words == "cancel":
            quit()
        if max_words == "":
            max_words = 20
        elif not bool(re.match('^[0123456789]+$', max_words)):
            print("Invalid max input, needs to be a whole number or nothing.")
            break

        word_letters = set(word_of_day)
        non_word_letters = set("abcdefghijklmnopqrstuvwxyz") - word_letters
        valid_words = []
        
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()

        for word in words:
            if len(set(word)) != 5:
                continue
            
            passes = 0

            for i in range(5):
                if Check(art[i], i):
                    passes += 1
            if passes == 5:
                valid_words.append(word)
                
        print("Matching words (" + str(len(valid_words[:int(max_words)])) + "/" + str(len(valid_words)) + "):", valid_words[:int(max_words)])
        loop = 1