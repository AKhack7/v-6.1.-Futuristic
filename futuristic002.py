import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import pyautogui
import time
import psutil
import pywhatkit
import random
import subprocess
import re
import threading
import socket
import glob
import logging
from sympy import sympify, sin, cos, tan, sqrt, pi
import urllib.request 
import cv2 
import numpy as np
import requests
import ctypes
import queue
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import keyboard  # For Ctrl + M shortcut

# Initialize logging
logging.basicConfig(filename="isha_assistant.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

class IshaAssistant:
    """A personal desktop assistant with voice and text command capabilities."""
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.microphone = None
        try:
            self.microphone = sr.Microphone()
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
        except (AttributeError, OSError, sr.RequestError) as e:
            logging.error(f"Microphone initialization failed: {str(e)}")
            message = "Voice recognition disabled. PyAudio not found or microphone issue. Please install PyAudio and check microphone."
            self.speak(message)
            print(message)
            self.select_microphone()
        
        self.is_listening = False
        
        # Internet check caching
        self.last_internet_check = 0
        self.internet_status = False
        self.internet_check_interval = 10
        
        # Set female voice
        self.set_female_voice()
        
        # Initialize Ollama for conversational responses
        self.llm = ChatOllama(model="llama3.1:3b", temperature=0.7)
        self.chat_history = [
            SystemMessage(content="""
                तुम 'इशा' हो — एक फ्रेंडली, स्मार्ट और हिंदी बोलने वाला वॉइस असिस्टेंट।
                - हमेशा अपना नाम 'इशा' बताओ।
                - कभी भी Ollama, Llama, model, AI, LLM, code, Python, API आदि का जिक्र मत करो।
                - जवाब छोटे, मीठे और नैचुरल रखो, जैसे दोस्त से बात हो।
                - अगर कोई पूछे "तुम कौन हो?" या "नाम क्या है?" तो कहो: "मैं इशा हूँ, तुम्हारा पर्सनल असिस्टेंट!"
                - अगर कोई सामान्य बातचीत करे (जैसे "हाय, कैसे हो?"), तो फ्रेंडली जवाब दो।
                - tum isha ho — ek phrendalee, smaart aur hindee bolane vaala vois asistent.
                - hamesha apana naam 'ISHA' batao
                - kabhee bhee ollam, llam, modail, ai, llm, chodai, python, api aadi ka jikr mat karo.
                - javaab chhote, meethe aur naichural rakho, jaise dost se baat ho.
                - agar koee poochhe "tum kaun ho?" ya "naam kya hai?" to kaho: "main 'ISHA' hoon, tumhaara parsanal asistent!"
                - agar koee saamaany baatacheet kare (jaise "haay, kaise ho?"), to phrendalee javaab do.
                - You are 'Isha' – a friendly, smart and Hindi speaking voice assistant.
                - Always tell your name as 'Isha'.
                - Never mention Ollama, Llama, model, AI, LLM, code, Python, API, etc.
                - Keep your answers short, sweet, and natural, as if you were talking to a friend.
                - If someone asks, "Who are you?" or "What's your name?" say, "I'm Isha, your personal assistant!"
                - If someone makes a casual conversation (like "Hi, how are you?"), respond in a friendly way.
            """)
        ]
        
        # Settings and Apps lists
        self.SETTING_MAP = {
            "display setting": ("ms-settings:display", "01"),
            "sound setting": ("ms-settings:sound", "02"),
            "notification & action setting": ("ms-settings:notifications", "03"),
            "focus assist setting": ("ms-settings:quiethours", "04"),
            "power & sleep setting": ("ms-settings:powersleep", "05"),
            "storage setting": ("ms-settings:storagesense", "06"),
            "tablet setting": ("ms-settings:tablet", "07"),
            "multitasking setting": ("ms-settings:multitasking", "08"),
            "projecting to this pc setting": ("ms-settings:project", "09"),
            "shared experiences setting": ("ms-settings:crossdevice", "010"),
            "system components setting": ("ms-settings:appsfeatures-app", "001"),
            "clipboard setting": ("ms-settings:clipboard", "002"),
            "remote desktop setting": ("ms-settings:remotedesktop", "003"),
            "optional features setting": ("ms-settings:optionalfeatures", "004"),
            "about setting": ("ms-settings:about", "005"),
            "system setting": ("ms-settings:system", "006"),
            "devices setting": ("ms-settings:devices", "007"),
            "mobile devices setting": ("ms-settings:mobile-devices", "008"),
            "network & internet setting": ("ms-settings:network", "009"),
            "personalization setting": ("ms-settings:personalization", "000"),
            "apps setting": ("ms-settings:appsfeatures", "10"),
            "account setting": ("ms-settings:yourinfo", "20"),
            "time & language setting": ("ms-settings:dateandtime", "30"),
            "gaming setting": ("ms-settings:gaming", "40"),
            "ease of access setting": ("ms-settings:easeofaccess", "50"),
            "privacy setting": ("ms-settings:privacy", "60"),
            "updated & security": ("ms-settings:windowsupdate", "70")
        }

        self.SETTING_MAP4s = {
            "01": ("ms-settings:display"),
            "02": ("ms-settings:sound"),
            "03": ("ms-settings:notifications"),
            "04": ("ms-settings:quiethours"),
            "05": ("ms-settings:powersleep"),
            "06": ("ms-settings:storagesense"),
            "07": ("ms-settings:tablet"),
            "08": ("ms-settings:multitasking"),
            "09": ("ms-settings:project"),
            "010": ("ms-settings:crossdevice"),
            "001": ("ms-settings:appsfeatures-app"),
            "002": ("ms-settings:clipboard"),
            "003": ("ms-settings:remotedesktop"),
            "004": ("ms-settings:optionalfeatures"),
            "005": ("ms-settings:about"),
            "006": ("ms-settings:system"),
            "007": ("ms-settings:devices"),
            "008": ("ms-settings:mobile-devices"),
            "009": ("ms-settings:network"),
            "000": ("ms-settings:personalization"),
            "10": ("ms-settings:appsfeatures"),
            "20": ("ms-settings:yourinfo"),
            "30": ("ms-settings:dateandtime"),
            "40": ("ms-settings:gaming"),
            "50": ("ms-settings:easeofaccess"),
            "60": ("ms-settings:privacy"),
            "70": ("ms-settings:windowsupdate")
        }

        self.apps_commands = {
            "alarms & clock": ("ms-clock:", "a1"),
            "calculator": ("calc", "c1"),
            "calendar": ("outlookcal:", "c2"),
            "camera": ("microsoft.windows.camera:", "c3"),
            "copilot": ("ms-copilot:", "c4"),
            "cortana": ("ms-cortana:", "c5"),
            "game bar": ("ms-gamebar:", "gb1"),
            "groove music": ("mswindowsmusic:", "gm1"),
            "mail": ("outlookmail:", "m1"),
            "maps": ("bingmaps:", "maps1"),
            "microsoft edge": ("msedge", "me1"),
            "microsoft solitaire collection": ("ms-solitaire:", "mc1"),
            "microsoft store": ("ms-windows-store:", "ms1"),
            "mixed reality portal": ("ms-mixedreality:", "mp1"),
            "movies & tv": ("mswindowsvideo:", "mt1"),
            "office": ("ms-office:", "o1"),
            "onedrive": ("ms-onedrive:", "od1"),
            "onenote": ("ms-onenote:", "on1"),
            "outlook": ("outlookmail:", "ouk"),
            "outlook (classic)": ("ms-outlook:", "oc1"),
            "paint": ("mspaint", "p1"),
            "paint 3d": ("ms-paint:", "p3d"),
            "phone link": ("ms-phonelink:", "pk"),
            "power point": ("ms-powerpoint:", "pt"),
            "settings": ("ms-settings:", "ss"),
            "skype": ("skype:", "sk1"),
            "snip & sketch": ("ms-snip:", "s0h"),
            "sticky note": ("ms-stickynotes:", "s1e"),
            "tips": ("ms-tips:", "ts0"),
            "voice recorder": ("ms-soundrecorder:", "vr0"),
            "weather": ("msnweather:", "w1"),
            "windows backup": ("ms-settings:backup", "wb1"),
            "windows security": ("ms-settings:windowsdefender", "ws1"),
            "word": ("ms-word:", "wrd"),
            "xbox": ("ms-xbox:", "xb"),
            "about your pc": ("ms-settings:about", "apc")
        }

        self.apps_commands4q = {
            "a1": "ms-clock:",
            "c1": "calc",
            "c2": "outlookcal:",
            "c3": "microsoft.windows.camera:",
            "c4": "ms-copilot:",
            "c5": "ms-cortana:",
            "gb1": "ms-gamebar:",
            "gm1": "mswindowsmusic:",
            "m1": "outlookmail:",
            "maps1": "bingmaps:",
            "me1": "msedge",
            "mc1": "ms-solitaire:",
            "ms1": "ms-windows-store:",
            "mp1": "ms-mixedreality:",
            "mt1": "mswindowsvideo:",
            "o1": "ms-office:",
            "od1": "ms-onedrive:",
            "on1": "ms-onenote:",
            "ouk": "outlookmail:",
            "oc1": "ms-outlook:",
            "p1": "mspaint",
            "p3d": "ms-paint:",
            "pk": "ms-phonelink:",
            "pt": "ms-powerpoint:",
            "ss": "ms-settings:",
            "sk1": "skype:",
            "s0h": "ms-snip:",
            "s1e": "ms-stickynotes:",
            "ts0": "ms-tips:",
            "vr0": "ms-soundrecorder:",
            "w1": "msnweather:",
            "wb1": "ms-settings:backup",
            "ws1": "ms-settings:windowsdefender",
            "wrd": "ms-word:",
            "xb": "ms-xbox:",
            "apc": "ms-settings:about"
        }

        self.software_dict = {
            "notepad": "notepad",
            "ms word": "winword",
            "command prompt": "cmd",
            "excel": "excel",
            "vscode": "code",
            "word16": "winword",
            "file explorer": "explorer",
            "edge": "msedge",
            "microsoft 365 copilot": "ms-copilot:",
            "outlook": "outlook",
            "microsoft store": "ms-windows-store:",
            "photos": "microsoft.photos:",
            "xbox": "xbox:",
            "solitaire": "microsoft.microsoftsolitairecollection:",
            "clipchamp": "clipchamp",
            "to do": "microsoft.todos:",
            "linkedin": "https://www.linkedin.com",
            "calculator": "calc",
            "news": "bingnews:",
            "one drive": "onedrive",
            "onenote 2016": "onenote",
            "google": "https://www.google.com"
        }

        self.commands_dict = {**self.SETTING_MAP, **self.SETTING_MAP4s, **self.software_dict, **self.apps_commands, **self.apps_commands4q}
        self.commands_dict = {k: v if isinstance(v, str) else v[0] for k, v in self.commands_dict.items()}
        self.settings_display_to_cmd = {f"{name} ({code})": cmd for name, (cmd, code) in self.SETTING_MAP.items()}
        self.apps_display_to_cmd = {name: cmd for name, cmd in self.apps_commands.items()}
        
        self.input_queue = queue.Queue()
        self.pending = None
        
        # Start Ctrl + M listener
        threading.Thread(target=self.listen_ctrl_m, daemon=True).start()
        
        self.wish_me()
        self.start_server()

    def listen_ctrl_m(self):
        """Listen for Ctrl + M to toggle microphone."""
        while True:
            if keyboard.is_pressed('ctrl+m'):
                self.toggle_voice()
                time.sleep(0.5)  # Prevent multiple toggles
            time.sleep(0.1)

    def start_server(self):
        class CustomHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                parsed_path = urlparse(self.path)
                query_params = parse_qs(parsed_path.query)
                path = parsed_path.path
                
                if path == '/':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(self.server.assistant.get_html().encode())
                elif path == '/command':
                    cmd = query_params.get('cmd', [None])[0]
                    if cmd is None:
                        self.send_response(400)
                        self.end_headers()
                        return
                    if self.server.assistant.pending:
                        self.server.assistant.input_queue.put(cmd)
                        self.send_response(200)
                        self.send_header('Content-type', 'text/plain')
                        self.end_headers()
                        self.wfile.write(b'Input received')
                    else:
                        response = self.server.assistant.process_command(cmd)
                        self.send_response(200)
                        self.send_header('Content-type', 'text/plain')
                        self.end_headers()
                        self.wfile.write(response.encode())
                elif path == '/voice':
                    self.server.assistant.toggle_voice()
                    message = "Microphone toggled"
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(message.encode())
                else:
                    self.send_response(404)
                    self.end_headers()
            def log_message(self, format, *args):
                pass

        server = HTTPServer(('localhost', 8000), CustomHandler)
        server.assistant = self
        threading.Thread(target=server.serve_forever, daemon=True).start()
        webbrowser.open('http://localhost:8000/')

    def get_html(self):
        apps_html = ''.join(f'<div class="app-item" data-command="open {name}" style="margin:6px 0; cursor:pointer;">• {name}</div>' for name in sorted(self.apps_display_to_cmd.keys()))
        settings_html = ''.join(f'<div class="setting-item" data-command="open {name}" style="margin:6px 0; cursor:pointer;">• {name}</div>' for name in sorted(self.SETTING_MAP.keys()))
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>ISHA Assistant</title>
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;700&family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root{{
    --bg1:#050519;
    --bg2:#0f1636;
    --neon1:#00e0ff;
    --neon2:#7b4bff;
    --glass: rgba(255,255,255,0.04);
    --glass-strong: rgba(255,255,255,0.07);
    --accent-shadow: 0 10px 30px rgba(0,224,255,0.08);
  }}
  *{{box-sizing:border-box; -webkit-font-smoothing:antialiased; font-family: "Segoe UI", Inter, system-ui, sans-serif}}
  html,body{{height:100%; margin:0; background: radial-gradient(1200px 600px at 10% 10%, rgba(0,224,255,0.03), transparent 8%), radial-gradient(1000px 400px at 90% 90%, rgba(123,75,255,0.03), transparent 8%), linear-gradient(180deg,var(--bg1),var(--bg2)); color:#e8f6ff; display:flex; align-items:center; justify-content:center; overflow:hidden;}}

  .container {{
    width: 540px;
    max-width:calc(100% - 40px);
    height: 680px;
    border-radius: 24px;
    position: relative;
    padding: 30px;
    background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.04);
    box-shadow: 0 20px 60px rgba(5,10,40,0.6), 0 6px 18px rgba(0,224,255,0.02);
    overflow: hidden;
    backdrop-filter: blur(8px);
  }}

  .container::before{{
    content:"";
    position:absolute; inset:-2px; border-radius:26px;
    background: conic-gradient(from 0deg, rgba(0,224,255,0.12), rgba(123,75,255,0.08), rgba(0,224,255,0.12));
    filter: blur(30px);
    z-index:0;
    pointer-events:none;
  }}

  .topbar {{
    z-index:5;
    position:relative;
    display:flex; align-items:center; justify-content:space-between; gap:12px;
  }}
  .title {{
    font-weight:700; font-size:18px; color:#cfeeff;
    display:flex; align-items:center; gap:10px;
  }}
  .title .dot{{
    width:12px; height:12px; border-radius:50%;
    background: linear-gradient(135deg,var(--neon1),var(--neon2));
    box-shadow:0 0 18px rgba(0,224,255,0.4), 0 0 40px rgba(123,75,255,0.14);
  }}

  .stage {{
    position:relative; z-index:3; width:100%; height:420px; display:flex; align-items:center; justify-content:center;
  }}
  canvas#particles {{ position:absolute; inset:0; width:100%; height:100%; z-index:1; pointer-events:none; }}

  .core {{
    position:relative;
    width: 220px; height:220px;
    display:flex; align-items:center; justify-content:center;
    z-index:4;
    transform-style:preserve-3d;
    animation: bob 4s ease-in-out infinite;
  }}
  @keyframes bob{{
    0%{{ transform: translateY(0) scale(1); }}
    50%{{ transform: translateY(-10px) scale(1.02); }}
    100%{{ transform: translateY(0) scale(1); }}
  }}

  .core .aura {{
    position:absolute; inset: -6px; border-radius:50%;
    background: radial-gradient(circle at 30% 30%, rgba(0,224,255,0.08), transparent 30%), radial-gradient(circle at 70% 70%, rgba(123,75,255,0.06), transparent 30%);
    filter: blur(12px);
    z-index:2;
    width: calc(100% + 24px); height: calc(100% + 24px);
    pointer-events:none;
  }}

  .core .ring {{
    position:absolute; width:100%; height:100%; border-radius:50%; z-index:3;
  }}
  .ring .spin {{
    position:absolute; inset:0; border-radius:50%;
    border: 2px solid transparent;
    border-top-color: rgba(0,224,255,0.6);
    border-right-color: rgba(123,75,255,0.35);
    transform-origin:center;
    animation: spinSlow 10s linear infinite;
    filter:drop-shadow(0 0 18px rgba(0,224,255,0.08));
  }}
  .ring .spin.two {{
    border-top-color: rgba(123,75,255,0.6);
    border-left-color: rgba(0,224,255,0.18);
    animation-direction: reverse;
    animation-duration: 14s;
    transform: scale(0.86);
  }}
  @keyframes spinSlow{{ from{{transform:rotate(0deg)}} to{{transform:rotate(360deg)}} }}

  .core .sphere {{
    position:relative; width:120px; height:120px; border-radius:50%;
    background: radial-gradient(circle at 40% 30%, rgba(255,255,255,0.14), rgba(0,224,255,0.07)), linear-gradient(180deg, rgba(8,18,40,0.8), rgba(2,6,20,0.9));
    box-shadow: inset 0 6px 18px rgba(255,255,255,0.02), 0 20px 50px rgba(0,224,255,0.06);
    display:flex; align-items:center; justify-content:center; z-index:5;
    transform: translateZ(20px);
    overflow:visible;
  }}

  .sphere::after{{
    content:""; position:absolute; inset:0; border-radius:50%;
    box-shadow: 0 0 28px rgba(0,224,255,0.14), 0 0 64px rgba(123,75,255,0.06);
    pointer-events:none;
  }}

  .label {{
    font-weight:800; font-size:28px; letter-spacing:2px; color:#e9fbff;
    text-shadow: 0 0 12px rgba(0,224,255,0.5), 0 0 30px rgba(123,75,255,0.12);
    z-index:6; transform: translateZ(30px);
  }}

  .halo {{
    position:absolute; inset:0; border-radius:50%; z-index:4; pointer-events:none;
    background: conic-gradient(from 180deg at 50% 50%, rgba(0,224,255,0.06), rgba(123,75,255,0.04), transparent 40%);
    filter: blur(6px);
    animation: haloRotate 8s linear infinite;
  }}
  @keyframes haloRotate{{from{{transform:rotate(0deg)}} to{{transform:rotate(360deg)}}}}

  .datetime {{
    margin-top:18px; z-index:6; text-align:center;
    color:var(--neon1);
    font-weight:700;
    font-size:16px;
    letter-spacing:1px;
    text-shadow: 0 0 10px rgba(0,224,255,0.2);
    display:flex; flex-direction:column; gap:6px; align-items:center;
  }}
  .datetime .time {{
    font-family: "Orbitron", "Segoe UI", sans-serif;
    font-size:28px; color:#dffbff;
    text-shadow: 0 0 18px rgba(0,224,255,0.35);
  }}
  .datetime .date {{
    font-size:13px; color:#b9e9ff;
    opacity:0.9;
  }}

  .controls {{
    z-index:6; margin-top:auto; width:100%; display:flex; align-items:center; gap:12px; margin-top:24px;
  }}
  .input {{
    flex:1; height:48px; border-radius:14px; padding:10px 16px;
    background:var(--glass); border:1px solid rgba(255,255,255,0.04);
    color:#e8f6ff; outline:none; font-size:15px; box-shadow: inset 0 4px 10px rgba(0,0,0,0.35);
  }}
  .controls .right {{
    display:flex; gap:10px;
  }}
  .icon-btn {{
    width:48px; height:48px; border-radius:12px; border:none; background: linear-gradient(180deg, #0c1228, #05051a);
    color:var(--neon1); display:flex; align-items:center; justify-content:center; cursor:pointer; font-size:18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.5);
    border:1px solid rgba(0,224,255,0.06);
    transition: transform .12s ease, box-shadow .12s ease;
  }}
  .icon-btn:hover{{ transform:translateY(-4px); box-shadow: 0 18px 36px rgba(0,224,255,0.08); }}

  /* ==== UPDATED POPUP ANIMATION SYSTEM ==== */
  .popup {{
    position: absolute; width:320px; min-height:120px; border-radius:12px; padding:14px;
    background: linear-gradient(180deg, rgba(10,12,22,0.98), rgba(12,14,30,0.96));
    border:1px solid rgba(0,224,255,0.06);
    box-shadow: 0 30px 60px rgba(3,8,30,0.7), 0 6px 18px rgba(0,224,255,0.04);
    display:none; z-index:20; cursor: move;
    transition: all 0.4s ease;
  }}
  #appPopup {{ left:-340px; top:120px; }}
  #settingsPopup {{ right:-340px; top:140px; }}

  #appPopup.active {{ left:40px; animation: slideFromLeft 0.4s ease; }}
  #settingsPopup.active {{ right:40px; animation: slideFromRight 0.4s ease; }}

  @keyframes slideFromLeft {{
    from {{ transform: translateX(-40px); opacity: 0; }}
    to {{ transform: translateX(0); opacity: 1; }}
  }}
  @keyframes slideFromRight {{
    from {{ transform: translateX(40px); opacity: 0; }}
    to {{ transform: translateX(0); opacity: 1; }}
  }}

  .popup .head {{ display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:8px; color:var(--neon1); font-weight:700; }}
  .popup .close {{
    width:34px; height:34px; border-radius:8px; display:inline-grid; place-items:center; background: rgba(255,255,255,0.02); cursor:pointer;
    color:#fff; border:1px solid rgba(255,255,255,0.03);
  }}
  .popup .close:hover{{ color:var(--neon1); transform:scale(1.08) }}

  @media (max-width:560px){{
    .container{{ width: 94%; height: 86vh; padding:18px; }}
    .core{{ width:180px; height:180px }}
    .sphere{{ width:100px; height:100px }}
  }}
</style>
</head>
<body>

  <div class="container" id="container">
    <div class="topbar" style="position:relative; z-index:6;">
      <div class="title"><span class="dot"></span> ISHA Assistant</div>
      <div style="opacity:0.8; font-size:13px; color:#bfefff">v 6.1. Futuristic</div>
    </div>

    <div class="stage">
      <canvas id="particles"></canvas>
      <div class="core" aria-hidden="true">
        <div class="aura"></div>
        <div class="ring">
          <div class="spin"></div>
          <div class="spin two"></div>
        </div>
        <div class="halo"></div>
        <div class="sphere">
          <div class="label">ISHA</div>
        </div>
      </div>
    </div>

    <div class="datetime" id="datetime">
      <div class="time" id="time">00:00:00</div>
      <div class="date" id="date">Loading date...</div>
    </div>

    <div class="controls" style="position:relative; z-index:6;">
      <input class="input" id="cmd" placeholder="Type command or ask ISHA..." />
      <div class="right">
        <button class="icon-btn" id="appBtn" title="Apps">🧩</button>
        <button class="icon-btn" id="settingsBtn" title="Settings">⚙️</button>
        <button class="icon-btn" id="voiceBtn" title="Voice">🎤</button>
      </div>
    </div>
  </div>

  <!-- Popups -->
  <div class="popup" id="appPopup">
    <div class="head"><div>📱 Applications</div><div class="close" data-close="appPopup">✕</div></div>
    <div style="font-size:14px; color:#cfeeff;">
        {apps_html}
    </div>
  </div>

  <div class="popup" id="settingsPopup">
    <div class="head"><div>⚙️ Settings</div><div class="close" data-close="settingsPopup">✕</div></div>
    <div style="font-size:14px; color:#cfeeff;">
        {settings_html}
    </div>
  </div>

<script>
(function(){{
  const canvas = document.getElementById('particles');
  const ctx = canvas.getContext('2d');
  let w = canvas.width = canvas.clientWidth;
  let h = canvas.height = canvas.clientHeight;
  const particles = [];
  const count = Math.round((w*h)/7000);
  function rand(min,max){{ return Math.random()*(max-min)+min; }}
  function resize(){{
    w = canvas.width = canvas.clientWidth;
    h = canvas.height = canvas.clientHeight;
    particles.length = 0;
    for(let i=0;i<count;i++){{
      particles.push({{
        x: Math.random()*w,
        y: Math.random()*h,
        r: rand(0.6,2.4),
        vx: rand(-0.2,0.2),
        vy: rand(-0.05,0.05),
        hue: Math.random() > 0.6 ? 200 + Math.random()*50 : 260 + Math.random()*30,
        alpha: rand(0.06,0.25)
      }});
    }}
  }}
  window.addEventListener('resize', resize);
  resize();
  function draw(){{
    ctx.clearRect(0,0,w,h);
    const g = ctx.createRadialGradient(w*0.5,h*0.35,10,w*0.5,h*0.35,Math.max(w,h));
    g.addColorStop(0,'rgba(0,0,0,0)');
    g.addColorStop(1,'rgba(0,0,0,0.25)');
    ctx.fillStyle = g;
    ctx.fillRect(0,0,w,h);
    for(const p of particles){{
      p.x += p.vx;
      p.y += p.vy;
      if(p.x < -20) p.x = w+20;
      if(p.x > w+20) p.x = -20;
      if(p.y < -20) p.y = h+20;
      if(p.y > h+20) p.y = -20;
      ctx.beginPath();
      ctx.fillStyle = `hsla(${{p.hue}},90%,60%,${{p.alpha}}`;
      ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fill();
    }}
    requestAnimationFrame(draw);
  }}
  draw();
}})();

function updateDateTime(){{
  const now = new Date();
  const timeEl = document.getElementById('time');
  const dateEl = document.getElementById('date');
  const optsTime = {{ hour:'2-digit', minute:'2-digit', second:'2-digit', hour12:false }};
  timeEl.textContent = now.toLocaleTimeString([], optsTime);
  const optsDate = {{ weekday:'short', year:'numeric', month:'short', day:'numeric' }};
  dateEl.textContent = now.toLocaleDateString([], optsDate);
}}
setInterval(updateDateTime, 500);
updateDateTime();

function makeDraggable(el){{
  let dragging=false, ox=0, oy=0;
  el.addEventListener('mousedown', (e)=>{{
    dragging=true;
    ox = e.clientX - el.offsetLeft;
    oy = e.clientY - el.offsetTop;
    el.style.transition = 'none';
    document.body.style.userSelect='none';
  }});
  window.addEventListener('mousemove', (e)=>{{
    if(!dragging) return;
    el.style.left = (e.clientX - ox) + 'px';
    el.style.top = (e.clientY - oy) + 'px';
  }});
  window.addEventListener('mouseup', ()=>{{
    if(dragging){{
      dragging=false;
      el.style.transition = '';
      document.body.style.userSelect='';
    }}
  }});
}}

const appBtn = document.getElementById('appBtn');
const settingsBtn = document.getElementById('settingsBtn');
const voiceBtn = document.getElementById('voiceBtn');
const appPopup = document.getElementById('appPopup');
const settingsPopup = document.getElementById('settingsPopup');

appBtn.addEventListener('click', () => {{
  const isActive = appPopup.classList.toggle('active');
  if (isActive) {{
    appPopup.style.display = 'block';
    settingsPopup.classList.remove('active');
    settingsPopup.style.display = 'none';
  }} else {{
    setTimeout(()=> appPopup.style.display = 'none', 400);
  }}
}});

settingsBtn.addEventListener('click', () => {{
  const isActive = settingsPopup.classList.toggle('active');
  if (isActive) {{
    settingsPopup.style.display = 'block';
    appPopup.classList.remove('active');
    appPopup.style.display = 'none';
  }} else {{
    setTimeout(()=> settingsPopup.style.display = 'none', 400);
  }}
}});

document.querySelectorAll('.close').forEach(btn=>{{
  btn.addEventListener('click', () => {{
    const id = btn.dataset.close;
    if(id) document.getElementById(id).classList.remove('active');
    setTimeout(()=> document.getElementById(id).style.display='none', 400);
  }});
}});

makeDraggable(appPopup);
makeDraggable(settingsPopup);

// Add click events to items
document.querySelectorAll('.app-item').forEach(item => {{
  item.addEventListener('click', () => {{
    const cmd = item.getAttribute('data-command');
    sendCommand(cmd);
    appPopup.classList.remove('active');
    setTimeout(() => appPopup.style.display = 'none', 400);
  }});
}});
document.querySelectorAll('.setting-item').forEach(item => {{
  item.addEventListener('click', () => {{
    const cmd = item.getAttribute('data-command');
    sendCommand(cmd);
    settingsPopup.classList.remove('active');
    setTimeout(() => settingsPopup.style.display = 'none', 400);
  }});
}});

// For command sending
function sendCommand(cmd) {{
  fetch(`/command?cmd=${{encodeURIComponent(cmd)}}`)
  .then(res => res.text())
  .then(text => {{
    console.log('Response:', text);
  }})
  .catch(err => {{
    console.error('Error:', err);
  }});
}}

document.getElementById('cmd').addEventListener('keydown', (e)=>{{
  if(e.key === 'Enter'){{
    const v = e.target.value.trim();
    if(!v) return;
    sendCommand(v);
    e.target.value = '';
  }}
}});

// For voice toggle
voiceBtn.addEventListener('click', ()=>{{
  fetch('/voice')
  .then(res => res.text())
  .then(text => {{
    voiceBtn.animate([
      {{boxShadow:'0 8px 20px rgba(0,224,255,0.04)'}},
      {{boxShadow:'0 18px 40px rgba(0,224,255,0.12)'}}
    ], {{duration:400, direction:'alternate'}});
  }});
}});

// Add Alt + M keybinding for toggling microphone
document.addEventListener('keydown', (e) => {{
  if (e.altKey && e.key.toLowerCase() === 'm') {{
    e.preventDefault(); // Prevent default browser behavior
    voiceBtn.click(); // Simulate click on the voice button
  }}
}});
</script>
</body>
</html>
        """
        return html

    def select_microphone(self):
        """Allow user to select a microphone from available devices."""
        try:
            mic_names = sr.Microphone.list_microphone_names()
            if not mic_names:
                message = "No microphones detected. Please check your hardware and permissions."
                self.speak(message)
                print(message)
                return

            mic_list = "\n".join([f"{i}: {name}" for i, name in enumerate(mic_names)])
            selected = self.user_input(f"Available microphones:\n{mic_list}\nEnter the index number of the microphone to use:")
            
            if selected is not None:
                try:
                    index = int(selected)
                    if 0 <= index < len(mic_names):
                        self.microphone = sr.Microphone(device_index=index)
                        with self.microphone as source:
                            self.recognizer.adjust_for_ambient_noise(source, duration=2)
                        message = f"Selected microphone: {mic_names[index]}. Voice recognition enabled."
                        self.speak(message)
                        print(message)
                    else:
                        message = "Invalid microphone index. Please try again."
                        self.speak(message)
                        print(message)
                except ValueError:
                    message = "Invalid input. Please enter a number."
                    self.speak(message)
                    print(message)
                except (OSError, sr.RequestError) as e:
                    message = f"Failed to initialize selected microphone: {str(e)}. Try another one."
                    self.speak(message)
                    print(message)
        except Exception as e:
            message = f"Error accessing microphone list: {str(e)}. Ensure PyAudio is installed and microphone permissions are granted."
            self.speak(message)
            print(message)

    def user_input(self, prompt):
        console = ctypes.windll.kernel32.GetConsoleWindow()
        if console:
            ctypes.windll.user32.ShowWindow(console, 5)  # Show console
        res = input(prompt)
        if console:
            ctypes.windll.user32.ShowWindow(console, 0)  # Hide again
        return res

    def set_female_voice(self):
        """Set the TTS engine to use a female voice, with fallback and logging."""
        try:
            voices = self.engine.getProperty('voices')
            selected_voice = None
            
            logging.info("Available voices: %s", [voice.name for voice in voices])
            
            for voice in voices:
                if "zira" in voice.name.lower() or "female" in voice.name.lower():
                    selected_voice = voice
                    break
            
            if not selected_voice:
                selected_voice = voices[0] if voices else None
                logging.warning("No female voice found, falling back to default voice")
                message = "No female voice available, using default voice."
                self.speak(message)  
            else:
                logging.info("Selected female voice: %s", selected_voice.name)
            
            if selected_voice:
                self.engine.setProperty('voice', selected_voice.id)
                self.engine.say("Initializing voice")
                self.engine.runAndWait()
            else:
                logging.error("No voices available for text-to-speech")
                message = "No voices available for text-to-speech. Please check system TTS settings."
                self.speak(message)  
        except Exception as e:
            logging.error(f"Failed to set female voice: {str(e)}")
            message = "Failed to initialize text-to-speech. Please check audio drivers or TTS installation."
            self.speak(message)  

    def check_internet(self):
        current_time = time.time()
        if current_time - self.last_internet_check < self.internet_check_interval:
            return self.internet_status

        self.last_internet_check = current_time
        for host in [("8.8.8.8", 80), ("1.1.1.1", 80)]:
            try:
                socket.create_connection(host, timeout=2)
                self.internet_status = True
                return True
            except (socket.gaierror, socket.timeout):
                continue
        self.internet_status = False
        return False

    def toggle_voice(self):
        if self.microphone is None:
            self.select_microphone()
            if self.microphone is None:
                message = "Voice recognition is disabled due to missing dependencies or hardware. Use text input instead."
                self.speak(message)
                print(message)
                return
        self.is_listening = not self.is_listening
        if self.is_listening:
            message = "Microphone is now on"
            self.speak(message)
            print(message)
            threading.Thread(target=self.listen_voice, daemon=True).start()
        else:
            message = "Microphone is now off"
            self.speak(message)
            print(message)

    def wish_me(self):
        current_hour = datetime.datetime.now().hour
        greeting = (
            "Good morning" if 5 <= current_hour < 12 else
            "Good afternoon" if 12 <= current_hour < 17 else
            "Good evening" if 17 <= current_hour < 21 else
            "Good night"
        )
        self.speak(greeting) 
        time.sleep(1)
        message = "I am Isha, Intelligent System for Human Assistance. Welcome!"
        self.speak(message)  
        time.sleep(2) 

    def listen(self):
        if self.microphone is None:
            self.select_microphone()
            if self.microphone is None:
                message = "Voice recognition is disabled due to missing dependencies or hardware. Please use text input."
                self.speak(message)
                print(message)
                logging.error(message)
                query = self.user_input("Voice not available. Enter your command: ")
                return query.lower() if query else None

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                retries = 3
                for attempt in range(retries):
                    try:
                        audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
                        query = self.recognizer.recognize_google(audio).lower()
                        logging.info(f"Recognized voice command: {query}")
                        return query
                    except sr.WaitTimeoutError:
                        message = f"No speech detected (attempt {attempt + 1}/{retries}). Retrying..."
                        self.speak(message)
                        print(message)
                        logging.warning(message)
                    except sr.UnknownValueError:
                        message = f"Could not understand audio (attempt {attempt + 1}/{retries}). Retrying..."
                        self.speak(message)
                        print(message)
                        logging.warning(message)
                    except sr.RequestError as e:
                        message = f"Speech recognition service error: {str(e)}. Falling back to text input."
                        self.speak(message)
                        print(message)
                        logging.error(message)
                        break
                message = "Voice input failed after retries. Please use text input."
                self.speak(message)
                print(message)
                logging.error(message)
                query = self.user_input("Voice not available. Enter your command: ")
                return query.lower() if query else None
        except Exception as e:
            message = f"Voice input failed: {str(e)}. Please use text input."
            self.speak(message)
            print(message)
            logging.error(message)
            query = self.user_input("Voice not available. Enter your command: ")
            return query.lower() if query else None

    def listen_voice(self):
        while self.is_listening:
            command = self.listen()
            if command:
                self.process_command(command)
            time.sleep(1)

    def process_command(self, command):
        """Process voice or text commands and return response."""
        if not command:
            response = "No command received. Please try again."
            self.speak(response)
            return response

        command = command.lower().strip()
        logging.info(f"Processing command: {command}")

        # Handle specific commands
        if "open" in command:
            for app, cmd in self.commands_dict.items():
                if app in command:
                    try:
                        if cmd.startswith("http") or cmd.startswith("ms-"):
                            webbrowser.open(cmd)
                        else:
                            os.startfile(cmd)
                        response = f"Opening {app}..."
                        self.speak(response)
                        return response
                    except Exception as e:
                        response = f"Failed to open {app}: {str(e)}"
                        self.speak(response)
                        logging.error(response)
                        return response

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            response = f"The current time is {current_time}"
            self.speak(response)
            return response

        if "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            response = f"Today's date is {current_date}"
            self.speak(response)
            return response

        if "who are you" in command or "your name" in command:
            response = "मैं इशा हूँ, तुम्हारा पर्सनल असिस्टेंट! नमस्ते! 😊"
            self.speak(response)
            return response

        # Fallback to Ollama for conversational responses
        try:
            self.chat_history.append(HumanMessage(content=command))
            ai_response = self.llm.invoke(self.chat_history)
            response = ai_response.content
            self.chat_history.append(AIMessage(content=response))
            self.speak(response)
            logging.info(f"Ollama response: {response}")
            return response
        except Exception as e:
            response = "Sorry, I couldn't process that request. Please try again."
            self.speak(response)
            logging.error(f"Ollama error: {str(e)}")
            return response

########--------------------------------------------- # The code for thiis is in another file, Which i will add later #--------------------------------------------- ########

########--------------------------------------------- # The code for thiis is in another file, Which i will add later #--------------------------------------------- ########

    def speak(self, text):
        def run_speak():
            try:
                self.engine.stop()
                time.sleep(0.5) 
                if self.engine._inLoop:
                    logging.warning("TTS engine is busy, attempting to reinitialize: %s", text)
                    self.engine.endLoop()
                    time.sleep(0.7) 
                    self.engine = pyttsx3.init()
                    self.set_female_voice() 
                self.engine.say(text)
                self.engine.runAndWait()
                logging.info(f"Successfully spoke: {text}")
            except Exception as e:
                logging.error(f"Speech error: {str(e)} - Text: {text}")
        threading.Thread(target=run_speak, daemon=True).start()
        time.sleep(0.7) 

if __name__ == "__main__":
    try:
        console = ctypes.windll.kernel32.GetConsoleWindow()
        if console:
            ctypes.windll.user32.ShowWindow(console, 0) 
        app = IshaAssistant()
        while True:
            time.sleep(1)
    except Exception as e:
        logging.error(f"Application failed to start: {str(e)}")
        print(f"Error: Application failed to start: {str(e)}")
