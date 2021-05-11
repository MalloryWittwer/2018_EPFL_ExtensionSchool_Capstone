import bpy
import random
 
def confetti(MatCol,r,g,b):
bpy.ops.mesh.primitive_plane_add()
bpy.ops.transform.resize(value=(.1,.1,.1))
#Resize to fit the scene
bpy.data.objects['Plane'].name = MatCol
#Rename the planes as the 1st paramater above
mat_name = MatCol
mat = bpy.data.materials.new(mat_name)
bpy.data.materials[mat_name].use_nodes = True
bpy.data.materials[mat_name].node_tree.nodes.new(type='ShaderNodeEmission')
inp = bpy.data.materials[mat_name].node_tree.nodes['Material Output'].inputs['Surface']
outp = bpy.data.materials[mat_name].node_tree.nodes['Emission'].outputs['Emission']
bpy.data.materials[mat_name].node_tree.links.new(inp,outp)
bpy.data.materials[mat_name].node_tree.nodes['Emission'].inputs[0].default_value = (r,g,b,1)
bpy.data.objects[MatCol].active_material = bpy.data.materials[mat_name]
#Run a loop 100 times
for index in range(100):
bpy.ops.object.select_all(action='DESELECT')
#If you don't deslect the other objects, the results are real weird
bpy.data.objects[MatCol].select = True
x=random.uniform(-10,10)
y=random.uniform(-10,10)
z=random.uniform(-10,10)
#Randomize some variables to plug into the location parameter
bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={&quot;linked&quot;:False,&quot;mode&quot;:'TRANSLATION'}, TRANSFORM_OT_translate={&quot;value&quot;:(x,y,z)})
#Duplicate the object and keep it unlinked
 
confetti(&quot;YellowMat&quot;, 1, 1, 0)
confetti(&quot;GreenMat&quot;, 0, 1, 0)
confetti(&quot;RedMat&quot;, 1, 0, 0)
confetti(&quot;BlueMat&quot;, 0, 0, 1)
