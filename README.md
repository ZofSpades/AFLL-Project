AFLL-Project
Overview
AFLL-Project is a Python-based parser that validates SQL syntax using YACC (Yet Another Compiler Compiler). It checks whether the SQL queries provided by the user adhere to correct syntax rules and provides feedback on errors.

Features
Parses user-provided SQL queries.
Validates syntax using YACC.
Provides error messages for invalid SQL syntax.
Supports common SQL commands (e.g., SELECT, INSERT, UPDATE, DELETE).
Requirements
Python 3.x
ply library (Python Lex-Yacc)
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/ZofSpades/AFLL-Project.git
Navigate to the project folder:
bash
Copy code
cd AFLL-Project
Install dependencies:
bash
Copy code
pip install ply
Usage
Run the parser script:

bash
Copy code
python parser.py
Enter an SQL query when prompted, and the parser will validate its syntax.