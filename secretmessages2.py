import random
letters='abcdefghijklmnopqrstuvwxyz'

def even_odd_swap(x):
    if len(x)%2!=0:
        x = x + ' '

    even_letters = x[0::2]
    odd_letters  = x[1::2]
    s=''

    for i in range(len(even_letters)):
        s = s+odd_letters[i]
        s = s+even_letters[i]
    
    return s

def swap_middle(x):
    if len(x)%2!=0:
        x = x + ' '

    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]
    
    s = ''
    s = s + second_half 
    s = s + first_half
    return s
    
def reverse(x):
    s = x[::-1]
    return s

def swap_mid_rev(x):
    s_swap = swap_middle(x)
    s = reverse(s_swap)
    return s

def swap_mid_rev_decode(x):
    s_rev = reverse(x)
    s = swap_middle(s_rev)
    return s

def reverse_word(x):
    words = x.split(' ')
    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
    return s

def caesar_cipher(x, n):   
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s + ' '
        else:
            idx = letters.find(x[i])
            new_idx = (idx+n)%26
            s = s + letters[new_idx]
    return s        

def atbash_cipher(x) :
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s+' '
        else:
            idx = letters.find(x[i])
            new_idx = 25 - idx
            s = s + letters[new_idx]
    return s
def viginere_cipher(x,key):
    s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s+' '
        else:
            idx=letters.find(x[i])
            new_idx = (idx+key[i%len(key)])
            s = s+letters[new_idx]
    return s

def viginere_cipherdecode(x,key):
    dkey=[0]* len(key)
    for i in range(len(key)):
        dkey[i] = 26-key[i]
        s=''
    for i in range(len(x)):
        if x[i] == ' ':
            s = s+' '
        else:
            idx=letters.find(x[i])
            new_idx = (idx+dkey[i%len(dkey)])
            s = s+letters[new_idx]
    return s


print()
print()


msg = 'plane incoming today'
secret_code = ''


for kk in range(10):
    n = random.randint(0, 25)
    secret_code = secret_code + letters[n]

msg = msg + secret_code

# Pick one of the four operations
encoder = random.randint(0, 4)
encoder = 0
if encoder == 0:
    msg_enc = msg
elif encoder == 1:
    msg_enc = even_odd_swap(msg)
elif encoder == 2:
    msg_enc = reverse(msg)
elif encoder == 3:
    msg_enc = swap_middle(msg)
else:
    msg_enc = atbash_cipher(msg)




i = 1
viginere= []
while i<5:
    viginere.append(random.randint(1,10))
decider = random.randint(0,1)
if decider == 0:
    msg_enemy = caesar_cipher(msg_enc, random.randint(1, 25))
else:
    msg_enemy = viginere_cipher(msg_enc, viginere)
print()
print('I am hearing ...')
print(msg_enemy)
print()

for kk in range(1, 26):
    msg_dec = caesar_cipher(msg_enemy, kk)
    msg_dec_eo = even_odd_swap(msg_dec)
    msg_dec_r  = reverse(msg_dec)
    msg_dec_ms = swap_middle(msg_dec)
    msg_dec_a = atbash_cipher(msg_dec)
    
    if msg_dec[0:20:1]=='plane incoming today':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec[20::1])
        break
    elif msg_dec_eo[0:20:1]=='plane incoming today':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec_eo[20::1])
        break
    elif msg_dec_r[0:20:1]=='plane incoming today':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec_r[20::1])
        break
    elif msg_dec_ms[0:20:1]=='plane incoming today':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec_ms[20::1])
        break
    elif msg_dec_a[0:20:1]=='plane incoming today':
        print('code cracked ...')
        print('Secret code is ...')
        print(msg_dec_ms[20::1])
        break
