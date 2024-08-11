import fitz
import os 

def agregar_imagen(pdf_original, pdf_final, imagen_png, x, y, ancho, alto):
    pdf_documento = fitz.open(pdf_original)
    imagen = fitz.open(imagen_png)
    pagina = pdf_documento[0]
    img_rect = fitz.Rect(x, y, x + ancho, y + alto)
    pagina.insert_image(img_rect, pixmap=imagen[0].get_pixmap(alpha=True))
    pdf_documento.save(pdf_final)
    pdf_documento.close()
    imagen.close()
    
if __name__ == "__main__":
    pdf_original = "CARTA.PDF"
    pdf_final = "CARTA_final.PDF"
    imagen_png = "FIRMA.png"
    x = 110
    y = 440
    ancho = 90
    alto = 90
    agregar_imagen(pdf_original, pdf_final, imagen_png, x, y, ancho, alto)
    os.rename(pdf_final, "CARTA_final_renombrada.pdf")

