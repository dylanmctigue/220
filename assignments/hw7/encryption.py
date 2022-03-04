def encode(message, key):

    output = ""

    for i in message:
        message_num = ord(i)
        sum_num = message_num + key
        character = chr(sum_num)
        output = output + character
    return output

def encode_better(message, key):
    message_length = len(message)
    key = str(key)

    concatenation = ""

    for i in range(message_length):

        each_letter_message = message[i]
        each_letter_key = key[i]

        message_num = ord(each_letter_message)
        message_new_num = message_num - 65

        keyword_num = ord(each_letter_key)
        keyword_new_num = keyword_num - 65

        sum_num = (message_new_num + keyword_new_num) % 58

        character = chr(sum_num + 65)

        concatenation = concatenation + character

    return concatenation