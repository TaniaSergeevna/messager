# messager
My project has 3 files :

-server.py
-sender.py
-receiver.py

Technology :

-Python 3.6
-Flask

Library :

-time
-datetime
-requests
-os

This project can be run on any computer with any OS. To ran we need install Python ( https://www.python.org/downloads/),
install Flask (pip install Flask) install time , datetime, requests and os.(need to install in the terminal).  

To start, open 4 terminals in the first run the server.py file (python server.py), do this using the python server.py command.
In the second, run the receiver.py file (python receiver.py). In others, run sender.py.(python sender.py). 
In the first terminal we will see the server working.The HTTP requests and the result of their execution will be visible in the terminal.
In the second terminal, we will see the output of messages.
In the latest terminals will be used as user pages. 
We enter data and only then can send SMS:
Enter username:
Mary or Jack
Enter password:
999(for Mary) or 123 (for Jack)

First, a server was created using the Flask library. 
Create list and dictionary  (messages = [{'username':'str','text':'str','time': 'float'}], and users = {'username': 'password'}) for storing data.
The send function is used to form new sms with jsona. In the sender.py file, a post request is implemented where we form json from the entered data.
In the history function, we select the necessary data that we get by the GET request in the receiver.py file. Convert from json to a convenient format
and output to the console.

https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html
https://python-scripts.com/requests
https://pythonworld.ru/moduli/modul-datetime.html
https://stackoverflow.com/questions/2084508/clear-terminal-in-python

