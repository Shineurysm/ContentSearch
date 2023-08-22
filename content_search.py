import glob
import os

def get_files():
    while True:
        search_directory = input("Input the directory you want to search through (or press Enter for current directory): ").strip()

        # the user pressed Enter
        if not search_directory:
            return glob.glob(f"{os.getcwd()}/*.txt")
        
        # the entered directory doesnt exist (start allover); else return the files
        if not os.path.exists(search_directory):
            print("The specified directory doesn't exist")
        elif not os.path.isdir(search_directory):
            print("The specified path is not a directory")
        else:
            return glob.glob(f"{search_directory}/*.txt")
        

def get_content_search():
    while True:
        search_for = input("Content that you want to search: ").lower() # content

        # if the variable isnt empty
        if search_for.strip():
            return search_for

def search_content(files, search_for):
    results = []

    # searching algo
    for file_path in files:
        try:
            occurrence_in_file = 0

            # iterating through the lines of the files
            with open(file_path, encoding = "utf-8") as pwd_file:
                for line in pwd_file:
                    words = line.lower().split()
                    occurrence_in_file += words.count(search_for)
                
                # obtain the basename of the file path as it is
                # still in its default state (C:\Users\....)
                file_name = os.path.basename(file_path)
                        
                if(occurrence_in_file > 0):
                    search_result = {
                        'file_name': file_name,
                        'search_content': search_for,
                        'occurrence_count': occurrence_in_file
                    }

                    # append it into the list and return it afterwards
                    results.append(search_result)

        except (FileNotFoundError, PermissionError) as e:
            print(f"Error reading file '{os.path.basename(file_path)}': {e}")

    return results

def main():
    files = get_files() # files
    search_for = get_content_search() # content that you want to search

    results = search_content(files, search_for) # searching algo

    if not len(results): # unable to find the content that the user wanted to find
        print(f"Unable to find '{search_for}' across the directory")
    else: # found it. printing the occurencce
        for result in results:
            print(f"Found '{result['search_content']}' in {result['file_name']} with an occurrence of {result['occurrence_count']}")

# start the program
if __name__ == "__main__":
    main()
