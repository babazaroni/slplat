import math

def get_xy(mb):
    degree_fact = 1.0
    angle = 0

    parts = mb.split()
    dir = ""
    for p in parts:
        if p.isalpha():
            dir += p.lower()

        try:
            val = float(p)

            if len(dir)==1:
                angle += val*degree_fact
                degree_fact /= 60.0
            if len(dir)==2:
                distance = val

        except:
            pass

 
    x = math.sin(2*math.pi * angle/360.0) * distance
    y = math.cos(2*math.pi * angle/360.0) * distance

    if dir == 'ne':
        x = x
        y = -y
    else:
        if dir == 'nw':
            x = -x
            y = -y
        else:
            if dir == 'se':
                x = x
                y = y
            else:
                if dir == 'sw':
                    x = -x
                    y = y
                else:
                    raise ValueError(mb)

    return x,y

    
def get_path_points(origin,path,x_sign = 1, y_sign = 1):

    x = [origin[0]]
    y = [origin[1]]

    branches = []

    scale = 1.0 #pixels per foot

    for mb in path:
        if mb == "pob":
            x = [x[-1]]
            y = [y[-1]]
            continue

        if type(mb) is list:
 
            branches.extend (get_path_points([x[-1],y[-1]],mb,x_sign,y_sign) )

        else:
            px,py = get_xy(mb)
            x.append(x[-1] + px * scale * x_sign)
            y.append(y[-1] + py * scale * y_sign)


    rval = [ (x,y) ]
    rval.extend(branches)
    
    return rval


