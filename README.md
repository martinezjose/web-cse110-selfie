# Lobster & Nachos App Engine Code 
This repo contains all the code we are using to build the web portion of 
our interactive menu project.

## Current version: 2 

## How To's

Downloading source code: 
```appcfg.py download_app -A lobster-nachos -V \<your_app_version\> \<output-dir\>```
V is version number (current one right above, update this often!)

Deploy app to app engine:
```appcfg.py update \<name\>```
\<name\> = where app.yaml is 

Note: Use version number with -V

Run:
```dev_appserver.py \<name\>```
(just use . when in directory)

Tests:
```python manage.py test```

Tips for Installing:

There are many turoials online to install google app engine (google it!). 
Make sure you instal python first (and django, which is easily 
done if you use pip).
