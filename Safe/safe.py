# /Safe/safe.py
from algo.initialize import*

class Safety:
    def __init__(s, key):
        s.enc_key = key
        
    async def safe_tool(s, parent, action):
        try:
            s.fernet = Fernet(s.enc_key)
        except Exception as e:
            return Error(False, e)
       
        try:
            s.parent = parent.encode()
            try:
                if action == 'encrypt':
                    s.content = s.fernet.encrypt(s.parent)
                elif action == 'decrypt':
                    s.content = s.fernet.decrypt(s.parent)            
            except Exception as e:
                return Error(False, e, f"Failed to {action} data, the {action}ion key >{s.enc_key}< used cannot {action} the data.")
                
            return s.content.decode()
        except Exception as e:
            raise Error(False, e)
        
               
if __name__=="__main__":
    pass
    