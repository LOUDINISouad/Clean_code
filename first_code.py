def get_area(shape: str,
             width: float = 0, 
             height: float = 0, 
             radius: float = 0) -> float:
   if shape == "circle":
       return 3.14159 * radius ** 2
   elif shape == "square":
       return width ** 2
   elif shape == "rectangle":
       return width * height
   else:
        raise ValueError