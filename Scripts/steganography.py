def read():
    # Read binary data
    #utf-8 fixes 'charmap' codec can't decode byte 0x8f
    with open('hiddenImage.png','rb') as file:
        data = file.read()
        #print(data)

def modify():
    # Hidden text to a zip image
    with open('hiddenMod.png', 'a+b') as appendString:
        data = appendString.write(b"HiddenTextTest")

def combine():
    #zip file in an image
    testZip = open('test.zip', 'rb')
    testByte = testZip.read()
    with open('hiddenZip.png', 'a+b') as appendString:      
        data = appendString.write(testByte)


read()
modify()
combine()