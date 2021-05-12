import os
from datetime import date
from dotenv import load_dotenv
load_dotenv()

os.chdir('code')
os.system(f"git pull origin {os.getenv('BRANCH')}")
os.system(os.getenv('INSTALL_DEPENDANCY_COMMAND'))
isBuildGenerated = os.system(os.getenv('BUILD_COMMAND'))

if(isBuildGenerated == 0):
    os.chdir("../backup")
    folderName = date.today()
    os.system(f"mkdir {folderName}")
    os.chdir("../code")
    os.system(f"echo {os.getenv('SYSTEM_PASSWORD')} | sudo -S rsync -av --progress . ../backup/{folderName} --exclude build --exclude .git --exclude node_modules")
    
    if(os.getenv('IS_AWS') == 'True'):
        os.system(f"scp -i {os.getenv('PEM_FOLDER_PATH')} -r ./build {os.getenv('SERVER_CONNECTION_URL')}:{os.getenv('SERVER_FOLDER_PATH')}")
    else:
        os.system(f"sudo rsync -avz -e 'ssh' ./build {os.getenv('SERVER_CONNECTION_URL')}:{os.getenv('SERVER_FOLDER_PATH')} -y")
    