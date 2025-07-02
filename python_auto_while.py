import os
from datetime import datetime, timedelta

# ! Mengatur upstream branch
os.system('git pull')  # Mengambil perubahan terbaru dari remote repository

start_date = datetime.strptime("2024-10-27", "%Y-%m-%d")
end_date = datetime.strptime("2024-11-06", "%Y-%m-%d")
current_date = start_date

while current_date <= end_date:
    for i in range(0, 20):
        d = 'Updated Daily Check'
        with open('test.txt', 'a') as file:
            file.write(d + '\n')

        os.system('git add test.txt')
        # Mengatur tanggal komit sesuai dengan current_date
        os.system(f'git commit --date="{current_date.strftime("%Y-%m-%d")}" -m "Update daily check"')

    current_date += timedelta(days=1)

os.system('git push')  # Mengirim perubahan lokal ke remote repository
