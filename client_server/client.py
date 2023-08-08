import sys
from os import walk, path
from requests import post


class Client:

    def __init__(self, folder_path, server_url="http://localhost:8080"):
        self.folder_path = folder_path
        self.server_url = server_url

    def check_path(self):
        if not path.isdir(self.folder_path):
            raise FileNotFoundError("!!!INPUT PATH IS WRONG!!!\n"
                                    "Input path: {}".format(self.folder_path))

    def send_to_server(self):
        self.check_path()
        self.iterate_files()

    def iterate_files(self):
        for subdir, dirs, files in walk(self.folder_path):
            for file in files:
                curr_path = path.join(subdir, file)
                self.send_file_path_to_server(curr_path)

    def send_file_path_to_server(self, file_path):
        file = {'file': file_path}
        post(self.server_url, json = file)


if len(sys.argv) == 2:
    client1 = Client(sys.argv[1])
    client1.send_to_server()
    print("Success!! Check the logs on server commandline")
else:
    raise ValueError("Running command should contain one argument (a string representing a path to a specific folder)")
