def greet(fx):
  def mfx(*args, **kwargs):
    print ("the function is about to start")
    result=fx(*args,**kwargs)
    print ("the function has been Ended")
    return result
  return mfx

def area_of_square(a,b):
  return (float(a)*float(b))

def area_of_circle(r):
  return (3.14*float(r)*float(r))

def area_of_triangle(b,h):
  return (0.5*float(b)*float(h))
@greet
def area_calculator():
  print ("I can provide you the are of 3 shapes Circle, Square, Triangle")
  shape=input("type the shape you want to take area of:  ").lower()
  if shape=="square":
    side=input("Enter the one side of square: ")
    print("the area of square is:", area_of_square(side,side))
  elif shape=="circle":
    r=input("Enter the radius of circle: ")
    print ("the area of the circle is:",area_of_circle(r))
  elif shape=="triangle":
    b=input("Enter the base of triangle: ")
    h=input("Enter the height of triangle: ")
    print ("the area of the triangle is:",area_of_triangle(b,h))
  else:
    print("please enter a valid shape")

area_calculator()