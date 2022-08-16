from crud_functions import *

main_list = []

terminate_program = False
while not terminate_program:
    print("""\
\n_________________________Entry_________________________

Type "1" to create
Type "2" to read
Type "3" to update
Type "4" to delete
Type "5" to generate csv
Type "6" to generate json
Type "7" to use data from a json file
Type "8" to generate local server
Type "9" to exit""")

    try:
        main_var = int(input("\nWhat do you want to do?: "))

        if main_var < 1 or main_var > 9:
            raise ValueError("Does not match any of the options")

    except ValueError:
        print("\nEnter a number according to the operation you want")

    else:
        if main_var == 1:
            create(main_list)

        elif main_var == 2:
            read(main_list)

        elif main_var == 3:
            update(main_list)

        elif main_var == 4:
            delete(main_list)

        elif main_var == 5:
            generate_csv(main_list)

        elif main_var == 6:
            generate_json(main_list)

        elif main_var == 7:
            main_list = use_saved_json(main_list)

        elif main_var == 8:
            stabilish_server(main_list)

        else:
            terminate_program = True
