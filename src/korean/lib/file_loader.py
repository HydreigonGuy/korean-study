
import os
import json

FILES_PATH = "../../../vocab"

def retrieve_file_contents(path):
    files = os.listdir(path)
    contents = {}

    for f in files:
        if os.path.isdir(os.path.join(path, f)):
            data = retrieve_file_contents(os.path.join(path, f))
            for d in data:
                contents[d] = data[d]
        elif os.path.isfile(os.path.join(path, f)):
            file = open(os.path.join(path, f))
            data = json.loads(file.read())
            file.close()
            for d in data:
                contents[d] = data[d]
    return (contents)
