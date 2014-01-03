file = "ULOYOYULSAEXOHUSMUWPXYYOVHQSHUWHSOHBRTAUWVRXALTXYTWZLXKSDOYBWKSRSDJTBRXBIOHVULOYXYYOVHQSHUOUGXYSHBRTAUSDZYOHVXJXYOBQWHWXEALXJSUOBYZJYUOUZUOWHBOALSRPWRULOYXYYOVHQSHUYZJQOUULSPWEEWGOHVOUSQYJTSQXOEJSPWRSULSQODDESWPHSMUQWHULPORYUDSYBROJSULSYZJYUOUZUOWHUXJESZYSDPWRULSESUUSRYARSYSHUOHULSAEXOHUSMUYSBWHDDSYBROJSBXRSPZEETLWGTWZJRSXIULSBOALSRULORDDSYBROJSXHDOQAESQSHUTWZRWGHBOALSRYTYUSQPWRSHBRTAUOHVXHDDSBRTAUOHVUSMUPOESYTWZQXTZYSXHTARWVRXQQOHVEXHVZXVSWPTWZRBLWOBSXEYWOHBEZDSXJROSPDOYBZYYOWHBWQAXROHVULSRSEXUOKSYSBZROUTWPTWZRBOALSRUWULSQWHWXEALXJSUOBYZJYUOUZUOWHBOALSRZYSDPWRULSUSMUWPULOYXYYOVHQSHUXYAXRUWPULSYZJQOYYOWHPWRULSULORDAXRUARWKODSXEOKSDSQWHYURXUOWHWPTWZRYTYUSQULOYXYYOVHQSHUGXYAWYUSDULRSSDXTYJSPWRSULSSHDWPXZVZYUOHULSTSXRUGSHUTULORUSSH"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file_length = len(file)

decrypt = []

def letter_freq():
        
    freq = []
    letter_freq = []

    for i in range (0,26):
        freq.append(0)
        for j in range (0, file_length):
            #print(file[j] + " " + letters[i])
            if file[j] == letters[i]:
                #print("found a match")
                freq[i] = freq[i] + 1
                #print("the new freq: " + str(freq[i]))
        letter_freq.append(str(freq[i]) + ": " + letters[i]  + " ")
        #letter_freq.append(freq)
    
    #print( letters )
    #print (freq)
    letter_freq.sort(reverse=True)
    #print ( letter_freq )
    return letter_freq

def letter_replace(text, original, replacement):
    #new_text = ""
    for i in range(0,len(text)):
        if text[i] == original:
            decrypt[i] = replacement
        #else:
            #new_text = new_text + "_"
            #new_text = new_text + text[i]
    
    #new_text = compare_text(new_text)
    #return new_text

def compare_text(text):
    new_text = ""
    for i in range(0,len(text)):
        if text[i] == file[i]:
            if text[i] != "R":
                new_text = new_text + "_"
            else:
                new_text = new_text + text[i]
        else:
            new_text = new_text + text[i]
    return new_text
    
def add_newline(text):
    new_text = text[0]
    for i in range(1,len(text)):
        new_text = new_text + text[i]
        if i % 30 == 0:
            new_text = new_text + "\n"
    return new_text


def main():    
    letter_freq()
    #['86: S ', '76: U ', '64: O ', '58: Y ', '49: W ', '48: H ', '46: R ', '42: X ', '35: L ', '26: Z ', '26: B ', '23: T ', '23: D ', 
    #'22: Q ', '22: A ', '20: P ', '19: E ', '18: J ', '17: V ', '6: G ', '5: K ', '5: M ', '2: I ', '0: N ', '0: F ', '0: C ']
    #pretty_file = add_newline(file)

    for i in range(0, file_length):
        decrypt.append(file[i])

    letter_replace( file, "A", "P" )
    letter_replace( file, "B", "C" )    
    letter_replace( file, "D", "D" )    
    letter_replace( file, "E", "L" )
    letter_replace( file, "G", "W" )
    letter_replace( file, "H", "N" )
    letter_replace( file, "I", "K" )
    letter_replace( file, "J", "B" )
    letter_replace( file, "K", "V" )
    letter_replace( file, "L", "H" )
    letter_replace( file, "M", "X" )
    letter_replace( file, "O", "I" )
    letter_replace( file, "P", "F" )
    letter_replace( file, "Q", "M" )
    letter_replace( file, "R", "R" )
    letter_replace( file, "S", "E" )
    letter_replace( file, "T", "Y" )
    letter_replace( file, "U", "T" )
    letter_replace( file, "V", "G" )
    letter_replace( file, "W", "O" )
    letter_replace( file, "X", "A" )
    letter_replace( file, "Y", "S" )
    letter_replace( file, "Z", "U" )



    #decrypt = compare_text(decrypt)
    decrypted = ""
    for i in range(0,len(decrypt)):
        decrypted = decrypted + decrypt[i]
    decrypted = add_newline(decrypted)

    print(decrypted)

if __name__ == '__main__':
   main()
