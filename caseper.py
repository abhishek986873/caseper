import pyfiglet

# Define the text to be printed
text = "CAESAR"

# Create the Ascii art text with slanted font
ascii_text = pyfiglet.figlet_format(text, font="slant")

# Print the text
print(ascii_text)
# printing a line that seprate the heading 
print("_"*71)

# making function that take  input of message that we want to code

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def encrypt_input():
	while True:
		message = input("WRITE MESSAGE THAT YOU WANT TO ENCRYPT ? [WITHOUT SPACES] = ")
		if not message.isalpha():
			print("ENTER A VALID WORD THAT CONTAIN ONLY LETTER AND WITHOUT SPACE!")
		else:
			break
		
		

	return message

#--------------------------------------------------------------------------------------------------------------

message = encrypt_input()
# code to detect whether the string is in upper or lower case if it is in lower case changing it into upper case
boolean = message.islower()
if boolean == True:
	message = message.upper()
print("_"*71)

#----------------------------------------------------------------------------------------------------------------

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#-------------------------------------------------------------------------------------------------------------------------

list1 = []
message_list = list(message)
message_length = len(message)
i = 0
while i<message_length:
	index = alphabet_list.index(message_list[i])
	list1.append(index)
	i = i+1


#-------------------------------------------------------------------------------------------------------------------------
# asking user that how many leter he want to shift


while True:
	shift = int(input("ENTER HOW MANY LETTER YOU WANT TO SHIFT = "))
# creating a temporary list that have reverse order value used to detect wheter encrypting is possible or not
	temp_list = sorted(list1, reverse=True)
	if temp_list[0]+shift >= 26:
		print(f"ENTER A VALID SHIFT NUMBER SHIFT BY {shift} IS NOT POSSIBLE !")
		
	else:
		break

#-------------------------------------------------------------------------------------------------------------------------
# creating a new list that is obtained by adding shift in list
print("_"*71)


list2 = []
for i in range(0,message_length):
	new_updated_list = list1[i] + shift
	list2.append(new_updated_list)
	
#-------------------------------------------------------------------------------------------------------------------------

# storing the encrypted letted in a string

list3 = []
i = 0
while i < message_length:
	coded_letter = alphabet_list[list2[i]]
	list3.append(coded_letter)
	i = i+1
final_coded_message = ''.join(list3)  # use join() to concatenate list of letters into a single string
print(final_coded_message)

print("_"*71)

# process of encoding the message start


def decrypt_input():
	decrypt = input("DO YOU WANT TO DECRYPT YOUR CODE = ")
	
