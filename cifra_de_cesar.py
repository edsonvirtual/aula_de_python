def cesarCipherEncryption(message, key):
    alphabot = "abcdefghijklmnopqrstuvwxyz"
    encoded = ""  
    
    for i in message:
        encodedLetterIndex = ((ord(i) - ord('a')) +key)% 26
        encoded += alphabot[encodedLetterIndex]      
    return encoded

def cesarcipherDecryption(crypto, key):
    alphabot = "abcdefghijklmnopqrstuvwxyz"
    decryptedMessage = ""
    
    for i in crypto:
        decodedLetterIndex = ((ord(i) - ord('a')) - key) % 26
        decryptedMessage += alphabot[decodedLetterIndex]
    
    return decryptedMessage

message = "ewerton"
cryptoMessage = cesarCipherEncryption(message, 10)
decyptionMessage = cesarcipherDecryption(cryptoMessage, 10)
print(cryptoMessage)
print(decyptionMessage)
    