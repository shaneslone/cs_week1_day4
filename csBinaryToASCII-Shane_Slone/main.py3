def csBinaryToASCII(binary):
    if binary == "":
        return ""
    charcount = int(len(binary)/8)
    letterstart = 0
    result = ""
    for i in range(charcount):
        currentchar = binary[letterstart:letterstart+8]
        result += chr(int(currentchar, 2))
        letterstart+=8
    return result

