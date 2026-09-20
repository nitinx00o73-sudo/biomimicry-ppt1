import bpy, math
from mathutils import Vector

# GAME DESIGN 1 — procedural apartment asset generator
# Run in Blender's Scripting workspace. It builds the same floor-plan-inspired
# apartment as the browser prototype and saves a .blend file.

bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)

def mat(name, color, rough=.65, metal=0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.roughness=rough; m.metallic=metal; return m
floor=mat('Warm Oak',(0.52,.31,.14),.8); wall=mat('Paint',(0.75,.78,.80),.8)
wood=mat('Wood',(0.28,.12,.045),.65); fabric=mat('Sofa Fabric',(0.02,.48,.62),.6)
white=mat('Beds',(0.9,.92,.94),.7); metal=mat('Metal',(.12,.15,.18),.35,.5)

def cube(name, loc, scale, material, bevel=0.04):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.object; o.name=name; o.scale=(scale[0]/2,scale[1]/2,scale[2]/2); bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if material:o.data.materials.append(material)
    if bevel:
        mod=o.modifiers.new('Soft edges','BEVEL');mod.width=bevel;mod.segments=3
    return o

cube('Floor',(0,0,0),(30,18,.2),floor)
for loc,sc in [((0,-9,1.5),(30,.3,3)),((0,9,1.5),(30,.3,3)),((-15,0,1.5),(.3,18,3)),((15,0,1.5),(.3,18,3)),
               ((-5,-6,1.5),(.25,6,3)),((5,-6,1.5),(.25,6,3)),((0,-2.6,1.5),(10,.25,3)),
               ((8,2.4,1.5),(4,.25,3)),((8,6,1.5),(4,.25,3)),((6,4.2,1.5),(.25,3.6,3)),
               ((-9,2.5,1.5),(12,.25,3)),((-5,5.6,1.5),(.25,6.2,3)),((0,5.6,1.5),(.25,6.2,3))]:
    cube('Wall',loc,sc,wall)

def bed(x,z):
    cube('Bed',(x, z, .45),(2.2,3,.6),white)
    cube('Blanket',(x+.3,z-.25,.82),(1.5,1.5,.12),fabric)
    cube('Pillow',(x-.55,z-1.05,.82),(.9,.55,.22),white)

bed(-8,-6.8);bed(8,-6.8);bed(11,6.8)
cube('Sofa',(0,2,.65),(4.8,1,.8),fabric);cube('SofaSide',(-1.9,3.3,.65),(1,2.4,.8),fabric)
cube('CoffeeTable',(0,-.2,.42),(2.2,1.1,.5),wood)
cube('DiningTable',(-8,-1,.75),(3.1,1.6,.75),wood)
for x in (-9,-7):cube('Chair',(x,-2.4,.7),(.65,.65,.7),wood)
for x,z in ((-11,1),(-11,2.5),(-8,4.2)):cube('KitchenCounter',(x,z,.9),(5,.65,.9),wood)
cube('TV',(3.7,-.2,1.8),(.18,3,2),metal)
for x,z in ((-3.8,-6.8),(3.8,-6.8),(11,4.8)):cube('Wardrobe',(x,z,1.1),(1.3,2.3,2.2),wood)

# Warm area lights
for x,z in ((-9,0),(0,1),(8,0),(11,6)):
    bpy.ops.object.light_add(type='AREA', location=(x,0,2.8));l=bpy.context.object;l.data.energy=550;l.data.shape='DISK';l.data.size=4
    l.data.color=(1.0,.72,.42)

# Camera preview
bpy.ops.object.camera_add(location=(20,-22,22));cam=bpy.context.object; bpy.context.scene.camera=cam
def point(obj, target):
    direction=Vector(target)-obj.location;obj.rotation_euler=direction.to_track_quat('-Z','Y').to_euler()
point(cam,(0,0,0));cam.data.lens=42

bpy.context.scene.render.engine='BLENDER_EEVEE_NEXT'
bpy.context.scene.render.resolution_x=1280;bpy.context.scene.render.resolution_y=720;bpy.context.scene.render.resolution_percentage=100
bpy.ops.wm.save_as_mainfile(filepath='GameDesign1_Apartment.blend')
print('Game Design 1 Blender scene generated.')
