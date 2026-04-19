import subprocess
import sys
import time

def run():
    print("--- Starting Retail Intelligence Orchestrator PRO ---")
    
    # Start Frontend (Streamlit)
    print("Frontend initialization...")
    frontend_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "client/app.py"],
        stdout=None,
        stderr=None,
        text=True
    )
    
    print("\n--- Intelligence Engine Active ---")
    print("Dashboard booting...")
    print("--------------------------\n")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nShutting down...")
        frontend_process.terminate()

if __name__ == "__main__":
    run()
