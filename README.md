 PythonAssessment

 Summative Lab: Analyze a News Article

 Project Overview

This project is a Python-based text analysis application developed as part of a summative programming laboratory assessment. The application analyzes the contents of a news article and extracts useful textual information using Python functions, regular expressions, loops, and built-in libraries.

The program demonstrates fundamental programming concepts including file handling, string processing, regular expressions, functions, loops, conditional statements, and the use of Python's standard library.

 Objectives

The application performs the following text analysis tasks:

- Count the number of occurrences of a user-specified word.
- Identify the most frequently occurring word in the article.
- Calculate the average word length.
- Count the total number of paragraphs.
- Count the total number of sentences.
- Allow the user to repeatedly search for different words until choosing to exit.

 Features

- Reads a news article from an external text file.
- Performs case-insensitive word searches.
- Uses Regular Expressions (Regex) for accurate text processing.
- Uses the Counter class from the collections module to determine word frequency.
- Calculates average word length while excluding punctuation.
- Counts paragraphs separated by blank lines.
- Counts sentences using punctuation marks.
- Interactive command-line interface.
- Handles common edge cases such as empty input.

Technologies Used

- Python 3
- Regular Expressions (`re`)
- Collections (`Counter`)
- Pathlib (`Path`)
- Visual Studio Code
- Git
- GitHub

 Project Structure

 PythonAssessment/
│
├── pythonAssessment.py
├── news_article.txt
├── README.md
├── TESTING.md
├── .gitignore
└── screenshots/
      ├── test1-program-start.png
      ├── test2-apple-search.png
      ├── test3-ai-search.png
      ├── test4-banana-search.png
      └── test5-quit.png



 Program Requirements

The following Python modules are used:

python
import re
from collections import Counter
from pathlib import Path
No external libraries are required.

 How to Run the Program

 Run the program
bash
python3 pythonAssessment.py
![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-5.png)

 Example Output

The most common word is: the
The average word length is: 5.22
Number of paragraphs: 19
Number of sentences: 48

Enter a word to search for (or type 'quit' to exit): apple
The word 'apple' appears 16 times.

Enter a word to search for (or type 'quit' to exit): machine
The word 'machine' appears 8 times.

Enter a word to search for (or type 'quit' to exit): quit
Goodbye!
 Functions Implemented

| Function | Description |
|----------|-------------|
| `count_specific_word()` | Counts the number of occurrences of a specified word. |
| `identify_most_common_word()` | Returns the most frequently occurring word. |
| `calculate_average_word_length()` | Calculates the average length of all words in the article. |
| `count_paragraphs()` | Counts paragraphs separated by blank lines. |
| `count_sentences()` | Counts sentences using punctuation marks. |
 Programming Concepts Demonstrated

This project demonstrates the following Python concepts:

- Functions
- Variables
- Conditional statements (`if/else`)
- `for` loops
- `while` loops
- File handling
- Regular Expressions (Regex)
- Data structures
- Modular programming
- User input handling
- String manipulation
Testing

The application was tested using several search terms, including:

| Search Word | Expected Result |
|-------------|-----------------|
| apple | Returns the number of occurrences in the article. |
| AI | Counts occurrences regardless of case. |
| banana | Returns 0 when the word is not present. |
| quit | Exits the application gracefully. |

Edge cases tested include:

- Empty strings
- Words not present in the article
- Multiple user searches during a single execution
Future Improvements

Possible enhancements include:

- Counting characters and unique words.
- Displaying the top 10 most common words.
- Exporting analysis results to a text or CSV file.
- Supporting multiple article files.
- Creating a graphical user interface (GUI).
- Adding automated unit tests.
Author
Maureen Gichuhi

