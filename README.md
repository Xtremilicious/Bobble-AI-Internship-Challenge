## How to Run

 1. Python 3.7.6 should be installed along with `pip`.
 2. Open console window inside the `source` folder.
 3. To run the code, type `python iterative_word_suggestion.py`

## How to Build (.exe file) - Already pre-built

 1. **First, make sure you are inside the `source` folder**
 2. To **build** the executable file type:
 3. `pip install pyinstaller`
 4. Then, `pyinstaller -F iterative_word_suggestion.spec
    --distpath ../build --workpath ../build/temp --clean`. This is only needed for building the project as an executable file.
 5. Lastly, for reading data from the CSV, the file should be in the same directory as the .exe file. Hence, `copy EnglishDictionary.csv ../build/`

## Problem Statement
Problem 1: Iterative Word Suggestion
Given a CSV* file with words and their frequency.

Build an executable file which should take a word, character by character input (only english ASCII characters), and print the 5 nearest matching words with highest frequency and the time taken to get the output in each iteration as well. Exit with ‘#’ sign or when there is no match found.

Output will be according to all the input characters.

Executable must be portable, should run on any 32-bit windows machine.

No other dependencies should be there for the executable to run.

  

Example:
k
Know, kiss, kill, kick, keyboard  250 μs
i
Kiss, kill, kick, kite, kitten  200 μs
l
Kill, killer, killed, kilobyte, kilogram, 238 μs
l
Kill, killer, killed, killable  296 μs
q
No match Found !! 150 μs
Exiting

Program Submission Rules:

-   There must be 2 directories. All the code should be in a directory named : “source” & the executable must be in the directory “build” with no other dependencies(not even compiler libraries dependency).
    
-   Code must be compilable. If some additional argument to be given for compilation, please prefer make or Cmake.
    
-   A README file should be there within the “source” directory with all the commands in sequence to build the project.
    

*Link to CSV file : [https://drive.google.com/open?id=12UJl_TjV_JlMVS9XCGLEXfboPXO4lMi3](https://drive.google.com/open?id=12UJl_TjV_JlMVS9XCGLEXfboPXO4lMi3)
