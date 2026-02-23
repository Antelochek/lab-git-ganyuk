import random
import time

count_char = int(input("Number of random characters: "))
start = time.time()

# Генерация случайной двоичной строки
word_sh = ""
for i in range(count_char * 8):
    word_sh += str(random.randint(0, 1))

# Преобразование в текст
normal_string = ''.join(chr(int(word_sh[i:i+8], 2)) for i in range(0, len(word_sh), 8))

end = time.time()

print(f"Binary: {word_sh}")
print("╔" + "═"*20 + "╗")
print(f"║ {normal_string:^18} ║")
print("╚" + "═"*20 + "╝")
print(f"Time: {end-start} seconds")
