This script will help you in automation of build, backup and deployment process.

## How to ue

1) Take a clone 

2) Generate SSH Keygen and add it into github or gitlab

3) Run git init in ## code ## folder

4) Run git add remote origin /ssh url of your repo

5) Create .env file with following details:-
    BRANCH='master'
    BUILD_COMMAND='npm run build'
    IS_AWS=True
    PEM_FOLDER_PATH='/path/to/your/.pemkey'
    SERVER_FOLDER_PATH='/home/example'
    SERVER_CONNECTION_URL='example@192.168.x.x'
    SYSTEM_PASSWORD='1234567890'
    INSTALL_DEPENDANCY_COMMAND='npm install'

6) Create following folders:-
    * backup
    * code

7) Open terminal and run # python deploy.py #


### Note
1) Ensure to install following things:-
    * Python
    * python_dotenv

2) This script is made for local server and aws server
3) Work on linux system
