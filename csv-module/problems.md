# Python CSV module

1. **Read a CSV file and print its contents**
   - Open and read a CSV file using `csv.reader()` and print each row.

2. **Write a list of lists to a CSV file**
   - Use `csv.writer()` to write multiple rows to a new CSV file.

3. **Read CSV data into a list**
   - Store the contents of a CSV file into a list of lists.

4. **Read a CSV file with a header**
   - Use `csv.DictReader()` to read a CSV file and print values by column name.

5. **Write data to a CSV file using a dictionary**
   - Use `csv.DictWriter()` to write a list of dictionaries into a CSV file.

6. **Count the number of rows in a CSV file**
   - Read a CSV file and print how many rows it contains (excluding the header).

7. **Extract a specific column from a CSV file**
   - Read a CSV file and print only the values from a specific column.

8. **Filter rows based on a condition**
   - Read a CSV file and print only the rows where a specific column meets a condition (e.g., salary > 50000).

9. **Sort a CSV file by a specific column**
   - Read a CSV file into a list of dictionaries and sort it by a particular column.

10. **Modify a specific column and write back to a new CSV**
    - Read a CSV file, update values in a specific column (e.g., increase all prices by 10%), and save it as a new file.

11. **Merge two CSV files by a common column**
    - Given two CSV files with a common column (e.g., "ID"), merge them into one file.

12. **Remove duplicate rows from a CSV file**
    - Read a CSV file, remove duplicate rows based on a specific column, and save the cleaned data.

13. **Read a large CSV file efficiently**
    - Process a large CSV file **line by line** instead of loading the entire file into memory.

14. **Calculate the sum and average of a numeric column**
    - Read a CSV file and compute the sum and average of a specific column.

15. **Convert a CSV file into a JSON file**
    - Read data from a CSV and save it as a JSON file.

16. **Validate CSV data before writing**
    - Ensure no empty fields exist before writing data to a CSV file.

17. **Handle missing values in a CSV file**
    - Identify and replace missing values (e.g., replace empty cells with `"N/A"`).

18. **Append new data to an existing CSV file**
    - Open a CSV file in append mode and add a new row of data.

19. **Encrypt and decrypt CSV data**
    - Read a CSV file, encrypt one of the columns (e.g., names), and write it back. Then, decrypt it when reading.

20. **Automate CSV data processing**
    - Write a script that **automatically updates** a CSV file daily by adding a new row with the current date and random values.
