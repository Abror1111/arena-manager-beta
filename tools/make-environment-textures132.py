"""Own seamless multi-scale PBR: no imported game images or stock photographs."""
from pathlib import Path
from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter,zoom
import hashlib,json
R=Path(__file__).resolve().parents[1];out=R/'public/environment132';out.mkdir(exist_ok=True);math_tau=np.pi*2;size=1024;yy,xx=np.mgrid[0:size,0:size]/size;rng=np.random.default_rng(132)
def noise(freq):
 a=rng.random((freq,freq));p=np.pad(a,1,mode='wrap');z=zoom(p,size/freq,order=3);offset=round(size/freq);return z[offset:offset+size,offset:offset+size]
def entry(p):return{'url':'/environment132/'+p.name,'localUrl':'/environment132/'+p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
manifest={'origin':'ARENA mathematical materials: chipped stone, plaster, concrete, moss and aggregate','families':{}}
for family in['desert','clay','industry','jungle','river','city']:
 manifest['families'][family]={}
 for role in['wall','stone','paving','roof']:
  large=noise(8);mid=noise(32);fine=rng.random((size,size));field=.55+.12*(large-.5)+.08*(mid-.5)+.018*(fine-.5);tint=np.ones((size,size,3),dtype=np.float32)
  if role=='roof':
   if family=='clay':
    u=(xx*12)%1;v=(yy*8)%1;channel=np.sin(u*np.pi);lap=np.clip((.04-v)/.04,0,1);height=field*.10+channel*.16-lap*.035;field+=channel*.035-lap*.08;tint*=np.array([1.03,.98,.91])
   elif family=='industry':
    u=(xx*8)%1;seam=np.exp(-np.minimum(u,1-u)*110);height=field*.05+seam*.12;field+=seam*.04
   elif family=='jungle':
    edge=np.minimum((xx*6)%1,(yy*6)%1);moss=np.clip((.55-large)*3,0,.45);height=field*.15-(edge<.02)*.07;tint[:,:,0]-=moss*.3;tint[:,:,1]+=moss*.06;tint[:,:,2]-=moss*.17;field-=(edge<.02)*.1
   else:height=field*.12;field-=np.clip((.42-mid)*.1,0,.05)
  elif role=='wall'and family in['desert','clay','river']:
   height=field*.22;plaster=gaussian_filter(np.maximum(0,.43-mid),2);height-=plaster*.18;field-=plaster*.12
   cracks=(np.abs(noise(16)-.5)<.009)&(large<.52);height-=cracks*.025;field-=cracks*.13
   streak=(np.sin(xx*math_tau*13+noise(4)*3)*.5+.5)**18*(.5+.5*np.cos(yy*math_tau));field-=streak*.018
   if family=='clay':tint*=np.array([1.03,1.0,.94])
  elif role=='stone'or family=='jungle':
   rows=8 if role=='stone'else 12;row=np.floor(yy*rows);u=(xx*9+(row%2)*.5)%1;v=(yy*rows)%1;edge=np.minimum(np.minimum(u,1-u),np.minimum(v,1-v));mortar=np.clip((.035-edge)/.035,0,1);height=field*.14+(1-mortar)*.11;field-=mortar*.14
   chips=np.clip((.42-mid)*2,0,.25)*(edge<.16);height-=chips*.12;field-=chips*.08
   if family=='jungle':
    moss=np.clip((.52-large)*5,0,.6)*(1-np.minimum(1,edge*3));tint[:,:,0]-=moss*.25;tint[:,:,1]+=moss*.08;tint[:,:,2]-=moss*.15
   if family=='river':tint*=np.array([1.03,1.01,.91])
  else:
   # Large concrete/asphalt panels, fine mineral aggregate and restrained seams.
   u=(xx*4)%1;v=(yy*4)%1;seam=(np.minimum(np.minimum(u,1-u),np.minimum(v,1-v))<.004);height=field*.10-seam*.045;field-=seam*.15
   if role=='paving':field-=.035;field+=(fine-.5)*.025
   stains=np.clip((.39-large)*.12,0,.025);field-=stains
  if role=='paving'and family in['desert','clay','river']:
   # Irregular worn pavers with broad, readable joints instead of tiny checker tiles.
   row=np.floor(yy*7);u=(xx*7+(row%2)*.5+noise(4)*.03)%1;v=(yy*7)%1;edge=np.minimum(np.minimum(u,1-u),np.minimum(v,1-v));seam=np.clip((.018-edge)/.018,0,1);height=field*.12+(1-seam)*.09;field-=seam*.12
  if role=='paving'and family in['desert','clay','river']:tint*=np.array([1.025,1.,.93])
  base={'wall':.80,'stone':.82,'paving':.79,'roof':.80}[role]
  if role=='paving'and family in['industry','city']:base=.76
  color=np.clip((base+(field-.55)*.4)[:,:,None]*tint,0,1);c=out/f'{family}-{role}-color.webp';Image.fromarray(np.uint8(color*255)).save(c,quality=94)
  h=Image.fromarray(np.float32(height),mode='F').resize((512,512),Image.Resampling.BILINEAR);h=np.asarray(h);dx=(np.roll(h,-1,1)-np.roll(h,1,1))*10;dy=(np.roll(h,-1,0)-np.roll(h,1,0))*10;normal=np.stack([-dx,-dy,np.ones_like(dx)],axis=2);normal/=np.linalg.norm(normal,axis=2,keepdims=True);n=out/f'{family}-{role}-normal.webp';Image.fromarray(np.uint8(np.clip(normal*.5+.5,0,1)*255)).save(n,lossless=True)
  rough=np.clip(.75+(mid-.5)*.18,.5,.95);rr=out/f'{family}-{role}-roughness.webp';Image.fromarray(np.uint8(rough*255)).resize((256,256),Image.Resampling.BILINEAR).save(rr,lossless=True)
  manifest['families'][family][role]={'color':entry(c),'normal':entry(n),'roughness':entry(rr)}
  print(family,role,flush=True)
manifest['generatorSHA256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();(R/'src/environment132-textures.json').write_text(json.dumps(manifest,indent=2)+'\n')
