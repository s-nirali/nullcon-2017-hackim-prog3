flag_enc = "63336C756448746861486C35634442684C565A686353467566513D3D"   # looks like a hex encoded ascii string

flag_unhex = flag_enc.decode('hex')
print flag_unhex
# flag_unhex = 'c3ludHthaHl5cDBhLVZhcSFufQ=='    # looks like it is base64 encoded

flag_unbase64 = flag_unhex.decode('base64')
print flag_unbase64
# flag_unbase64 = 'synt{ahyyp0a-Vaq!n}'   # looks like a flag but encrypted with a cipher
# Observer that 'synt' could be 'flag'and 'ahyyp0a' could be 'nullc0n'

# Cipher is a Ceasar cipher with shift = 13
flag = ''
for c in flag_unbase64:
    i = ord(c)
    if c.isupper():
        i += 13
        i = i-90+64 if i>90 else i
    elif c.islower():
        i += 13
        i = i-122+96 if i>122 else i
    else:
        pass
    flag += chr(i)

print flag
