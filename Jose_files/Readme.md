Jose Lucar 12/8/2020 Instructions to connect GUI with database 

-You need to download in your terminal the following:
  For the Backend: pip install pymongo, pip install pymongo[srv], pip install pythondns
  For the GUI: pip install Kivy, pip install kivy-deps.angle, pip install kivy-deps.glew,
  pip install kivy-deps.gstreamer, pip install kivy-deps.sdl2 and pip install kivymd

-You need the to import the following libraries: login_class.py, create_user_class.py and create_manager_class.py

-You need to store the following images in your project file anf keep the same names for those png images:
  covidshield.png
  greenshield.png
  yellowshield.png
  Medical.png
  redshield.png

-I deleted 'self.show_data' from 'on_release: self.show_data' in line 154
  to fix an error and add the functionality for button 'register'.

-After finishing installing the correct packages into your terminal and importing
  the correct python files, you need to run all the 3 python files in line 28 before you run the application python file. 

-Lines added for backend purposes to Covid_19_tracking_app:
  16-19, 21-49, 50-61, 70, 73, 151, 159, 167, 179, 192, 200, 208, 220, 281, 289, 300, 471, 474, 
  538-539, 580-581, 882-887, 891-896, 899-913, 917-932, 940-955, 960-975

- Added screens: [<RegisterScreenManager>, lines: 185-224]-> Credit to John's code for [<RegisterScreen>,lines: 185-224]
           [<StartSurveyManagerScreen>, lines: 377-445]-> Credit to John's code for [<StartSurveyScreen>,lines: 310-374]
