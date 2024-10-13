from PIL import Image, ImageFilter
import time
import os

# Cria o diretório de saída, se não existir
output_directory = 'bigger_DB/images/outputs'

# Começa um timer
start_time = time.time()

# Caminho do diretório de entrada
input_directory = 'bigger_DB/images/inputs'

# Processa todas as imagens no diretório de entrada
for filename in os.listdir(input_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Filtra apenas arquivos de imagem
        original_image_path = os.path.join(input_directory, filename)
        original_image = Image.open(original_image_path)
        
        # Aplica o filtro Box Blur
        box_blurred_image = original_image.filter(ImageFilter.BoxBlur(radius=3))
        
        # Salva a imagem desfocada com um novo nome
        output_filename = f"{os.path.splitext(filename)[0]}_blurred.jpg"  # Novo nome com _blurred
        box_blurred_image.save(os.path.join(output_directory, output_filename))

# Para o timer
end_time = time.time()

# Calcula e printa o tempo de processamento
processing_time = end_time - start_time
print(f"Tempo de processamento: {processing_time:.4f} segundos")
