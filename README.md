# Password-Generator
Day 2 of Python: A terminal based password generating project.

> **How the code is written?**

1) time and random modules are used
2) time module for seeding random with the current second
3) random module is for selecting random choices from the three lists i.e Letters, Numbers and Special Characters
4) Letter List is created which contains all alphabets, Numbers list contains all numbers from 0 to 9 and Special
   Characters list contains special characters
5) You have to provide the length of password as well as the total number of numbers and total number of special
   characters, The number of characters will be calculated on the basis of the remaining free slots in password
   
7) password length, number of special characters you want to add, total numbers you want in password, all are
   checked, either number of characters you want or number of numbers you want are  smaller than total password length
   or not.
8) 3 for loops get all the random letters, numbers and special characters based on the password length

> **How it actually works?**

you just have to provide the following inputs:
1) Password length
2) Number of special characters
3) Total number of numbers

Password of that specific length will be generated.

> **Exceptions:**
1) All sort of exceptions will be handled by try except
2) For handling logic errors here are the following logic errors which are resolved
   1) if total numnber of numbers in password is less than the total length of password
       but the sum of total number of numbers you want in pass and special characters goes
       out of the passwords range.
   2) if length of password is smaller than any of the two things i.e;
          Total number of numbers you want and special characters you want in password

> **Note: The number of letters in the password will be computed automatically by the formula**

`number of simple letters in password = special characters in password - total numbers in password`
