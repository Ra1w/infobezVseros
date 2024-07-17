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
        mas = [[True] * y for i in range(x)]
        mas[0][0] = False
        i = 0
        while i < size:
            x1 = randint(0, x - 1)
            y1 = randint(0, y - 1)
            if mas[x1][y1]:
                t = pixels[x1, y1]
                sim = ord(message[i])
                if sim > 1023:
                    sim -= 896
                pixels[x1, y1] = (t[0], t[1], sim)
                mas[x1][y1] = False
                i += 1
        image.save(file_path)
    def decrypt(file_path):
        image = Image.open(file_path)
        pixels = image.load()
        answer = ""
        x, y = image.size
        m = pixels[0, 0]
        seed(m[0] * 1000000 + m[1] * 1000 + m[2])
        mas = [[True]*y for i in range(x)]
        mas[0][0] = False
        k = 100
        i = 0
        while i * k < x*y:
            x1 = randint(0, x - 1)
            y1 = randint(0, y - 1)
            if mas[x1][y1]:
                sim = pixels[x1, y1][2]
                if sim > 127:
                    sim += 896
                answer += chr(sim)
                mas[x1][y1] = False
                i += 1
        return answer