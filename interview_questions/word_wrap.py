def word_wrap(sentence, max):
    words = sentence.split()

    result = []
    count = 0
    temp = ""

    for i, word in enumerate(words[:-1]):
        if len(word) + count > max:
            result.append(temp)
            temp = ""
            count = 0
        count += (len(word) + 1)
        if count < max:
            if len(words[i+1]) + count > max:
                temp += word
            else:
                temp += (word + " ")
    result.append(temp + words[-1])
    return result


print(word_wrap("She sells seashells by the seashore", 14))