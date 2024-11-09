def count_substring(mainstring, substring): # function that counts the number of times a substring appears in a mainstring
  if len(substring) > len(mainstring): # if the substring is longer than the mainstring
    return 0 # return 0
  counter = 0 # counter for the number of times the substring appears in the mainstring
  
  for i in range(0, len(mainstring) - len(substring) + 1): # loop through the mainstring
    tester = mainstring[i:i + len(substring)] # create a substring of the mainstring
    if tester == substring:
      counter += 1
  return counter # return the number of times the substring appears in the mainstring


def main(): # main function that takes in input from the user
  stop_running = False # boolean to stop the program
  while not stop_running: # while the program is not stopped
    mainstring = input('Please input a main string: ') # take in the main string
    if mainstring == '': # if the main string is empty
      stop_running = True # stop the program
    else: # if the main string is not empty
      substring = input('Please input a substring: ') # take in the substring
      num = count_substring(mainstring, substring)  # call the function to count the number of times the substring appears in the main string
      print(f'The substring {substring} appears {num} times in the main string') # print the number of times the substring appears in the main string
        
if __name__ == "__main__":
  main()
      
      
  