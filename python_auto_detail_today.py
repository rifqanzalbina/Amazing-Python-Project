import os

# Mengatur upstream branch dan mengambil perubahan terbaru dari remote repository
os.system("git pull")

# Melakukan loop untuk menambahkan dan meng-commit perubahan sebanyak 20 kali
for i in range(20):
    d = "Updated Daily Check"
    
    # Menulis perubahan ke dalam file
    with open("test.txt", "a") as file:
        file.write(d + "\n")

    # Menambahkan file ke staging
    os.system("git add test.txt")
    
    # Commit dengan tanggal yang ditentukan
    os.system('git commit --date="2025-07-01T00:00:00" -m "Update daily check"')

# Mengirim perubahan lokal ke remote repository
os.system("git push")