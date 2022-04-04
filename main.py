import re

import numpy
import numpy as np

def text_bin(text,encoding="utf-8",errors = "surrogatepass"):
    bits = bin(int.from_bytes(text.encode(encoding,errors),"big"))[2:]
    return bits.zfill(8*((len(bits)+7)//8))

entry_text = input("Text: ")
entry_text = text_bin(entry_text)
print(entry_text)
n_sum = int(input("Summators' count: "))
summator = []
for i in range(n_sum):
    n_reg = int(input("Count of connected registers:"))
    mid_summator = []
    for j in range(n_reg):
        mid_summator.append(int(input("Register_"+str(i+1)+": ")))
        if mid_summator[j]>3:
            exit()
    summator.append(mid_summator)
print("______sum__________")
print(summator)
print("______splitted_text__________")

coded_sum = []
for i in range(len(entry_text)):
    coded_sum.append(int(entry_text[i]))
print(coded_sum)
print("_______i(x)_________")
ix = np.poly1d(coded_sum)
print(ix)
coded_sum = []
for j in range(len(summator)):
    a = [0,0,0]
    for i in range(len(summator[j])):
        a[summator[j][i]-1] = 1
    coded_sum.append(a)
gx =[]
for i in range(n_sum):
    gx.append(np.poly1d(coded_sum[i]))
    print("_______g"+str(i+1)+"(x)_________")
    print(np.poly1d(coded_sum[i])) ##траблы c x^2

cx = []
for i in range(len(gx)):
    cx.append(ix*gx[i])
f = []
for i in range(len(cx)):
    for j in range(len(cx[i])):
        if cx[i][j] % 2 == 0:
            cx[i][j] = 0
        else:
            cx[i][j] = 1
    print("______c"+str(i+1)+"(x)__________")
    print(cx[i])
    f.append(np.asarray(cx[i].coef,list).tolist())
print("_______coef_________")

c = 0
for i in range(len(f)):
    if c < len(f[i]):
        c = len(f[i])
print("max = ", c)
for i in range(len(f)):
    f[i] = f[i][::-1]
    print(len(f[i]))
    while len(f[i]) < c:
        f[i].append(0)
print(f)
pol = []
for i in range(len(f)):
    if len(pol)<len(f[i]):
        pol = f[i]
f.remove(pol)
if len(f)>0:
    for i in range(len(f)):
        for j in range(len(f[i])):
            pol[j] = str(pol[j])+str(f[i][j])
print("____eq____")
print(pol)
coded_text = ""
for i in range(len(pol)):
    coded_text = coded_text + pol[i]
print("____coded_____")
print(coded_text)
print(len(entry_text))
print(len(coded_text))
print("____decoded_____")
from numpy.polynomial import polynomial
dec_pol = [coded_text[i:i+n_sum] for i in range(0, len(coded_text), n_sum)]
print(dec_pol)
dec_willy = []
for i in range(len(dec_pol)):
    dec_willy.append(int(dec_pol[i][0]))
dec_willy = dec_willy[::-1]
dec_willy = np.poly1d(dec_willy)
dec_willy = np.polydiv(dec_willy, gx[0])
print(dec_willy[0])
f = []
strok = ""
f = np.asarray(dec_willy[0].coef,list).tolist()
for i in range(len(f)):
    f[i] = str(f[i])
    f[i] = f[i].replace(".0","")
    f[i] = f[i].replace("-", "")
    if int(f[i]) % 2 == 0:
        f[i] = "0"
    else:
        f[i] = "1"
for i in range(len(f)):
    strok = strok + str(f[i])
print(strok)
def textf(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
print(textf(strok))