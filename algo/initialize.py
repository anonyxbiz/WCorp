# /algo/initialize.py
import os, asyncio as a, random, json_stream, base64, json as j, secrets, pathlib, textwrap, argparse
from re import sub
from bottle import Bottle, route, run, request, static_file, response as r, post, get, put, delete, template, redirect, HTTPResponse, abort, hook
import requests as rqs
from bs4 import BeautifulSoup as bs4
from datetime import datetime as dt
from cryptography.fernet import Fernet
from discord import SyncWebhook

p = print

app_info = {'title': 'gAAAAABmSpkNXGxMymPKFKuk3mPNKTxTfCqjPGdivJizB13if089HxaTQgbgwcuAQD5VXwSfGK9yN8lUU9Q0tb_E4xL0v4WkwA==', 'url': 'https://example.com'}

parser = argparse.ArgumentParser()
parser.add_argument('-key', "--key")   
parser.add_argument('-url', "--url")    
parser.add_argument('-stay', "--stay")    
args = parser.parse_args()

safe_key = args.key or None
app_info['url'] = args.url or None

class Error(Exception):
    def __init__(self, status=None, e=None, detail=None):
        self.errors = {
            'status': status,
            'error': str(e).replace('Fernet', 'WCorp')
        }
        abort(status, self.errors)
    
    def __str__(self):
        return dict(self.errors)

def safe(do=None, job=None):
    if do == "en":
        job = Fernet(safe_key).encrypt(job.encode()).decode()
    else:
        job = Fernet(safe_key).decrypt(job.encode()).decode()
    return job  
                        
if __name__ == "__main__":
    pass