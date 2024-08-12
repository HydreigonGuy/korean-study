
# Input format
#
# { "to do":"하다" }

# Output format
#
# {
#   "to do":[
#     {"word":"하다", "description":"", exmples:[]}
# ]
# }


import os
import json

FILES_PATH = "./vocab"

def retrieve_file_contents(path):
    files = os.listdir(path)

    for f in files:
        if os.path.isdir(os.path.join(path, f)):
            retrieve_file_contents(os.path.join(path, f))
        elif os.path.isfile(os.path.join(path, f)):
            if "new." not in f:
                file = open(os.path.join(path, f))
                data = json.loads(file.read())
                file.close()
                f = open(os.path.join(path, "new." + f), "w")
                str = "{\n"
                for d in data:
                    str = str + '  "' + d + '":[\n    {\n      "word":"' + data[d] + '",\n      "description":"", "exmples":[]\n    }\n  ],\n'
                str = str[:-2] + "\n}"
                # print(str)
                f.write(str)
                f.close()

retrieve_file_contents(FILES_PATH)
