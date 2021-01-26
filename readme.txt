Walmart Coding Challenge: Movie Theater Seating Challenge

Assumptions:
1) If a member of another party is within three seats horizontally, they must have at least one row buffer

e.g.
if O is a person and X is an empty seat,

XXXOXXX
OXXXXXX 

is NOT allowed but

XXXOXXX
XXXXXXX
OXXXXXX

is allowed


2) Customers of same party care about sitting near each row (e.g. same row)


Building and running on a particular input file
python movietheater.py INPUT_FILE OUTPUT_FILE


Examine output of Test Cases
testcases.bat



Algorithm (explained in detail as comment in movietheater.py)
- I start with biggest groups and end with smallest groups, I determine if the group can fit inside this row, if not, try the next row
       - Optimization possibility: check if available space can fit at least HALF of group or THIRD of group
       - for large groups
- Prioritizes: 
    - seating most people so that there are fewer seats left unoccupied that could be occupied
    - not splitting up parties into different areas of a Theater

Disadvantages
- Does not respect reservation request order
    - Possible solution: Grab only up to first 200 people to make a request and use algorithm from there
- Disadvantages smaller groups 
    - Possible solution: Split reservation requests into big group queue and small group queue and alternate
    between these two groups when finding seats for a particular party






