# Importing libraries
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from customtkinter import *
from PIL import Image, ImageTk,ImageFont,ImageDraw



path = ""
color=(250,250,250)
font=24
my_image=""

# image uploader function
def image_uploader():
    file_types = [("Image files", "*.png;*.jpg;*.jpeg")]
    global path
    path = filedialog.askopenfilename(filetypes=file_types)

    # if file is selected
    if len(path):
        img = Image.open(path)
        img = img.resize((1280, 720))
        pic = ImageTk.PhotoImage(img)

        # re-sizing the app window in order to fit picture
        # and buttom

        label.configure(image=pic)
        label.image = pic
        watermark_button.configure(state=NORMAL)
        save_button.configure(state=NORMAL)



    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")

# Add Text To Photo
def watermark():
    global my_image
    my_image=Image.open(path).convert("RGBA")
    global font

    text_font=ImageFont.truetype("arial.ttf", font)
    text_to_add=watermark_text.get()

    overlay = Image.new("RGBA", my_image.size, (0, 0, 0, 0))
    edit_image = ImageDraw.Draw(overlay)

    # Get the size of the text
    bbox = edit_image.textbbox((0, 0), text_to_add, font=text_font)

    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate center position
    x = (my_image.width - text_width) / 2
    y = (my_image.height - text_height) / 2

    edit_image.text(
        (x, y),
        text_to_add,
        fill=(color),
        font=text_font
    )
    my_image = Image.alpha_composite(my_image, overlay)


    # Show the watermarked image in Tkinter
    display_image = my_image.convert("RGB")
    display_image = display_image.resize((1280, 720))
    pic = ImageTk.PhotoImage(display_image)

    label.configure(image=pic)
    label.image = pic

def my_color():
        my_colors = colorchooser.askcolor()

        if my_colors[1] is not None:
            global color
            color = my_colors[0]

            # Update the color preview
            color_button.configure(fg_color=my_colors[1])

            if path:
                watermark()

def my_font(value):
    global font
    font=value
    watermark()

def save():
    global my_image
    # Save
    my_image.save("watermarked_image.png")

# Main method
if __name__ == "__main__":
    # defining tkinter object
    app = CTk()
    controls_frame = CTkFrame(app)
    image_frame = CTkFrame(app)
    # setting title and basic size to our App
    app.title("Water mark app")
    app.geometry("1700x900")

    # adding background
    app.configure(background='gray12')

    # adding background color to our upload button
    app.option_add("*Label*Background", "white")
    app.option_add("*Button*Background", "white")

    controls_frame.pack(side="left", fill="y", padx=20, pady=20)

    image_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    label = Label(image_frame)
    label.grid(row=0,column=1,padx=10,pady=10, sticky="n")



    # defining our upload button
    uploadButton = CTkButton(controls_frame, text="Choose Image", command=image_uploader,font=("Helvetica", 24))
    uploadButton.grid(row=0,column=0,padx=10,pady=10)

    # define our watermark button
    watermark_button = CTkButton(controls_frame,text="Add watermark",command=watermark,font=("Helvetica", 24),state=DISABLED)
    watermark_button.grid(row=1,column=0,padx=10,pady=10)
    # Entry Box
    watermark_text_label=CTkLabel(controls_frame,text="Type your Watermark:",font=("Helvetica", 24))
    watermark_text_label.grid(row=2,column=0,padx=10,pady=10)
    watermark_text= CTkEntry(controls_frame,font=("Helvetica", 24),width=200)
    watermark_text.grid(row=5,column=0,padx=10,pady=10)

    #font size
    font_size=CTkLabel(controls_frame,text="Font Size",font=("Helvetica", 24))
    font_size.grid(row=6, column=0, padx=10, pady=10)
    font_slider = CTkSlider(controls_frame, from_=20, to=150, command=my_font)
    font_slider.grid(row=7,column=0,padx=10,pady=10)

    # define the color button
    color_label=CTkLabel(controls_frame,text="Color",font=("Helvetica", 24))
    color_label.grid(row=8, column=0, padx=10, pady=10)
    color_button = CTkButton(controls_frame, text="",fg_color="white", command=my_color, font=("Helvetica", 15))
    color_button.grid(row=9, column=0, padx=10, pady=10)

    # define our watermark button
    save_button = CTkButton(controls_frame, text="Save Image", command=save, font=("Helvetica", 24),state=DISABLED)
    save_button.grid(row=10, column=0, padx=10, pady=10)

    app.mainloop()