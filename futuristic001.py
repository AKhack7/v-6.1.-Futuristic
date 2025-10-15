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
        
        self.wish_me()
        
        self.start_server()

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

    def play_song01(self):
        if self.check_internet():
            playlist_links = [
                "https://youtu.be/TtgzkepDNhQ?si=WUDM3Q6x8DyizG5a",
                "https://youtu.be/7IpOlGos6Bs?si=6TEn68tNr2Qo77f_",
                "https://youtu.be/jnDGIe1J-Yk?si=KCwaEXKNI8zrj8Qp",
                "https://youtu.be/MhXCj8E9CZU?si=fe9mpvtLWGnNJuzr",
                "https://youtu.be/dFbdAaVWRcM?si=Ig1Y4XkgyvruDLBU",
                "https://youtu.be/hHuG7FIKgtc?si=lTBdOKhm2T7_IWcq",
                "https://youtu.be/MIMLtLkQDtE?si=sCQmOiF_NxtPA0If",
                "https://youtu.be/OErqCa7v03U?si=JL4dfBMwVYkFVai2",
                "https://youtu.be/SRyh893Jxwo?si=jY86nVy2Ifken84n",
                "https://youtu.be/I2tQZEMPH54?si=tzYHKf4wYg6QKQB3",
                "https://youtu.be/gPpQNzQP6gE?si=PbOooxxsdf-vcWUp",
                "https://youtu.be/YzfbpPQLmtE?si=sTGUJj80Gx8_ES2L",
                "https://youtu.be/dFbdAaVWRcM?si=1UNY5MyanPvW4qLE",
                "https://youtu.be/XpWVQzBXxDA?si=nrF9BbNn6o8PjsEX",
                "https://youtu.be/NW6Dgax2d6I?si=Q6Qwol39C0yP4dB5"
            ]
            try:
                url = random.choice(playlist_links)
                webbrowser.open(url)
                time.sleep(5)  # Increased delay for browser loading
                pyautogui.press("k")  # Play video
                message = "Playing a song from YouTube"
                self.speak(message)
                print(message)
                logging.info(message)
                return message
            except Exception as e:
                message = f"Failed to play song from YouTube: {str(e)}. Trying local music..."
                self.speak(message)
                print(message)
                logging.error(message)
                return self.play_local_song()
        else:
            message = "No internet connection. Trying local music..."
            self.speak(message)
            print(message)
            logging.warning(message)
            return self.play_local_song()

    def play_song02(self):
        if self.check_internet():
            playlist_links = [
            "https://youtu.be/mClF6mJV5xM?si=4TW7kdAQfkOKuX3q",
            "https://youtu.be/BBAyRBTfsOU?si=7GOhfjA85eRDHw5m",
            "https://youtu.be/VuG7FfrXF0?si=-KryrmufQE8M7inM",
            "https://youtu.be/hgi2MYAFgE8?si=oJGGL71LdVpoizYA",
            "https://youtu.be/q1zbZAR8Zpg?si=5XWeo8dOtpdbL4tj",
            "https://youtu.be/j9GxZ6MtJSU?si=uPgmsPnkwL4FXCTm",
            "https://youtu.be/NW6Dgax2d6I?si=Uin23C695HcaDBsx",
            "https://youtu.be/MhXCj8E9CZU?si=-uNMwkST4JMUptlp"
            ]
            try:
                url = random.choice(playlist_links)
                webbrowser.open(url)
                time.sleep(5)
                pyautogui.press("k")
                message = "Playing a lofi song"
                self.speak(message)
                print(message)
                logging.info(message)
                return message
            except Exception as e:
                message = f"Failed to play lofi song from YouTube: {str(e)}. Trying local music..."
                self.speak(message)
                print(message)
                logging.error(message)
                return self.play_local_song()
        else:
            message = "No internet connection. Trying local music..."
            self.speak(message)
            print(message)
            logging.warning(message)
            return self.play_local_song()

    def play_song03(self):
        if self.check_internet():
            playlist_links = [
            "https://youtu.be/i61nN7hcbPA?si=LtwJVEhMR8hISG9",
            "https://youtu.be/5Lyw1XnaFjo?si=usBbK8O1Ag_3qgUl",
            "https://youtu.be/EjPXobiqy4s?si=jkxA5TFiS55N3e_t",
            "https://youtu.be/qSqqvhjNet4?si=5SAVAHe1mQY87Tnz"
            ]
            try:
                url = random.choice(playlist_links)
                webbrowser.open(url)
                time.sleep(5)
                pyautogui.press("k")
                message = "Playing a sad song"
                self.speak(message)
                print(message)
                logging.info(message)
                return message
            except Exception as e:
                message = f"Failed to play sad song from YouTube: {str(e)}. Trying local music..."
                self.speak(message)
                print(message)
                logging.error(message)
                return self.play_local_song()
        else:
            message = "No internet connection. Trying local music..."
            self.speak(message)
            print(message)
            logging.warning(message)
            return self.play_local_song()

    def play_song04(self):
        if self.check_internet():
            playlist_links = [
            "https://youtu.be/6d5SS0gS5bU?si=cB35VDNsJMHVYpMR",
            "https://youtu.be/FTI96c3mGG0?si=P4e1SiqZH_rhpp6R",
            "https://youtu.be/gqgi0h97OVo?si=DN-tel-PO1EmWMV0",
            "https://youtu.be/axepn8QqxRk?si=rLm6sMNyvVC4_U8b",
            "https://youtu.be/I-_LHvTeVy4?si=gND1OdGGGItn4u75",
            "https://youtu.be/i1HpSzorjlc?si=HLRc_0pyqa3sDwyX",
            "https://youtu.be/zing4uQ3dR4?si=ht6f4myziP3zdQf9",
            "https://youtu.be/BsqrmY91nUQ?si=n6GQyvvC4jqIhTKj",
            "https://youtu.be/75a1BlcYZ2Q?si=IFHXuxp2aT9oPH0D",
            "https://youtu.be/4HRC6c5-2lQ?si=m7PM8SvxxRd3fYDU",
            "https://youtu.be/7lfFZs50JHM?si=DujIefGwo8dj_2hl",
            "https://youtu.be/u5JRSsoBXT0?si=reyrnW2uSUhgsBzP",
            "https://youtu.be/GTOdXVfrXF0?si=pr3olOdtYk9WnGMi",
            "https://youtu.be/84TjXsRHf6Q?si=fscJqVOIpdN6q8Qg"
            ]
            try:
                url = random.choice(playlist_links)
                webbrowser.open(url)
                time.sleep(5)
                pyautogui.press("k")
                message = "Playing a romantic song"
                self.speak(message)
                print(message)
                logging.info(message)
                return message
            except Exception as e:
                message = f"Failed to play romantic song from YouTube: {str(e)}. Trying local music..."
                self.speak(message)
                print(message)
                logging.error(message)
                return self.play_local_song()
        else:
            message = "No internet connection. Trying local music..."
            self.speak(message)
            print(message)
            logging.warning(message)
            return self.play_local_song()

    def play_local_song(self):
        music_dir = os.path.expanduser("~/Music")
        music_files = glob.glob(os.path.join(music_dir, "*.mp3"))
        if music_files:
            song = random.choice(music_files)
            try:
                os.startfile(song)
                message = f"Playing {os.path.basename(song)} from local storage"
                self.speak(message)
                print(message)
                logging.info(message)
                return message
            except Exception as e:
                message = f"Failed to play local song: {str(e)}"
                self.speak(message)
                print(message)
                logging.error(message)
                return message
        else:
            message = "No music files found in the Music directory."
            self.speak(message)
            print(message)
            logging.warning(message)
            return message

    def open_google(self):
        try:
            webbrowser.open("https://www.google.com")
            message = "Opening Google"
            self.speak(message)
            print(message)
            logging.info(message)
            return message
        except Exception as e:
            message = f"Failed to open Google: {str(e)}"
            self.speak(message)
            print(message)
            logging.error(message)
            return message

    def handle_settings_apps_commands(self, command):
        cmd = None
        if command in self.commands_dict:
            cmd = self.commands_dict[command]
        elif command in self.settings_display_to_cmd:
            cmd = self.settings_display_to_cmd[command]
        elif command in self.apps_display_to_cmd:
            cmd = self.apps_display_to_cmd[command]

        if cmd:
            try:
                if cmd.startswith("http"):
                    webbrowser.open(cmd)
                elif cmd.startswith("ms-") or ":" in cmd:
                    subprocess.run(["start", "", cmd], shell=True)
                else:
                    subprocess.run(["start", "", cmd], shell=True)
                message = f"Opening {command}"
                self.speak(message)
                print(message)
                logging.info(message)
                return message
            except Exception as e:
                message = f"Failed to open {command}: {str(e)}"
                self.speak(message)
                print(message)
                logging.error(message)
                return message
        return None

    def process_command(self, command):
        logging.info(f"Processing command: {command}, Internet: {self.internet_status}")
        command = command.lower().strip()

        if self.pending:
            self.input_queue.put(command)
            return "Input received for pending request."

        # Handle "open" commands for apps and settings
        if command.startswith("open "):
            app_or_setting = command[5:].strip()
            result = self.handle_settings_apps_commands(app_or_setting)
            if result:
                return result

        # Time commands
        if command in [
            "what is the time", "tell me the time", "current time", "time now",
            "what time is it", "what's the time", "time", "what time"
        ]:
            message = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(message)
            return message

        # Date commands
        elif command in [
            "what is the date", "tell me the date", "current date", "date now",
            "what date is it", "what's the date", "date", "what date"
        ]:
            message = datetime.datetime.now().strftime("%A, %B %d, %Y")
            self.speak(message)
            return message

        # Play song command
        elif command in [
            "play song", 
            "play a song", 
            "isha play music",
            "isha play song", 
            "isha play a song", 
            "isha play music"
            ]:
            return self.play_song01()
        

        elif command in [
            "play lofi song", 
            "play a lofi song", 
            "play lofi music",
            "isha play lofi song", 
            "isha play a lofi song", 
            "isha play lofi music",
            "lofi song",
            "isha lofi song"
            ]:

            return self.play_song02()
        
        elif command in [
            "play sad song", 
            "play a sad song", 
            "play sad music",
            "isha play sad song", 
            "isha play a sad song", 
            "isha play sad music",
            "sad song",
            "isha sad song"

            ]:
            return self.play_song03()
        
        elif command in [
            "play romantic song", 
            "play a romantic song", 
            "play romantic music",
            "isha play romantic song", 
            "isha play a romantic song", 
            "isha play romantic music",
            "isha romantic song",
            "romantic song"
            ]:
            return self.play_song04()

        elif "hello" in command or "hello isha" in command or "hi" in command or "hi isha" in command:
            self.hello()
        elif "thank you isha" in command or "thank you" in command or "thanks isha" in command:
            self.thank_you_reply()
        elif "what you mane" in command or "what is your name" in command:
            self.what_is_your_name()
        elif "good morning" in command or "morning" in command or "good morning isha" in command or "isha good morning" in command:
            self.morningtime()
        elif (
            "restart" in command
            or "isha pc restart now" in command
            or "restart now" in command
            or "isha restart the pc" in command
            or "restart pc" in command
            or "isha restart pc" in command
            or "reboot" in command
            or "isha reboot pc" in command
            or "reboot pc" in command
            or "isha reboot now" in command
            or "reboot now" in command
            or "restart computer" in command
            or "isha restart computer" in command
            or "reboot computer" in command
            or "isha reboot computer" in command
            or "computer restart" in command
            or "isha computer restart" in command
            or "computer reboot" in command
            or "isha computer reboot" in command
            or "mujhe pc restart karo" in command
            or "isha pc restart karo" in command
        ):
            self.restart_pc()

        elif  (
            "shutdown" in command
            or "isha shutdown now" in command
            or "shutdown now" in command
            or "shutdown pc" in command
            or "isha shutdown pc" in command
            or "pc shutdown" in command
            or "isha pc shutdown" in command
            or "turn off pc" in command
            or "isha turn off pc" in command
            or "isha turn off the pc" in command
            or "turn off computer" in command
            or "isha turn off computer" in command
            or "computer shutdown" in command
            or "isha computer shutdown" in command
            or "power off pc" in command
            or "isha power off pc" in command
            or "isha pc power off" in command
            or "mujhe pc band kar do" in command
            or "isha pc band kar do" in command
            or "band karo pc" in command
        ):
            self.shutdown_pc()

        elif command in [
            "open run command",
            "open run",
            "isha open run command",
            "run command",
            "run",
            "isha run",
            "isha open run",
            "start run",
            "isha start run",
            "execute run",
            "isha execute run",
            "run box",
            "open run box",
            "isha run box kholo",
            "run dialog",
            "open run dialog",
            "isha run dialog",
            "isha run kholo",
            "run kholo",
            "mujhe run chahiye",
            "isha run dikhao"
        ]:

            self.open_run_command()
        elif command in [
            "open setting",
            "open settings",
            "isha open setting",
            "isha open settings",
            "settings",
            "setting",
            "isha setting",
            "isha settings",
            "start settings",
            "open pc settings",
            "open system settings",
            "isha open system settings",
            "system settings",
            "computer settings",
            "isha computer settings",
            "windows settings",
            "open windows settings",
            "isha windows settings",
            "mujhe setting dikhao",
            "isha setting kholo",
            "setting kholo",
            "all settings",
            "isha all settings",
            "control setting",
            "control settings",
            "isha control settings"
        ]:

            self.open_settings()

        if command in [
            "what is the time",
            "isha what is the time",
            "aaj time kya hai",
            "time",
            "tell me the time",
            "current time",
            "please tell me time",
            "time batao",
            "abhi kitne baje hain",
            "abhi ka time kya hai",
            "time bolo",
            "isha time bolo",
            "kya time hai",
            "abhi ka time",
            "now time",
            "current clock",
            "please tell me the current time",
        ]:
            self.get_time()

        elif "find now" in command or "give me a answer" in command or "isha find now" in command or "search" in command or "search now" in command or "isha search now" in command or "isha find" in command or "find" in command or "isha search" in command:
            self.find_now()

        elif "open phone camera" in command or "isha open phone camera" in command or "phone camera" in command:
            self.came2()

        elif command.startswith("solve ") or re.match(r"^\d+\s*[\+\-\*/]\s*\d+", command):
            expression = command[6:] if command.startswith("solve ") else command
            self.solve_math(expression)

        elif command in [
            "open calculator",
            "calculator",
            "isha open calculator",
            "isha calculator",
            "calculator khol do",
            "calculator chalao",
            "isha calculator kholo",
            "open calc",
            "calc",
            "start calculator",
            "run calculator",
            "mujhe calculator chahiye",
            "calculate",
            "isha calculate",
            "calci",
            "isha calci",
            "please open calculator"
        ]:
            self.open_calculator()

        elif command in ["open minimize", "minimize"]:
            self.minimize_windows()

        elif command in ["search", "app", "file", "setting"]:
            self.open_search()

        elif command in ["news", "show news", "isha show news"]:
            if self.check_internet():
                self.open_news_widget()
            else:
                message = "News requires internet. Opening local news app instead."
                self.speak(message)
                print(message)
                subprocess.run(["start", "msnweather:"], shell=True)

        elif command in [
            "open about setting",
            "about setting",
            "isha open about setting",
            "isha about setting",
            "about this pc",
            "isha about this pc",
            "isha open about this pc",
            "isha open about pc",
            "isha about pc",
            "about pc",
            "open about pc",
            "isha pc details",
            "pc details",
            "isha open pc details",
            "my pc details",
            "isha my pc details",
            "computer details",
            "isha computer details",
            "isha system info",
            "system info",
            "open system info",
            "isha open system info",
            "mujhe pc ke bare me batao",
            "pc ke bare me",
            "isha pc ke bare me"
        ]:

            self.open_about_settings()

        elif command in [
            "open project screen",
            "show project screen",
            "isha open project screen",
            "isha project screen",
            "isha show me project screen",
            "isha show me a project screen",
            "project screen",
            "open projection",
            "open project",
            "isha open project",
            "isha projection",
            "projection settings",
            "open projection settings",
            "isha projection settings",
            "display project",
            "display projection",
            "connect to display",
            "isha connect to display",
            "projector screen",
            "open projector screen",
            "isha projector screen",
            "screen projection",
            "isha screen projection",
            "isha screen project",
            "mujhe project screen dikhao",
            "project screen kholo",
            "isha project screen kholo"
        ]:

            self.open_project_screen()

        elif command in [
            "enhanced security",
            "isha active enhanced security",
            "isha open enhanced security",
            "open enhanced security",
            "isha open security",
            "isha open windows security",
            "windows security",
            "open windows security",
            "isha windows security",
            "active windows security",
            "activate enhanced security",
            "isha activate enhanced security",
            "security settings",
            "isha security settings",
            "open security settings",
            "isha open security settings",
            "system security",
            "isha system security",
            "enhanced security active",
            "isha enhanced security active",
            "mujhe security dikhao",
            "isha security dikhao"
        ]:

            self.open_performance_settings()

        elif command in [
            "open feedback",
            "showing feedback",
            "show feedback",
            "isha show me feedback",
            "isha show feedback",
            "isha showing a feedback",
            "isha showing feedback",
            "isha open feedback",
            "isha feedback",
            "isha feedbacks",
            "show me a feedbacks",
            "feedback",
            "show feedback hub",
            "open feedback hub",
            "isha open feedback hub",
            "isha show feedback hub",
            "feedback hub",
            "isha feedback hub",
            "mujhe feedback dikhao",
            "isha feedback dikhao",
            "show my feedback",
            "isha show my feedback",
            "display feedback",
            "isha display feedback",
            "isha display feedback hub",
            "feedback panel",
            "isha feedback panel",
            "open feedback panel",
            "isha open feedback panel"
        ]:

            self.open_feedback_hub()

        elif command in  [
            "open xbox",
            "xbox",
            "game bar",
            "open game bar",
            "isha open game bar",
            "isha open xbox",
            "isha xbox",
            "isha start xbox",
            "start xbox",
            "launch xbox",
            "isha launch xbox",
            "isha game bar open karo",
            "game bar kholo",
            "isha game bar chalu karo",
            "xbox chalu karo",
            "isha xbox chalu karo"
        ]:
            self.open_game_bar()

        elif "iti" in command:
            self.open_25()

        elif (
            "youtube" in command
            or "isha youtube" in command
            or "manoranjan suru kiya jaaye" in command
            or "isha open youtube" in command
            or "open youtube" in command
            or "isha chalu karo youtube" in command
            or "isha youtube kholo" in command
            or "youtube chalu karo" in command
        ):
            self.open_youtube()

        elif (
            "instagram" in command
            or "isha open instagram" in command
            or "instagram chalu karo" in command
            or "isha instagram" in command
            or "open instagram" in command
            or "isha instagram kholo" in command
            or "instagram kholo" in command
            or "isha chalu karo instagram" in command
            or "gili gili chu" in command 
            or "gili gili chhu" in command 
            or "gili gili suit" in command
        ): 
            self.open_instagram()

        elif command in ["open mic", "isha open mic", "mic"]:
            self.open_voice_typing()

        elif command in [
            "connect",
            "show all connect",
            "show network",
            "isha show network",
            "isha shw me a all connect network",
            "show all connect network",
            "isha show me network",
            "isha connect panel",
            "network",
            "isha network",
            "open network",
            "isha open network",
            "network settings",
            "isha network settings",
            "mujhe network dikhao",
            "network panel",
            "isha network panel",
            "connected devices",
            "isha connected devices",
            "wifi connections",
            "isha wifi connections",
            "isha show wifi",
            "wifi panel",
            "isha wifi panel"
        ]:

            self.open_connect_panel()

        elif command in [
            "lock screen",
            "screen lock kar do",
            "isha lock screen",
            "isha look screen",
            "lock my pc",
            "isha lock my pc",
            "lock computer",
            "isha lock computer",
            "isha screen lock karo",
            "screen lock",
            "lock now",
            "isha lock now",
            "mujhe screen lock karo",
            "isha mujhe screen lock karo",
            "lock the screen",
            "isha lock the screen"
        ]:
            self.lock_screen()

        elif command in ["show all menu"]:
            self.open_quick_menu()

        elif command in  [
            "open cortana",
            "isha open cortana",
            "isha cortana",
            "launch cortana",
            "isha launch cortana",
            "start cortana",
            "isha start cortana",
            "cortana",
            "isha cortana chalu karo",
            "isha cortana kholo",
            "isha cortana open karo",
            "cortana open",
            "isha open cortana assistant"
        ]:
            self.open_cortana()

        elif command in [
            "open clipboard",
            "show clipboard",
            "isha open clipboard",
            "isha show me clipboard",
            "clipboard",
            "isha clipboard",
            "isha clipboard history",
            "show clipboard history",
            "open clipboard history",
            "isha open clipboard history",
            "clipboard panel",
            "isha clipboard panel",
            "mujhe clipboard dikhao",
            "isha clipboard dikhao",
            "display clipboard",
            "isha display clipboard",
            "show me clipboard",
            "isha show clipboard"
        ]:
            self.open_clipboard_history()

        elif command in ["duplicate window"]:
            self.open_notifications()

        elif "select all text" in command or "select all" in command or "isha select all text" in command or "isha select all" in command:
            self.select_all_text()

        elif (
            "caption chalu karo" in command
            or "caption on" in command
            or "isha on caption" in command
            or "caption band karo" in command
            or "isha caption band karo" in command
            or "isha caption on karo" in command
            or "isha caption off karo" in command
            or "turn on captions" in command
            or "turn off captions" in command
            or "enable captions" in command
            or "disable captions" in command
            or "captions" in command
            or "isha captions" in command
            or "captions on" in command
            or "captions off" in command
            or "isha enable captions" in command
            or "isha disable captions" in command
        ):
            self.toggle_caption()

        elif command in [
            "open download",
            "isha open download",
            "isha open download file",
            "isha open file download",
            "file download",
            "downloads",
            "open downloads",
            "isha open downloads",
            "isha downloads",
            "download folder",
            "isha download folder",
            "open download folder",
            "isha open download folder",
            "my downloads",
            "isha my downloads",
            "download file",
            "isha download file",
            "file downloader",
            "open file downloader",
            "isha open file downloader",
            "download section",
            "isha download section",
            "isha download kholo",
            "download kholo",
            "mujhe download dikhayo",
            "isha downloads dikhao"
        ]:

            self.open_downloads()

        elif ("how much power left" in command
              or "how much power we have" in command 
              or "battery in query" in command
              or "isha how much power left" in command
              or "isha how much power we have" in command 
              or "isha battery in query" in command
              or "battery" in command
              or "isha battery" in command
              or "isha show battery" in command
              or "show battery" in command
            
            ):

            self.btr()

        elif "h1" in command.lower() or "open h1" in command or "isha open h1" in command:
            self.open_chatbox()

        elif "download photo" in command or "download picture" in command or "isha download photo" in command or "isha download picture" in command or "dd photo" in command or "dd picture" in command:
            self.download_picture()

        elif "download reel" in command or "download storie" in command or "download instagram reel" in command or "instagram reel download" in command or "isha download instagram reel" in command or "download instagram stories" in command or "download instagram storie" in command or "isha downloas instagram storie" in command or "isha instagram storie download" in command or "isha instagram stories download" in command or "ist reel" in command:
            self.download_instagram_reel()

        elif "stop song" in command or "stop" in command or "stop music" in command or "isha song band karo" in command:
            self.stop_song()

        elif (
            "mute" in command
            or "unmute" in command
            or "song mute" in command
            or "song unmute" in command
            or "isha song mute" in command
            or "isha song unmute" in command
            or "awaaz band karo" in command
            or "awaaz chalu karo" in command
            or "isha awaaz band karo" in command
            or "isha awaaz chalu karo" in command
            or "band karo song" in command
            or "song band karo" in command
            or "chalu karo song" in command
            or "play music off" in command
            or "pause music" in command
            or "pause song" in command
            or "stop music" in command
            or "stop song" in command
            or "isha music band karo" in command
            or "isha music chalu karo" in command
            or "turn off song" in command
            or "turn on song" in command
            or "turn off music" in command
            or "turn on music" in command
        ):
            self.mute_unmute()

        elif  (
            "full screen" in command
            or "screen full karo" in command
            or "isha full screen" in command
            or "maximize screen" in command
            or "isha maximize screen" in command
            or "screen maximize karo" in command
            or "isha screen maximize karo" in command
            or "screen bada karo" in command
            or "isha screen bada karo" in command
            or "expand screen" in command
            or "isha expand screen" in command
            or "screen expand karo" in command
            or "isha screen expand karo" in command
            or "screen full" in command
            or "isha screen full" in command
            or "bada karo screen" in command
            or "isha bada karo screen" in command
            or "screen enlarge" in command
            or "isha screen enlarge" in command
            or "enlarge screen" in command
        ):

            self.full_screen()

        elif "phone camera off" in command or "off camera phone" in command or "isha phone camera off" in command:
            self.cmaw21()

        # Open Google command
        elif command in ["open google", "launch google", "go to google"]:
            return self.open_google()

        # Weather command
        elif command in ["weather", "check weather", "what's the weather"]:
            return self.get_weather()

        # WhatsApp command
        elif command in ["open whatsapp", "launch whatsapp", "send whatsapp message"]:
            return self.open_whatsapp()

        # Instagram login command
        elif command in ["login instagram", "log into instagram", "open instagram"]:
            return self.login_instagram()

        # Greeting command
        elif command in ["hi", "hello", "hey"]:
            message = "Hello! How can I assist you today?"
            self.speak(message)
            return message

        # Default unrecognized command
        message = f"Command not recognized: {command}"
        self.speak(message)
        return message
    
    def get_weather(self):
        if self.check_internet():
            message = "Which city's weather do you want to check?"
            self.speak(message)
            self.pending = 'weather_city'
            city = self.input_queue.get()
            self.pending = None
            if not city or city.lower() in ["none", "cancel", "no"]:
                message = "No city provided. Please try again."
                self.speak(message)
                return message
            try:
                response = requests.get(f"https://wttr.in/{city}?format=%C+%t", timeout=5)
                response.raise_for_status()
                weather_info = response.text.strip()
                if not weather_info:
                    message = f"No weather data available for {city}."
                    self.speak(message)
                    return message
                # Cache
                with open("weather_cache.txt", "w") as f:
                    f.write(f"{city}:{weather_info}:{int(time.time())}")
                message = f"Weather in {city}: {weather_info}"
                self.speak(message)
                return message
            except requests.RequestException as e:
                message = f"Failed to fetch weather for {city}: {str(e)}. Please check the city name or internet connection."
                self.speak(message)
                return message
        else:
            try:
                with open("weather_cache.txt", "r") as f:
                    cache_data = f.read().strip()
                    if not cache_data:
                        message = "No internet connection and no cached weather available."
                        self.speak(message)
                        return message
                    city, weather_info, timestamp = cache_data.split(":", 2)
                    age = int(time.time()) - int(timestamp)
                    if age < 3600:
                        message = f"No internet. Showing cached weather for {city}: {weather_info}"
                        self.speak(message)
                        return message
                    else:
                        message = "No internet and cached weather is too old."
                        self.speak(message)
                        return message
            except (FileNotFoundError, ValueError) as e:
                message = f"No internet connection and no valid cached weather available: {str(e)}."
                self.speak(message)
                return message

    def open_whatsapp(self):
        if not self.check_internet():
            message = "WhatsApp requires an internet connection. Opening notepad instead."
            self.speak(message)
            subprocess.run(["start", "", "notepad"], shell=True)
            return message

        message = "Please provide a phone number with country code."
        self.speak(message)
        self.pending = 'whatsapp_contact'
        contact = self.input_queue.get()
        self.pending = None
        if contact and re.match(r"^\+\d{10,15}$", contact):
            message = "What message should I send?"
            self.speak(message)
            self.pending = 'whatsapp_message'
            message_text = self.input_queue.get()
            self.pending = None
            if message_text and message_text not in ["none", "cancel", "no"]:
                try:
                    webbrowser.open("https://web.whatsapp.com")
                    time.sleep(20)
                    pywhatkit.sendwhatmsg_instantly(contact, message_text, wait_time=20, tab_close=True)
                    message = f"Message sent to {contact}"
                    self.speak(message)
                    return message
                except Exception as e:
                    message = f"Failed to send WhatsApp message: {str(e)}"
                    self.speak(message)
                    return message
            else:
                message = "No message provided"
                self.speak(message)
                return message
        else:
            message = "Invalid or no contact provided. Please use country code, e.g., +1234567890"
            self.speak(message)
            return message

    def hello(self):
        """Respond to a greeting."""
        responses = ["Hi!", "hello there..?"]
        message = random.choice(responses)
        self.speak(message)
        print(message)

    def thank_you_reply(self):
        """Respond to a thank you."""
        responses = ["Welcome, I can help you!", "Welcome!"]
        message = random.choice(responses)
        self.speak(message)
        print(message)

    def what_is_your_name(self):
        """Respond with the assistant's name."""
        responses = ["I am Isha", "My name is Isha"]
        message = random.choice(responses)
        self.speak(message)
        print(message)

    def morningtime(self):
        """Respond to a morning greeting."""
        responses = ["Good morning", "Morning there, kaise ho?"]
        message = random.choice(responses)
        self.speak(message)
        print(message)

    def restart_pc(self):
        """Restart the PC."""
        try:
            message = "Restarting the PC in 10 seconds. Press Ctrl+C to cancel."
            self.speak(message)
            print(message)
            time.sleep(10)  # Give time to cancel for demo
            subprocess.run(["shutdown", "/r", "/t", "1"], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            message = f"Failed to restart the PC: {str(e)}"
            self.speak(message)
            print(message)

    def shutdown_pc(self):
        """Shut down the PC."""
        try:
            message = "Shutting down the PC in 10 seconds. Press Ctrl+C to cancel."
            self.speak(message)
            print(message)
            time.sleep(10)  # Give time to cancel for demo
            subprocess.run(["shutdown", "/s", "/t", "1"], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            message = f"Failed to shut down the PC: {str(e)}"
            self.speak(message)
            print(message)

    def open_settings(self):
        """Open Windows settings using Win+I."""
        try:
            pyautogui.hotkey('win', 'i')
            message = "Opening settings"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open settings: {str(e)}"
            self.speak(message)
            print(message)

    def open_run_command(self):
        """Open the Run command dialog using Win+R."""
        try:
            pyautogui.hotkey('win', 'r')
            message = "Opening run command"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open run command: {str(e)}"
            self.speak(message)
            print(message)

    def get_time(self):
        """Display the current time."""
        try:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            message = f"The current time is {current_time}"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Error retrieving time: {str(e)}"
            self.speak(message)
            print(message)

    def find_now(self):
        """Search for a query on Google or open file explorer offline."""
        if self.check_internet():
            message = "Tell me what to search"
            self.speak(message)
            print(message)
            search_query = self.listen()
            if search_query and search_query not in ["none", "cancel", "no"]:
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                message = f"Searching for {search_query} on Google"
                self.speak(message)
                print(message)
            else:
                message = "No search query provided"
                self.speak(message)
                print(message)
        else:
            message = "No internet connection. Opening local file explorer."
            self.speak(message)
            print(message)
            subprocess.run(["explorer"], shell=True)

    def came2(self):
        """Open phone camera stream with user-provided URL."""
        if not self.check_internet():
            message = "Phone camera streaming requires an internet connection."
            self.speak(message)
            print(message)
            logging.error(message)
            return message

        default_url = "https://192.168.43.1:8080/shot.jpg"
        message = f"Please provide the phone camera stream URL (default: {default_url})"
        self.speak(message)
        print(message)
        self.pending = 'camera_url'
        url = self.input_queue.get()
        self.pending = None
        url = url.strip() if url and url.strip() not in ["none", "cancel", "no"] else default_url

        try:
            import cv2
            import numpy as np
            import urllib.request
            window_name = 'IPWebcam'
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(url, timeout=5).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                if img is None:
                    raise ValueError("Failed to decode image from stream")
                cv2.imshow(window_name, img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.destroyAllWindows()
            message = "Phone camera stream opened successfully"
            self.speak(message)
            print(message)
            logging.info(message)
            return message
        except Exception as e:
            message = f"Failed to open phone camera stream: {str(e)}"
            self.speak(message)
            print(message)
            logging.error(message)
            return message

    def solve_math(self, expression):
        """Solve a mathematical expression using sympy."""
        try:
            expression = expression.strip().replace(" ", "")
            expr = sympify(expression, locals={"sin": sin, "cos": cos, "tan": tan, "sqrt": sqrt, "pi": pi})
            result = expr.evalf()
            if result.is_integer:
                result = int(result)  
            else:
                result = round(float(result), 6)  
            message = f"The result is {result}"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Sorry, I couldn't solve that math problem: {str(e)}"
            self.speak(message)
            print(message)

    def open_calculator(self):
        """Open the Windows Calculator app."""
        try:
            subprocess.run(["start", "calc"], shell=True, check=True)
            message = "Opening Calculator"
            self.speak(message)
            print(message)
        except subprocess.CalledProcessError as e:
            message = f"Failed to open Calculator: {str(e)}"
            self.speak(message)
            print(message)

    def minimize_windows(self):
        """Minimize all windows using Win+M."""
        try:
            pyautogui.hotkey('win', 'm')
            message = "Minimizing all windows"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to minimize windows: {str(e)}"
            self.speak(message)
            print(message)

    def open_search(self):
        """Open Windows search using Win+Q."""
        try:
            pyautogui.hotkey('win', 'q')
            message = "Opening search"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open search: {str(e)}"
            self.speak(message)
            print(message)

    def open_news_widget(self):
        """Open the Windows news widget using Win+W."""
        try:
            pyautogui.hotkey('win', 'w')
            message = "Opening news widget"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open news widget: {str(e)}"
            self.speak(message)
            print(message)

    def open_about_settings(self):
        """Open About settings using ms-settings:about."""
        try:
            subprocess.run(["start", "ms-settings:about"], shell=True, check=True)
            message = "Opening about settings"
            self.speak(message)
            print(message)
        except subprocess.CalledProcessError as e:
            message = f"Failed to open about settings: {str(e)}"
            self.speak(message)
            print(message)

    def open_project_screen(self):
        """Open project screen settings using Win+P."""
        try:
            pyautogui.hotkey('win', 'p')
            message = "Opening project screen"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open project screen: {str(e)}"
            self.speak(message)
            print(message)

    def open_performance_settings(self):
        """Open performance settings using Win+S."""
        try:
            pyautogui.hotkey('win', 's')
            message = "Opening performance settings"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open performance settings: {str(e)}"
            self.speak(message)
            print(message)

    def open_feedback_hub(self):
        """Open Feedback Hub using Win+F."""
        try:
            pyautogui.hotkey('win', 'f')
            message = "Opening feedback hub"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open feedback hub: {str(e)}"
            self.speak(message)
            print(message)

    def open_game_bar(self):
        """Open Game Bar using Win+G."""
        try:
            pyautogui.hotkey('win', 'g')
            message = "Opening game bar"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open game bar: {str(e)}"
            self.speak(message)
            print(message)

    def open_25(self):
        """Open ITI admission website."""
        try:
            webbrowser.open("https://itiadmission.gujarat.gov.in/")
            message = "Opening ITI admission website"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open ITI website: {str(e)}"
            self.speak(message)
            print(message)

    def open_youtube(self):
        """Open YouTube website."""
        try:
            webbrowser.open("https://youtube.com/")
            message = "Opening YouTube"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open YouTube: {str(e)}"
            self.speak(message)
            print(message)

    def open_instagram(self):
        """Open Instagram website."""
        try:
            webbrowser.open("https://www.instagram.com/")
            message = "Opening Instagram"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open Instagram: {str(e)}"
            self.speak(message)
            print(message)

    def open_voice_typing(self):
        """Open voice typing using Win+H."""
        try:
            pyautogui.hotkey('win', 'h')
            message = "Opening voice typing"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open voice typing: {str(e)}"
            self.speak(message)
            print(message)

    def open_connect_panel(self):
        """Open connect panel using Win+K."""
        try:
            pyautogui.hotkey('win', 'k')
            message = "Opening connect panel"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open connect panel: {str(e)}"
            self.speak(message)
            print(message)

    def lock_screen(self):
        """Lock the screen using Win+L."""
        try:
            pyautogui.hotkey('win', 'l')
            message = "Locking screen"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to lock screen: {str(e)}"
            self.speak(message)
            print(message)

    def open_quick_menu(self):
        """Open quick menu using Win+X."""
        try:
            pyautogui.hotkey('win', 'x')
            message = "Opening quick menu"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open quick menu: {str(e)}"
            self.speak(message)
            print(message)

    def open_cortana(self):
        """Open Cortana using Win+C."""
        try:
            pyautogui.hotkey('win', 'c')
            message = "Opening Cortana"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open Cortana: {str(e)}"
            self.speak(message)
            print(message)

    def open_clipboard_history(self):
        """Open clipboard history using Win+V."""
        try:
            pyautogui.hotkey('win', 'v')
            message = "Opening clipboard history"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open clipboard history: {str(e)}"
            self.speak(message)
            print(message)

    def open_notifications(self):
        """Open notifications using Win+N."""
        try:
            pyautogui.hotkey('win', 'n')
            message = "Opening notifications"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open notifications: {str(e)}"
            self.speak(message)
            print(message)

    def select_all_text(self):
        """Select all text using Ctrl+A."""
        try:
            pyautogui.hotkey('ctrl', 'a')
            message = "Selecting all text"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to select all text: {str(e)}"
            self.speak(message)
            print(message)

    def toggle_caption(self):
        """Toggle captions on/off."""
        # Assuming this is for media or system captions; implement as needed
        message = "Toggling captions"
        self.speak(message)
        print(message)
        # Add actual toggle logic if available, e.g., pyautogui or subprocess

    def open_downloads(self):
        """Open the Downloads folder."""
        try:
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            subprocess.run(["explorer", downloads_path], shell=True, check=True)
            message = "Opening Downloads folder"
            self.speak(message)
            print(message)
        except subprocess.CalledProcessError as e:
            message = f"Failed to open Downloads folder: {str(e)}"
            self.speak(message)
            print(message)

    def btr(self):
        """Check the system battery percentage."""
        try:
            battery = psutil.sensors_battery()
            if battery is None:
                message = "Battery information is not available. This system may not have a battery."
            else:
                percentage = battery.percent
                message = f"System has {percentage}% battery"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Error retrieving battery information: {str(e)}"
            self.speak(message)
            print(message)

    def open_chatbox(self):
        """Open the hack.chat chatbox."""
        try:
            webbrowser.open("https://hack.chat/?Isha")
            message = "Opening chatbox"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open chatbox: {str(e)}"
            self.speak(message)
            print(message)

    def download_picture(self):
        """Open Pixabay for downloading pictures."""
        try:
            webbrowser.open("https://pixabay.com/")
            message = "Opening Pixabay to download pictures"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open Pixabay: {str(e)}"
            self.speak(message)
            print(message)

    def download_instagram_reel(self):
        """Open a website to download Instagram reels."""
        try:
            webbrowser.open("https://igram.world/reels-downloader/")
            message = "Opening Instagram reel downloader"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to open Instagram reel downloader: {str(e)}"
            self.speak(message)
            print(message)

    def stop_song(self):
        """Stop the currently playing song."""
        time.sleep(1)
        pyautogui.press('k')
        message = "Stopping the song"
        self.speak(message)
        print(message)

    def mute_unmute(self):
        """Toggle mute/unmute for media."""
        time.sleep(1)
        pyautogui.press('m')
        message = "Toggling mute/unmute"
        self.speak(message)
        print(message)

    def full_screen(self):
        """Toggle full screen for media."""
        time.sleep(1)
        pyautogui.press('f')
        message = "Toggling full screen"
        self.speak(message)
        print(message)

    def cmaw21(self):
        """Disconnect phone camera stream."""
        try:
            import cv2
            cv2.destroyAllWindows()
            message = "Phone camera stream disconnected"
            self.speak(message)
            print(message)
            logging.info(message)
            return message
        except Exception as e:
            message = f"Failed to disconnect phone camera stream: {str(e)}"
            self.speak(message)
            print(message)
            logging.error(message)
            return message

    def login_instagram(self):
        if not self.check_internet():
            message = "Instagram login requires an internet connection. Opening local Photos app instead."
            self.speak(message)
            print(message)
            logging.warning(message)
            subprocess.run(["start", "", "microsoft.photos:"], shell=True)
            return message

        try:
            from selenium import webdriver
            from selenium.webdriver.common.by import By
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
        except ImportError as e:
            message = f"Required dependencies (selenium, webdriver_manager) not installed: {str(e)}"
            self.speak(message)
            print(message)
            logging.error(message)
            return message

        message = "Enter Instagram username"
        self.speak(message)
        print(message)
        self.pending = 'instagram_user'
        username = self.input_queue.get()
        self.pending = None
        if not username or username.strip() in ["none", "cancel", "no"]:
            message = "Login cancelled: Username not provided"
            self.speak(message)
            print(message)
            logging.info(message)
            return message

        message = "Enter Instagram password"
        self.speak(message)
        print(message)
        self.pending = 'instagram_pass'
        password = self.input_queue.get()
        self.pending = None
        if not password or password.strip() in ["none", "cancel", "no"]:
            message = "Login cancelled: Password not provided"
            self.speak(message)
            print(message)
            logging.info(message)
            return message

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.set_page_load_timeout(30)
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)  # Increased delay for page load

            user_input = driver.find_element(By.NAME, "username")
            pass_input = driver.find_element(By.NAME, "password")
            user_input.send_keys(username)
            pass_input.send_keys(password)
            pass_input.send_keys(Keys.RETURN)
            time.sleep(10)  # Increased delay to handle login process

            # Check for login success (basic check for homepage)
            if "accounts/login" not in driver.current_url:
                message = "Logged into Instagram successfully"
                self.speak(message)
                print(message)
                logging.info(message)
                # Keep browser open for user interaction
                return message
            else:
                message = "Login failed: Incorrect credentials or additional verification required"
                self.speak(message)
                print(message)
                logging.error(message)
                driver.quit()
                return message
        except Exception as e:
            message = f"Failed to log into Instagram: {str(e)}"
            self.speak(message)
            print(message)
            logging.error(message)
            return message

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
