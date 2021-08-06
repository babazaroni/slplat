import math

def nb(val):  # check for not boolean.
    return not isinstance(val,bool)

def get_xy(mb):
    def set_mode(key):
        nonlocal mode
        if key in ['dir','delta','radius','length','cw','ccw','t','tangent','right','left']:
            mode = key

            return True
        return False

    set_mode("dir")

    angle = 0.0
    degree_fact = 1.0

    dir = ""

    tangent_dir = distance = radius = arc_length = delta_angle = cw = tangent_curve = curve_dir = False

    rx = []
    ry = []

    for m in mb.split():
        if set_mode(m):
            if mode == 'delta':
                angle = 0.0
                degree_fact = 1.0
            if mode == 'ccw':
                cw = -1
            if mode == 'cw':
                cw = 1

            if mode == 't' or mode == 'tangent':
                tangent_curve = 1

            if mode == 'r' or mode == 'right':
                curve_dir = 1
            if mode == 'l' or mode == 'left':
                curve_dir = -1

            continue

        try:
            val = float(m)
        except:
            if m.lower() in 'nswe':
                dir += (m.lower())
                if len(dir) == 2:
                    mode = 'distance'
                    continue
        else:

            if mode == 'dir':
                angle += val*degree_fact
                degree_fact /= 60.0
                tangent_dir = angle
            if mode == 'distance':
                distance = val
            if mode == 'delta':
                angle += val*degree_fact
                degree_fact /= 60.0
                delta_angle = angle
            if mode == 'radius':
                radius = val
            if mode == 'length':
                arc_length = val

    if nb(tangent_dir):

        if dir == 'ne':
            pass
        else:
            if dir == 'nw':
                tangent_dir = 360 - tangent_dir
            else:
                if dir == 'se':
                    tangent_dir = 180 - tangent_dir
                else:
                    if dir == 'sw':
                        tangent_dir = 180 + tangent_dir
                    else:
                        raise ValueError(mb)

        tangent_dir %= 360.0

        if nb(distance):

            x = math.sin(math.radians(tangent_dir)) * distance
            y = -math.cos(math.radians(tangent_dir)) * distance


            rx.append(x)
            ry.append(y)


    #storyofmathematics.com/circle-chord

    if nb(tangent_dir) and nb(tangent_curve) and nb(curve_dir):
        if curve_dir == 1:
            delta_angle = 90
            cw = 1
        else:
            delta_angle = 270
            cw = -1

    #print()
    #print()

    #print("tangent_curve:",tangent_curve)
    #print("curve_dir:",curve_dir)

    #print("tangent_dir",tangent_dir)
    #print("delta_angle",delta_angle)
    #print("radius:",radius)
    #print("arc_length:",arc_length)
    #print("cw:",cw)


    if nb(tangent_dir)  and nb(delta_angle) and nb(radius) and nb(arc_length) and nb(cw):
        #print("found arc dir_angle({}) delta({}) radius({}) length({})".format(tangent_dir,delta_angle,radius,arc_length))
        arc_measure = arc_length/radius  # radians
        radial_dir = math.radians( (tangent_dir + delta_angle) % 360)   # dir to center of circle
        inside_triangle_angle = math.pi/2 - arc_measure/2
        chord_direction = radial_dir + inside_triangle_angle
        chord_length = 2 * radius * math.sin(arc_measure/2)


        #print("arc_length",arc_length)
        #print("radius:",radius)
        #print("arc_measure",math.degrees(arc_length/radius))
        #print("tangent_dir:",tangent_dir)
        #print("delta_angle:",delta_angle)
        #print("radial_dir:",math.degrees(radial_dir))
        #print("inside_triangle_angle:",math.degrees(inside_triangle_angle))
        #print("chord_direction:",math.degrees(chord_direction))
        #print("chord_length:",chord_length)


        #chord direction needs debugging
    
        x = math.sin(chord_direction) * chord_length
        y = -math.cos(chord_direction) * chord_length

        #rx.append(x)
        #ry.append(y)
        #rx.append(-x)
        #ry.append(-y)


        arc_step_count = 40
        arc_step = arc_measure/arc_step_count

        #print('arc_step:',arc_step,type(arc_step))

        center_x = radius * math.sin(math.radians(radial_dir))
        center_y = radius * math.cos(math.radians(radial_dir))

        reverse_radial_dir = math.radians(180) - radial_dir
        reverse_radial_dir = radial_dir

        ref_x = radius * math.sin(reverse_radial_dir)
        ref_y = radius * math.cos(reverse_radial_dir)
    

        for i in range(arc_step_count):
            reverse_radial_dir += arc_step * cw
            x = radius * math.sin(reverse_radial_dir)
            y = radius * math.cos(reverse_radial_dir)
            rx.append(ref_x - x)
            ry.append(-(ref_y - y))
            ref_x = x
            ref_y = y

    return rx,ry


    
def get_path_points(origin,path,x_sign = 1, y_sign = 1):

    x = [origin[0]]
    y = [origin[1]]

    branches = []

    scale = 1.0 #pixels per foot

    for mb in path:

        if type(mb) is list:
 
            branches.extend (get_path_points([x[-1],y[-1]],mb,x_sign,y_sign) )

        else:

            if mb == "pob":
                x = [x[-1]]
                y = [y[-1]]
                continue

            px,py = get_xy(mb)

            for zx,zy in zip(px,py):
                x.append(x[-1] + zx * scale * x_sign)
                y.append(y[-1] + zy * scale * y_sign)



    rval = [ (x,y) ]
    rval.extend(branches)
    
    return rval

