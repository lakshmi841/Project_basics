# Project_basics
A web application to print Hello World program.
#
TECHNOLOGIES AND FRAMEWORKS USED:
Framework: React, Django
Languages: Javascript, html, css,python

#
To Test On Local Machine
#
1. Clone repository to your local machine
2. Run pipenv install in the root directory of project
3. Run cd client in the project root and then run npm i in the client directory
4. Run pipenv shell
5. Run python ./manage.py makemigrations
6. Run python ./manage.py migrate
7. Lastly, run python ./manage.py runserver to start Django development server on Localhost 8000
8. On a seperate terminal, run cd client then npm start to run the React frontend server on Localhost 3000
9. Run stepes 6-8 as needed when changes to the model is made.