import os, random

# Mengatur upstream branch
os.system('git branch --set-upstream-to=origin/main main')

os.system('git pull')  # Mengambil perubahan terbaru dari remote repository

for i in range(0, 150):
    d = str(i) + ' days ago'
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add test.txt')
    os.system('git commit --date="2024-07-05" -m 1')

os.system('git push')  # Mengirim perubahan lokal ke remote repository