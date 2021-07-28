import os
import random
import string
import robot
import paramiko
import setuptools


__version__ = '1.0.0'



class TestSSH(object):
    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.lib = paramiko.SSHClient()

    def login_to_host(self, ip, port, username, password):
        try:
            self.lib.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.lib.connect(ip, port=port, username=username, password=password)
            print("Connection Opened")

        except paramiko.ssh_exception.AuthenticationException:
            print("An error occured while trying to login. Please verify"
                  "the username and password.")
            raise

        except paramiko.ssh_exception.NoValidConnectionsError:
            print("An error occured while trying to login. Please verify"
                  "the IP Address and the Port.")
            raise




    def logout_from_host(self):
        try:
            self.lib.close()
            print("Connection closed.")
        except:
            print("An error occured while closing the connection.")



    def execute_command(self, command):
        try :
            print("Executing command: " + command)
            stdin, stdout, stderr = self.lib.exec_command(command)
            if len("".join(stderr.readlines()).strip()) != 0:
                raise
            return "".join(stdout.readlines()).strip()


        except:
            print("an error occured while executing the command. An "
                  "error was returned from execution of the command.")

    def create_file(self, name, content, directory):
        try :
            concat = directory + "/" + name
            self.lib.exec_command("echo '" + content + "'>" + concat + ".txt")
        except:
            print("an error occured while creating the file.")
            raise

    def get_file(self, remote, local):
        try :
            if TestSSH.check_if_file_exists(self, remote) is False:
                print("remote file doesnt exist..")
                return
            stfp = self.lib.open_sftp()
            stfp.get(remote, local)

        except FileNotFoundError:
            print("an error occured while trying to get the file. Please make sure"
                  "your local path and the remote path are both correct.")
            raise

        except PermissionError:
            print("an error occured while trying to get the file. Please make sure"
                  "the right permissions are given.")
            raise



    def put_file(self, source, destination):
        try:
            if os.path.exists(source) is False:
                print("Source path can not be found! exiting..")
                return

            print("Copying " + source + " to " + destination)

            stfp = self.lib.open_sftp()
            stfp.put(source,destination)
        except FileNotFoundError:
            print("an error occured while trying to get the file. Please make sure"
                  "your local path and the remote path are both correct.")
            raise

        except PermissionError:
            print("an error occured while trying to get the file. Please make sure"
                  "the right permissions are given.")
            raise


    def delete_files_in_dir(self, destination):
        try:
            if TestSSH.check_if_directory_exists(self, destination) is False:
                print("remote directory doesnt exist..")
                return
            else:
                self.execute_command("rm " + destination + "/*")
        except:
            print("an error occured while trying to delete files in a directory.")
            raise

    def check_if_directory_exists(self, destination):
        stdin,stdout,stderr = self.lib.exec_command("test -d " + destination + " && echo found "
                                                                             "|| echo not found")
        if "found" in stdout.readline():
            return True
        else:
            return False

    def check_if_file_exists(self, destination):
        stdin,stdout,stderr = self.lib.exec_command("test -f " + destination + " && echo found "
                                                                         "|| echo not found")
        print("------")

        if "found" in stdout.readline():
            return True
        else:
            return False


m = TestSSH()
m.login_to_host("127.0.0.1","2222","anwar","root1234")
m.execute_command("lss")
m.delete_files_in_dir("toCopy")
#m.logout_from_host()