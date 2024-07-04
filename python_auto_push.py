import datetime
import os

start_date = datetime.date(2023, 1, 1)  # Tanggal awal yang diinginkan
end_date = datetime.date(2024, 7, 4)  # Tanggal akhir yang diinginkan

for i in range((end_date - start_date).days + 1):
    commit_date = start_date + datetime.timedelta(days=i)
    with open('test.txt', 'a') as file:
        file.write(str(commit_date) + '\n')
    os.system(f'git add test.txt')
    os.system(f'git commit --date="{commit_date} 12:00:00" -m 1')

os.system('git push -u origin main')