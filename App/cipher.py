from PIL import Image

class Blue_changing:
    def encrypt(message, file_path):
        image = Image.open(file_path)
        pixels = image.load()
        size = len(message)
        x, y = image.size
        for i in range(min(size, x*y)):
            t = pixels[i % x, i // x]
            pixels[i % x, i // x] = (t[0], t[1], ord(message[i]))
        image.save(file_path)
    def decrypt(file_path):
        image = Image.open(file_path)
        pixels = image.load()
        answer = ""
        x, y = image.size
        for j in range(y):
            for i in range(x):
                answer += chr(pixels[i, j][2])
        return answer