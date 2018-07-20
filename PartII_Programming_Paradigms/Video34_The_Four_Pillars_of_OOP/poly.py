# https://gist.github.com/calthoff/3d04ec8427e202c6430975956b4a4f19


shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
         a_shape.draw_circle()
