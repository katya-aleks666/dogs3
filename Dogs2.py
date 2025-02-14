from tkinter import *
from tkinter import messagebox as mb
import requests
from PIL import Image,ImageTk
from io import BytesIO


def get_dog_image():
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except Expection as e:
        mb.showerror("Ошибка", f"Возникла ошибка при запросе к API {e}")
        return None


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            response = requests.get(image_url,steam=True)
            response.rais_for_status()
            img_data = BytesIo(response.content)
            img=Image.opem(img_data)
            img.thumbnail((300,300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img
        except Exception as e:
            mb.showerror("Ошибка",f"Возникла ошибка  при загрузке изображения{e}")


window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label=Label()
label.pack(pady=10)

button = Button(text="Загрузиить изображение", command=show_image)
button.pack(pady=10)
window.mainloop()






