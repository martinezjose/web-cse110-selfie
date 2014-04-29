#Django Framework for Google App Engine
This project will hold the web pages and web apis for our interactive menu project.

##Install the App Engine Python SDK
###Linux/MacOS
Download and install Google Cloud SDK by running the following command in your shell or Terminal:

1. ```curl sdk.cloud.google.com | bash```
(Or, you can download google-cloud-sdk.zip or google-cloud-sdk.tar.gz, unpack it, and launch the ./google-cloud-sdk/install.sh script.)

2. Restart your shell or Terminal.

3. Authenticate to Google Cloud Platform by running
`gcloud auth login.`

###Windows
`https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip`

1. Download the Cloud SDK archive using the above link and unpack it by right-clicking google-cloud-sdk.zip file and selecting Extract All.

2. Launch `google-cloud-sdk\install.bat` script and follow the installation prompts.

3. Restart your Command Prompt (cmd.exe) session, and authenticate to Google Cloud Platform by running gcloud auth login.

##You'll need Python 2.7.6

Download and install the following package:
###Windows
https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi

###Mac
https://www.python.org/ftp/python/2.7.6/python-2.7.6-macosx10.6.dmg

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

Right now, this is a very simple Django application. I will be adding the basic template and classes shortly.
