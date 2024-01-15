import os
from pathlib import Path
import logging


package_name = "mongodb_connect"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_crud.py", 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

class Logger:
    """ This class is used for creating log file and code tracking"""
    def __init__(self,logfile):
        # Create a logger object
        self.logger = logging.getLogger(__name__)
        # Set the logging level
        self.logger.setLevel(logging.INFO)
        # Adding Handlers
        streamhandler = logging.StreamHandler()
        filehandler = logging.FileHandler(logfile)
        # Setting the format
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        #Setting the format to handlers
        streamhandler.setFormatter(formatter)
        filehandler.setFormatter(formatter)
        #Adding the handlers to logger
        self.logger.addHandler(streamhandler)
        self.logger.addHandler(filehandler)
    
    def log(self,msg,level='info') -> None:
        '''This method is used for saving various levels of logging'''
        if level == 'info':
            self.logger.info(msg)
        elif level == 'error':
            self.logger.error(msg,exc_info=True)
        elif level == 'warning':
            self.logger.warning(msg)


class ProjectStructure:

    def __init__(self,logger):
        self.logger = logger
    
    def create_files(self,files) -> None:
        for file in files:
            # using Path from pathlib sinces it handles files based on the sytem configration linur or windows
            filepath = Path(file)
            filedir,filename = os.path.split(filepath)
            if filedir != '':
                os.makedirs(filedir,exist_ok=True)
                self.logger.log(f"creating file directory : {filedir} for filename : {filename}","info")
            if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
                with open(filepath,'w'):
                    pass
                    self.logger.log(f"creating filename: {filename}","info")
            else:
                self.logger.log(f"filepath {filepath} already exists","warning")


      
# if __name__ == "__main__":
#     logger = Logger(os.path.join(os.getcwd(),'logger.log'))
#     folder = ProjectStructure(logger)
#     folder.create_files(list_of_files)