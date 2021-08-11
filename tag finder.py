import unittest

class MyTagFinderTest(unittest.TestCase):

    def test_string1(self):
        c = tagFinder('provide strings : <p class="row" style="font-size: 16px; color: #000;">귀하가 사용하고 계신 브라우저는 스크립트를 지원하고 있지 않아서, 레이아웃 및 컨텐츠가 정상적으로 동작 하지 않을 수 있습니다. 스크립트 기능을 활성화 하시길 권장합니다.<br></p>')
        self.assertEqual(c, False)

    def test_string2(self):
        c = tagFinder('provide strings : <p class="row" style="font-size: 16px; color: #000;">귀하가 사용하고 계신 브라우저는 스크립트를 지원하고 있지 않아서, 레이아웃 및 컨텐츠가 정상적으로 동작 하지 않을 수 있습니다. 스크립트 기능을 활성화 하시길 권장합니다.<br></p>')
        self.assertEqual(c, ['<p>', '<br>', '</p>'])

def tagFinder(string):
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


# print(main(input("provide strings : ")))
if __name__ == '__main__':
    unittest.main()