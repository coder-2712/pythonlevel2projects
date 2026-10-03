import sys
letters ='abcdefghijklmnopqrstuvwxyz'
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

print("You are a top astrophysicist who has just recieved a message from space!")
print("However, the signal has gotten mixed up and some of the message is lost...")
print("All that was left was 'WE ARE COMING AT'. The rest of the message is scrambled!")
print("the aliens will wage war on Planet Earth if you cannot welcome them on time !!!")
print("The human race's survival depends on decoding this message. You can reshuffle the signals to get another mix of the same message.")
print("Humanity is counting on you. No pressure or anything though.")
print("enter the time below in words. if the answer is wrong a shuffled statement will come out. You have five tries.")
print("Note: enter time in numbers format X:YZ AM/PM")
x = 'we will be here at nine fifteen pm please be ready we expect a great welcome party'

aa= atbash_cipher('catcat')

x_even_odd = even_odd_swap(x)
print(x_even_odd)

answer = input("whats the time?")
if answer == "9:15 PM":
    print("That's right! Good Job!")
    sys.exit("Well, you should get ready now. Bye!")
else:
    print("Wrong! try again with another mix-up!")
    x_rev = reverse(x)
    print(x_rev)
    secondtry = input("whats the time?")


if secondtry == "9:15 PM":
    print("That's right! Good Job!")
    sys.exit("Well, you should get ready now. Bye!")
else:
    print("Wrong! try again with another mix-up!")
    x_rev_word = reverse_word(x)
    print(x_rev_word)
    thirdtry = input("whats the time?")

if thirdtry == "9:15 PM":
    print("That's right! Good Job!")
    sys.exit("Well, you should get ready now. Bye!")
else:
    print("Wrong! try again with another mix-up!")
    x_swap_mid = swap_middle(x)
    print(x_swap_mid)
    fourthtry = input("whats the time?")

if fourthtry == "9:15 PM":
    print("That's right! Good Job!")
    sys.exit("Well, you should get ready now. Bye!")
else:
    print("Wrong! try again with another mix-up!")
    x_swap_mid_rev = swap_mid_rev(x)
    print(x_swap_mid_rev)
    fifthtry = input("whats the time?")
    print()

if fifthtry == "9:15 PM":
    print("That's right! Good Job!")
    sys.exit("Well, you should get ready now. Bye!")
else:
    print("Wrong! try again with another mix-up!")
    x_atbash= atbash_cipher(x)
    print(x_atbash)
    sixthtry = input("whats the time?")
    print()

if sixthtry == "9:15 PM":
    print("That's right! Good Job!")
    sys.exit("Well, you should get ready now. Bye!")
else:
    print("You have failed. The aliens are not pleased. Enjoy your last few minutes alive. The whole message was:")
    print(even_odd_swap(x_even_odd))
    print(reverse(x_rev))
    print(reverse_word(x_rev_word))
    print()

