### 1) creamos el payload con msfvenom o lo programamos
### 2) Creamos la imagen:

    from PIL import Image
    
    # Crear una imagen en blanco de 500x340 píxeles
    imagen = Image.new('RGB', (500, 340), color = (255, 255, 255))
    
    # Guardar la imagen
    imagen.save('imagen.png')


### 3) agregamos el payload a la imagen

    from stegano import lsb
    
    # Ocultar el código JSP en la imagen
    secreto = lsb.hide("imagen.png", "holamundo.jsp")
    
    # Guardar la imagen con el código oculto
    secreto.save("imagen_con_payload.png")
