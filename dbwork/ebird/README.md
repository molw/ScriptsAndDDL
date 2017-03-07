## Testing Instructions
1. Spin up an OpenShift cluster and make a project
2. On your local machine go into the templates directory and do the following
command

    `oc new-app -f ./db.json`

3. then on your machine again

    `oc rsync ../ebird masterdb-1-xu29k:/tmp`

4. then

  `oc rsh masterdb-1-xu29k`

5. Once inside the pod (password for postgres is the word "password"):

       psql -U postgres -h 127.0.0.1 -W

       create database molw;

       \q

       cd /tmp/ebird/

       psql -U postgres -h 127.0.0.1 -W -f birdobs.ddl molw #you can ignore the error
       
       psql -U postgres -h 127.0.0.1 -W -f small.sql molw
