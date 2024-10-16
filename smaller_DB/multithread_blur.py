import threading
from PIL import Image, ImageFilter
import time

# Imagem 1
def process_image1():
    original_image = Image.open('smaller_DB/images/inputs/image1.jpg')
    box_blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=3))
    box_blurred_image.save('smaller_DB/images/outputs/image1_blurred.jpg')


# Imagem 2
def process_image2():
    original_image = Image.open('smaller_DB/images/inputs/image2.jpg')
    box_blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=3))
    box_blurred_image.save('smaller_DB/images/outputs/image2_blurred.jpg')


# Imagem 3
def process_image3():
    original_image = Image.open('smaller_DB/images/inputs/image3.jpg')
    box_blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=3))
    box_blurred_image.save('smaller_DB/images/outputs/image3_blurred.jpg')

# Começa um timer
start_time = time.time()

# Criando as threads
image1 = threading.Thread(target=process_image1)
image2 = threading.Thread(target=process_image2)
image3 = threading.Thread(target=process_image3)


# Iniciando as threads
image1.start()
image2.start()
image3.start()

# Para o timer
end_time = time.time()

# Calcula e printa o tempo de processamento
processing_time = end_time - start_time
print(f"Tempo de processamento: {processing_time:.4f} segundos")