from PIL import Image

def expand2square(path, background_color = (0, 0, 0)):
    pil_img = Image.open(path)
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

# img = Image.open("try4.jpg")
# im_new = expand2square(img, (0, 0, 0))
# im_new.save('astronaut1.png', quality=95)

