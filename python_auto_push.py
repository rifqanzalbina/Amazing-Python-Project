import datetime
import os

start_date = datetime.date(2022, 1, 1)  # Tanggal awal yang diinginkan
end_date = datetime.date(2023, 1, 20)  # Tanggal akhir yang diinginkan
# end_date = datetime.date.today() # Tanggal yang sesuai hari ini

for i in range((end_date - start_date).days + 1):
    commit_date = start_date + datetime.timedelta(days=i)
    for j in range(10):  # Melakukan 10 commit setiap hari
        with open('test.txt', 'a') as file:
            file.write(f"{commit_date} - Commit ke-{j+1}\n")
        os.system(f'git add test.txt')
        os.system(f'git commit --date="{commit_date} {j}:00:00" -m "{j+1}"')

os.system('git push -u origin main')