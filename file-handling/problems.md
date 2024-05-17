# Python - File handling

1. Write a program to write the text `Hello, World!\n` to a file named `hello.txt`.
2. Write a program to read the contents of file `hello.txt` and print it to the terminal.
3. Write a program to append the text `Appended text\n` to hello.txt and then read the entire file and print its contents.
4. Write a program to write multiple lines to a file `lines.txt`.

    ```
    Kurma is an avatar
    Narasimha is an avatar
    Rama is an avatar
    Krishna is an avatar
    ```
5. Read the file `data_file.txt` and count the following
    1. Total number of new lines
    2. Total number of words
    3. Total number of vowels
    4. Total number of consonants
    5. Print each word and it's frequency (i.e no duplicate words are allowed)
6. Copy the contents of file `data.txt` to `data_copy.txt`.
7. Merge two files `file1.txt` and `file2.txt` to `merged_file.txt`
8. Take student information from the user and store it in the text file named "student_data.csv"

   step1: use while loop and ask the user below info
   
    1. first_name
    2. last_name
    3. course_name
    4. phone

   step2: save the data to file
   
   step2: ask user if she/he want to continue entering the data.
   
   step3: if user want to continue entering the data then repeat the steps from steps from step1
   
   step4: if not then quit the program

   after saving the student data. it should look like below.
   
   > student_data.csv
   ```
   anji, b, python, 987654321
   john, h, java, 789654123
   ```
10. write a program to manage the phone contacts by using the file as a database.

  show the below options to the user

  1. display available contacts
  2. modify the contact
  3. add new contact
  4. delete the contact
        
  user will chose one of above options.

   * If user enters input as 1 then show all available contacts to the user
   * If user enters input as 2 then ask for the phone number and ask user if user want to edit phone number or contact name
       based on the input modify the contact name or phone number.
   * If user enters input as 3 the ask for the phone number and contact name and save it.
   * If user enters input as 4 then then find the contact and delete it and save the data to the file.
  
   sample database looks like below.

   ```
   Anji, 987123654
   Raju, 987124653
   Mona, 987134653
   John Snow, 887134653
   ```

10. convert the CSV file data to HTML file.

    > contacts.csv
    
    ```csv
     Anji, 987123654
     Raju, 987124653
     Mona, 987134653
     John Snow, 887134653
    ```
    
    > contacts.html
    
    ```
    <html>
        <body>
          <table>
            <tr>
              <td>Anji</td>
              <td>987123654</td>
            </tr>
            <tr>
              <td>Raju</td>
              <td>987124653</td>
            </tr>
            <tr>
              <td>Mona</td>
              <td>987134653</td>
            </tr>
            <tr>
              <td>John Snow</td>
              <td>887134653</td>
            </tr>
          </table>
        </body>
    </html>
    ```
