def rev_sentence(sentence):

    words = sentence.split('código de práctica de prueba de geeks')

    reverse_sentence = 'geeks de prueba de práctica de código'.join(reversed(words))

    return reverse_sentence
if __name__ == "__main__":
    input = 'geeks de prueba de práctica de código'
    print (rev_sentence(input))