# defining some constants
ATTRIBUTES = ["address", "area", "town", "postal_code", "property_type",
              "floor_size", "TOP", "bedrooms", "bathroom", "asking price"]

ADDRESS=0
AREA=1
TOWN=2
POSTAL=3
TYPE=4
SIZE=5
TOP=6
BEDRM=7
BATHRM=8
PRICE=9

PROPERTY_LISTING_FILE_PATH = "property_listing.txt"
REGISTERED_USERS_FILE_PATH = "reg_users.txt"

# convert file to dictionary
def property_file_to_dict():
    # initialize an empty list to store the properties
    properties_dict = {}
    property_list = []

    # open the file in read mode
    f = open(PROPERTY_LISTING_FILE_PATH, 'r')

    # read each line of the file
    for line in f:

        # split the line into a list of values
        values = line.strip().split(':')

        # when it meets the divider ----, start new property
        if (line.startswith("--") == True):
            properties_dict[property_name] = property_list
            property_list = []  # reset property_list

        # record property number
        elif (values[1] == ""):
            property_name = values[0]

        # add the values to the properties list
        elif (values[1] != ""):
            property_list.append(values[1].strip())

    f.close()

    return properties_dict

# save new users into a database
def save_user_info(basic_info):
    f = open(REGISTERED_USERS_FILE_PATH, "a")
    f.write(basic_info["name"]+","+basic_info["area"]+","+basic_info["property_type"])
    f.write("\n")
    

# retrieve existing users from database
def user_exist(name):
    # initialize an empty list to store the properties
    basic_info = {}

    # open the file in read mode
    f = open(REGISTERED_USERS_FILE_PATH, 'r')

    # read each line of the file
    for line in f:

        # split the line into a list of values
        values = line.strip().split(',')

        if name == values[0]:
            basic_info["name"]=values[0]
            basic_info["area"]=values[1]
            basic_info["property_type"]=values[2]
            break

    f.close()

    return basic_info


# input basic information

def input_basic_info():

    name = input("Enter name to check if you are an existing user: ")

    # for existing users, the function will return the non empty basic_info dictionary
    basic_info = user_exist(name)

    # for new users
    if basic_info == {}:

        basic_info["name"] = name

        print("Hi "+name+", please provide more information so we can register you!")

        area = input("Which area do you live in now? ")
        basic_info["area"] = area

        while True:
            property_type = input(
                "What kind of property are you looking for? HDB, CONDO or BUNGALOW? ")
            if property_type.lower() == "hdb" or property_type.lower() == "condo" or property_type.lower() == "bungalow":
                break
            else: 
                print("Invalid property type, choose either HDB, CONDO or BUNGALOW")
        basic_info["property_type"] = property_type.lower()

        save_user_info(basic_info)
    
    else:
        print("Welcome back "+name+"!")
    return basic_info


# setting criterias for search
def set_criterias():
    criterias = {}
    while True:
        print("="*10)
        print("Current Criterias\n---------- ")
        for key in criterias:
            print(key, ": ", criterias[key])
        print("="*10)
        option = input(
            "Select option to set criteria for\n0. Exit criteria settings\n1. Budget\n2. Location \n3. Size \n4. Number of bedrooms\n")
        if option.isdigit() == False or int(option) < 0 or int(option) > 4:
            print("Invalid input!")
        else:
            option = int(option)

            if option == 0:
                return criterias
            elif option == 1:
                criterias["budget"] = int(input("Enter your budget: "))
            elif option == 2:
                criterias["location"] = input(
                    "Enter your preferred location: ")
            elif option == 3:
                criterias["size"] = int(input("Enter the size(in sq feet) you require: "))
            elif option == 4:
                criterias["bedroom"] = int(
                    input("Enter number of bedrooms you require: "))
        print()

# displaying properties
def display_properties(properties_dict):
    print("="*10)
    print("Listing ", len(properties_dict), "propert(y/ies)")
    print("="*10)

    for key, value in properties_dict.items():
        print(key + ":")
        for i in range(len(key)):
            # print("KEY IS", key)
            print(ATTRIBUTES[i], ": ", value[i])
        print()

# return an array of properties that fits the criterias


def match_suitable_properties(criterias, properties_dict, basic_info):
    print("="*10)
    print("Property Types: ",basic_info["property_type"].lower())
    if("budget" in criterias.keys()):
        print("budget (max): ",criterias["budget"])
    if("location" in criterias.keys()):
        print("preferred location: ",criterias["location"])
    if("size" in criterias.keys()):
        print("preferred size: ",criterias["size"])
    if("bedroom" in criterias.keys()):
        print("number of bedroom: ",criterias["bedroom"])
    print("="*10)

    matched_properties = {}

    # make sure property type is correct
    for key,value in properties_dict.items():
        if (basic_info["property_type"].lower() in value[TYPE].lower()):
            matched_properties[key] = value

    # make sure criterias set are correct
    if (criterias!={}):
        if("budget" in criterias.keys()):
            for key,value in list(matched_properties.items()):
                if (criterias["budget"]<int(value[PRICE])):
                    matched_properties.pop(key)

        if("location" in criterias.keys()):
            for key,value in list(matched_properties.items()):
                print("AREA!", value[AREA], "CRITERIAS",criterias["location"])
                if (criterias["location"].lower() not in value[AREA].lower()):
                    matched_properties.pop(key)

        if("size" in criterias.keys()):
            for key,value in list(matched_properties.items()):
                if (criterias["size"] > int(value[SIZE])):
                    matched_properties.pop(key)

        if("bedroom" in criterias.keys()):
            for key,value in list(matched_properties.items()):
                if (criterias["bedroom"] > int(value[BEDRM])):
                    matched_properties.pop(key)

    return matched_properties

# displaying main menu


def display_menu():
    print("Welcome!")
    while True:
        try: 
            option = int(input("Choose an option\n0. Exit\n1. Sign Up(for new users) or Log in \
            \n2. Set Criterias\n3. Search!\n"))
            
            print()
            return option
        except:
            print("Please enter a valid number. Your options are 0, 1, 2, 3")

def main():
    basic_info = {}
    criterias = {}

    # convert properties into array
    properties_dict = property_file_to_dict()

    # print(properties_dict)
    display_properties(properties_dict)


    # user input
    while True:
        option = display_menu()
        if option == 0:
            # exit
            return

        elif option == 1:
            print("Inputting basic info...")
            # input basic info
            basic_info = input_basic_info()

        elif option == 2:
            print("Setting criterias...")
            print("basic info dict ", basic_info)
            # set criterias
            if (basic_info == {}):
                print("Choose option 1 to set up profile first!")
            else:
                print("="*10)
                print("Hello ", basic_info["name"],
                      "! Lets set up some search criterias")
                criterias = set_criterias()

        elif option == 3:
            if (basic_info == {}):
                print("Choose option 1 to set up profile!")

            else:
                print("Hello ", basic_info["name"], "!")
                print("Searching properties...")

                # if (criterias == {}):
                #     # display all properties because no criterias
                #     print(
                #         "Listing all properties. To set properties, choose option 2 from the menu")
                #     print("="*10)
                #     display_properties(properties_dict)
                # else:
                print("Listing properties based on the following criterias...")
                matched_properties = match_suitable_properties(
                    criterias, properties_dict, basic_info)
                display_properties(matched_properties)
        print()


main()
