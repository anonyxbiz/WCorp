# test.py
from Safe.safe import*

def Raise(e=None):
    p(e)

async def key_gen(size=32):
    return secrets.token_urlsafe(size)+'='

async def main():  
    dis_hook = safe('de',app_info['title'])
    p(dis_hook)
           
if __name__=="__main__":
    a.run(main())
