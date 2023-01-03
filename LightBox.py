#Đây là code phần mềm chỉnh sửa ảnh cơ bản Light Box
#Nhóm 7 - Môn Xử kí & Truyền thông Đa phương tiện
#Thành viên:    Phan Quý Đạt - B20DCPT057
#               Nguyễn Tài Tuệ - B20DCPT183
#               Nguyễn Thị Hồng Hải - B20DCPT073

import tkinter as tk
from tkinter import *

import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog, ttk, messagebox, colorchooser
import cv2

class Main():
    def __init__(self, main):
        self.main = main
        self.window()

    def window(self):
        self.main.geometry("862x514")
        self.main.title("Light Box - Photo Editing App")
        self.main.configure(bg = "#F5F5F5")
        window_icon = PhotoImage(file='elements/LightBoxIcon.png')
        self.main.iconphoto(False,window_icon)

        self.welcome = Frame(self.main, width=862, height=514, bd=0, bg="#F5F5F5")
        self.editing = Frame(self.main, width=862, height=514, bd=0, bg="#2D2D2D")

        # ======= Welcome Window =======

        self.show_frame(self.welcome)

        self.text_qq = PhotoImage(file="elements/textqq.png")
        self.text= Label(self.welcome, image=self.text_qq)
        self.text.place(x=50, y=47, width=331, height=309)

        self.open_image_img = PhotoImage(file="elements/open_img.png")
        self.open_image_but = Button(
            self.welcome,
            image=self.open_image_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.chon_anh,
            relief="flat")
        self.open_image_but.place(x=104.0,y=400.0,width=178,height=50)

        self.cover_img = PhotoImage(file="elements/cover_artwork.png")
        self.cover_artwork = Label(self.welcome,image=self.cover_img)
        self.cover_artwork.place(x=385, y=35, width=445, height=445)

        # ======= Editing Window =======
        self.image_zone = Canvas(self.editing,bg="gray",width=646, height=434,
                                 bd=0, highlightthickness=0, relief="ridge")
        self.image_zone.place(x=115,y=63)

            #Thanh tác vụ
        self.task_bar = Frame(self.editing, width=862, height=45, bd=0, highlightthickness=0, bg="#9D5642")
        self.task_bar.place(x=0, y=0)
        self.back_to_welcome_img = PhotoImage(file="elements/back_to_welcome.png")
        self.back_to_welcome_but = Button(
            self.editing,
            image=self.back_to_welcome_img,
            borderwidth=0,
            highlightthickness=0,
            command= self.back,
            relief="flat")
        ToolTip(widget= self.back_to_welcome_but, text= "Back to Welcome window")
        self.back_to_welcome_but.place(x=26.0, y=1.0, width=42, height=42)

        self.reset_img = PhotoImage(file="elements/reset.png")
        self.reset_but = Button(
            self.editing,
            image=self.reset_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.reset,
            relief="flat")
        ToolTip(widget=self.reset_but, text="Reset to original image")
        self.reset_but.place(x=216.0, y=3.0, width=46, height=39)

        self.cancel_img = PhotoImage(file="elements/X.png")
        self.cancel_but = Button(
            self.editing,
            image=self.cancel_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.cancel_action,
            relief="flat")
        ToolTip(widget=self.cancel_but, text="Discard this change")
        self.cancel_but.place(x=404.0, y=3.0, width=48, height=39)

        self.apply_img = PhotoImage(file="elements/V.png")
        self.apply_but = Button(
            self.editing,
            image=self.apply_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.apply_action,
            relief="flat")
        ToolTip(widget=self.apply_but, text="Apply filter & transform")
        self.apply_but.place(x=595.0, y=3.0, width=51, height=39)

        self.download_img = PhotoImage(file="elements/download.png")
        self.download_but = Button(
            self.editing,
            image=self.download_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.save_img,
            relief="flat")
        ToolTip(widget=self.download_but, text="Download this image")
        self.download_but.place(x=788.0, y=5.0, width=34, height=34)
        #self.download_but['state'] = 'disabled'


            #Menu chính
        self.main_menu = Frame(self.editing,width=94,height=469,bd=1,bg="#DEC6B4")
        self.main_menu.place(x=0,y=45)

        self.crop_rotate_button_img = PhotoImage(file="elements/crop_button.png")
        self.crop_rotate_button = Button(
            self.main_menu,
            image=self.crop_rotate_button_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_crop_menu,
            relief="flat")
        ToolTip(widget=self.crop_rotate_button, text="Pop up transform menu")
        self.crop_rotate_button.place(x=22.0, y=20.0, width=50, height=49)

        self.brightness_img = PhotoImage(file="elements/brightness.png")
        self.brightness_button = Button(
            self.main_menu,
            image=self.brightness_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_brightness_menu,
            relief="flat")
        ToolTip(widget=self.brightness_button, text="Pop up brightness menu")
        self.brightness_button.place(x=22.0, y=96.0, width=50, height=49)

        self.contrast_img = PhotoImage(file="elements/contrast.png")
        self.contrast_button = Button(
            self.main_menu,
            image=self.contrast_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_contrast_menu,
            relief="flat")
        ToolTip(widget=self.contrast_button, text="Pop up contrast menu")
        self.contrast_button.place(x=22.0, y=172.0, width=50, height=49)

        self.split_channels_img = PhotoImage(file="elements/split_channels.png")
        self.split_channels = Button(
            self.main_menu,
            image=self.split_channels_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_split_menu,
            relief="flat")
        ToolTip(widget=self.split_channels, text="Pop up RGB menu")
        self.split_channels.place(x=22.0, y=248.0, width=50, height=49)

        self.filter_img = PhotoImage(file="elements/fx.png")
        self.filter_button = Button(
            self.main_menu,
            image=self.filter_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_filter_menu,
            relief="flat")
        ToolTip(widget=self.filter_button, text="Pop up filter menu")
        self.filter_button.place(x=22.0, y=324.0, width=50, height=49)

        self.draw_img = PhotoImage(file="elements/draw.png")
        self.draw_button = Button(
            self.main_menu,
            image=self.draw_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_draw_menu,
            relief="flat")
        ToolTip(widget=self.draw_button, text="Pop up draw menu")
        self.draw_button.place(x=22.0, y=400.0, width=50, height=49)

        self.shift_button = Label(
            self.main_menu,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

            #Menu mở rộng
        self.count = 0
        self.x = 862
        self.w = 60
        self.extended_menu = Frame(self.editing, width=60, height=243, bg="#2D2D2D",
                                   bd=0, highlightthickness=0, relief='ridge')
        self.extended_menu.place(x=862, y=146)

        self.img_trough = tk.PhotoImage(file='elements/trough.png')
        self.img_slider = tk.PhotoImage(file='elements/slider.png')
        self.style = ttk.Style(self.main)
        self.style.element_create('trough', 'image', self.img_trough)
        self.style.element_create('slider', 'image', self.img_slider)

        self.style.layout('custom.Vertical.TScale',
                     [('trough', {'sticky': 'ns'}),
                      ('slider', {'side': 'top', 'sticky': '',
                                  'children': [('custom.Vertical.Scale.label', {'sticky': ''})]
                                  })])
        self.style.configure('custom.Vertical.TScale', background='#DEC6B4')

    #Dưới đây là các chức năng của từng nút
    def back(self):
        response = tk.messagebox.askyesno(
            "Back?",
            "Back to Welcome window? \n"
            "Every changes will be discarded")
        if not response:
            return
        self.editing.place_forget()
        self.refresh_extend_menu()
        self.shift_button.place_forget()

    def reset(self):
        response = tk.messagebox.askyesno(
            "Reset?",
            "Do you want to discard all changes?")
        if not response:
            return
        self.edited_image = self.original_image
        self.filtered_image = self.original_image
        self.hien_thi_anh(self.edited_image)
        try:
            self.bri_scale.set(0)
            self.con_scale.set(0)
        except:
            return
        self.image_zone.unbind("<Button 1>")
        self.image_zone.unbind("<ButtonPress>")
        self.image_zone.unbind("<B1-Motion>")
        self.image_zone.unbind("<ButtonRelease>")
        self.image_zone.unbind("<Enter>")
        self.image_zone.unbind("<Leave>")

    def cancel_action(self):
        self.image_zone.delete(self.line)
        self.filtered_image = self.edited_image
        self.hien_thi_anh(self.edited_image)

        try:
            self.bri_scale.set(0)
            self.con_scale.set(0)
        except:
            return

        self.image_zone.unbind("<Button 1>")
        self.image_zone.unbind("<ButtonPress>")
        self.image_zone.unbind("<B1-Motion>")
        self.image_zone.unbind("<ButtonRelease>")
        self.image_zone.unbind("<Enter>")
        self.image_zone.unbind("<Leave>")

    def apply_action(self):

        self.edited_image = self.filtered_image
        self.hien_thi_anh(self.edited_image)

        try:
            self.bri_scale.set(0)
            self.con_scale.set(0)
            self.image_zone.delete(self.line)
        except:
            return

        self.image_zone.unbind("<Button 1>")
        self.image_zone.unbind("<ButtonPress>")
        self.image_zone.unbind("<B1-Motion>")
        self.image_zone.unbind("<ButtonRelease>")
        self.image_zone.unbind("<Enter>")
        self.image_zone.unbind("<Leave>")

    def save_img(self):
        original_file_type = self.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        if not filename:
            filename = "Untilted"
        filename = filename + "." + original_file_type
        self.filename = filename

        save_as_image = self.filtered_image
        cv2.imwrite(filename, save_as_image)
        print('Image saved with path'+ filename)


    def chon_anh(self):
        self.image_zone.delete("all")
        self.filename = filedialog.askopenfilename(title='Choose Image',
            filetypes=[('Image Files', '*.tif *.jpg *.png *.jpeg'),
                        ("All files", '*.*')])
        if not self.filename:
            tk.messagebox.showerror(
                title="No image chosen!", message="You haven't chosen any image.")
            return
        self.original_image = cv2.imdecode(np.fromfile(self.filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        self.edited_image = cv2.imdecode(np.fromfile(self.filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        self.filtered_image = cv2.imdecode(np.fromfile(self.filename, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

        self.hien_thi_anh(self.edited_image)
        self.show_frame(self.editing)

    def resize(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = width / height
        self.new_width = width
        self.new_height = height

        if height > 434 or width > 646:
            if ratio > 1:
                self.new_width = 646
                self.new_height = int(646 / ratio + 1)
            else:
                self.new_height = 434
                self.new_width = int(434 * ratio - 10)

        #self.ratio = height / self.new_height

        bgr = cv2.resize(image, (self.new_width, self.new_height))
        self.filtered_image = cv2.cvtColor(bgr, cv2.COLOR_RGB2BGR)

    def hien_thi_anh(self,image=None):
        self.image_zone.delete("all")
        if image is None:
            image = self.edited_image()
        else:
            image = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = width / height
        self.new_width = width
        self.new_height = height

        if height > 434 or width > 646:
            if ratio > 1:
                self.new_width = 646
                self.new_height = int(646 / ratio)
                if self.new_height > 434:
                    self.new_height = 434
                    self.new_width = int(434 * ratio)
            else:
                self.new_height = 434
                self.new_width = int(434 * ratio)

        self.ratio = height / self.new_height

        self.new_image = cv2.resize(image, (self.new_width+1, self.new_height+1))
        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image))

        self.image_zone.config(width=self.new_width, height=self.new_height)
        self.image_zone.place(x=438-self.new_width/2, y=280-self.new_height/2)
        self.image_zone.create_image(
            self.new_width/2, self.new_height/2, image=self.new_image)

    def refresh_extend_menu(self):
        self.count = 0
        self.x = 862
        try:
            self.extended_menu.place_forget()
            self.image_zone.unbind("<Button 1>")
            self.image_zone.unbind("<ButtonPress>")
            self.image_zone.unbind("<B1-Motion>")
            self.image_zone.unbind("<ButtonRelease>")
            self.image_zone.unbind("<Enter>")
            self.image_zone.unbind("<Leave>")
        except:
            pass
        self.extended_menu = Frame(self.editing, width=60, height=243, bg="#2D2D2D",
                                   bd=0, highlightthickness=0, relief='ridge')
        self.extended_menu.place(x=862, y=146)
        self.extended_menu_img = PhotoImage(file='elements/extended_menu.png')
        self.extended_menu_back = Label(self.extended_menu, image=self.extended_menu_img,
              bd=0, highlightthickness=0, background="#2D2D2D")
        self.extended_menu_back.place(x=0, y=0)
        self.filtered_image = self.edited_image
        self.hien_thi_anh(self.edited_image)
        #x=781

    def lop(self):
        if self.count < 8:
            self.x -= 81/8
            self.extended_menu.place(x=self.x, y=83)
            self.count += 1
            self.main.after(24, self.lop)
    def loop(self):
        if self.count < 8:
            self.x -= 81/8
            self.extended_menu.place(x=self.x, y=146)
            self.count += 1
            self.main.after(24, self.loop)
    def looop(self):
        if self.count < 8:
            self.x -= 81/8
            self.extended_menu.place(x=self.x, y=247)
            self.count += 1
            self.main.after(24, self.looop)
    def loooop(self):
        if self.count < 8:
            self.x -= 81/8
            self.extended_menu.place(x=self.x, y=122)
            self.count += 1
            self.main.after(24, self.loooop)

    def brightness(self,event):
        value = self.bri_scale.get()

        rgb = cv2.cvtColor(self.edited_image, cv2.COLOR_BGR2RGB)
        r,g,b = cv2.split(rgb)
        r = cv2.add(r, value)
        r[r > 255] = 255
        r[r < 0] = 0
        g = cv2.add(g, value)
        g[g > 255] = 255
        g[g < 0] = 0
        b = cv2.add(b, value)
        b[b > 255] = 255
        b[b < 0] = 0

        final_rgb = cv2.merge((r,g,b))
        self.filtered_image = cv2.cvtColor(final_rgb, cv2.COLOR_RGB2BGR)

        self.hien_thi_anh(self.filtered_image)

    def contrast(self, event):
        value = self.con_scale.get()

        f = 131 * (value + 127) / (127 * (131 - value))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        self.filtered_image = cv2.addWeighted(self.edited_image, alpha=alpha_c, beta=0, src2=0, gamma=gamma_c)

        self.hien_thi_anh(self.filtered_image)

    def tach_mau_lam(self):
        self.image = cv2.resize(self.edited_image, (self.new_width, self.new_height))
        self.blank = np.zeros(self.image.shape[:2], dtype='uint8')
        b, g, r = cv2.split(self.image)
        self.blue = cv2.merge([b, self.blank, self.blank])
        self.green = cv2.merge([self.blank, g, self.blank])
        self.red = cv2.merge([self.blank, self.blank, r])

        pixel_array = np.full((self.new_height, self.new_width, 3), self.blue, dtype=np.uint8)
        self.filtered_image = pixel_array
        self.hien_thi_anh(self.filtered_image)
    def tach_mau_do(self):
        self.image = cv2.resize(self.edited_image, (self.new_width, self.new_height))
        self.blank = np.zeros(self.image.shape[:2], dtype='uint8')
        b, g, r = cv2.split(self.image)
        self.blue = cv2.merge([b, self.blank, self.blank])
        self.green = cv2.merge([self.blank, g, self.blank])
        self.red = cv2.merge([self.blank, self.blank, r])

        pixel_array = np.full((self.new_height, self.new_width, 3), self.red, dtype=np.uint8)
        self.filtered_image = pixel_array
        self.hien_thi_anh(self.filtered_image)
    def tach_mau_luc(self):
        self.image = cv2.resize(self.edited_image, (self.new_width, self.new_height))
        self.blank = np.zeros(self.image.shape[:2], dtype='uint8')
        b, g, r = cv2.split(self.image)
        self.blue = cv2.merge([b, self.blank, self.blank])
        self.green = cv2.merge([self.blank, g, self.blank])
        self.red = cv2.merge([self.blank, self.blank, r])

        pixel_array = np.full((self.new_height, self.new_width, 3), self.green, dtype=np.uint8)
        self.filtered_image=pixel_array
        self.hien_thi_anh(self.filtered_image)

    def crop_action(self):
        self.rectangle_id = 0
        self.crop_start_x = 0
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.image_zone.bind("<ButtonPress>", self.start_crop)

    def start_crop(self, event):
        self.crop_start_x = event.x
        self.crop_start_y = event.y
        self.image_zone.bind("<B1-Motion>", self.crop)

    def crop(self, event):
        if self.rectangle_id:
            self.image_zone.delete(self.rectangle_id)

        self.crop_end_x = event.x
        self.crop_end_y = event.y

        self.rectangle_id = self.image_zone.create_rectangle(self.crop_start_x, self.crop_start_y,
                                                         self.crop_end_x, self.crop_end_y, width=1)
        self.image_zone.bind("<ButtonRelease>", self.end_crop)

    def end_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        x = slice(start_x, end_x, 1)
        y = slice(start_y, end_y, 1)

        self.filtered_image = self.filtered_image[y, x]
        self.hien_thi_anh(self.filtered_image)


    def end(self, event):
        pass

    def rotate_left(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.hien_thi_anh(self.filtered_image)
    def rotate_right(self):
        self.filtered_image = cv2.rotate(
            self.filtered_image, cv2.ROTATE_90_CLOCKWISE)
        self.hien_thi_anh(self.filtered_image)
    def vertical_action(self):
        self.filtered_image = cv2.flip(self.filtered_image, 0)
        self.hien_thi_anh(self.filtered_image)
    def horizontal_action(self):
        self.filtered_image = cv2.flip(self.filtered_image, 2)
        self.hien_thi_anh(self.filtered_image)

    def show_frame(self,frame):
        frame.place(x=0,y=0)

    def show_crop_menu(self):
        self.shift_button_img = PhotoImage(file='elements/o_crop_button.png')
        self.shift_button.config(image=self.shift_button_img)
        self.shift_button.place(x=22.0, y=20.0)

        self.refresh_extend_menu()
        self.extended_menu.config(height=394)
        self.extended_menu_img = PhotoImage(file='elements/5_extended_menu.png')
        self.extended_menu_back.config(height=394,image=self.extended_menu_img)

        self.crop_img = PhotoImage(file='elements/crop.png')
        self.crop_but = Button(
            self.extended_menu,
            image=self.crop_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.crop_action,
            relief="flat")
        ToolTip(widget= self.crop_but, text= "Draw a rectangle to crop.")
        self.crop_but.place(x=10, y=17, width=40, height=40)

        self.rotate_left_img = PhotoImage(file='elements/rotate_left.png')
        self.rotate_left_but = Button(
            self.extended_menu,
            image=self.rotate_left_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.rotate_left,
            relief="flat")
        ToolTip(widget=self.rotate_left_but, text="Rotate 90º Counter clockwise")
        self.rotate_left_but.place(x=10, y=96, width=40, height=40)

        self.rotate_right_img = PhotoImage(file='elements/rotate_right.png')
        self.rotate_right_but = Button(
            self.extended_menu,
            image=self.rotate_right_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.rotate_right,
            relief="flat")
        ToolTip(widget=self.rotate_right_but, text="Rotate 90º Clockwise")
        self.rotate_right_but.place(x=10, y=175, width=40, height=40)

        self.horizontal_img = PhotoImage(file='elements/horizontal.png')
        self.horizontal_but = Button(
            self.extended_menu,
            image=self.horizontal_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.horizontal_action,
            relief="flat")
        ToolTip(widget=self.horizontal_but, text="Horizontal Image")
        self.horizontal_but.place(x=10, y=254, width=40, height=40)

        self.vertical_img = PhotoImage(file='elements/vertical.png')
        self.vertical_but = Button(
            self.extended_menu,
            image=self.vertical_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.vertical_action,
            relief="flat")
        ToolTip(widget=self.vertical_but, text="Vertical Image")
        self.vertical_but.place(x=10, y=333, width=40, height=40)
        self.lop()

    def show_brightness_menu(self):
        self.shift_button_img = PhotoImage(file='elements/o_brightness.png')
        self.shift_button.config(image=self.shift_button_img)
        self.shift_button.place(x=22.0, y=96.0)

        self.refresh_extend_menu()

        class CustomScale(ttk.Scale):
            def __init__(self, master=None, **kw):
                kw.setdefault("orient", "vertical")
                self.variable = kw.pop('variable', tk.DoubleVar(master))
                ttk.Scale.__init__(self, master, variable=self.variable, **kw)
                self._style_name = '{}.custom.{}.TScale'.format(self, kw[
                    'orient'].capitalize())  # unique style name to handle the text
                self['style'] = self._style_name

        self.bri_scale = CustomScale(self.extended_menu, from_=200, to=-200, command=self.brightness)
        self.bri_scale.place(x=12, y=16)
        self.loop()

    def show_contrast_menu(self):
        self.shift_button_img = PhotoImage(file='elements/o_contrast.png')
        self.shift_button.config(image=self.shift_button_img)
        self.shift_button.place(x=22.0, y=172.0)

        self.refresh_extend_menu()

        class CustomScale(ttk.Scale):
            def __init__(self, master=None, **kw):
                kw.setdefault("orient", "vertical")
                self.variable = kw.pop('variable', tk.DoubleVar(master))
                ttk.Scale.__init__(self, master, variable=self.variable, **kw)
                self._style_name = '{}.custom.{}.TScale'.format(self, kw[
                    'orient'].capitalize())  # unique style name to handle the text
                self['style'] = self._style_name

        self.con_scale = CustomScale(self.extended_menu, from_=100, to=-100, command=self.contrast)
        self.con_scale.place(x=12, y=16)
        self.loop()

    def show_split_menu(self):
        self.shift_button_img = PhotoImage(file='elements/o_split_channels.png')
        self.shift_button.config(image=self.shift_button_img)
        self.shift_button.place(x=22.0, y=248.0)

        self.refresh_extend_menu()

        self.red_img = PhotoImage(file='elements/red.png')
        self.red_but = Button(
            self.extended_menu,
            image=self.red_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.tach_mau_do,
            relief="flat")
        ToolTip(widget=self.red_but, text="Show red channel")
        self.red_but.place(x=13, y=23, width=34, height=32.38)

        self.green_img = PhotoImage(file='elements/green.png')
        self.green_but = Button(
            self.extended_menu,
            image=self.green_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.tach_mau_luc,
            relief="flat")
        ToolTip(widget=self.green_but, text="Show green channel")
        self.green_but.place(x=13, y=106, width=35, height=36)

        self.blue_img = PhotoImage(file='elements/blue.png')
        self.blue_but = Button(
            self.extended_menu,
            image=self.blue_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.tach_mau_lam,
            relief="flat")
        ToolTip(widget=self.blue_but, text="Show blue channel")
        self.blue_but.place(x=20, y=185, width=21, height=36)
        self.loop()

    def show_filter_menu(self):
        self.shift_button_img = PhotoImage(file='elements/o_fx.png')
        self.shift_button.config(image=self.shift_button_img)
        self.shift_button.place(x=22.0, y=324.0)

        self.refresh_extend_menu()
        self.extended_menu.config(height=309)
        self.extended_menu_img = PhotoImage(file='elements/4_extended_menu.png')
        self.extended_menu_back.config(height=309, image=self.extended_menu_img)

        self.nega_img = PhotoImage(file='elements/nega.png')
        self.nega_but = Button(
            self.extended_menu,
            image=self.nega_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.nega,
            relief="flat")
        ToolTip(widget=self.nega_but, text="Negative")
        self.nega_but.place(x=7, y=25, width=46, height=46)

        self.bw_img = PhotoImage(file='elements/bw.png')
        self.bw_but = Button(
            self.extended_menu,
            image=self.bw_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.bw,
            relief="flat")
        ToolTip(widget=self.bw_but, text="Black & White")
        self.bw_but.place(x=7, y=96, width=46, height=46)

        self.sketch_img = PhotoImage(file='elements/sketch.png')
        self.sketch_but = Button(
            self.extended_menu,
            image=self.sketch_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.sketch,
            relief="flat")
        ToolTip(widget=self.sketch_but, text="Pencil Sketch")
        self.sketch_but.place(x=7, y=167, width=46, height=46)

        self.emboss_img = PhotoImage(file='elements/emboss.png')
        self.emboss_but = Button(
            self.extended_menu,
            image=self.emboss_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.emboss,
            relief="flat")
        ToolTip(widget=self.emboss_but, text="Emboss")
        self.emboss_but.place(x=7, y=238, width=46, height=46)

        self.loooop()

    def show_draw_menu(self):
        self.shift_button_img = PhotoImage(file='elements/o_draw.png')
        self.shift_button.config(image=self.shift_button_img)
        self.shift_button.place(x=22.0, y=400.0)

        self.refresh_extend_menu()

        self.orange = PhotoImage(file='elements/orange.png')
        self.orange_but = Button(
            self.extended_menu,
            image=self.orange,
            borderwidth=0,
            highlightthickness=0,
            command=self.orange_action,
            relief="flat")
        ToolTip(widget=self.orange_but, text="Select Orange")
        self.orange_but.place(x=17, y=29, width=26, height=26)

        self.brown = PhotoImage(file='elements/brown.png')
        self.brown_but = Button(
            self.extended_menu,
            image=self.brown,
            borderwidth=0,
            highlightthickness=0,
            command=self.brown_action,
            relief="flat")
        ToolTip(widget=self.brown_but, text="Select Brown")
        self.brown_but.place(x=17, y=109, width=26, height=26)

        self.white = PhotoImage(file='elements/white.png')
        self.white_but = Button(
            self.extended_menu,
            image=self.white,
            borderwidth=0,
            highlightthickness=0,
            command=self.white_action,
            relief="flat")
        ToolTip(widget=self.white_but, text="Select White")
        self.white_but.place(x=17, y=194, width=26, height=26)
        self.loop()

        self.color_img = PhotoImage(file='elements/color.png')
        self.color_but = Button(
            self.extended_menu,
            image=self.color_img,
            borderwidth=0,
            highlightthickness=0,

            relief="flat")
        ToolTip(widget=self.color_but, text="Choose color")
        #self.color_but.place(x=0, y=0, width=60, height=60)

        #self.looop()

        #self.color_code = ((255, 0, 0), '#ff0000')
        #self.color_code = (255, 0, 0)

    def choose_color(self):
        self.color_code = colorchooser.askcolor(title="Choose color")

    def orange_action(self):
        self.image_zone.bind("<ButtonPress>", self.start_draw)
        self.image_zone.bind("<B1-Motion>", self.orange_draw)
    def brown_action(self):
        self.image_zone.bind("<ButtonPress>", self.start_draw)
        self.image_zone.bind("<B1-Motion>", self.brown_draw)
    def white_action(self):
        self.image_zone.bind("<ButtonPress>", self.start_draw)
        self.image_zone.bind("<B1-Motion>", self.white_draw)

    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
        self.draw_ids = []

    def orange_draw(self, event):
        print(self.draw_ids)
        self.line=self.image_zone.create_line(self.x, self.y, event.x, event.y, width=3,
                                              fill='#EA853B', capstyle=ROUND, smooth=True)
        self.draw_ids.append(self.line)

        cv2.line(self.filtered_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
                 (int(event.x * self.ratio), int(event.y * self.ratio)),
                 (59,133,234), thickness=int(self.ratio * 2), lineType=8)
        self.x = event.x
        self.y = event.y
    def brown_draw(self, event):
        print(self.draw_ids)
        self.draw_ids.append(self.image_zone.create_line(self.x, self.y, event.x, event.y, width=3,
                                                     fill='#9D5642', capstyle=ROUND, smooth=True))

        cv2.line(self.filtered_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
                 (int(event.x * self.ratio), int(event.y * self.ratio)),
                 (66,86,157), thickness=int(self.ratio * 2), lineType=8)
        self.x = event.x
        self.y = event.y
    def white_draw(self, event):
        print(self.draw_ids)
        self.draw_ids.append(self.image_zone.create_line(self.x, self.y, event.x, event.y, width=3,
                                                     fill='#F5F5F5', capstyle=ROUND, smooth=True))

        cv2.line(self.filtered_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
                 (int(event.x * self.ratio), int(event.y * self.ratio)),
                 (245,245,245), thickness=int(self.ratio * 2), lineType=8)
        self.x = event.x
        self.y = event.y

    def nega(self):
        self.filtered_image = 255 - self.edited_image
        self.hien_thi_anh(self.filtered_image)
    def bw(self):
        self.filtered_image = cv2.cvtColor(
            self.edited_image, cv2.COLOR_BGR2GRAY)
        self.filtered_image = cv2.cvtColor(
            self.filtered_image, cv2.COLOR_GRAY2BGR)
        self.hien_thi_anh(self.filtered_image)
    def sketch(self):
        ret, self.filtered_image = cv2.pencilSketch(
            self.edited_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
        self.hien_thi_anh(self.filtered_image)
    def emboss(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])
        self.filtered_image = cv2.filter2D(self.original_image, -1, kernel)
        self.hien_thi_anh(self.filtered_image)

class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        widget.bind('<Enter>', self.enter)
        widget.bind('<Leave>', self.leave)

    def enter(self, event):
        self.showTooltip()

    def leave(self, event):
        try:
            self.hideTooltip()
        except:
            return

    def showTooltip(self):
        self.tooltipwindow = tw = tk.Toplevel(self.widget)
        #tw.pack(side="right")
        tw.overrideredirect(True)
        tw.geometry("+{}+{}".format(self.widget.winfo_rootx()+45, self.widget.winfo_rooty()))
        label = tk.Label(tw, text = self.text, background = "#DEC6B4", relief = 'solid', borderwidth = 0.5).pack()

    def hideTooltip(self):
        tw = self.tooltipwindow
        tw.destroy()
        self.tooltipwindow = None

class Notice(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
    def notice_wd(self):
        pass

root = Tk()
Main(root)
root.resizable(False, False)
root.mainloop()