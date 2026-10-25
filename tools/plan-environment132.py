"""Safe decoration anchors from ARENA's own 1.31 architectural plans."""
from pathlib import Path
from shapely import Polygon,box,Point
import json,math,random
R=Path(__file__).resolve().parents[1];maps={}
families={'dust2':'desert','mirage':'desert','inferno':'clay','nuke':'industry','train':'industry','ancient':'jungle','ancient-night':'jungle','anubis':'river','overpass':'city','vertigo':'city','cache':'city'}
roof_types={'desert':['dome','ventilation','dish','roof_arcade'],'clay':['chimney','chimney','dish'],'industry':['ventilation','steel_truss','dish'],'jungle':['buttress','roof_arcade'],'river':['dome','roof_arcade','buttress'],'city':['ventilation','dish','steel_truss']}
radii={'dome':.86,'ventilation':.81,'dish':.85,'chimney':.56,'buttress':.7,'roof_arcade':1.35,'steel_truss':1.45}
kit=json.loads((R/'src/environment132-kit.json').read_text());radii.update({m['id']:m['footprintRadius']+.035 for m in kit['models']})
for n,(id,family)in enumerate(families.items()):
 p=json.loads((Path('/workspace/.arena-tools/rebuilt131-plans')/(id+'.json')).read_text());rng=random.Random(132+n);roofs=[];facades=[]
 for i,plot in enumerate(p['plots']):
  if plot['kind']!='building'or i==p['landmark']['plot']:continue
  poly=Polygon(plot['outer'],plot['holes']);c=poly.representative_point()
  if not plot.get('assembly')and len(roofs)<26:
   kind=rng.choice(roof_types[family]);radius=radii[kind]
   for scale in[1,.8,.62]:
    if poly.covers(box(c.x-radius*scale,c.y-radius*scale,c.x+radius*scale,c.y+radius*scale)):
     y=plot['base']+plot['height']+.085;roofs.append({'kind':kind,'x':round(c.x,4),'z':round(c.y,4),'y':round(y,4),'scale':scale,'yaw':round(rng.random()*math.tau,4),'plot':i,'radius':radius*scale});break
  if plot.get('assembly')or len(facades)>=18:continue
  ring=plot['outer'];area=sum(a[0]*b[1]-b[0]*a[1]for a,b in zip(ring,ring[1:]+ring[:1]));direction=1 if area>0 else-1
  for a,b in zip(ring,ring[1:]+ring[:1]):
   dx=b[0]-a[0];dz=b[1]-a[1];length=math.hypot(dx,dz)
   if length<2.25:continue
   nx=dz/length*direction;nz=-dx/length*direction;facades.append({'kind':'carved_lintel'if family in['desert','jungle','river']else'balcony','x':round((a[0]+b[0])/2+nx*.025,4),'z':round((a[1]+b[1])/2+nz*.025,4),'y':round(plot['base']+.12,4),'scale':round(min(.7,(plot['height']-.1)/1.9),4)if family in['clay','city','industry']else round(min(.85,(plot['height']-.1)/1.74),4),'yaw':round(math.atan2(nx,nz),5),'plot':i});break
 domain=Polygon(p['domain']['outer']);green=[]
 for j in range(48):
  q=domain.exterior.interpolate((j+.3)*domain.exterior.length/48);c=domain.centroid;dx=q.x-c.x;dz=q.y-c.y;l=math.hypot(dx,dz);d=8.5+rng.random()*15;x=q.x+dx/l*d;z=q.y+dz/l*d
  green.append({'kind':'rock_cluster'if j%3==0 or family=='desert'else'fern_patch','x':round(x,3),'z':round(z,3),'scale':round(.6+rng.random()*.9,3),'yaw':round(rng.random()*math.tau,4)})
 stairs=[]
 for c in p['connectors']:
  a,b=c['vertices'][0],c['vertices'][3];dy=b[1]-a[1];distance=math.hypot(b[0]-a[0],b[2]-a[2])
  if abs(dy)>.13 and distance>.45 and len(stairs)<18:stairs.append({'a':a,'b':b,'width':.58})
 maps[id]={'family':family,'boundary':p['domain']['outer'],'groundY':p['groundY'],'sourceTrees':p['trees'],'foundation':p['foundation']['outer'],'roofDetails':roofs,'facadeDetails':facades,'scenery':green,'stairs':stairs,'heightReference':[min(v for r in p['rows']for v in r[1][2::3]),max(v for r in p['rows']for v in r[1][2::3])]}
 print(id,'roof',len(roofs),'facades',len(facades),'stairs',len(stairs))
(R/'src/environment132-layout.json').write_text(json.dumps({'revision':132,'maps':maps},separators=(',',':'))+'\n')
