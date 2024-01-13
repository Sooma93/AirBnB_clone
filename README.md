# AirBnB Clone - The console

The console for airbnb project. Create a command interpreter that can modify or delete the database The users like the administrator of 
the app Airbnb clone has the posibility of the manipulate objects and data of the application, this objects are:

* User
* Places
* States
* Cities
* Amenities
* Reviews

# Files 

* HBNHCommand: console.py
* Amenity: models/amenity.py
* BaseModel: models/base_model.py
* City: models/city.py
* models.init : models/init.py
* Place: models/place.py
* Review: models/review.py
* State: models/state.py
* User: models/user.py
* FileStorage: models/engine/file_storage.py
* engine.init: models/engine/init.py

 How To run the command interpreter:

 $ ./console.py

# Examples

Interactive mode:

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
 

Non-interactive mode:

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

# AUTHORS

* Minatalla Sabri - https://github.com/<Minatallasabr>
* Tasneem Adam - https://github.com/<Sooma93>

