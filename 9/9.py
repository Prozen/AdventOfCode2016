def decompress(s):
    if s == "":
        return s
    if s[0] == '(':
        x = s.find('x')
        end = s.find(')')
        length = int(s[1:x])
        count = int(s[x+1:end])
        return decompress(s[end+1:end+1+length])*count + decompress(s[end+1+length:])
    return s[0] + decompress(s[1:])
print(len(decompress("(27x12)(20x12)(13x14)(7x10)(1x12)A")))
