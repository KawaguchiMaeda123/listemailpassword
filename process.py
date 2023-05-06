import re

input_file = 'list.txt'
output_file = 'output.txt'
email_password_pairs = []

# Membaca file input
with open(input_file, 'r') as file:
    lines = file.readlines()

# Memeriksa setiap baris untuk pola email dan kata sandi
for i in range(0, len(lines), 2):
    email = lines[i].strip()
    password = lines[i+1].strip()

    # Mengecek pola email dan kata sandi
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) and re.match(r'^[a-zA-Z0-9]+$', password):
        email_password_pairs.append(f'{email}|{password}')

# Menyimpan hasil dalam file output
with open(output_file, 'w') as file:
    file.write('\n'.join(email_password_pairs))

print('Proses selesai. Hasil disimpan dalam file output.txt.')
