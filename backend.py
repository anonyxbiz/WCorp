# backend.py
from algo.initialize import*
from algo.apps import Components, Discord, Pages
# from Algorithms.ai import Wazingai
from asyncio import run

class Wazingai:
    def __init__(self):
        self.api_key = run(safe('de',"gAAAAABmSm_QDaBc8MD98uY5FZu0V2Y6j76CQWZQODlqM9XK1CF1wUyM_6sI4Fz7YJaYxU4-wiyCu36l7vDZJqoB9lK3Ig2VVdB3-fh3aXcujn5LIOVtfuUUjp0rJLwAGLnPcoutKgEG"))
        self.system_prompt = run(safe('de',"gAAAAABmSnRC2YXv-DZU7KkqgprDxZs44phb7L7Xqm5sU2KhH4C0B4-981tBAwUbW1xE6kCO9k4ZAK-tJub5GDn9r5tXJVjwVzgcfUWTqxXQMjf0t4hipkzWqidWbeZo8skdBgayO05R5acj7Odbgg4BOSzefoBB8umYliNHHbWLInToIQOjMBAHTmE_Lw5d_1qInYcPrD_INdcPyv3M7CvFDk-5d-2h0nzGcJBZOlU91eQUk9p2kYznfNvkeOQnXLZgxoL9O1lyZPAoQ1GlQo_bJDw5q6bfU4VxSq2EQZIyE7n8ihMgPmi_ILmecqM0jZ41qinpicKIhbtbQrY-xZ14AbwYqvNQdVKt1l1zkMzvCZkP2ykN3tW8RI-74njXL48FnSy1r0nIps1NimKVzwitJHfRyj07yqwDY45S0zOZ3p0yCxkdpnKcQLrZlfyY4D1byc9ZXA6e0pp1ye1b5aqe1ANQTukgprtCPAgWYJ9xBNVhdPtgQlD9dEa__LEG-FE9ouTdK0KGMfWYZjq9vf3MdiR-jyYPraU-HqX8Xs0beDwUCjSnXWkMXOEzvPQVguXI4r33Tpq0gP92SqPjPBoyoVzfnXglyHtYgkpt5Ol_X2BZLHRHLDPwWNO3zTz5tSSEVMy8nUzuTvzEkpp2haAyRnhpCjexsuqzjK-4apL-HCXahw0IfHWK1MWmxIIz1_2h_M4zKzxqNBdhfMyTx7shJwe5MH4eq-egy3iwSEMn5fqBIpc0FJKtIKG8oGFW_dX_2TH372v-p41HjTCZJnIeeTNXG_m-TzqHEB78fCR2vMNIIA57OxzACMVw0i9wLbCLRnLdksLfDsZT5kjV_6sl0lxjRvoJtUnq5VpQX-WaGhLeNhjfaHOdl6AVYRIRzUNoRzX_iHUnM-rrYDPUKmpbxFDjWDZyZ05sxHJ39uxOjbYnw8Udsl2TxO6giTG8AI0Nw7biUcIVt5_aj6AQ3pX_447JQeAJD2QNzgdeTwDfxW3FqQg6JN4F9PLiHRO4vw2h3gNJ4v4rbxAR5tBTpZhIH22W0XPQO6jNInUFtGKvdTFlyeHpQlxunOhhw8_HargGqrhjYBPjetOlYpz_KyRdDAkk4C2CVfkFXbZrWbYywPfi4tq5iD832ZxSooJcbsDSOy694credfJqYlchDWznF4JWkmbZDO7ghkZPApEvuiAE-9Fc_GO2-jLQ2h3mUtdgXG9enlsD7VzKye6Hdltn42VHFtCxzqHn8qjVvnwxydNSjg8RfjQ8yZwR6csHOtsD8N3RDEfXwGbBwb0CqeE0li2bV3kRDocuofkb5MMz5ZowDYoZoZCnmpPAEnExMm_tN4ZJePWurgcH1qi-12ofXv5nD6kHf--ZzAyWBQXItlCpMopVx_WHqO0IlKjqse22GeeKDdDUyPl0BlDJxuk1Sa0l8lzKCYehBs_OfhsMyECHKD03J1SUa5pKJvvikxQHJz2DUYfanJ7Ehbkl7H29FPZdkU2ZaUnF_iV17cDlInVzBp1oKTGCCs7Sy03fEnpVJrDIH21U1bTtUCp9jdEV7qHKARyBvaQgTENfMOXAsiOums1JJ_AqAis-UKy4duqhU2dah3OShxCE_e1WSDG6GSE4Y44sULmBqfV3zFEuzaPn7ABvqZ5z4F0aaV3DQMFqV8z3V5NWkIfoR8Y04bNHpRneTsWR_esY75xrBzK_KoXTouN99V7mG3p0gHWzmUpAktQ1nGL8crv0gNXziF-kPoz84YhsoLTYETyW6UMiIZaOMEuh-AoiXacQI63LVmvVOUXmXZXruBwl5iOGZOLXpwGd2HSptOANZW7OT17ssPflCJIp9-lGF5PfmMN2LyIjpGVQnPn9SOCdHsFfyEBemzAU6JO9Q_yHzNdQDxhPsyvD-5YjhdSqlWfSjhhS-RF4xjhvPVRPPTkv0ZT3MuyrJSxn_efsPxX_XAKxV8g_NCClzoUGFBYuzBCGojrW16I7bS06s73nHX1gV3IiXUaLsHV7fu_-MyuEPjdSK1a1NQ50H1cXSvinWPbFHc8h87LbvbxU2oBJ5M4cbSdm7mh1_jabzmYWFGGN9lcvT-ZyldSEcFO5C4ZDykFnTfXQ0gPb6og5hCoLvveJdMgBjPzksHTRZoro3nQ75Fuh0H1zVmcijqR652yb90cxhdAryaA_p-30RUDDkr7Y0PCXoFTWzTt93P5KcwDFLZnp3T3JgOyFYnmDehabXDFNRzv6ZEJ2vm_ZWSOAwrPH5Gg5tRLUV8kvuj0yoO0qSPfMROvzWdUAIeneKnUHWP22CefbaKw4GtLzL9Y3LBvOOz9kkKWVWehsK41MWI1Bks9W_61-UUmYiyzlf0EOlSVMXoW-Uf-LwPjk8aSxNFRzvyq1jjGH39oasjTg5xc_xX2Qx4jFTSUpXFYgCPor6j8M_r3s0fAz9chN79-Ag68mezwEUPmAxqqdL4HwuTZtVe-CIm_jvl4UX-Ux2nfwuM3WsTK2meDjkHuHF1wv"))
        
    async def chat(self, prompt):
        prompt = system_prompt + f"You: I am waiting for a question.\n{prompt}"
        
        ai = "Hi there"
        self.response = {'status': 'processed', 'ai': ai}
        
        return self.response
        
class Backend_apps:
    def __init__(self):
        self.comps = Components()
        self.set_headers = Pages()
        self.wazingai = Wazingai()
        
    async def incoming(self, request):
        try:
            if request.method == "GET":
                return request.query
                    
            elif request.method == "POST": 
                return await self.comps.get_json(request)
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
    
    async def dealer(self, request, response):
        await self.set_headers.verify_request(request, response, do='headers only')
        try:
            req_data = await self.incoming(request)   
            if req_data:
                model = req_data["model"] 
                query = req_data["query"]
                ip = request.remote_addr
                  
                if model == 'ai':
                    detail = await self.wazingai.aidata(query, ip)
                else:
                    detail = query
                
                data = detail
            else:
                abort(403, "Something wen't wrong processing your request")
                
        except Exception as e:
            await Discord().logger(f'Application log: {e}')
            abort(403, f"Something wen't wrong on our end {e}")
        return data
        
if __name__ == '__main__':
    pass