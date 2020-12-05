# Exam-2 (Below are thinking process explanations for problems 1-5)

Kevin_Aofia Exam 2

1)Minimum Falling Path
  DEFINE PROBLEM:
    Find the shortest falling path from a given input.
        I want to start in a row, and in that row, explore all options
          Then I wanted to explore all other rows except for the first row, this is the remaining rows.
          When I am exploring these rows I want to find the minimum element in our path and keep them.
        After I am done falling, I want to recall back to wherever I fell the least.
  Sub-Solutions:
      Things I want to store:
          I want to store our first row, because that is all our starting points of falling
          I want to store our remaining rows left to fall because we cannot fall through our starting position
          I want to store the min value that we fall through and that value can only be at most one before or after our start position
          Lastly, I want to save this information before falling again so I can recall after we have fell x amount of times
  IDEAL/D7:
    Please skip to end of README for answer (I will answer this collectively)
  
2)Palindromic Substrings
  DEFINE PROBLEM:
      Count the number of palindromic strings in a given string.
          I want to use a given string n and compare the string n[0] with the rest of the string n[:]
          So, I can explore a string a letter at a time
              and while doing that, i need to take the letters that are not that letter and check if it is a palindrome
              if the word is a palindrome, I will want the information where this happened so i do not count twice
              once I have done this, I can update my count by one and check next possibility
  Sub-Solutions:
      Things I want to store:
          I need to store our letters so we know where we are starting
          I need to store the index information where we are so I can check for duplicate possiblities
          I need to store the substring word in order to check if it is a palindrome.
          I need to store the number of occurences that we find a palindrome.
  IDEAL/D7:
    Please skip to end of README for answer (I will answer this collectively)
    
3)Arithmetic Slices
  DEFINE PROBLEM:
      Find the arithmetic slices of an array.
          I want to store all the numbers in the array and return that
          I want to store all the numbers in the array -1 position and return that
          I want to sore all the numbers in the array starting from +1 position and return that
  Sub-Solutions:
      Things I want to store:
          I need to store all elements except for the last element
          I need to store all the elements except for the first element
          I need to store all the elements in the array
          I need to return all of this information
  IDEAL/D7:
    Please skip to end of README for answer (I will answer this collectively)

4)Minimum ASCII Delete For Two Strings
  DEFINE PROBLEM:
      Find the cost to make two strings equal
          For this problem I need to store the ASCII and letters and have them correspond to a given ASCII value
          Given two strings, I will take both strings and find the letters that are making them unequal
          I need to then find the sum of what these letters would cost to delete from the two strings
  Sub-Solutions:
      Things I want to store:
          I need to store ASCII values 
          I need to store alphabet letters
          I need to store the difference of letters in the strings
          I need to store the sum of the letters in opposite strings
          I need to return the sum of the letters we added using ASCII values
  IDEAL/D7:
    Please skip to end of README for answer (I will answer this collectively)

5)Maximum Length of Pair Chain
  DEFINE PROBLEM:
      Find the length of the longest consecutive pair of arrays.
      Given an array, I will need to iterate through a list of array pairs.
      and through these arrays, I will have to check if their y coordinate is less than the next pairs x coordinate
      if that case is true, then we can connect them and thus increase our length
  Sub-Solutions:
      Things I want to store:
          list of array length
          length of longest pair sequence
  IDEAL/D7:
    Please skip to end of README for answer (I will answer this collectively)
    
  IDEAL/D7:
       To solve these problems I needed to not only use these techniques, but persist through the urge to not follow them. A lot of the times, I wanted to give up because I had other work due, but, i hackeled through, used these processes to solve them faster. I wrote down a lot in my oneNote and redefined what it was I was trying to solve as well as revisiting my trial and errors. I definitely benefited with writing down on something before anything. I found it so useful to look at english and translate to code than it is to code and make english from that.
       I had to have a lot of confidence in myself to approach these problems and anticipate good results but learned a lot about my problem solving skills in doing do.
       Personally reflecting on these problems. I am sure I solved the test cases that I made, and wish I had more time to see if the other test cases passed or failed. But might I add that, I need some work on DP, because at times I feel that what I am doing is dynamically structured but my self doubt was pushing to think to do it differently.
