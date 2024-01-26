import os

# Получение простых чисел p и q из переменных среды
p = int(os.environ.get('p'))
q = int(os.environ.get('q'))

n = p * q
m = (p - 1) * (q - 1)

# Шифрование сообщения
def encrypt(message):
    return pow(message, 2, n)

def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

# Дешифрование сообщения
def decrypt(cip):
    n = p * q
    
    d, yp, yq = gcd_extended(p, q)
    mp, mq = int(cip**((p + 1)/4) % p), int(cip**((q + 1)/4) % q)
    
    x1 = (yp * p * mq + yq * q * mp) % n
    x2 = n - x1
    x3 = (yp * p * mq - yq * q * mp) % n
    x4 = n - x3

    return x1, x2, x3, x4

# Пример использования
message = 24
ciphertext = encrypt(message)
decrypted_message = decrypt(ciphertext)

print(f'Исходное сообщение: {message}')
print(f'Зашифрованное сообщение: {ciphertext}')
print(f'Расшифрованное сообщение: {decrypted_message}')