## Contact Book Project
###### Luis Venegas | UFM | May 12, 2020

#### The Project
This contact book project is meant to demonstrate starter proficiency in both 
the python language and basic programming skills. The project consists of a terminal
GUI \(unless I implement this into a flask framework\). The the Contact Book 
will allow the user to create, remove, edit and interact with their contact list. 
The contacts are saved and loaded back in when the user quits and restarts the script. 

#### How it works
Utilizing as much base python as possible, the project consists of a series of functions that provide the backbone of the script, while using control structures to determine the flow of the application. 
The underlying data structure of the project is a JSON file which is converted into a 
python dictionary for user manipulation. The contacts list is then exported as a CSV for convenience. 

###### Libraries Used
- emoji (PyPy, not django Emoji)
- validators
- json
- re
- time
- csv
