import os

# Check whether the specified path exists or not
def check_create_dir(path):

    isExist = os.path.exists(path)
    
    if not isExist:

        # Create a new directory because it does not exist
        # ! Membuat direktori baru karena file tidak ada
        os.makedirs(path)
        print("Direktori baru telah terbuat !")

    else:
         print("Direktori sudah ada ! ")