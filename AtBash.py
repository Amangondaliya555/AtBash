decrypted_msg = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
tebahpla = "zyxwvutsrqponmlkjihgfedcba"
message = input("Enter your message : ")
message = message.lower()
word = message.translate({ord(x): y for (x, y) in zip(alphabet, tebahpla)})
print(word)