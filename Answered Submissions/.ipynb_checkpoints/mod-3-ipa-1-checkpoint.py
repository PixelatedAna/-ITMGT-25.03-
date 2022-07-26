'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT letter 
    #INPUT shift 
    list_of_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #HAVE string of letters

    if letter == " ": #CONDITION " " or "letter"
        return str(letter) #OUTPUT " "
    
    else:
        original_letter_position = list_of_letters.index(letter) #GET original letter position in list string
        shifted_letter_position = (original_letter_position + shift) %  26 #ADD shift to letter position GET remainder for over 26
        shifted_letter = list_of_letters[shifted_letter_position] #GET shifted letter from shifted position
        return str(shifted_letter) #OUTPUT shifted letter

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT message
    #INPUT shift
    list_of_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #HAVE string of letters
    ciphered_message = "" #HAVE blank string ciphered_message

    for character in message:#LOOP for every character in message
        if character == " ": #IF " "
            ciphered_message = ciphered_message + " " #ADD " " to ciphered_message

        else: #ELSE
            original_character_position = list_of_letters.index(character)#GET position of original character in list
            shifted_character_position = (original_character_position + shift) % 26 #ADD shift to original position GET remainder for over 26
            shifted_character = list_of_letters[shifted_character_position] #GET letter in shifted position
            ciphered_message = ciphered_message + shifted_character #ADD shifted letter to ciphered_message

    return ciphered_message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT letter
    #INPUT letter_shift
    list_of_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #HAVE list of letters in string

    if letter == " ": #IF " "
        return letter #OUTPUT " " 
    else: #ELSE:
        original_letter_position = list_of_letters.index(letter) #GET position of original letter in list
        number_equivalent = list_of_letters.index(letter_shift) #GET number equivalent of letter_shift
        shifted_position = (original_letter_position + number_equivalent) % 26 #ADD number equivalent to original position, remainder for over 26
        shifted_letter = list_of_letters[shifted_position] #GET shifted letter from shifted position
        return shifted_letter #OUTPUT shifted letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    15 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT message
    #INPUT key
    list_of_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #HAVE list of letters string
    ciphered_message = "" #HAVE blank string ciphered_message

    for start in range(0,len(message),len(key)): #LOOP for every start of the message sliced into key length
        character_position = 0 #HAVE character position in sliced message to 0
        for letter in message[start:start+len(key)]: #LOOP for every letter in sliced message
            if letter == " ": #IF " "
                ciphered_message = ciphered_message + " " #ADD " " to ciphered_message
                character_position = character_position + 1 #ADD 1 to move character position

            else: #ELSE
                original_letter_position = list_of_letters.index(letter) #GET position of original letter in list
                key_letter = key[character_position] #GET key letter with the same position as the message letter
                number_equivalent = list_of_letters.index(key_letter) #GET number equivalent of key letter in list
                shifted_position = (original_letter_position + number_equivalent) % 26 #ADD number equivalent to original position, remainder for over 26
                shifted_letter = list_of_letters[shifted_position] #GET shifted letter
                ciphered_message = ciphered_message + shifted_letter #ADD shifted letter to ciphered_message
                character_position = character_position + 1 #ADD 1 to move character position

    return ciphered_message #OUTPUT ciphered_message

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.
    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.
    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale
    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".
    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT message
    #INPUT shift
    ciphered_message = "" #HAVE blank string ciphered_message


    if (len(message) % shift) == 0: #IF remainder of len(message)/shift = 0
        row_length = len(message)//shift 
        character_position = 0
        while len(ciphered_message) < len(message): #LOOP until len(ciphered_message) is greater than or equal to len(message)
            for start in range(character_position,len(message),row_length): #LOOP for each letter in row
                letter = message[start] #GET letter in start position
                ciphered_message = ciphered_message + letter #ADD letter to ciphered_message
            character_position = character_position + 1 #ADD 1 to character position to go to next column

    else: #ELSE
        
        while (len(message)%shift) != 0:
            message = message + ("_") #ADD "_" to message
        
        #COPY if code
        row_length = len(message)//shift 
        character_position = 0
        while len(ciphered_message) < len(message): #LOOP until len(ciphered_message) is greater than or equal to len(message)
            for start in range(character_position,len(message),row_length): #LOOP for each letter in row
                letter = message[start] #GET letter in start position
                ciphered_message = ciphered_message + letter #ADD letter to ciphered_message
            character_position = character_position + 1 #ADD 1 to character position to go to next column

    return ciphered_message

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.
    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.
    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"
    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #INPUT message
    #INPUT shift
    deciphered_message = "" #HAVE blank string deciphered_message

    character_position = 0
    while len(deciphered_message) < len(message): #LOOP until len(deciphered_message) is greater than or equal to len(message)
        for start in range(character_position,len(message),shift): #LOOP for each letter in row
            letter = message[start] #GET letter in start position
            deciphered_message = deciphered_message + letter #ADD letter to ciphered_message
        character_position = character_position + 1 #ADD 1 to character position to go to next column

    return deciphered_message