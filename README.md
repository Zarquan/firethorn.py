# firethorn.py

Python client for the Firethorn project
(http://wfau.metagrid.co.uk/code/firethorn)
Contains functionality allowing users (admins) to create resources (jdbc/adql/ivoa) and users to create workspaces, 
navigate the metadata, import schemas and run queries.


## Installation Instructions (virtualenv)

### Install pip

### Install virtualenv

`pip3 install virtualenv`

### Grab a copy of the github project  

`git clone https://github.com/stvoutsin/firethorn.py.git`

### Initialize a virtual environment in the project directory

`virtualenv --python=/usr/bin/python3 firethorn.py/`

### Activate the virtualenv 

`cd firethorn.py/`

`source bin/activate`

### (Optional) Set environment configuration variables

`datahost=`

`datadata=`

`datauser=`

`datapass=`

`datacatalog=`

`datatype=`

`adminuser=`

`adminpass=`

`admingroup=`

`datadriver=`

`endpoint=`

`osa_endpoint=`

`maxrows =`



### Install Firethorn using pip 

`pip3 install firethorn.py/`

## Run Python and import Firethorn

`bin/python3.4` 

..

`import firethorn`

..

..
