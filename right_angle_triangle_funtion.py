#right angle triangle
def right_angle_triangle(num):
    right_angle_triangle_form = '' 
    for row in range(abs(num) + 1):
        print("#" * row)
    return right_angle_triangle_form
triangle =right_angle_triangle(2)
print(triangle)