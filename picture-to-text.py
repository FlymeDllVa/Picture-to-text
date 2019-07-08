def picture_to_text(img, spaces="    ", text=""):
    """
    Translate image to text with tabulation

    Keyword arguments:
    img -- the path to the picture (example: 1.png)
    spaces -- type of indentation between lines (default: '    ')
    text -- text at the beginning of lines (default: '')

    :return: the text from the image

    """
    import locale
    locale.setlocale(locale.LC_ALL, 'C')
    from PIL import Image
    from tesserocr import PyTessBaseAPI, RIL, image_to_text
    image = Image.open(img)
    areas = {}
    with PyTessBaseAPI() as api:
        api.SetImage(image)
        for i, (im, box, _, _) in enumerate(api.GetComponentImages(RIL.TEXTLINE, True)):
            api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
            areas[i] = {"line": api.GetUTF8Text().strip(), "confidence": api.MeanTextConf(), "x": box['x'],
                        "y": box['y'], "width": box['w'], "heigh": box['h']}
    min_x = min(areas.values(), key=lambda item: item['x'])['x']
    areas = {key: {"line": values["line"],
                   "confidence": values["confidence"],
                   "x": values["x"] - min_x,
                   "y": values["y"],
                   "width": values["width"],
                   "heigh": values["heigh"]} for key, values in areas.items()}
    if len(areas) > 1:
        min_x = sorted(areas.values(), key=lambda item: item['x'])[1]['x']
    else:
        min_x = min(areas.values(), key=lambda item: item['x'])['x']
    return "\n".join([f"{spaces * item['x']}{item['line']}" for item in {
        key: {"line": values["line"], "confidence": values["confidence"], "x": int(values["x"] / min_x),
              "y": values["y"], "width": values["width"], "heigh": values["heigh"]} for key, values in
        areas.items()}.values()])
