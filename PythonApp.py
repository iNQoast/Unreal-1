def duplicate_encode(word):
    
    iter_word = str(word.lower())
    check_list = []
    formatted_list = []
    position = 0

    print('Checking word: {}'.format(iter_word))

    for i in iter_word:

        position += 1
        
        if i not in check_list and i not in (iter_word[position:]):

            check_list.append(i)
            i = '('
            formatted_list.append(i)
        else:

            check_list.append(i)
            i = ')'
            formatted_list.append(i)

    print('Result: {}'.format(''.join(map(str, formatted_list))))

    return ''.join(map(str, formatted_list))    
    

duplicate_encode('BLsfUIB')