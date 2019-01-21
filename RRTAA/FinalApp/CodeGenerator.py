from qrcodegen import *
import random

def code_Generate():
    chars = "ASDFGHJKLQWERTYUIOPZXCVBNM!@#$%^&*() {}:\"|<>?_~zxcvbnm,./asdfghjkl;\'\\]qwertyuiop[1234567890-+="
    code = ""
    for i in range (10):
        code += chars[random.randint(0,len(chars)-1)]
    print(code)
    qr0 = QrCode.encode_text(code, QrCode.Ecc.MEDIUM)
    svg = qr0.to_svg_str(4)
    return svg


print(code_Generate())