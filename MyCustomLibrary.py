import os
import random
import string
import robot
import paramiko
import setuptools



from SSHLibrary import SSHLibrary
__version__ = '1.0.0'
lib = SSHLibrary()

class MyCustomLibrary(object):
    ROBOT_LIBRARY_VERSION = __version__
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def open_connection_and_login(self, ip, port, username, password):

        lib.open_connection(ip, port=port)
        output = lib.login(username, password)
        if "Welcome to Ubuntu" in output:
            print("Logged in successfully.")
        else:
            print("Login failed.")


    def close_connection_and_logout(self):
        lib.close_connection()
        print("Connection closed.")

    def execute_my_command(self, command):
        print("Executing command: " + command)
        output = lib.execute_command(command)
        print("Successful")
        print(output)
        return output

    def copy_directory_from_source_to_vm(self, source, destination):
        if os.path.exists(source) is False:
            print("Source path can not be found! exiting..")
            return
        print("Copying " + source + " to " + destination)
        if MyCustomLibrary.check_if_directory_exists(self,destination) is True:
            output = lib.execute_command("rm -r " + destination)

        output = lib.put_directory(source,destination)
        print("Success.")

    def copy_file_from_source_to_vm(self, source, destination):
        if os.path.exists(source) is False:
            print("Source path can not be found! exiting..")
            return

        print("Copying " + source + " to " + destination)
        if MyCustomLibrary.check_if_file_exists(self,destination) is True:
            output = lib.execute_command("rm -r "+destination)

        output = lib.put_file(source,destination)
        print("Success.")

    def delete_files_in_directory(self,destination):
        if MyCustomLibrary.check_if_directory_exists(self,destination) is False:
            print("remote directory doesnt exist..")
            return
        else:
            lib.execute_command("rm "+destination+"/*")
            print("Success")


    def create_file_in_vm(self,name,content,directory):
        if MyCustomLibrary.check_if_file_exists(self,directory) is True:
            output = lib.execute_command("rm -r "+directory)
        concat = directory+"/"+name
        lib.execute_command("echo '"+content+"'>"+concat+".txt")
        print("success")


    def check_if_directory_exists(self,destination):
            found_or_not = MyCustomLibrary.execute_my_command(self, "test -d "+destination+" && echo found "
                                                                                           "|| echo not found")
            if found_or_not == "found":
                print("Directory exists! continuing..")
                return True
            else:
                return False


    def get_file_from_vm(self,remote,local):
        if MyCustomLibrary.check_if_file_exists(self,remote) is False:
            print("remote file doesnt exist..")
            return
        lib.get_file(remote,local)
        print("success")

    def check_if_file_exists(self,destination):
            found_or_not = MyCustomLibrary.execute_my_command(self, "test -f "+destination+" && echo found "
                                                                                           "|| echo not found")
            if found_or_not == "found":
                print("File exists! continuing..")
                return True
            else:
                return False

