from circle import Circle
from rectangle import Rectangle
if __name__=="__main__":
    c1=Circle("Orange",12)
    c2=c1.clone()
    c2.r=18
    c1.display()
    c2.display()