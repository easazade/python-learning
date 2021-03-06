# why do we use venv?
# let's say we have multiple projects that uses django some use version 1 and some use version 2 of django
# now if we update our pip django module to version 2 we will hit a problem for our projects that use the version
# so we create a virtual environment for each project and each project will have its own modules downloaded separately

# to create a virtual env run command
# python -m venv venv //second venv is the name of our environment. it's a convention
# to activate the venv run command
# venv\Scripts\activate.bat
# to deactivate venv just run command
# deactivate
# we can easily delete the environment with one of these commands
# rmdir venv /s

# now one of the benefits of venv is that it allows us to export our packages so that someone else code create an
# environment with our dependency list. now the venv does it is that it creates a list of all the packages in our
# environment and puts the in a .txt file to do this just run command
# pip freeze > requirements.txt

# to install all the packages from requirements.txt file run command
# pip install -r requirements.txt
