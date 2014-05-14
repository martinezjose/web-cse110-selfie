#Django Framework for Google App Engine
This project will hold the web pages and web apis for our interactive menu project.

##Install the App Engine Python SDK
###Linux/MacOS
Download and install Google Cloud SDK by running the following command in your shell or Terminal:

1. ```curl sdk.cloud.google.com | bash```
(Or, you can download https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip or https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz, unpack it, and launch the ./google-cloud-sdk/install.sh script.)

2. Restart your shell or Terminal.

3. Authenticate to Google Cloud Platform by running
`gcloud auth login`.

###Windows
`https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip`

1. Download the Cloud SDK archive using the above link and unpack it by right-clicking google-cloud-sdk.zip file and selecting Extract All.

2. Launch `google-cloud-sdk\install.bat` script and follow the installation prompts.

3. Restart your Command Prompt (cmd.exe) session, and authenticate to Google Cloud Platform by running `gcloud auth login`.

##You'll need Python 2.7.6 for x86

Download and install the following package:
###Windows
https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi

###Mac
https://www.python.org/ftp/python/2.7.6/python-2.7.6-macosx10.6.dmg

###Verify installation
Run the following inside a terminal or command prompt:

1. `python`

2. `>>> import sys`

3. `>>> print(sys.version)`

Verify that the version it's 2.7.6.

##You'll need Django also, version 1.6.4 (make sure you install Python first)
###Windows/Linux/MacOS
1. Download the following package:
https://www.djangoproject.com/download/1.6.4/tarball/
2. Unpackage it to the folder of your preference
3. From the terminal/cmd, go to the folder where you unpackaged django
4. Run the following command `setup.py install`
5. Add the `Scripts` folder that was just created at the root folder where Python is installed to the `PATH` environment variable.
6. Check that everything works by checking the usage of the following command gets printed: `django-admin.py`.

## Run Locally

`cd appengine-django-skeleton`

Run this project locally from the command line:
`./manage.py runserver`
See the output in your browser at http://localhost:8000

This project uses manage.py to call the development server. See the other management commands for other options.

#Deploy

###To deploy the application:

Deploy the application with: `appcfg.py --oauth2 update [projectDirectory]` or use the App Engine Launcher.

#Next Steps

Right now, we have a very simple Django application. I will be adding the basic template and classes shortly.
