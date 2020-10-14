alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 2

newMessage = ''
message = input('Enter the message: ')
for character in message: 
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key)%26
        newCharacter = alphabet[newPosition]
        #print('the new character is :',newCharacter)
        newMessage += newCharacter
  
    
print("The secret message for the input message is: ",newMessage)
