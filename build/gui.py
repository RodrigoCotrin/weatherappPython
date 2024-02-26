import requests
import gettext

from tkinter import messagebox
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\AD\weatherappPython\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("weatherapp")


window.geometry("500x500")
window.configure(bg = "#FFFFFF")

def get_weather_data(city):
    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    
    if weather_data.json()['cod'] == '404':
        return None
    else:
        return {
            'weather': weather_data.json()['weather'][0]['main'],
            'temp': round(weather_data.json()['main']['temp']),
            'wind_speed': weather_data.json()['wind']['speed'],
            'feels_like': round(weather_data.json()['main']['feels_like']),
            'humidity': weather_data.json()['main']['humidity']
        }

def update_weather(event=None):
    city = entry_1.get()
    weather_data = get_weather_data(city)

    canvas.itemconfig(temp_text_id, text=f"{weather_data['temp']}")
    canvas.itemconfig(weather_text, text=f"{weather_data['weather']}")
    canvas.itemconfig(wind_speed_text, text=f"{weather_data['wind_speed']} km/h")
    canvas.itemconfig(feels_like_text, text=f"{weather_data['feels_like']}ºC")
    canvas.itemconfig(humidity_text, text=f"{weather_data['humidity']}%")
    
def exibir_mensagem():
    messagebox.showinfo("Informe a Cidade!", "Você não informou nenhuma cidade")
    
def btn3click():
    cidade_informada = entry_1.get()
    if not cidade_informada:
        exibir_mensagem()
    else:
        update_weather()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    184.0,
    60.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=34.5,
    y=43.0,
    width=299.0,
    height=37.0
)

temp_text_id = canvas.create_text(
    236.0,
    126.0,
    anchor="nw",
    text="29",
    fill="#000000",
    font=("Poppins ExtraLight", 100 * -1)
)

canvas.create_text(
    360.0,
    133.0,
    anchor="nw",
    text="º",
    fill="#000000",
    font=("Poppins Light", 50 * -1)
)

weather_text = canvas.create_text(
    250.0,
    237.0,
    anchor="nw",
    text="Mostly Sunny",
    fill="#000000",
    font=("Poppins Light", 20 * -1)
)

wind_speed_text = canvas.create_text(
    44.0,
    376.0,
    anchor="nw",
    text="8 km/h",
    fill="#000000",
    font=("Poppins Medium", 20 * -1)
)

humidity_text = canvas.create_text(
    217.0,
    370.0,
    anchor="nw",
    text="57%",
    fill="#000000",
    font=("Poppins Medium", 25 * -1)
)

feels_like_text = canvas.create_text(
    392.0,
    368.0,
    anchor="nw",
    text="32ºC",
    fill="#000000",
    font=("Poppins Medium", 25 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=428.0,
    y=113.0,
    width=31.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=459.0,
    y=114.0,
    width=30.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=btn3click,
    relief="flat"
)
button_3.place(
    x=428.0,
    y=44.0,
    width=30.0,
    height=30.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    238.0,
    343.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    135.0,
    193.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    76.0,
    343.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    419.0,
    343.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()


