from PIL import Image

class Blue_changing:
    def encrypt(message, file_path):
        image = Image.open(file_path)
        pixels = image.load()
        size = len(message)
        x, y = image.size
        for i in range(min(size, x*y)):
            t = pixels[i % x, i // x]
            sim = ord(message[i])
            if sim > 1023:
                sim -= 896
            pixels[i % x, i // x] = (t[0], t[1], sim)
        image.save(file_path)
    def decrypt(file_path):
        image = Image.open(file_path)
        pixels = image.load()
        answer = ""
        x, y = image.size
        for j in range(y):
            for i in range(x):
                sim = pixels[i, j][2]
                if sim > 127:
                    sim += 896
                answer += chr(sim)
        return answer
