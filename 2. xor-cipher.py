key = 12693 # int
string = input("Enter Text: ") #string - str
# you could assing the type by using for example varname:str or varname:int

string_new = ''

for ch in string:
    ascii_ch = ord(ch)
    ch_new_ascii = ascii_ch ^ key
    ch_new = chr(ch_new_ascii)
    string_new += ch_new
    # equals to string_new = string_new + ch_new

print(string_new)

##final_string =''
##
##for ch in string_new:
##    ascii_ch = ord(ch)
##    ch_new_ascii = ascii_ch ^ key
##    ch_new = chr(ch_new_ascii)
##    final_string += ch_new
##
##print(final_string)
