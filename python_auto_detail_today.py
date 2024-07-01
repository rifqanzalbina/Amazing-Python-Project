import os
from datetime import datetime, timedelta

os.system('git pull')  # Mengambil perubahan terbaru dari remote repository

today = datetime.now().date()
num_commits_per_loop = 10  # Jumlah commit per loop

for i in range(50):
    for j in range(num_commits_per_loop):
        date = today - timedelta(days=i)
        d = date.strftime('%Y-%m-%d')
        if date <= today:
            with open('test.txt', 'a') as file:
                file.write(d + '\n')
            os.system(f'git add test.txt')
            os.system(f'git commit --date="{d}" -m "Commit on {d}"')
        else:
            break
    if date > today:
        break

os.system('git push -u origin main')