import subprocess
from subprocess import call
import os

password = os.environ['MYSQL_PASSWORD']
def database_backup():
    welcome = """
    # ######################################
    # Creating a database backup           #
    # ######################################
    """
    print(welcome)
    rc = call(["./sample.sh", str(password)])

database_backup()