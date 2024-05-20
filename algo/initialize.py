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
parser.add_argument('-t', "--thread",)    
args = parser.parse_args()

with open('secret.json') as f:
    f = j.load(f)
    safe_key = f[0]['key']  
    app_info['url'] = f[0]['url']

class Error(Exception):
    def __init__(self, status=None, e=None, detail=None):
        self.errors = {
            'status': status,
            'error': str(e).replace('Fernet', 'WCorp'),
            'detail': detail
        }
    
    def __str__(self):
        return str(self.errors)

def safe(do=None, job=None):
    if do == "en":
        job = Fernet(safe_key).encrypt(job.encode()).decode()
    else:
        job = Fernet(safe_key).decrypt(job.encode()).decode()
    return job  
                        
if __name__ == "__main__":
    p(Success('eh'))