sentence = input()

def count_vowels(sentence): # function to count the number of vowels in a sentence
    vowels = "aeiouAEIOU" # list of vowels
    count = 0 # counter for the number of vowels
    for i in sentence: # loop through the sentence
        if i in vowels: # check if the character is a vowel
            count += 1 # increment the counter
    return count # return the number of vowels
  
print(f"This sentance has this many amount of vowels: ",count_vowels(sentence)) # print the number of vowels in the sentence