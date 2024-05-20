# apps.py
from algo.initialize import*
from algo.traffic import Analytics
from Safe.safe import Safety

class Pages:
    def __init__(s):
        s.app = Components()
        s.analytics = Analytics()
        
    async def page_manager(s, page, request, response):
        ip = request.remote_addr
        await s.analytics.check(ip)
        set_res = await s.response_config(request, response)
        
        if not set_res:
            msg = 'You"re not supposed to be here'
            await Discord().logger('Request Aborted from IP: {}, Error message: {}'.format(ip, msg))
            abort(403, msg)
                
        if os.path.isfile(f'static/page/{page}.html'):
            page_content = {'token': set_res, 'views': 'views'}
            return template(f'static/page/{page}.html', page_content=page_content)
            
        else:
            msg = "The page you're looking for cannot be found"
            await Discord().logger('Request Aborted from IP: {}, Error message: {}'.format(ip, msg))
            
            abort(404, msg)
            
    async def response_config(s, request, response):
        verification = await s.verify_request(request, response, do='all')
        
        return verification
    
    async def verify_request(s, request, response, do):
        host = await s.app.get_header(request, 'Host')
        try:
            if do == 'all':
                ip = request.remote_addr
                token = "test"
                
            response.set_header('strict-transport-security', 'max-age=63072000; includeSubdomains')
            response.set_header('x-frame-options', 'SAMEORIGIN')
            response.set_header('x-xss-protection', '1; mode=block')
            response.set_header('x-content-type-options', 'nosniff')
            response.set_header('referrer-policy', 'origin-when-cross-origin')
            response.set_header('server', 'Secure')
            
            if do == 'all':
                return token
            else:
                return response
        except Exception as e:
            await Discord().logger('Request Aborted from IP: {}, Error message: {}'.format(ip, e))
            abort(406, e)            
    
class Components:
    def __init__(s):
        s.allowed_origins = {'tonka.wazing.site', 'devops.wazing.site'}
        safe = Safety(safe_key)

    async def encrypt(s, parent):
        try:
            token = await s.safe.safe_tool(token, 'encrypt')
            return token
        except Exception as e:
            return Error(False, e)
            
    async def decrypt(s, token):
        try:
            content = await s.safe.safe_tool(token, 'decrypt')
            return content
        except Exception as e:
            return Error(False, e)
               
    async def get_json(s, r):    
        return j.loads(r.body.getvalue().decode('utf-8'))          
        
    async def get_header(s, request, value):    
        return request.get_header(value)

def keepmealive(url, other):
    # Get the site to keep it active
    quits = 0
    gets = 0
    try:
        while quits <= 1:
            sleep(30)
            rqs.get(url)
            gets += 1
            
    except KeyboardInterrupt:
        quits += 1
        p('Keepalive Stopping...')
    except Exception as e:
        raise Error(False, e)

class Discord:
    def __init__(self):
        self.server_name = "App"
        self.dis_hook = safe('de',"gAAAAABmSoPJZdUtTgkBjEicKtBZhBGiwekRfK17-WdyMzWOLuMVlWXcCb5vEyJMu3UHxn5cReVxAWB1b0Q_CK-vhkemH5ERmz0MakPaldW2_NVYiWiJcXk2YVx4UCNjbmMnP1agIZY50fbm4vwZFoMEvZoNSNmTEgKRXSDjHEGkdT7PrlCQ_HbKEaQTdd3QkyHT0xUvuPt5Q2zfNVAsMQ2NXVcuKK_frdk6Cf6Q3TH2VCO-uDO-bcw=") or None
          
    async def logger(self, msg):
        try:
            msg = self.server_name +': '+ str(msg)
            webhook = SyncWebhook.from_url(self.dis_hook)
            
            if webhook.send(content=msg):
                return True
            else:
                return Error(False, 'Something went"t wrong logging')
        except Exception as e:
            return Error(False, e)

if __name__ == '__main__':
    pass