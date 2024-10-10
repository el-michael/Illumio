# Illumio Technical Assessment

## Assumptions
1. Files (lookup_table.csv and flow_logs.txt) are given and there is at least 1 entry in the files.
2. Only protocols used currently is 'icmp', 'tcp' and 'udp'. More can be added if neccessary.
3. Each entry in lookup_table.csv file has UNIQUE and CORRECT data.
4. There is sufficient resources (memory and cpu) to run this script.
5. Lookup_table file always has a header.
6. Entries in flow_logs file are separated by white spaces only.
7. Matched tags are accounted for in lowercase and '-' is considered an invalid field.

## Instructions to Compile
### Compile through IDE
1. Download the repo or clone it from github.
2. Open up main.py file with a (VSCode, Intelij etc.), run and compile from IDE

### Compile through terminal
1. Download the repo or clone it from github
2. Change directories to where the main.py is supposed to be
3. Remove 'output.txt' file and run the following:
   ```sh
   python3 main.py
   ```

With