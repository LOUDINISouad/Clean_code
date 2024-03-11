def get_display_image(article: dict, watermark: str) -> str:
    image = None
    if 'image' in article and 'displayImage' in article and article['displayImage']:
        if watermark:
            image = apply_watermark(article['image'], watermark)
        else:
            image = article['image']
    return image

def apply_watermark(image: str, watermark: str) -> str:
    # Placeholder for watermark application logic
    return f"{image} with {watermark}"
