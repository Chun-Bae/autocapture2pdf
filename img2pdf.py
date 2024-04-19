from PIL import Image
import os

def convert_images_to_pdf(image_folder, output_pdf_path):    
    image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.png')]
    
    image_files.sort()
    
    first_image = Image.open(image_files[0]).convert('RGB')
    
    other_images = [Image.open(img).convert('RGB') for img in image_files[1:]]
    
    first_image.save(output_pdf_path, save_all=True, append_images=other_images)

    print(f'PDF file has been created: {output_pdf_path}')

image_folder = './img'
output_pdf_path = 'output.pdf'

convert_images_to_pdf(image_folder, output_pdf_path)
