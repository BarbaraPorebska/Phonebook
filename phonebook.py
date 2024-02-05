# Do not modify this list
from tarfile import AREGTYPE
from tkinter import Y
from io import StringIO
import sys


phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

ugly_phone_list = ["98-333-111", "12--323-566", "123-34-221", "99-948-321", "-12-123-346",
                     "894-58438-543", "85-234-222",
                     "12-333-444-", "99-888--433", "15-465-876", "98-555-22", "-3-355-333", "3--344-53", "--2--45---",
                     "11-111-222", "12#22$34$222", "98 223 555"]


print("These are the valid phone numbers in your phonebook:")
list_of_valid_numbers = [] 
for i in range(0,len(phone_list)):
    if len(phone_list[i]) == 10:
        print(phone_list[i])
        list_of_valid_numbers.append(phone_list[i])



print("and these are the wrong ones:") 
for i in range(0,len(phone_list)):
    if len(phone_list[i]) is not 10:
        print(phone_list[i])

          
print("The area codes:") 

#TUTAJ DRUKUJEMY 2 PIERWSZE ZNAKI KAŻDEGO ELEMENTU:
area_codes = []
for string in list_of_valid_numbers:            
    print(string[:2])     
    area_codes.append(string[:2])

#TUTAJ DRUKUJEMY 2 PIERWSZE ZNAKI KAŻDEGO ELEMENTU:
print("and the numbers without the area codes:")
only_phone_numbers = []
for string in list_of_valid_numbers:            
    print(string[3:10])
    only_phone_numbers.append(string[3:10])             

# TUTAJ PRINTUJEMY TYLKO UNIKALNE KIERUNKOWE
set_result = set(area_codes)  
print("The unique area codes:") 
unique_area_codes = list(set_result)
 
for item in unique_area_codes: 
    print(item)


for unique_area_code in unique_area_codes:
    area_code_counter = 0
    for area_code in area_codes:
        if area_code == unique_area_code:
            area_code_counter += 1
    print(unique_area_code, " ", area_code_counter)



# "These are the pretty phone numbers:"
# "and these are the ugly ones:"

