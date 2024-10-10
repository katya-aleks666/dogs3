from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image,ImageTk
from io import BytesIO





def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url,steam=True)
            response.rais_for_status()
            img_data = BytesIo(response.content)
            img=Image.opem(img_data)
            img.thumbnail((300,300))
            label.config(image=img)
            label.image = img
        except Exception as e:
            mb.showerror("Ошибка",f"Возникла ошибка {e}")


window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label=Label()
label.pack(pady=10)

button = Button(text="Загрузиить изображение", command=show_image)
button.pack(pady=10)
window.mainloop()






