from crud_functions import *

main_list = []

terminate_program = False
while not terminate_program:
    print('\n_________________________Entry_________________________\n'
          '\nType "1" to create'
          '\nType "2" to read'
          '\nType "3" to update'
          '\nType "4" to delete'

          '\nType "5" to generate csv'
          '\nType "6" to generate json'
          '\nType "7" to use data from a json file\n'

          '\nNEEDS INTERNET ACCESS (MUST INTERRUPT)'
          '\nType "8" to generate server to display data in json\n'

          '\nType "9" to exit')

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
