from PIL import Image


imgs = ["1.jpg", "2.jpg", "3.jpg"]
im0 = Image.open(imgs[0])
im_others = []
for x in imgs:
    im_others.append(Image.open(x))
im0.save('out.gif', save_all=True, append_images=im_others, optimize=False, duration=200, loop=0) # 200 ms between two frames