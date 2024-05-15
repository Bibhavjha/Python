#WAP to input a letter and check Vowel/consonant 
Letter=input('Enter a letter ')
letter=Letter.lower()
match letter:
    case 'a'|'e'|'i'|'o'|'u' :
        print("vowel")
    case Other:
        print("consonant")
