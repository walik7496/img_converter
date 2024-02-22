import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import magic

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Converter")

        self.image_label = tk.Label(master)
        self.image_label.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.select_button = tk.Button(self.button_frame, text="Выбрать изображение", command=self.select_image)
        self.select_button.pack(side=tk.LEFT)

        self.convert_button = tk.Button(self.button_frame, text="Конвертировать", command=self.convert_image)
        self.convert_button.pack(side=tk.LEFT)

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.preview_size_label = tk.Label(master, text="Размер превью:")
        self.preview_size_label.pack()
        self.preview_size_entry = tk.Entry(master)
        self.preview_size_entry.insert(tk.END, "200x200")
        self.preview_size_entry.pack()

        self.save_size_label = tk.Label(master, text="Размер сохраненного изображения:")
        self.save_size_label.pack()
        self.save_size_entry = tk.Entry(master)
        self.save_size_entry.insert(tk.END, "800x600")
        self.save_size_entry.pack()

        self.image = None

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.tiff;*.webp;*.svg;*.ico;*.bpg;*.bmp;*.pcx;*.tga;*.img;*.xisf;*.sid;*.sgi;*.pgf;*.pam;*.nrrd;*.ilbm;*.flif;*.fits;*.drw;*.ecw;*.cgm;*.eps;*.hdr;*.xbm;*.xar;*.wmf;*.ufo;*.svgz;*.rpf;*.rla;*.mrsid;*.ipg;*.hd")])
        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path):
        self.image = Image.open(file_path)
        self.render_image()

    def render_image(self):
        preview_size = tuple(map(int, self.preview_size_entry.get().split('x')))
        resized_image = self.image.resize(preview_size)
        photo = ImageTk.PhotoImage(resized_image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def convert_image(self):
        if self.image is None:
            return

        mime = magic.Magic(mime=True)
        file_type = mime.from_file(self.image.filename)
        if 'image' not in file_type:
            self.status_label.config(text="Выбранный файл не является изображением.")
            return

        if self.image.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.pcx', '.tga', '.ico', '.webp', '.eps')):
            converted_image = self.image.convert("RGB")
        else:
            converted_image = self.image

        save_size = tuple(map(int, self.save_size_entry.get().split('x')))
        converted_image = converted_image.resize(save_size)

        save_path = filedialog.asksaveasfilename(defaultextension=".*", filetypes=[
            ("JPEG", "*.jpg"),
            ("PNG", "*.png"),
            ("GIF", "*.gif"),
            ("TIFF", "*.tiff"),
            ("BMP", "*.bmp"),
            ("PCX", "*.pcx"),
            ("TGA", "*.tga"),
            ("ICO", "*.ico"),
            ("WebP", "*.webp"),
            ("EPS", "*.eps")
        ])
        if save_path:
            try:
                converted_image.save(save_path)
                self.status_label.config(text="Конвертация успешно завершена.")
            except Exception as e:
                self.status_label.config(text=f"Ошибка при сохранении: {str(e)}")

def main():
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
