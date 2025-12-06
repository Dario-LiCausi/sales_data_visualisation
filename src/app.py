"""
This app does:
    .convert a raw data txt file into a clean data csv file
    .upload the clean data into a db
    .create infographics out of the clean data

This app features:
    .a cli interface / eventually gui
    .the option to select the file to process (eventually)
"""

def main():
    print("\nDATA CLEANER\n")
    while True:
        user_selection = input(
            "0. Quit application\n"
            "1. Select file\n"
            "2. Process raw data file and load to Database\n\n"
            "Selection an option: "
        ).strip()

        if user_selection == "1":
            print("\nUnfortunately the function is not implemented yet, soz!\n")
            continue
        elif user_selection == "2":
            print("\nUnfortunately the function is not implemented yet, soz!\n")
            continue
        if user_selection == "0":
            print("\nOk, bye!\n")
            break

        print("\nError! Wrong value or selection, please try again.\n")


main()
