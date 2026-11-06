"""ARENA original, deterministic electronic score. No input recordings or melodies.
Requires numpy/scipy, ffmpeg/libmp3lame. Run: python compose-music40.py OUTPUT
All oscillators, drum sounds and note events are synthesized here. No franchise samples.
"""
from pathlib import Path
import numpy as np,json,hashlib,subprocess,sys
from scipy.signal import butter,sosfilt
from scipy.io import wavfile
RATE=44100
out=Path(sys.argv[1] if len(sys.argv)>1 else '/dev/shm/arena-music40-assets');(out/'audio').mkdir(parents=True,exist_ok=True)
pcm=Path('/dev/shm/arena-music40-pcm');pcm.mkdir(exist_ok=True)
rng=np.random.default_rng(4040)
def hz(m):return 440*2**((m-69)/12)
def filt(x,cut,kind='lowpass'):
 return sosfilt(butter(2,cut,fs=RATE,btype=kind,output='sos'),x).astype(np.float32)
def env(n,attack=.008,release=.08):
 e=np.ones(n,dtype=np.float32);a=min(n//2,int(RATE*attack));r=min(n//2,int(RATE*release));
 if a:e[:a]=np.sin(np.linspace(0,np.pi/2,a,dtype=np.float32))**2
 if r:e[-r:]=np.cos(np.linspace(0,np.pi/2,r,dtype=np.float32))**2
 return e
samples={}
def synth(midi,duration,kind):
 key=(midi,round(duration,5),kind)
 if key in samples:return samples[key]
 n=round(duration*RATE);t=np.arange(n,dtype=np.float32)/RATE;f=hz(midi)
 if kind=='pad':
  x=np.zeros(n,np.float32)
  for detune,weight in [(-.0025,.22),(0,.44),(.0025,.22)]:
   for h in range(1,9):x+=np.sin(2*np.pi*f*(1+detune)*h*t+np.sin(t*.7)*.07)*(weight/(h**1.7))
  x=filt(x,2100)*(1+np.sin(2*np.pi*.13*t)*.08)*env(n,.16,.3)
 elif kind=='bass':
  phase=2*np.pi*f*t;x=(np.sin(phase)+.24*np.sin(phase*2)+.10*np.sin(phase*3))*np.exp(-t*3.2)*env(n,.004,.04);x=np.tanh(x*1.3)*.7
 elif kind=='arp':
  x=(np.sin(2*np.pi*f*t)+.25*np.sin(2*np.pi*f*2.004*t)+.10*np.sin(2*np.pi*f*3*t))*np.exp(-t*7)*env(n,.008,.08)
 else:
  fm=np.sin(2*np.pi*f*1.001*t+np.sin(2*np.pi*f*2*t)*np.exp(-t*4)*1.2)
  x=(fm*.6+np.sin(2*np.pi*f*.998*t)*.3)*np.exp(-t*2.7)*env(n,.018,.16)
 samples[key]=x.astype(np.float32);return samples[key]
def drum(kind):
 if kind in samples:return samples[kind]
 dur={'kick':.42,'snare':.24,'hat':.09,'open':.24,'rim':.13}[kind];t=np.arange(round(dur*RATE),dtype=np.float32)/RATE;noise=rng.normal(0,1,len(t)).astype(np.float32)
 if kind=='kick':
  phase=2*np.pi*(47*t+93*.026*(1-np.exp(-t/.026)));x=np.sin(phase)*np.exp(-t*13)+filt(noise,5000,'highpass')*.08*np.exp(-t*160)
 elif kind=='snare':x=filt(noise,1800,'highpass')*.55*np.exp(-t*21)+np.sin(2*np.pi*183*t)*.23*np.exp(-t*28)
 elif kind in ['hat','open']:
  metallic=sum(np.sin(2*np.pi*f*t)for f in [6321,7813,9257])*.07;x=filt(noise*.4+metallic,6500,'highpass')*np.exp(-t*(55 if kind=='hat'else 18))
 else:x=(np.sin(2*np.pi*1570*t)*.3+filt(noise,3000,'highpass')*.12)*np.exp(-t*47)
 samples[kind]=(x*env(len(t),.001,.012)).astype(np.float32);return samples[kind]
scores=[
 dict(key='menu',title='Glass Horizon',bpm=108,bars=32,root=50,seed=401,loop=True,mode='calm'),
 dict(key='match',title='Vector Pursuit',bpm=116,bars=32,root=45,seed=402,loop=True,mode='drive'),
 dict(key='win',title='Signal Ascending',bpm=120,bars=3,root=60,seed=403,loop=False,mode='victory'),
 dict(key='loss',title='After the Static',bpm=96,bars=3,root=50,seed=404,loop=False,mode='reflect'),
 dict(key='planted',title='Critical Circuit',bpm=120,bars=16,root=43,seed=405,loop=False,mode='tension'),
 dict(key='countdown',title='Last Ten',bpm=120,bars=5,root=55,seed=406,loop=False,mode='countdown'),
]
clips=[];analysis=[];events=[]
for score in scores:
 beat=60/score['bpm'];bar=beat*4;duration=bar*score['bars'];n=round(duration*RATE);prng=np.random.default_rng(score['seed']);music=np.zeros((n,2),np.float32);rhythm=np.zeros_like(music);root=score['root'];mode=score['mode'];loop=score['loop'];noteEvents=[]
 def add(target,sound,at,gain=1,pan=0):
  start=round(at*RATE);pan=np.clip(pan,-1,1);weights=np.array([np.sqrt((1-pan)/2),np.sqrt((1+pan)/2)],np.float32)*gain;v=sound[:,None]*weights
  if start<0:v=v[-start:];start=0
  if start>=n:return
  first=min(len(v),n-start);target[start:start+first]+=v[:first]
  if loop and first<len(v):target[:min(len(v)-first,n)]+=v[first:first+n]
 def note(midi,at,length,kind,gain,pan=0):add(music,synth(midi,length,kind),at,gain,pan);noteEvents.append([round(at,5),midi,round(length,5),kind,round(gain,4),round(pan,3)])
 progression=[(0,[0,3,7,10,14]),(-5,[0,4,7,11]),(3,[0,4,7,14]),(-2,[0,5,7,10])]
 if mode=='victory':progression=[(0,[0,4,7,11]),(5,[0,4,7,14]),(7,[0,4,7,10])]
 if mode=='reflect':progression=[(0,[0,3,7,14]),(-5,[0,3,7,10]),(-2,[0,5,7,10])]
 for b in range(score['bars']):
  at=b*bar;change=progression[(b//2)%len(progression)] if mode not in ['victory','reflect']else progression[b%3];shift,chord=change;base=root+shift;section=(b//8)%4
  padGain=.13 if mode=='drive'else .19 if mode=='calm'else .12
  if mode=='countdown':padGain=.07
  for j,interval in enumerate(chord):note(base+12+interval,at,bar+.42,'pad',padGain/len(chord),-.7+j*1.4/max(1,len(chord)-1))
  steps=[0,1.5,2,3.5]if mode in ['drive','tension','countdown']else[0,2.5]
  for step in steps:note(base-12,at+step*beat,beat*.68,'bass',.20 if mode!='reflect'else .10)
  if mode!='reflect':
   for step in [0,2]:add(rhythm,drum('kick'),at+step*beat,.50 if mode!='calm'else .31)
   for step in [1,3]:add(rhythm,drum('snare'),at+step*beat,.20 if mode!='calm'else .10,.08)
   for step in np.arange(0,4,.5):add(rhythm,drum('hat'),at+step*beat,float(prng.uniform(.055,.105)),-.25 if step%1 else .25)
   if mode in ['drive','tension','countdown']or section==2:add(rhythm,drum('open'),at+3.5*beat,.065,.38)
  else:
   for step in [1.5,3.5]:add(rhythm,drum('rim'),at+step*beat,.08,.3)
  pattern=[0,2,1,3,1,4,2,3];density=8 if mode in ['drive','tension','countdown']else 4
  for j in range(density):
   if mode=='calm'and b%8 in [0,7]and j%2:continue
   degree=pattern[(j+b%4)%len(pattern)]%len(chord);octave=24 if mode!='reflect'else 12;midi=base+octave+chord[degree]
   note(midi,at+j*4/density*beat,beat*.8,'arp',.09 if mode!='countdown'else .07,(-.5 if j%2 else .5))
  if (b%4 in [2,3]and mode in ['calm','drive'])or mode=='victory':
   motif=[7,10,14,12]if mode!='victory'else [7,12,16,19]
   note(root+12+motif[(b//2)%4],at+beat*.5,beat*2.2,'lead',.10,-.12)
  if mode=='countdown':
   for k in range(4):note(base+24+(12 if b>2 else 7),at+k*beat,beat*.3,'arp',.10,0)
 # Pump the instrumental bus slightly around each kick without changing percussion.
 t=np.arange(n,dtype=np.float32)/RATE;duck=1-.22*np.exp(-np.mod(t,beat*2)/.07);music*=duck[:,None]
 dry=music.copy()
 for delay,gain in [(beat*.75,.18),(beat*1.5,.085),(beat*2.25,.035)]:
  d=round(delay*RATE)
  if loop:music+=np.roll(dry[:,::-1],d,axis=0)*gain
  else:music[d:]+=dry[:-d,::-1]*gain
 room=np.empty_like(music);room[:,0]=filt(dry[:,0],4300);room[:,1]=filt(dry[:,1],4300)
 for delay,gain in [(.037,.10),(.071,.08),(.113,.065),(.173,.045),(.257,.025)]:
  d=round(delay*RATE)
  if loop:music+=np.roll(room[:,::-1],d,axis=0)*gain
  else:music[d:]+=room[:-d,::-1]*gain
 x=music+rhythm
 if not loop:x*=env(n,.015,.70 if mode in ['victory','reflect']else .035)[:,None]
 x-=x.mean(axis=0);rms=float(np.sqrt(np.mean(x*x)));x*=.125/max(.001,rms);x=np.tanh(x*1.15)/1.15;peak=float(np.max(np.abs(x)));x*=min(1,.84/max(.001,peak));
 wav=pcm/(score['key']+'.wav');wavfile.write(wav,RATE,np.round(x*32767).astype(np.int16));temp=out/(score['key']+'.mp3')
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-c:a','libmp3lame','-q:a','3','-ar',str(RATE),'-metadata','title='+score['title'],'-metadata','artist=ARENA','-metadata','album=ARENA Original Score 40',str(temp)],check=True)
 data=temp.read_bytes();digest=hashlib.sha256(data).hexdigest();file=out/'audio'/(digest+'.mp3');temp.rename(file)
 clips.append({'key':'music:'+score['key'],'url':'audio/'+file.name,'bytes':len(data),'sha256':digest,'duration':duration,'origin':'arena-original','pack':'arena-music40','title':score['title'],'bpm':score['bpm'],'source':{'author':'ARENA original procedural score40','method':'New note score, synthesized oscillators/percussion and original DSP; no external samples or source-game recordings','seed':score['seed'],'license':'Project-authored composition; no third-party media grant implied'}})
 analysis.append({'key':score['key'],'title':score['title'],'bpm':score['bpm'],'bars':score['bars'],'duration':duration,'sampleRate':RATE,'channels':2,'peak':float(np.max(np.abs(x))),'rms':float(np.sqrt(np.mean(x*x))),'loop':loop,'boundaryJump':float(np.max(np.abs(x[-1]-x[0]))),'waveformSHA256':hashlib.sha256(wav.read_bytes()).hexdigest(),'encodedSHA256':digest,'bytes':len(data),'noteEvents':len(noteEvents)})
 events.append({'key':score['key'],'notes':noteEvents});print('Composed',score['key'],score['title'],round(duration,2),'seconds',len(data),'bytes',flush=True)
(out/'music-manifest40.json').write_text(json.dumps({'schema':1,'assetType':'arena-runtime-audio','source':{'type':'ARENA original score40','externalSamples':[],'externalMelodyInputs':[],'generatorSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},'clips':clips},indent=2)+'\n');(out/'analysis40.json').write_text(json.dumps(analysis,indent=2)+'\n');(out/'score40.json').write_text(json.dumps(events,separators=(',',':'))+'\n')
