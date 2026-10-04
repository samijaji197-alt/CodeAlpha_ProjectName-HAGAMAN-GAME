TASK AUTOMATION WITH PYTHON SCRIPTS
=====================================

This package contains all three automation ideas, fully implemented.

------------------------------------------------------
1) move_jpgs.py
------------------------------------------------------
Goal: Move all .jpg files from one folder to another.
Concepts: os, shutil, file handling

How to use:
  1. In the same folder as the script, create a folder named "source_folder"
     and put some .jpg / .jpeg files inside it.
  2. Run:  python move_jpgs.py
  3. A new folder "jpg_files" will be created, and all .jpg files will be
     moved into it.

You can change SOURCE_FOLDER and DESTINATION_FOLDER at the top of the
script if you want different folder names.

------------------------------------------------------
2) extract_emails.py
------------------------------------------------------
Goal: Extract all email addresses from a .txt file and save them.
Concepts: re, file handling

How to use:
  1. Make sure "input.txt" (included in this package) is in the same
     folder as the script. It already contains sample email addresses
     for testing, including some invalid ones that should be ignored.
  2. Run:  python extract_emails.py
  3. Found emails are printed to the screen and saved to
     "emails_found.txt".

You can change INPUT_FILE and OUTPUT_FILE at the top of the script,
or replace input.txt with your own text file.

------------------------------------------------------
3) scrape_title.py
------------------------------------------------------
Goal: Scrape the title of a fixed webpage and save it.
Concepts: requests, re, file handling

Requires the "requests" library. If it isn't installed, run:
  pip install requests

How to use:
  1. By default the script fetches https://www.python.org
     (change the URL variable at the top of the script to any page
     you like).
  2. Run:  python scrape_title.py
  3. The page's <title> is printed to the screen and saved to
     "page_title.txt".

Note: This script needs an internet connection to work, since it
downloads a real webpage.

------------------------------------------------------
Requirements
------------------------------------------------------
- Python 3.x
- "requests" library (only needed for scrape_title.py):
    pip install requests
