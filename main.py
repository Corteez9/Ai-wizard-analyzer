from fastapi import FastAPI
import threading
import time

app = FastAPI()
bot_running = False
log = []

def mock_bot_logic():
    global bot_running
    count = 0
    while bot_running:
        log.append(f"Bot tick {count}")
        time.sleep(5)
        count += 1

@app.get("/")
def read_root():
    return {"message": "AI Wizard backend is live."}

@app.get("/start")
def start_bot():
    global bot_running
    if not bot_running:
        bot_running = True
        threading.Thread(target=mock_bot_logic, daemon=True).start()
        return {"status": "Bot started"}
    return {"status": "Bot already running"}

@app.get("/stop")
def stop_bot():
    global bot_running
    bot_running = False
    return {"status": "Bot stopped"}

@app.get("/status")
def bot_status():
    return {"running": bot_running, "log": log[-10:]}