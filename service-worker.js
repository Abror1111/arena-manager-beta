// Binary models use the verified asset cache. This worker keeps only the app
// shell and small images, so the browser can reopen the club without a network.
const SHELL='arena-shell-1.26';
const base=new URL('./',self.registration.scope),index=new URL('index.html',base).href;
self.addEventListener('install',event=>event.waitUntil((async()=>{
 const cache=await caches.open(SHELL),response=await fetch(index,{cache:'reload'});if(!response.ok)throw Error('Shell unavailable');
 const text=await response.clone().text();await cache.put(index,response);
 const assets=[...text.matchAll(/(?:src|href)="([^"]+)"/g)].map(m=>new URL(m[1],index)).filter(u=>u.origin===base.origin&&u.pathname.startsWith(base.pathname)&&/\.(js|css)$/.test(u.pathname));
 for(const url of assets){const r=await fetch(url,{cache:'reload'});if(!r.ok)throw Error('Shell asset unavailable');await cache.put(url.href,r);}
 await self.skipWaiting();
})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{for(const key of await caches.keys())if(key.startsWith('arena-shell-')&&key!==SHELL)await caches.delete(key);await self.clients.claim();})()));
async function downloadedImage(request){
 const cache=await caches.open('arena-verified-assets-v1'),url=new URL(request.url);
 for(const key of await cache.keys())if(new URL(key.url).pathname===url.pathname)return cache.match(key);
}
self.addEventListener('fetch',event=>{
 const request=event.request,url=new URL(request.url);
 if(request.method!=='GET'||url.origin!==base.origin||!url.pathname.startsWith(base.pathname)||/\.(glb|cmesh|apk)$/.test(url.pathname))return;
 if(request.mode==='navigate'){
  event.respondWith((async()=>{try{const r=await fetch(request);if(!r.ok)throw Error('Offline');return r;}catch{return await (await caches.open(SHELL)).match(index)||Response.error();}})());return;
 }
 if(!/\.(js|css|png|webp|svg)$/.test(url.pathname))return;
 event.respondWith((async()=>{
  const cache=await caches.open(SHELL),hit=await cache.match(request);if(hit)return hit;
  try{const r=await fetch(request);if(r.ok)await cache.put(request,r.clone());return r;}
  catch{return await downloadedImage(request)||Response.error();}
 })());
});
