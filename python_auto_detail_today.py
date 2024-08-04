import os, random

# Mengatur upstream branch
os.system('git pull')  # Mengambil perubahan terbaru dari remote repository

for i in range(0, 20):
    d = 'Updated Daily Check'
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add test.txt')
    os.system('git commit --date="2024-08-04" -m 1')

os.system('git push') # Mengirim perubahan lokal ke remote repository   