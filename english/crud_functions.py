from json import loads, dumps
from random import randint
from http.server import HTTPServer, BaseHTTPRequestHandler
from time import strftime, localtime, time


###############################################################
#                   USAGE: CREATE A SERVER                    #
#              WARNING: NEEDS INTERNET TO BE USED             #
#                                                             #
# ==> class: NeuralHTTP                                       #
#                                                             #
#     "to_get": makes server able to suport method GET        #
#     "to_post": makes server able to suport method POST      #
#                                                             #
#                                                             #
# "define_port": control erroneus inputs from the user        #
# "create_server": tries creating the server                  #
# "stabilish_server": create server with methods GET e POST   #
###############################################################


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        json_file = open("main.json", "r")
        json_text = json_file.read()

        self.send_response(200)
        self.send_header("Content_type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(f'{json_text}', "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content_type", "application/json")
        self.end_headers()

        date = strftime("%Y-%mmm-%d %H:%M:%S", localtime(time()))
        self.wfile.write(bytes("{'time':'" + date + "'}", "utf-8"))


def define_port():
    defined = False
    while not defined:
        try:
            port_input = int(input("Type the number of the PORT: "))

        except ValueError:
            print("\nUse only numbers to define the PORT\n")

        else:
            return port_input


def create_server(host, port):
    try:
        server = HTTPServer((host, port), NeuralHTTP)

    except:
        return "Server creation failed"

    else:
        return server


def stabilish_server(any_list):
    verified = check_data(any_list)
    if verified == "No Data":
        return False

    host = input("Type your IP address: ")
    port = define_port()

    crud = dumps(any_list, indent=4, sort_keys=True)

    file = open(r"main.json", "w")
    file.write(crud)
    file.close()

    server = create_server(host, port)

    if server == 'Server creation failed':
        print("\nIt was not possible to create the server")
        return False

    print(f'\nServer running in: http://{host}:{port}/')
    server.serve_forever()


###############################################################
# USAGE: SAVE CRUD IN FILE AND MAKE IT ABLE TO BE USED AGAIN  #
#                                                             #
# "generate_json_in_html": save data in a html file           #
#                                                             #
# "generate_json": save data in a json file                   #
###############################################################

def check_data(any_list):
    try:
        any_list[0].keys()

    except:
        print("There is no data to be saved")
        return 'No Data'

    else:
        pass


def generate_csv(any_list):
    verified = check_data(any_list)
    if verified == "No Data":
        return False

    define_name = input("Enter a name for the new csv file: ")

    if define_name == '':
        print("\nThe file needs a name")
        return False

    filename = f"{define_name}.csv"

    try:
        file = open(f"{filename}", "w", encoding="utf-8")

    except:
        print("\nThe file cannot be saved because it contains special characters")
        return False

    else:
        pass

    for coluns in any_list[0].keys():
        file.write(f"{coluns},")

    file.write("\n")

    for all_data in range(len(any_list)):
        for values in any_list[all_data].values():
            file.write(f"{values},")

        file.write("\n")

    print(f'The file "{filename}" was created')
    file.close()


def json_check_and_create(file, data):
    try:
        file = open(f"{file}", "w", encoding="utf-8")

    except:
        print("\nThe file cannot be saved because it contains special characters")
        return False

    else:
        file.write(data)
        file.close()
        print(f'The "{file}" was created')


def generate_json(any_list):
    verified = check_data(any_list)
    if verified == "No Data":
        return False

    crud = dumps(any_list, indent=4, sort_keys=True)

    define_name = input("Enter a name for the new json file: ")

    if define_name == '':
        print("\nThe file needs a name")
        return False

    filename = f"{define_name}.json"

    json_check_and_create(filename, crud)


###############################################################
#            USAGE: USE SAVED DATA IN JSON FILE               #
#                                                             #
# "use_saved_json": use a json file to use other functions    #
#                                                             #
# "assure_file": try accessing the json file                  #
# "convert_to_python_dictionary": converts the accessed json  #
###############################################################


def use_saved_json(any_list):
    print("\nWarning! All unsaved data will be excluded!")
    warning = input("Continue? Yes or No?: ").lower()

    if warning == "yes" or warning == "y":
        path = input("\nWrite the name of the json file or the path of the same: ")

        access_file = assure_file(path)
        converted_json = convert_to_python_dictionary(access_file)

        if not access_file or not converted_json:
            return any_list

        return converted_json

    else:
        print("\nOperation canceled")
        return any_list


def assure_file(file_path):
    if file_path.find(".json") == -1:
        file_path = f"{file_path}.json"

    try:
        file = open(file_path, "r")
        file_text = file.read()

        file.close()

    except:
        print("\nFile does not exist")
        return False

    else:
        print("\nFile found")
        return file_text


def convert_to_python_dictionary(json_file):
    try:
        saved_json = loads(json_file)

    except:
        print("Unsupported json file")
        return False

    else:
        print("Operation was successful")
        return saved_json


###############################################################
#           MATCH INPUT FOR ID OR NAME PRE-EXISTENT           #
#                                                             #
# "sub_search": asks the user the search method               #
#                                                             #
# "match_id" and "match_name": search for registered data     #
###############################################################


def sub_search(any_list, usage):
    search_method = input(f"{usage} for id or name?: ").lower()

    if search_method == "id":
        return match_id(any_list)

    elif search_method == "name":
        return match_name(any_list)

    else:
        print(f'\nCan only "{usage}" by defining data id or name')
        return 'not_match'


def match_id(any_list):
    search_id = input("\nType a pre-existing ID: ")
    for data_object in range(len(any_list)):

        if any_list[data_object]["id"] == search_id:
            print("\nID found!\n")
            return data_object

    print("\nID not found")
    return "not_match"


def match_name(any_list):
    search_name = input("\nType a pre-existing name: ")
    for data_object in range(len(any_list)):

        if any_list[data_object]["name"] == search_name:
            print("\nName found!\n")
            return data_object

    print("\nName not found")
    return "not_match"


###############################################################
#    VERIFY IF ID & NAME ALREADY EXISTS BEFORE REGISTERING    #
#                                                             #
# "generate_random_id": generates a ramdom id in "create"     #
#                                                             #
# "create_new_id": let the user create a new id in "update"   #
#                                                             #
# "create_new_name": is used in "create" and "update"         #
###############################################################


def generate_random_id(any_list):
    new_id = False
    while not new_id:

        random_id = "{:0>8}".format(randint(0, 99999999))

        for data_object in range(len(any_list)):
            if any_list[data_object]["id"] == random_id:
                pass

        return random_id


def create_new_id(any_list, new_id):
    for data_object in range(len(any_list)):
        if any_list[data_object]["id"] == new_id:
            print("ID already existent")
            return "already_exists"

    return new_id


def create_new_name(any_list, new_name):
    for data_object in range(len(any_list)):
        if any_list[data_object]["name"] == new_name:
            print("\nName already existent")
            return "already_exists"

    return new_name


###############################################
#                                       .o0   #
#                                      "000   #
#   .ooooo.  oooo d0b oooo  oooo   .oooo000   #
#  d00' `"Y0 `000""0P  000  `000  d00   000   #
#  000        000      000   000  000   000   #
#  000   .o0  000      000   000  000   000   #
#  `Y0bod0P' d000b     `V00V"V0P' `Y0bod00P"  #
#                                             #
#   Create     Read      Update     Delete    #
###############################################


###############################################################
#                            CREATE                           #
#                                                             #
#   creates a new data object and store it in the main_list   #
###############################################################


def create(any_list):
    # Recieve new data from user

    name = input("\nType name: ")
    description = input("Enter a description: ")

    if name == '' or description == '':
        print("Fill all the fields")
        return False

    # Verify if it already exists

    newer_id = generate_random_id(any_list)
    newer_name = create_new_name(any_list, name)

    if newer_name == "already_exists":
        return False

    # Create new data recieved from user and store it

    dic = {"id": newer_id, "name": newer_name, "description": description}

    any_list.append(dic)

    return any_list


###############################################################
#                             READ                            #
#                                                             #
#     run a loop to display the data and format the print     #
###############################################################


def read(any_list):
    verified = check_data(any_list)
    if verified == "No Data":
        return False

    print("\n")

    for data_object in range(len(any_list)):
        print(f"||  ID : {any_list[data_object]['id']}\n"
              f"|| NAME: {any_list[data_object]['name']}\n"
              f"|| DESC: {any_list[data_object]['description']}\n")


###############################################################
#                            UPDATE                           #
#                                                             #
#     replace pre-existent data in main_list for new data     #
###############################################################


def update(any_list):
    # Search data to be updated
    verified = check_data(any_list)
    if verified == "No Data":
        return False

    update_data = sub_search(any_list, "Update")

    if update_data == "not_match":
        return False

    # Recieve new data from user

    update_id = input("Type new ID: ")
    update_name = input("Type new name: ")
    update_description = input("Type a new descripition: ")

    if update_id == '' or update_name == '' or update_description == '':
        print("Fill all the fields")
        return False

    # Verify if it already exists

    newer_id = create_new_id(any_list, update_id)
    newer_name = create_new_name(any_list, update_name)

    if newer_id == "already_exists" or newer_name == "already_exists":
        return False

    # Create new data recieved from user

    dic = {"id": newer_id, "name": newer_name, "description": update_description}

    # Update for searched data

    any_list[update_data] = dic

    print("\nSucefully changed")
    return any_list


###############################################################
#                            DELETE                           #
#                                                             #
#            delete pre-existent data in main_list            #
###############################################################


def delete(any_list):
    # Search data to be deleted
    verified = check_data(any_list)
    if verified == "No Data":
        return False

    delete_data = sub_search(any_list, "Delete")

    if delete_data == "not_match":
        return False

    # Deleted searched data
    any_list = any_list.pop(delete_data)

    print("\nSucefully deleted")
    return any_list
