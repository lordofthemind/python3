def rszImg(len, wdth):
    from PIL import Image

    image = Image.open('tdrvr.png')

    print(f"Current size : {image.size}")

    rsizedImg = image.resize((len, wdth))

    rsizedImg.save('rszd_tdrvr ('+str(len)+') .jpg')

    print(f"New size : {rsizedImg.size}")

sz1 = int(input("Enter length: "))
sz2 = int(input("Enter Width: "))
rszImg(sz1, sz2)