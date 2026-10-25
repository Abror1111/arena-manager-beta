"""Original carved, curved architectural assemblies for 1.32. No source game meshes."""
import bpy,bmesh,math,json,ast,hashlib,random
from pathlib import Path
from mathutils import Vector,Matrix
R=Path(__file__).resolve().parents[1];OUT=R/'public/environment132';OUT.mkdir(exist_ok=True);bpy.ops.wm.read_factory_settings(use_empty=True)
M={};objects=[];records=[]
for name,c in {'wall':(.78,.74,.64,1),'stone':(.70,.71,.64,1),'roof':(.64,.37,.23,1),'metal':(.38,.49,.51,1),'steel':(.43,.51,.54,1),'glass':(.15,.31,.39,1),'wood':(.43,.29,.17,1),'leaf':(.32,.48,.22,1),'bark':(.35,.27,.17,1)}.items():
 m=bpy.data.materials.new(name);m.use_nodes=True;m['arenaRole']=name;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=c;p.inputs['Roughness'].default_value=.43 if name in['metal','steel','glass']else .82;m.diffuse_color=c;M[name]=m

def mesh(name,verts,faces,role):
 data=bpy.data.meshes.new(name);data.from_pydata(verts,[],faces);data.materials.append(M[role]);data.update();o=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(o);objects.append(o);return o

def bevel(o,w=.025):
 bm=bmesh.new();bm.from_mesh(o.data);edges=[e for e in bm.edges if e.is_manifold and e.calc_face_angle(0)>.35]
 if edges:bmesh.ops.bevel(bm,geom=edges,offset=w,segments=2,affect='EDGES',clamp_overlap=True)
 bmesh.ops.recalc_face_normals(bm,faces=bm.faces);bm.to_mesh(o.data);bm.free();return o

def box(x,y,z,w,d,h,role='stone',edge=.025):
 v=[(sx*w/2,sy*d/2,sz*h/2)for sz in[-1,1]for sx,sy in[(-1,-1),(1,-1),(1,1),(-1,1)]];o=mesh('crafted_'+role,v,[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)],role);o.location=(x,y,z)
 return bevel(o,min(edge,min(w,d,h)*.18))if edge else o

def turned(x,y,z,profile,role='metal',segments=32):
 v=[]
 for rad,zz in profile:
  for i in range(segments):a=i*math.tau/segments;v.append((x+rad*math.cos(a),y+rad*math.sin(a),z+zz))
 faces=[]
 for j in range(len(profile)-1):
  for i in range(segments):a=j*segments+i;b=j*segments+(i+1)%segments;faces.append((a,b,b+segments,a+segments))
 faces.extend([tuple(reversed(range(segments))),tuple((len(profile)-1)*segments+i for i in range(segments))]);o=mesh('lathed_profile',v,faces,role)
 for p in o.data.polygons:p.use_smooth=len(p.vertices)==4
 return o

def tube(points,r=.025,role='metal',segments=9):
 v=[]
 for i,p in enumerate(points):
  p=Vector(p);t=(Vector(points[min(i+1,len(points)-1)])-Vector(points[max(0,i-1)])).normalized();u=t.cross(Vector((0,0,1)))
  if u.length<.01:u=t.cross(Vector((0,1,0)))
  u.normalize();b=t.cross(u).normalized()
  for j in range(segments):v.append(tuple(p+r*(u*math.cos(j*math.tau/segments)+b*math.sin(j*math.tau/segments))))
 f=[]
 for i in range(len(points)-1):
  for j in range(segments):a=i*segments+j;b=i*segments+(j+1)%segments;f.append((a,b,b+segments,a+segments))
 f.extend([tuple(reversed(range(segments))),tuple((len(points)-1)*segments+j for j in range(segments))]);return mesh('bent_closed_pipe',v,f,role)

def arch(x,y,z,r=.65,h=.95,depth=.14):
 for i in range(13):
  a=i*math.pi/13+.012;b=(i+1)*math.pi/13-.012;v=[]
  for yy in[-depth/2,depth/2]:
   for rad,t in[(r,a),(r,b),(r+.15,b),(r+.15,a)]:v.append((x+rad*math.cos(t),y+yy,z+h+rad*math.sin(t)))
  bevel(mesh('carved_arch_stone',v,[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)],'stone'),.012)
 for side in[-1,1]:
  for j in range(5):box(x+side*(r+.075),y,z+(j+.5)*h/5,.15,depth,h/5-.014,'stone',.014)

def canopy_leaves(x,y,z,s=1):
 for i in range(10):
  angle=i*2.399;v=[]
  for j in range(9):
   t=j/8;length=.64*s;wide=math.sin(t*math.pi)*.09*s;px=x+math.cos(angle)*length*t;py=y+math.sin(angle)*length*t;zz=z+.32*s*math.sin(t*2.7)
   v.extend([(px-math.sin(angle)*wide,py+math.cos(angle)*wide,zz),(px,py,zz+.025*s),(px+math.sin(angle)*wide,py-math.cos(angle)*wide,zz)])
  mesh('folded_curved_leaf',v,[(j*3+k,j*3+k+1,(j+1)*3+k+1,(j+1)*3+k)for j in range(8)for k in[0,1]],'leaf')

def ventilation():
 box(0,0,.12,1.4,1.15,.24,'steel');box(0,0,.47,1.22,.97,.6,'metal',.045)
 for side in[-1,1]:
  for j in range(13):o=box(-.53+j*.088,side*.5,.46,.035,.055,.43,'steel',.009);o.rotation_euler[0]=side*.2
 turned(0,0,.78,[(.36,0),(.4,.045),(.4,.08),(.34,.095)],'steel')
 for j in range(9):
  a=j*math.tau/9;v=[(.04*math.cos(a),.04*math.sin(a),.88),(.31*math.cos(a+.21),.31*math.sin(a+.21),.89),(.32*math.cos(a+.49),.32*math.sin(a+.49),.91),(.11*math.cos(a+.43),.11*math.sin(a+.43),.93)];mesh('twisted_fan_blade',v,[(0,1,2,3)],'metal')
 turned(0,0,.86,[(.10,0),(.09,.1)],'metal',20)
 for x in[-.46,.46]:tube([(x,.38,.63),(x,.58,.63),(x,.66,.45),(x,.66,.14)],.045,'metal')
 for x in[-.62,.62]:
  for y in[-.46,.46]:turned(x,y,.74,[(.025,0),(.025,.025)],'steel',8)

def dome():
 turned(0,0,0,[(.70,0),(.74,.07),(.64,.14),(.64,.38),(.70,.42),(.70,.49),(.67,.57),(.59,.73),(.44,.92),(.24,1.08),(.065,1.15),(.02,1.17)],'stone',40)
 for i in range(16):
  a=i*math.tau/16;tube([(.69*math.cos(a),.69*math.sin(a),.48),(.57*math.cos(a),.57*math.sin(a),.76),(.28*math.cos(a),.28*math.sin(a),1.06),(.04*math.cos(a),.04*math.sin(a),1.18)],.014,'metal',6)
 turned(0,0,1.15,[(.07,0),(.07,.06),(.02,.14),(.025,.31),(.005,.39)],'metal',20)
 for i in range(8):a=i*math.tau/8;box(.645*math.cos(a),.645*math.sin(a),.27,.10,.10,.16,'glass',.015)

def chimney():
 for j in range(7):
  for x in[-.19,.19]:box(x,0,.08+j*.14,.365,.61,.125,'wall',.012)
 box(0,0,1.05,.87,.79,.12,'stone')
 for x in[-.32,.32]:box(x,0,1.22,.11,.71,.27,'stone')
 # Curved cap with a sealed underside and ridge ribs.
 turned(0,0,1.2,[(.36,0),(.35,.12),(.28,.24),(.04,.33)],'roof',24);tube([(0,-.33,1.42),(0,.33,1.42)],.045,'roof')

def carved_lintel():
 arch(0,0,0,.61,.84,.12);box(0,-.045,.73,1.15,.055,1.4,'wood',.015)
 for i in range(10):box(-.51+i*.113,.0,.67,.025,.03,1.24,'metal',.005)
 for z in[.22,.71,1.11]:box(0,.025,z,1.13,.03,.025,'metal',.004)
 box(0,0,1.63,.3,.18,.22,'stone',.03)
 for side in[-1,1]:
  turned(side*.71,0,0,[(.13,0),(.13,.10),(.10,.14),(.08,.74),(.12,.81),(.12,.88)],'stone',16)
 box(0,0,.02,1.6,.21,.06,'stone')

def dish():
 turned(0,0,0,[(.41,0),(.43,.10),(.28,.18)],'metal',24);tube([(0,0,.13),(0,0,.6),(.12,0,.82)],.07,'steel',12)
 # Double-surface paraboloid and continuous rim.
 v=[];rings=8;segments=32
 for back in[0,1]:
  for j in range(rings+1):
   rad=max(.012,j/rings*.63)
   for i in range(segments):a=i*math.tau/segments;v.append((rad*math.cos(a),rad*math.sin(a),.78+rad*rad*.8-back*.035))
 f=[];count=(rings+1)*segments
 for back in[0,1]:
  for j in range(rings):
   for i in range(segments):a=back*count+j*segments+i;b=back*count+j*segments+(i+1)%segments;f.append((a,b,b+segments,a+segments))
 for i in range(segments):a=rings*segments+i;b=rings*segments+(i+1)%segments;f.append((a,b,b+count,a+count))
 o=mesh('parabolic_receiver',v,f,'metal')
 for p in o.data.polygons:p.use_smooth=True
 for a in[0,2.1,4.2]:tube([(.59*math.cos(a),.59*math.sin(a),1.07),(.11*math.cos(a),.11*math.sin(a),1.3),(0,0,1.31)],.018,'steel',7)
 turned(0,0,1.24,[(.07,0),(.075,.14)],'steel',16)

def buttress():
 for z,r in[(0,.54),(.14,.47),(.27,.39),(.42,.33),(1.24,.33),(1.36,.42),(1.49,.49)]:turned(0,0,z,[(r,0),(r,.11)],'stone',16)
 for i in range(16):a=i*math.tau/16;tube([(.32*math.cos(a),.32*math.sin(a),.5),(.32*math.cos(a),.32*math.sin(a),1.25)],.035,'stone',7)
 box(0,0,1.64,1.04,.88,.19,'stone',.045);canopy_leaves(.24,.15,1.72,.65)

def balcony():
 box(0,-.005,.86,1.8,.36,.12,'stone');arch(0,-.04,.4,.55,.62,.10);box(0,-.05,1.18,1.02,.045,.8,'glass',.008)
 for i in range(13):tube([(-.84+i*.14,.18,.94),(-.84+i*.14,.18,1.33)],.012,'metal',7)
 tube([(-.88,.18,1.35),(.88,.18,1.35)],.02,'metal',8)
 for x in[-.87,.87]:tube([(x,.18,1.35),(x,-.10,1.35)],.018,'metal',8)
 for i in range(8):
  x=-.86+i*.246;tube([(x,-.11,1.9),(x,.09,1.89),(x,.22,1.75)],.012,'metal',7)
 v=[(-.9,-.11,1.9),(.9,-.11,1.9),(-.9,.24,1.74),(.9,.24,1.74)];mesh('curved_awning',v,[(0,1,3,2)],'roof')

def rock_cluster():
 rng=random.Random(132)
 for x,y,s in[(-.36,0,.6),(.3,.2,.45),(.10,-.36,.34)]:
  data=bpy.data.meshes.new('weathered_stone');bm=bmesh.new();bmesh.ops.create_icosphere(bm,subdivisions=2,radius=s)
  for v in bm.verts:
   v.co*=.85+rng.random()*.26;v.co.x+=x;v.co.y+=y;v.co.z=v.co.z*.7+s*.72
  bm.to_mesh(data);bm.free();data.materials.append(M['stone']);o=bpy.data.objects.new('eroded_sculpted_rock',data);bpy.context.collection.objects.link(o);objects.append(o)
 canopy_leaves(-.3,.2,.06,.6)

def fern_patch():
 tube([(0,0,0),(0,0,.21)],.055,'bark',8);canopy_leaves(0,0,.12,1.4)
 for i in range(6):
  a=i*math.tau/6;axis=(math.cos(a),math.sin(a))
  for j in range(7):
   t=(j+.5)/8;x=axis[0]*t*.65;y=axis[1]*t*.65;z=.13+math.sin(t*2.4)*.25
   for side in[-1,1]:
    leaf=[(x,y,z),(x-axis[1]*side*.12*(1-t)+axis[0]*.08,y+axis[0]*side*.12*(1-t)+axis[1]*.08,z+.025),(x+axis[0]*.13,y+axis[1]*.13,z-.015)];mesh('fern_leaflet',leaf,[(0,1,2)],'leaf')

def roof_arcade():
 for x in[-.85,.85]:
  for y in[-.48,.48]:turned(x,y,0,[(.23,0),(.25,.10),(.18,.17),(.13,1.18),(.24,1.24),(.24,1.33)],'stone',20)
 for y in[-.48,.48]:arch(0,y,.43,.72,.50,.18)
 box(0,0,1.72,2.14,1.35,.16,'stone',.04)
 for i in range(9):box(-.98+i*.245,0,1.86,.17,1.38,.14,'roof',.025)
 for side in[-1,1]:canopy_leaves(side*.72,0,1.9,.6)

def steel_truss():
 for y in[-.3,.3]:
  for z in[.12,.72]:tube([(-1.25,y,z),(1.25,y,z)],.035,'steel',8)
  for i in range(10):
   x=-1.25+i*.25;tube([(x,y,.12),(x+.25,y,.72)],.025,'metal',7);tube([(x,y,.72),(x+.25,y,.12)],.025,'metal',7)
 for x in[-1.25,1.25]:
  for y in[-.3,.3]:tube([(x,y,0),(x,y,.76)],.065,'metal',10)
 for x in[-1,0,1]:tube([(x,-.3,.72),(x,.3,.72)],.025,'steel',7)

def skyline_tower():
 for j in range(3):
  w=2.4-j*.38;d=1.9-j*.24;base=j*2.4;box(0,0,base+1.2,w,d,2.4,'wall',.07)
  for floor in range(4):
   z=base+.45+floor*.56;box(0,0,z,w+.04,d+.04,.06,'metal',.012)
   for side in[-1,1]:
    for k in range(5):box(-w/2+.22+k*(w-.44)/4,side*(d/2+.018),z+.22,.24,.035,.32,'glass',.01)
    for k in range(3):box(side*(w/2+.018),-d/2+.23+k*(d-.46)/2,z+.22,.035,.27,.32,'glass',.01)
 turned(0,0,7.24,[(.3,0),(.2,.3),(.025,.37),(.025,1.4)],'metal',16)

names=['ventilation','dome','chimney','carved_lintel','dish','buttress','balcony','rock_cluster','fern_patch','roof_arcade','steel_truss','skyline_tower'];roots=[]
for i,name in enumerate(names):
 objects=[];globals()[name]();verts=[];faces=[];roles=[];polyroles=[]
 for o in objects:
  o.data.calc_loop_triangles();matrix=o.matrix_world;offset=len(verts);verts.extend(tuple(matrix@v.co)for v in o.data.vertices);role=o.data.materials[0].name
  if role not in roles:roles.append(role)
  for t in o.data.loop_triangles:faces.append(tuple(offset+j for j in t.vertices));polyroles.append(roles.index(role))
 data=bpy.data.meshes.new(name);data.from_pydata(verts,[],faces);data.update()
 for role in roles:data.materials.append(M[role])
 uv=data.uv_layers.new(name='crafted_uv')
 for poly,index in zip(data.polygons,polyroles):
  poly.material_index=index;axis=max(range(3),key=lambda a:abs(poly.normal[a]));dims=[a for a in range(3)if a!=axis]
  for li in poly.loop_indices:v=data.vertices[data.loops[li].vertex_index].co;uv.data[li].uv=(v[dims[0]]*.6,v[dims[1]]*.6)
 root=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(root);root.location=(i*7,0,0);root['arenaCraftedModel']=name;root['arenaOrigin']='ARENA curved and carved architecture 132';roots.append(root)
 records.append({'id':name,'node':name,'catalog':[i*7,0,0],'triangles':len(faces),'footprintRadius':max(math.hypot(v[0],v[1])for v in verts),'bounds':[min(v[0]for v in verts),min(v[2]for v in verts),min(-v[1]for v in verts),max(v[0]for v in verts),max(v[2]for v in verts),max(-v[1]for v in verts)]})
 data_old={o.data for o in objects};bpy.data.batch_remove(ids=set(objects));bpy.data.batch_remove(ids={d for d in data_old if d.users==0});print('CRAFTED',name,len(faces),flush=True)
bpy.context.preferences.filepaths.save_version=0;bpy.ops.wm.save_as_mainfile(filepath='/workspace/shared/ARENA-crafted-132.blend',compress=True)
p=OUT/'crafted.glb';bpy.ops.export_scene.gltf(filepath=str(p),export_format='GLB',export_animations=False,export_cameras=False,export_extras=True)
m={'origin':'Original ARENA sculpted and assembled geometry','models':records,'library':{'url':'/environment132/crafted.glb','localUrl':'/environment132/crafted.glb','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}}
(R/'src/environment132-kit.json').write_text(json.dumps(m,indent=2)+'\n')
