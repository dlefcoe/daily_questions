from ursina import (
    Ursina, 
    Entity, 
    EditorCamera, 
    color, 
    curve, 
    invoke, 
    scene, 
    Text
)

# Initialize the engine
app = Ursina()

# Position the camera to look down at an angle
editor_cam = EditorCamera()
editor_cam.rotation_x = 30   # Tilt down
editor_cam.rotation_y = -45  # Angle to see Top, Front, Right

# Standard Rubik's Cube colors
COLOR_MAP = {
    'U': color.white,    # Top
    'D': color.yellow,   # Bottom
    'F': color.green,    # Front
    'B': color.blue,     # Back
    'L': color.orange,   # Left
    'R': color.red,      # Right
    'internal': color.black
}

cubies = []

# Generate the 26 cubies out of solid, unlit geometry to avoid rendering bugs
for x in (-1, 0, 1):
    for y in (-1, 0, 1):
        for z in (-1, 0, 1):
            if (x, y, z) == (0, 0, 0):
                continue  # Skip the core
            
            # Create an invisible center point for this cubie to act as a parent
            cubie = Entity(position=(x, y, z))
            
            # Determine face colors based on physical position on the cube
            up_color    = COLOR_MAP['U'] if y == 1 else COLOR_MAP['internal']
            down_color  = COLOR_MAP['D'] if y == -1 else COLOR_MAP['internal']
            right_color = COLOR_MAP['R'] if x == 1 else COLOR_MAP['internal']
            left_color  = COLOR_MAP['L'] if x == -1 else COLOR_MAP['internal']
            front_color = COLOR_MAP['F'] if z == 1 else COLOR_MAP['internal']
            back_color  = COLOR_MAP['B'] if z == -1 else COLOR_MAP['internal']

            # Build the cubie out of 6 thin 3D boxes
            sticker_thickness = 0.05
            box_scale = 0.92  # Leaves a nice clean gap between cubies
            
            # Top Face (U)
            Entity(parent=cubie, model='cube', color=up_color, 
                   scale=(box_scale, sticker_thickness, box_scale), 
                   position=(0, 0.5, 0), unlit=True)
            
            # Bottom Face (D)
            Entity(parent=cubie, model='cube', color=down_color, 
                   scale=(box_scale, sticker_thickness, box_scale), 
                   position=(0, -0.5, 0), unlit=True)
            
            # Right Face (R)
            Entity(parent=cubie, model='cube', color=right_color, 
                   scale=(sticker_thickness, box_scale, box_scale), 
                   position=(0.5, 0, 0), unlit=True)
            
            # Left Face (L)
            Entity(parent=cubie, model='cube', color=left_color, 
                   scale=(sticker_thickness, box_scale, box_scale), 
                   position=(-0.5, 0, 0), unlit=True)
            
            # Front Face (F)
            Entity(parent=cubie, model='cube', color=front_color, 
                   scale=(box_scale, box_scale, sticker_thickness), 
                   position=(0, 0, 0.5), unlit=True)
            
            # Back Face (B)
            Entity(parent=cubie, model='cube', color=back_color, 
                   scale=(box_scale, box_scale, sticker_thickness), 
                   position=(0, 0, -0.5), unlit=True)
            
            cubies.append(cubie)

# Rotation logic
rotation_helper = Entity()
turning = False

def rotate_side(axis, slice_value, angle):
    global turning
    if turning:
        return
    turning = True
    
    rotation_helper.rotation = (0, 0, 0)
    
    for c in cubies:
        pos = [round(c.world_position.x), round(c.world_position.y), round(c.world_position.z)]
        target_val = pos[0] if axis == 'x' else pos[1] if axis == 'y' else pos[2]
        
        if target_val == slice_value:
            c.parent = rotation_helper
            
    if axis == 'x':
        rotation_helper.animate_rotation_x(angle, duration=0.2, curve=curve.linear)
    elif axis == 'y':
        rotation_helper.animate_rotation_y(angle, duration=0.2, curve=curve.linear)
    elif axis == 'z':
        rotation_helper.animate_rotation_z(angle, duration=0.2, curve=curve.linear)
        
    invoke(reset_parents, delay=0.22)

def reset_parents():
    global turning
    for c in cubies:
        if c.parent == rotation_helper:
            c.world_parent = scene
    turning = False

# Keyboard input mapping
def input(key):
    # --- CLOCKWISE MOVES (Lowercase) ---
    if key == 'r': rotate_side('x', 1, 90)     # Right
    if key == 'l': rotate_side('x', -1, -90)   # Left
    if key == 'u': rotate_side('y', 1, 90)     # Up
    if key == 'd': rotate_side('y', -1, -90)   # Down
    if key == 'f': rotate_side('z', 1, 90)     # Front
    if key == 'b': rotate_side('z', -1, -90)   # Back

    # --- COUNTER-CLOCKWISE MOVES (Uppercase / Shift) ---
    if key == 'R': rotate_side('x', 1, -90)    # Right Prime (R')
    if key == 'L': rotate_side('x', -1, 90)    # Left Prime (L')
    if key == 'U': rotate_side('y', 1, -90)    # Up Prime (U')
    if key == 'D': rotate_side('y', -1, 90)    # Down Prime (D')
    if key == 'F': rotate_side('z', 1, -90)    # Front Prime (F')
    if key == 'B': rotate_side('z', -1, 90)    # Back Prime (B')

# On-screen HUD guide
Text(
    text="Right-Click + Drag to Rotate Camera\n"
         "Clockwise: r, l, u, d, f, b\n"
         "Counter-Clockwise: Shift + (R, L, U, D, F, B)", 
    position=(-0.85, 0.45), 
    scale=1.2
)

app.run()