
<pre>
< PROJECT ROOT >
   |
   |-- social_app/
   |    | -- __init__.py                   # Bundle all above sections and expose 
   |    | -- config.py                     # App Configuration
   |    | -- util.py                       # Helpers to manipulate date, files 
   |    | -- db.py                         # Database Tables 
   |    | -- forms.py                      # App Forms: login, registration
   |    | -- views.py                      # App Routing
   |    |
   |    |-- static/ # CSS files, Javascripts files
   |    |    |-- css/      
   |    |    |-- js/
   |    |    |-- files/

   |    |-- templates/
   |    |-- | -- register.html
   |    |-- | -- login.html
   |    |-- | -- home.html


-- requirements.txt      # Application Dependencies
-- server.py             # Start the app in development and production

************************************************************************
</pre>


## TO DO
add requirement text file :DONE
add unique email and username check for register new user : KINDA DONE
fix flash() for login and register routes :DONE


## Notes
social_app: is the package (a package need an __init__ module)
from social_app import moduleName 
from . import moduleName (relative import . means from this folder)
from social_app.moduleName import (somethings in the module)


When u get port is taken etc when u run flask use: 
sudo lsof -i :5000  (to see program taking port then) kill -9 <PID>