from PIL import Image
from random import seed, randint

class Blue_changing:
    def encrypt(message, file_path):
        image = Image.open(file_path)
        pixels = image.load()
        size = len(message)
        x, y = image.size
        m = pixels[0, 0]
        seed(m[0]*1000000 + m[1]*1000 + m[2])
        mas = []
        for i in range(x):
            for j in range(y):
                mas.append([i, j])
        mas.pop(0)
        for i in range(min(size, x*y - 1, 80000)):
            t1 = randint(0, len(mas) - 1)
            t = pixels[mas[t1][0], mas[t1][1]]
            sim = ord(message[i])
            if sim > 1023:
                sim -= 896
            pixels[mas[t1][0], mas[t1][1]] = (t[0], t[1], sim)
            mas.pop(t1)
        image.save(file_path)
    def decrypt(file_path):
        image = Image.open(file_path)
        pixels = image.load()
        answer = ""
        x, y = image.size
        m = pixels[0, 0]
        seed(m[0] * 1000000 + m[1] * 1000 + m[2])
        mas = []
        for i in range(x):
            for j in range(y):
                mas.append([i, j])
        mas.pop(0)
        for i in range(min(x*y - 1, 80000)):
            t1 = randint(0, len(mas) - 1)
            sim = pixels[mas[t1][0], mas[t1][1]][2]
            if sim > 127:
                sim += 896
            answer += chr(sim)
            mas.pop(t1)
        return answer
