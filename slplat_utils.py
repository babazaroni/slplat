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
            y = math.cos(math.radians(tangent_dir)) * distance

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



        degrees_per_step = 15.0
        arc_step_count = round(math.degrees(arc_measure)/degrees_per_step) + 1 # so you get at least 1
        arc_step = arc_measure/arc_step_count

        #print('arc_step:',arc_step,type(arc_step))


        ref_x = radius * math.sin(radial_dir)
        ref_y = radius * math.cos(radial_dir)
    

        for i in range(arc_step_count):
            radial_dir += arc_step * cw
            x = radius * math.sin(radial_dir)
            y = radius * math.cos(radial_dir)
            rx.append(ref_x - x)
 #           ry.append(-(ref_y - y))
            ry.append(ref_y - y)
            ref_x = x
            ref_y = y

    return rx,ry


    
def get_path_points(origin,path):

    x = [origin[0]]
    y = [origin[1]]

    branches = []

    scale = 1.0 #pixels per foot

    property_sets = []
    segment_sets = []

    property_set = {'ls': 'solid','color':'black'}

    for mb in path:

        if type(mb) is list:
 
            branch_segments,branch_property_sets = get_path_points([x[-1],y[-1]],mb) 

            segment_sets.extend(branch_segments)
            property_sets.extend(branch_property_sets)

        if type(mb) is dict:
            segment_sets.append({'x':x,'y':y})
            property_sets.append(property_set)

            x = [x[-1]]
            y = [y[-1]]

            property_set = property_set.copy()

            for key in mb.keys():
                property_set[key] = mb[key]

        if type(mb) is str:

            if mb == "pob":
                x = [x[-1]]
                y = [y[-1]]
                continue

            px,py = get_xy(mb)

            for zx,zy in zip(px,py):
                x.append(x[-1] + zx * scale)
                y.append(y[-1] + zy * scale)

    segment_sets.append({'x':x,'y':y})
    property_sets.append(property_set)

    return segment_sets,property_sets

def get_as_mb(segments):
    """Convert points back to metes and bounds
    """

    ref_x = 0.0
    ref_y = 0.0

    mbs = []
    
    for segment in segments:

        xa = segment['x']
        ya = segment['y']

        for x,y in zip(xa,ya):

            if x==0 and y==0:
                continue

            dx = x - ref_x
            dy = y - ref_y

            mb = ""

            if dx == 0:
                if dy >= 0:
                    mb = 'n 0 e {}'.format(dy)
                else:
                    mb = 's 0 w {}'.format(-dy)
            else:
                if dy == 0:
                    if dx >= 0:
                        mb = 'n 90 e {}'.format(dx)
                    else:
                        mb = 'n 90 w {}'.format(-dx)
                else:

                    ang = math.degrees(math.atan(dx/dy))
                    ang = round(ang,10)

                    if dy >= 0:
                        mb = "n {}".format(abs(ang))
                        if dx >= 0:
                            mb += " e"
                        else:
                            mb += " w"
                    else:
                        mb = "s {}".format(abs(ang))
                        if dx >= 0:
                            mb += " e"
                        else:
                            mb += " w"

            length = math.sqrt(dx**2 + dy**2)
            length = round(length,10)

            mb += " {}".format(length)
 
            ref_x = x
            ref_y = y

            mbs.append(mb)
    
    return mbs




def last_point(segments):
    seg = segments[-1]
    return [seg['x'][-1],seg['y'][-1]]

class plot_info():
    def __init__(self,text,origin,path,aux_info = None):
        self.text = text
        self.origin = origin
        self.path = path
        self.selected = False
        self.aux_info = aux_info


