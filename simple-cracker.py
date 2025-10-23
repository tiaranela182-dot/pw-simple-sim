# simple_cracker.py
# Simulasi super-sederhana: buat 1 user lokal -> hash password -> coba kata di dictionary.
# KHUSUS EDUKASI. Jangan pake ke akun nyata.

import hashlib, secrets, time

ITER = 100_000

def hash_pass(pw, salt):
    return hashlib.pbkdf2_hmac('sha256', pw.encode(), salt, ITER).hex()

# 1) Buat user contoh (kamu bisa ubah passwordnya di sini)
username = "demo"
password_plain = "123456"   # <-- ganti ini kalau mau eksperimen (tetap lokal)
salt = secrets.token_bytes(8)
password_hash = hash_pass(password_plain, salt)

print("User dibuat:", username)
print("Password (plain) untuk demo:", password_plain)
print("Salt (hex):", salt.hex())
print("Hash (hex):", password_hash)
print("\nMulai simulasi dictionary attack...\n")

# 2) Dictionary (daftar kata yg akan dicoba) - gampang diubah
dictionary = [
    "password", "123456", "qwerty", "letmein", "admin", "000000",
    "1234", "4321", "password123", "iloveyou"
]

start = time.time()
attempts = 0
found = None

for word in dictionary:
    attempts += 1
    h = hash_pass(word, salt)
    print(f"[{attempts}] mencoba: {word} -> hash: {h[:12]}...")  # tampil ringkas
    if h == password_hash:
        found = word
        print("\n>> Berhasil! password ditemukan:", found)
        break

elapsed = time.time() - start
if not found:
    print("\nGagal menemukan password dari dictionary.")
print(f"Percobaan: {attempts}. Waktu: {elapsed:.4f} detik.")
