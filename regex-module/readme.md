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



