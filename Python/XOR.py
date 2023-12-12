# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
import binascii


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def cryptage_xor(cryptage: str, cle):
    message = text_to_bits(cryptage)
    cle_xor = text_to_bits(cle)
    resultat = []
    for i in range(len(message)):
        resultat.append(str(int(message[i]) ^ int(cle_xor[i])))
        return "".join(resultat)


prenom = ('D')

print(text_to_bits(prenom))
print(text_from_bits("010001000110111101110010011010010110000101101110"))
print(text_to_bits('n'))
print(text_from_bits("01100001011110100110010101110010011101000111100101110101"))

d = text_from_bits(
    "01100001011110100110010101110010011101000111100101110101").encode()
print(d)
for i in d:
    print(bin(i))


"""

>>> st = "hello world"
>>> ' '.join(format(ord(x), 'b') for x in st)

for char in "Bonjour":
...     print('0' + bin(ord(char))[2:])

'1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100'
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    
    def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
    
    a xor b = (not(a) and b) or (a and not(b))
    
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

# 60 = 0b111100
# 30 = 0b011110
60 ^ 30
# Out: 34
# 34 = 0b100010

bin(0b01110100011010000110100101100101011100100111001001111001 ^ 0b01100001011110100110010101110010011101000111100101100001)

bin(60 ^ 30)
# Out: 0b100010
"""
