def my_long_word(number, sentence):
    result = ""
    word = ""
    for char in sentence:
        if char != " ":
            word += char
        else:
            if len(word) > number:
                result += word + " "
            word = ""
    if len(word) > number:
        result += word
    return result
