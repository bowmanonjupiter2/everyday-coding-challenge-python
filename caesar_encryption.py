def caesar_decrypt(encrypted_str: str, k: int) -> str:
    lower_case_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_alphabet = lower_case_alphabet.upper()

    encrypted_list = encrypted_str.split()
    decrypted_list = []
    for encrypted_word in encrypted_list:
        decrypted_word = ''
        for i in range(len(encrypted_word)):
            curr_encrypted_char = encrypted_word[i]
            if not curr_encrypted_char.isalpha():
                decrypted_word += curr_encrypted_char
            else:
                if curr_encrypted_char.isupper():
                    curr_idx = upper_case_alphabet.find(curr_encrypted_char)
                    decrypted_idx = (curr_idx + k + 26) % 26
                    decrypted_char = upper_case_alphabet[decrypted_idx]
                    decrypted_word += decrypted_char
                else:
                    curr_idx = lower_case_alphabet.find(curr_encrypted_char)
                    decrypted_idx = (curr_idx + k + 26) % 26
                    decrypted_char = lower_case_alphabet[decrypted_idx]
                    decrypted_word += decrypted_char

        decrypted_list.append(decrypted_word)

    decrypted_sentence = ' '.join(decrypted_list)
    return decrypted_sentence


def test():
    test_encrypted_str = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
    decrypted_result = caesar_decrypt(test_encrypted_str, 2)
    print(decrypted_result)


if __name__ == '__main__':
    test()
