import random
import time

word = ""
word_sh = ""
ch = ""
count_char = int(input("Number of random characters:"))
start = time.time()
for i in range(count_char*8):
    word_sh += str(random.randint(0,1))
end = time.time()
print(word_sh)
print(f"time: {end-start}")
normal_string = ''.join(chr(int(word_sh[i:i+8], 2)) for i in range(0, len(word_sh), 8))
print(normal_string)
