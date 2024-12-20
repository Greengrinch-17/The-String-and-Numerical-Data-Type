str_manip= input("Enter a sentence: ")
length= len(str_manip)
print( "The length of the string is "+ str(length) )
new_sentence= str_manip.replace(str_manip[-1],"@")

print(f" str_manip.replace(str_manip[-1],""@""): {new_sentence}")
print(new_sentence)
last_3=str_manip[-1] +str_manip[-2]+str_manip[-3]
print(last_3)
five_letter_word=str_manip[0]+str_manip[1]+str_manip[2] +str_manip[-2]+str_manip[-1]
print(five_letter_word) 
