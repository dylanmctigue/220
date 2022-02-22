"""
Name: Dylan McTigue
hw5.py

Problem: Use python strings, lists, slicing, and indexing to write simple programs.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    full_name = input("Enter a name(first last): ")
    full_name_split = full_name.split(" ")
    print(full_name_split[1], end=", ")
    print(full_name_split[0])
name_reverse()

def company_name():
    domain = input("Enter a domain: ")
    domain_split = domain.split(".")
    print(domain_split[1])
company_name()

def initials():
    students = eval(input("how many students are in the class?"))

    for num in range(students):
        question = "What is the name of student " + str(num + 1) + "? "
        name = input(question)

        name_split = name.split(" ")
        first = name_split[0][0]
        last = name_split[1][0]
        first_last_initials = first + last
        print(first_last_initials)
initials()

def names():
    name_list = input("Enter a list of names: ")
    list_split = name_list.split(" ")
    comma_list_split = name_list.split(", ")

    acc_first = 0
    acc_last = 1

    for _ in range(len(comma_list_split)):
        first = list_split[acc_first][0]
        last = list_split[acc_last][0]

        acc_first = acc_first + 2
        acc_last = acc_last + 2

        first_last_initials = first + last
        print(first_last_initials, end=" ")
names()

def thirds():
    num_sentences = eval(input("Enter the number of sentences: "))
    third = ""

    for sent_num in range(num_sentences):
        question = "enter sentence " + str(sent_num + 1) + ": "
        sentence = input(question)

        third = third + sentence[::3]
    print(third)
thirds()

def word_average():
    sentence = input("enter a sentence: ")
    sentence_split = sentence.split(" ")

    acc_sum = 0

    list_length = len(sentence_split)

    for i in range(list_length):
        acc_sum = acc_sum + int(len(sentence_split[i]))

    average = acc_sum / list_length

    print(average)
word_average()

def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")

    sentence_split = sentence.split(" ")
    length = len(sentence_split)

    pig_list = []

    for i in range(length):
        first_letter = sentence_split[i][0]
        word = sentence_split[i]
        word_replace = word.replace(first_letter, "")

        pig_word = word_replace + first_letter + "ay"
        pig_list.append(pig_word)

    pig_words = " ".join(pig_list)

    pig_lower = pig_words.lower()

    print(pig_lower)
pig_latin()

if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
