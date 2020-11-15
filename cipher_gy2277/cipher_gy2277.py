def cipher(text, shift, encrypt=True):
    """
    Encrypting or deecrpting using Caesar cipher.

    Parameters
    ----------
    text : str
      The contents to be encrypted or decrypted
    shift : int
      A fixed number of positions that each letter in text is shifted down (positive) or up (negative)
    encrypt : bool
      If True, then the text is encrypted; otherwise, the text is decrypted
    
    Returns
    -------
    str
      The encrypted or decrypted text.

    Examples
    --------
    >>> from cipher_gy2277 import cipher_gy2277
    >>> text = "cat"
    >>> shift = 3
    >>> cipher_yuan_gan.cipher(text, shift)
    'fdw'
    
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
