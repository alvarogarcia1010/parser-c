from utilities.token import Token
from utilities.types import Types
import re
    
def readSource(fd):
    with open(fd, 'r') as file:
        data = file.read()
    return readSourceString(data + '$')

def readSourceString(string):
    index = 0
    tokens = list()
    while index < len(string):
        token = separateToken(string, index)
        if token is None:
            break
        index = token.end
        tokens.append(token)
    return tokens

def separateToken(string, begin):
    if begin < 0 or begin >= len(string):
        raise IndexError(string, 'Index out of bounds: ' + begin)
    for type in Types:
        pattern = r'.{' + str(begin) + '}' + type.value
        match = re.match(pattern, string, re.DOTALL)
        if match:
            end = match.end(1)
            return Token(begin, end, string[begin:end], type)
    else:
        return Token(begin, begin+1, string[begin:begin+1], Types.SYNTAX_ERROR)
    return None
