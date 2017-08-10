import random
secret = random.randint(1, 99)
guess = 0
tries = 0

print "Tony! I have a SERET"
print "1..99"
while guess != secret and tries < 6:
    guess = input("what's your guess?")
    if guess < secret:
        print "Tai xiao le"
    elif guess > secret:
        print "Tai da le"
    tries = tries + 1

if guess == secret:
    print "OKKKKKKK niu!"
else:
    print "cuo le"
    print "zhengque de shi:", secret