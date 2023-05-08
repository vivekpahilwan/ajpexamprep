

def bittobyte(bits):
    bytes = bits / 8
    return bytes


def bytestomb(bytes):
    mb = bytes / (1024 ** 2)
    return mb

def bytestogb(bytes):
    gb = bytes / (1024 ** 3)
    return gb

def bytestotb(bytes):
    tb = bytes / (1024 ** 4)
    return tb


print(bittobyte(1293))
print(bytestomb(123515))
print(bytestogb(289923))
print(bytestotb(26782343))