# Python - Regular expression

**Basic Syntax:**

*   `.`: Matches any character except newline.
*   `^`: Matches the start of a string.
*   `$`: Matches the end of a string.
*   `*`: Matches 0 or more repetitions of the preceding pattern.
*   `+`: Matches 1 or more repetitions of the preceding pattern.
*   `?`: Matches 0 or 1 repetition of the preceding pattern.
*   `{m,n}`: Matches from `m` to `n` repetitions of the preceding pattern.
*   `[]`: Matches any single character within the brackets.
*   `|`: Acts as an OR operator.
*   `\`: Escapes special characters or signals a special sequence.

**Special Sequences:**

*   `\d`: Matches any digit (equivalent to `[0-9]`).
*   `\D`: Matches any non-digit.
*   `\w`: Matches any alphanumeric character (equivalent to `[a-zA-Z0-9_]`).
*   `\W`: Matches any non-alphanumeric character.
*   `\s`: Matches any whitespace character.
*   `\S`: Matches any non-whitespace character.
*   `\b`: Matches a word boundary.
*   `\B`: Matches a non-word boundary.

**Common Methods:**

*   `re.match()`: Checks for a match only at the beginning of the string.
*   `re.search()`: Searches for the first location where the regex pattern produces a match.
*   `re.findall()`: Finds all substrings where the regex pattern produces a match.
*   `re.finditer()`: Returns an iterator yielding match objects for all matches.
*   `re.sub()`: Replaces matches with a string.
*   `re.split()`: Splits a string by the occurrences of the regex pattern.
*   `re.fullmatch()`: Return a Match object if the whole string matches a pattern

## Examples

### Email Validation

```python
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False
```

### Extract Emails from text file

```python
import re

def extract_emails_from_file(file_path):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    with open(file_path, 'r') as file:
        content = file.read()
    emails = re.findall(pattern, content)
    return emails
```

### Split by Commas and Spaces

```python
import re

def split_str_by_pattern(content, pattern):
    output = re.split(pattern, content)
    return output

content = "apple, orange,banana , grape, lemon"
pattern = r',\s*'
output = split_str_by_pattern(content, pattern)
print(output)
```

### Extract domain from URL

```python
import re

def extract_domain(url):
    pattern = r'^(?:https?://)?(?:www\.)?([^:/\n?]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

urls = [
    "http://www.example.com/path/to/page",
    "https://example.org",
    "https://sub.domain.co.uk/path?query=param",
    "http://www.example.com:8080"
]

for url in urls:
    print(f"URL: {url} -> Domain: {extract_domain(url)}")
```

### Extract dates from text

```python
import re

def find_dates(text):
    # Define the regex pattern for matching dates in the format DD/MM/YYYY
    date_pattern = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})\b'
    
    # Find all matches of the pattern in the text
    dates = re.findall(date_pattern, text)
    
    # Reconstruct the full date from the matched groups
    full_dates = ['/'.join(date) for date in dates]
    
    return full_dates

# Example usage
text = """
Here are some dates: 23/04/2021, 05/11/2020, and an invalid date 32/13/2020.
Also, check 01/01/2000 and 29/02/2024 for leap year considerations.
"""

dates = find_dates(text)
print(dates)
```
