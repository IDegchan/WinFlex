import requests
from PIL import Image
from io import BytesIO
import dearpygui.dearpygui as dpg

window_width = 1000
window_height = 800

directory = __file__.replace("gui.py", "")
font = directory + "fonts/pixel.ttf"

dpg.create_context()

dpg.create_viewport(title="YouTube Client", decorated=False)
dpg.configure_viewport(0, x_pos=400, y_pos=75, width=window_width, height=window_height)
dpg.set_viewport_max_height(window_height)
dpg.set_viewport_max_width(window_width)

with dpg.font_registry():
    with dpg.font(font, 20, default_font=True, tag="Default") as f:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
    custom_font = dpg.add_font(file=font, size=50)

def load_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        return Image.open(image_data)
    else:
        raise Exception(response.status_code)

def open_search_window():
    dpg.configure_item("main", show=False)
    dpg.configure_item("search_window", show=True)
    dpg.set_primary_window(search_window, value=True)

def open_main_window():
    dpg.configure_item("main", show=True)
    dpg.configure_item("search_window", show=False)
    dpg.set_primary_window(main_window, value=True)

def search():
    dpg.configure_item("main", show=False)
    dpg.configure_item("search_window", show=False)
    #dpg.configure_item("answer", show=True)
    dpg.set_primary_window(main_window, value=True)

    yt = YouTube()
    value = dpg.get_value("search")
    results = yt.search(value)

    #load thumbnails
    for i in results:
        video = results[i]

        url = video["thumbnail"]
        image = load_image_from_url(url)

        image = image.convert("RGBA")
        width, height = image.size
        image_data = image.tobytes()

        with dpg.texture_registry():
            dpg.add_static_texture(width, height, image_data, tag=i)
    

    
    print(results)

with dpg.window(no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, show=False, tag="search_window") as search_window:
    with dpg.group(horizontal=True):
        title = dpg.add_text(
            default_value="Search",
            pos=[window_width // 2 - 110, window_height // 2 - 100]
        )
        dpg.bind_item_font(title, custom_font)

    with dpg.group(horizontal=True, pos=[window_width // 3.5 - 150, window_height //2 + 18]): 
        btn = dpg.add_button(label="Назад", callback=open_main_window)
        question = dpg.add_input_text(width=550, tag="search")
        btn = dpg.add_button(label="Знайти", callback=search)
        #img = dpg.add_image_button()

with dpg.window(no_collapse=True, no_resize=True, no_close=True,
                no_title_bar=True, tag="main") as main_window:
    with dpg.group(horizontal=True):
        title = dpg.add_text(
            default_value="YouTube Client",
            pos=[window_width // 2 - 210, window_height // 2 - 100]
        )
        dpg.bind_item_font(title, custom_font)

    with dpg.group(horizontal=True, pos=[window_width // 2 - 125, window_height //2 + 18]): 
        btn = dpg.add_button(label="Пошук", callback=open_search_window)

dpg.bind_font("Default")
dpg.set_primary_window(window=main_window, value=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()