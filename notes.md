

# Project Stucture 

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

