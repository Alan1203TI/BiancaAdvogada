"""Atualiza títulos de notícias do RSS oficial do STJ. Usa apenas Python padrão."""
from pathlib import Path
import datetime,json,re,unicodedata,urllib.request,xml.etree.ElementTree as ET,argparse
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'assets/news-snapshot.json'
FEED='https://res.stj.jus.br/hrestp-c-portalp/RSS.xml'
def normalize(t):
 return ''.join(c for c in unicodedata.normalize('NFD',t.lower()) if unicodedata.category(c)!='Mn')
def parse(xml):
 items=[]
 for x in ET.fromstring(xml).findall('.//item'):
  title=(x.findtext('title') or '').strip();url=(x.findtext('link') or '').strip();n=normalize(title)
  if not url.startswith('https://www.stj.jus.br/') or not re.search(r'penal|prisao|preso|carcer|habeas|trafico|criminal|crime|condena|absolvi|juri\b|violencia domestica|pena\b|penas\b|prova.*polici|busca.*mandado',n):continue
  m=re.search(r'/(\d{2})(\d{2})(\d{4})-',url);date=f'{m[3]}-{m[2]}-{m[1]}' if m else None
  category='Execução penal' if re.search(r'execucao|presidio|carcer|progressao|remicao',n) else 'Processo penal' if re.search(r'habeas|prova|juri|busca|prisao|absolvi',n) else 'Direito Penal'
  items.append(dict(title=title,url=url,date=date,source='STJ',category=category))
  if len(items)==12:break
 if not items:raise ValueError('Nenhum item criminal válido no RSS')
 return items
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--feed-file');args=ap.parse_args()
 try:
  if args.feed_file:xml=Path(args.feed_file).read_bytes()
  else:
   req=urllib.request.Request(FEED,headers={'User-Agent':'BiancaMorandiNews/1.0','Accept':'application/rss+xml,application/xml,text/xml'})
   with urllib.request.urlopen(req,timeout=45) as response:xml=response.read()
  data={'items':parse(xml),'fetchedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'scheduled'}
  DEST.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
  print(f"Notícias atualizadas: {len(data['items'])}")
 except Exception as e:
  if not DEST.exists():raise
  data=json.loads(DEST.read_text(encoding='utf8'));data['mode']='archive';DEST.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
  print(f'Fonte temporariamente indisponível; mantendo seleção anterior ({type(e).__name__}).')
