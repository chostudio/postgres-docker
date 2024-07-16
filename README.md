# postgres-docker




start the python virtual environment
Windows 
.\venv\Scripts\activate 
Mac
source .venv/bin/activate


use this command to create the container from the image if you haven't already.

docker run --name postgres_container -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres

once the container is made you can use these to stop and run it
docker stop postgres_container
docker start postgres_container

if you make changes to the code, you need to build the container again, stop the container (if you're changing it while it's running), and start up the container again. (the period at the end is not a typo, you need it)
docker build -t postgres_container .       

run the python file to initialize the schema and insert values into the database
python3 root.py