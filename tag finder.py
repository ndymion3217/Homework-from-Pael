def main(string):
    result = []
    tag = ''
    start = False
    tagend = False
    for spell in string:
        if spell == '<' and start is not True:
            tag += spell
            start = True
        elif spell == '<' and start:
            tag = spell
        elif spell == '>':
            if tagend or tag != '':
                tag += spell
                tagend = False
                start = False
                if tag != '<>':
                    result.append(tag)
                tag = ''
        elif spell == ' ' and start:
            tagend = True
        elif start and tagend is not True:
            tag += spell
        #print(result, tag, spell)
    return result if result else False


print(main(input("provide strings : ")))