# text: large text in which to find the possible substring
# sstring: the string whose anagram needs to be the substring of text
# We break the letters of the sstring and check if the letter occur as a substring of text. 
# Hence can be any of the anagram of sstring.
def check_anagram_substring(text,sstring):
	# create a frequency dict of the string
	s_dict={}
	for ch in sstring: # dictionary to check if the substring is a valid anagram
		if(ch in s_dict):
			s_dict[ch]=s_dict[ch]+1
		else:
			s_dict[ch]=1
	# iterate over the main function to check 
	s_dict_running=s_dict.copy();
	i=0
	count=0
	# iterate over the text finding 
	while i <(len(text)-len(sstring)+1):
		flag=0
		j=0
		# maintain j over valid substring checked
		while(j<len(sstring)):
			ch=text[i+j]
			count+=1
			# if the character is in sstring and is not used in the current substring more than required
			# include it in the substring
			if(ch in s_dict_running):
				if(s_dict_running[ch]>0): 
					s_dict_running[ch]-=1
					j+=1
				else:
					#if character is in sstring but is used more than required, move starting of substring to 1 
					#character ahead of its previous occurance 
					for temp in range(0,j):
						count+=1
						if(text[temp+i]==ch):
							i=i+temp+1
							j+=1
							break
						else:
							s_dict_running[text[temp+i]]+=1
							j-=1
			else:
				# reset dictionary if an out of sstring character is encountered 
				# and start the search of substing 1 character ahead of it i=i+j+i
				if(j>0):
					s_dict_running=s_dict.copy()
				flag=1
				i=i+j+1
				break
		if(flag==0):
			# complete length substring found
			return True
	# check for substring complete no substring found
	return False;

# call check_anagram_substring
text=raw_input('Enter text : ')
sstring=raw_input('Enter string to search : ')
print(check_anagram_substring(text,sstring))
				
