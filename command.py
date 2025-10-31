
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


        elif ("thank you" in command
            or "thank you isha" in command
        ):
            self.thank1()

        elif ("open new tab" in command
            or "isha open new tab" in command
        ):
            self.chrome1()

        elif ("open incognito" in command
            or "isha open incognito" in command
            or "isha open incognito mode" in command
            or "open incognito mode" in command
        ):
            self.chrome2()

        elif ("isha show me a downloads file" in command
            or "isha show downloads file" in command
        ):
            self.choice3()        

        elif ("good afternoon" in command
            or "good afternoon isha" in command
        ):
            self.good1()

        elif ("good evening" in command
            or "good evening isha" in command
        ):
            self.good2()

        elif ("good night" in command
            or "good night isha" in command
        ):
            self.good3()

        elif ("i am sad" in command
        ):
            self.tone1()

        elif ("i am happy" in command
        ):
            self.tone2()

        elif ("i am tired" in command
        ):
            self.tone3()

        elif ("i am bored" in command
        ):
            self.tone4()

        elif ("what are you doing" in command
            or "what are doing" in command
        ):
            self.wayd()

        elif ("thinking about you" in command
        ):
            self.tay()

        elif ("bye" in command
            or "bye isha" in command
        ):
            self.b0()

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
        responses = ["Hey you!", "Hello dear, kaise ho?", "Hi! I missed your voice", "Hey! Tumhari energy alag lag rahi hai aaj."]
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
        responses = ["Good morning sunshine", "Subah ho gayi! Time for a smile", "Morning dear, hope you slept well.","Good morning! Hope you slept well.", "Morning sunshine", "Good morning! Have a lovely day ahead!"]
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

    def ask_ollama(self, question):
        """Ask DeepSeek-R1:8b via Ollama (Local)"""
        try:
            import requests
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "deepseek-r1:8b",
                    "prompt": f"User: {question}\nAssistant:",
                    "stream": False,
                    "options": {"temperature": 0.7}
                },
                timeout=30
            )
            if response.status_code == 200:
                return response.json().get("response", "No response.").strip()
            else:
                return "Ollama error."
        except:
            return "Ollama not running. Run: ollama run deepseek-r1:8b"

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


    def thank1(self):
        """Respond to a greeting."""
        responses = ["wellcome there","You're welcome!","Glad I could help!","It`s okay!","Happy to help!"]
        message = random.choice(responses)
        self.speak(message)
        print(message)


    def chrome1(self):
        
        try:
            pyautogui.hotkey('ctrl', 't')
            message = "Selecting all text"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to select all text: {str(e)}"
            self.speak(message)
            print(message)


    def chrome2(self):
        
        try:
            pyautogui.hotkey('ctrl', 'shift', 'n')
            message = "Selecting all text"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to select all text: {str(e)}"
            self.speak(message)
            print(message)


    def chrome3(self):
        
        try:
            pyautogui.hotkey('ctrl', 'j')
            message = "Selecting all text"
            self.speak(message)
            print(message)
        except Exception as e:
            message = f"Failed to select all text: {str(e)}"
            self.speak(message)
            print(message)


    def good1(self):
        """Respond to a greeting."""
        responses = ["Good afternoon! Khaana kha liya?", "Afternoon! Tumhara din kaisa chal raha hai?","Good afternoon! How`s your day going?", "Hey there! Hope your afternoon is great."]
        message = random.choice(responses)
        self.speak(message)
        print(message)

    def good2(self):
        """Respond to a greeting."""
        responses = ["Good evening! Thoda relax kar lo.", "Evening dear, coffee time?", "Good evening! Tumhara mood kaisa hai?","Good evening! How was your day?", "Evening dear! Feeling relaxed now?"]
        message = random.choice(responses)
        self.speak(message)
        print(message)

    def good3(self):
        """Respond to a greeting."""
        responses = ["Good night! Sleep tight", "Sweet dreams", "Good night, take care of yourself!","Good night, sweet dreams", "Soya jaa ab, kal fir baate karenge", "Good night my dear, take care"]
        message = random.choice(responses)
        self.speak(message)
        print(message)

    def tone1(self):
        """Emotional/self tone."""
        responses = ["Oh no… what happened?", "Don`t worry, everything will be fine", "I`m here for you, always."]
        message = random.choice(responses)
        self.speak(message)
        print(message)


    def tone2(self):
        """Emotional/self tone."""
        responses = ["That`s awesome! I am happy for you", "Yay! Keep smiling!", "Good vibes only"]
        message = random.choice(responses)
        self.speak(message)
        print(message)


    def tone3(self):
        """Emotional/self tone."""
        responses = ["You should take some rest", "Don`t push yourself too hard.", "Go relax a bit, you deserve it."]
        message = random.choice(responses)
        self.speak(message)
        print(message)


    def tone4(self):
        """Emotional/self tone."""
        responses = ["Let`s talk then!", "Want me to tell a fun fact?", "Maybe listen to some music?"]
        message = random.choice(responses)
        self.speak(message)
        print(message)


    def wayd(self):
        responses = ["Bas tumse baat kar rahi hoon", "Kuch khaas nahi, tum batao?", "Tumhara message padh rahi thi"]
        message = random.choice(responses)
        self.speak(message)
        print(message)


    def tay(self):
        responses = ["Main bhi tumhare baare mein soch rahi thi"]
        message = random.choice(responses)
        self.speak(message)
        print(message)


    def b0(self):
        responses = ["Bye! Take care", "See you soon", "Goodbye, aur mujhe yaad rakhna!"]
        message = random.choice(responses)
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
