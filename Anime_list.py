print("Anime Title List")

anime_list = [] # empty list
proceed = True   
count = 1


while proceed == True:
    print("\nResponse:\nC - Continue\nRv - Review Your List\nDel - Delete One Item on List\nDll - Delete all\nE - Exit")
    response = input("Do you want to list your anime: ")
    if response == "C":
        anime = input("Enter the title of an Anime: ")
        anime_list.append(anime)
    elif response == "Rv":
        print("Here is your anime list")
        for i in anime_list:
            print(f"\t- {i}")  
    elif response == "Del":
        remove = input("Enter the anime that you want to delete: ")
        anime_list.remove(remove)
    elif response == "Dll":
        anime_list.pop()
    elif response == "E":
        print("Will done! Here is your Anime List:")
        for i in anime_list:
            print(f"\t- {i}") 

