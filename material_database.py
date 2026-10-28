import json  # json module import kiya data ko clean print karne ke liye

def material_mini_database():
    # materials ka database - har material ke properties store hain
    materials = {
        "aluminium": {
            "name": "aluminium",
            "melting_point": 660,  # melting point in celsius
            "density": 2700,  # density in kg/m3
            "density_unit": "kg/m3",

        },
        "iron": {
            "name": "iron",
            "melting_point": 1538,
            "density": 7874,
            "density_unit": "kg/m3",

        },
        "copper": {
            "name": "copper",
            "melting_point": 1085,
            "density": 8960,
            "density_unit": "kg/m3",
            "thermal_conductivity": {  # thermal conductivity vs temperature
                "300k": 400,
                "100k": 1000,
                "4k": 1000,
                "0.1k": 50
            }

        },
        "titanium": {
            "name": "titanium",
            "melting_point": 1668,
            "density": 4500,
            "density_unit": "kg/m3",

        },
        "germanium": {
            "name": "germanium",
            "melting_point": 938,
            "density": 5323,
            "density_unit": "kg/m3",

        },
        "silicon": {
            "name": "silicon",
            "melting_point": 1414,
            "density": 2329,
            "density_unit": "kg/m3",

        },
        "sapphire": {
            "name": "sapphire",
            "melting_point": 2040,
            "density": 3980,
            "density_unit": "kg/m3",

        },
        "uranium": {
            "name": "uranium",
            "melting_point": 1405,
            "density": 19050,
            "density_unit": "kg/m3",
        },

        "carbon": {
            "name": "carbon",
            "melting_point": 3550,
            "density": 2260,
            "density_unit": "kg/m3",
        },
        "graphene": {
            "name": "graphene",
            "melting_point": 4000,
            "density": 2260,
            "density_unit": "kg/m3",
        },

        "hydrogen": {
            "name": "hydrogen",
            "melting_point": 14.01,
            "density": 0.0899,
            "density_unit": "kg/m3",
        }
    }
    return materials  # pura database return kar diya

# old commented code delete - humne better functions bana diye hain

def show_menu(names):
    # ye function user ko material names ke saath index dikhata hai
    for index, material in enumerate(names):
        print(f"{index + 1}. {material}")  # index + 1 because user ko 1 se count chahiye, 0 se nahi

def get_material_properties():
    # main function - user se input leke material properties return karta hai
    materials = material_mini_database()  # database load kiya
    names = list(materials.keys())  # sirf names nikale list mein
    show_menu(names)  # menu dikhaya (function call)

    # user se input liya (string format mein)
    RAW_INPUT = input("Enter material index : ")

    # try/except block - agar user text "abc" type kare to error handle ho
    try:
        material_index = int(RAW_INPUT)  # string ko number mein convert kiya
    except ValueError:
        print("ERROR: Invalid material index - please enter a number")
        return None  # error return

    # range check - index valid hai ya nahi
    if 1 <= material_index <= len(names):
        material_name = names[material_index - 1]  # index se material name nikala
        return materials[material_name]  # database se data return kiya
    else:
        print("ERROR: Invalid material index - number out of range")
        return None  # error return

# main block - file run hone par ye execute hoga
if __name__ == "__main__":
    result = get_material_properties()  # function call
    if result is not None:  # agar result mila (error nahi aaya)
        print(json.dumps(result, indent=4))  # clean format mein print kiya


