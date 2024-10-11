
import sys
import colorama
from colorama import Fore, Style
import logging
import tkinter as tk
from tkinter import Tk, Button, Label, Checkbutton, messagebox
import threading
import time

# Initialize colorama for CLI colored text output
colorama.init(autoreset=True)

# Fixing log formatting
def log_speed_test(download_speed, upload_speed, ping):
    """Logs the test results to a file with cleaner formatting."""
    logging.basicConfig(filename='speedtest_results.log', level=logging.INFO,
                        format='%(asctime)s - Download: %(download)s Mbps, Upload: %(upload)s Mbps, Ping: %(ping)s ms')
    logging.info('', extra={'download': f'{download_speed:.2f}', 'upload': f'{upload_speed:.2f}', 'ping': f'{ping:.2f}'})
    print(Fore.YELLOW + "Results logged to speedtest_results.log")

# CLI Part
def logo_text():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to SpeedWave | v2.2")

def display_test_types():
    print("Choose the test type:")
    print(Fore.GREEN + "Press 's' for Single-threaded speedtest")
    print(Fore.GREEN + "Press 'm' for Multi-threaded speedtest")

def perform_speedtest(threads=None):
    """Performs a speed test with optional threading (single-threaded if threads=1)."""
    try:
        import speedtest
        st = speedtest.Speedtest()
        st.get_best_server()

        print(Fore.MAGENTA + Style.BRIGHT + "Testing... Please wait.")
        download_speed = st.download(threads=threads) / 10**6  # Mbps
        upload_speed = st.upload(threads=threads) / 10**6  # Mbps
        ping = st.results.ping

        print(Fore.GREEN + f"Download Speed: {download_speed:.2f} Mbps")
        print(Fore.GREEN + f"Upload Speed: {upload_speed:.2f} Mbps")
        print(Fore.GREEN + f"Ping: {ping:.2f} ms")
        
        # Option to log results
        log_speed_test(download_speed, upload_speed, ping)

    except speedtest.SpeedtestException as e:
        print(Fore.RED + f"Speedtest error: {e}")
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}")

def main_cli():
    """Main function for CLI-based speed test."""
    logo_text()
    display_test_types()

    choice = input("Enter your choice (s/m): ").strip().lower()

    if choice == 's':
        print(Fore.MAGENTA + Style.BRIGHT + "Performing single-threaded speedtest...")
        perform_speedtest(threads=1)
    elif choice == 'm':
        print(Fore.MAGENTA + Style.BRIGHT + "Performing multi-threaded speedtest...")
        perform_speedtest()  # Multi-threaded by default
    else:
        print(Fore.RED + "ERROR: Invalid choice")
        return

# GUI Part

def run_gui_speedtest(threads=None):
    """Performs the speed test in a separate thread to prevent blocking the GUI."""
    # Display loading message
    result_label.config(text="Running speed test... Please wait.", fg="blue")
    root.update_idletasks()

    def perform_test():
        try:
            import speedtest
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download(threads=threads) / 10**6  # Convert to Mbps
            upload_speed = st.upload(threads=threads) / 10**6  # Convert to Mbps
            ping = st.results.ping

            result_label.config(text=f"Download: {download_speed:.2f} Mbps\nUpload: {upload_speed:.2f} Mbps\nPing: {ping:.2f} ms", fg="green")

            if log_var.get():
                log_speed_test(download_speed, upload_speed, ping)

        except speedtest.SpeedtestException as e:
            result_label.config(text=f"Speedtest error: {e}", fg="red")
        except Exception as e:
            result_label.config(text=f"Unexpected error: {e}", fg="red")

    threading.Thread(target=perform_test).start()

def create_gui():
    """Creates the GUI for SpeedWave with an improved layout and larger window."""
    global root
    root = Tk()
    root.title("SpeedWave - Internet Speed Test")
    root.geometry("500x400")  # Larger window size
    root.iconbitmap('resources/icons/icon.ico')

    global result_label, log_var
    log_var = tk.BooleanVar()

    Label(root, text="Welcome to SpeedWave", font=("Arial", 20, "bold")).pack(pady=20)

    Button(root, text="Run Single-Threaded Speed Test", command=lambda: run_gui_speedtest(threads=1), font=("Arial", 12)).pack(pady=10)
    Button(root, text="Run Multi-Threaded Speed Test", command=lambda: run_gui_speedtest(), font=("Arial", 12)).pack(pady=10)

    result_label = Label(root, text="Results will be shown here", font=("Arial", 14), fg="green")
    result_label.pack(pady=20)

    # Checkbox for logging results
    Checkbutton(root, text="Log Results", variable=log_var, font=("Arial", 12)).pack()

    Button(root, text="Exit", command=root.quit, font=("Arial", 12)).pack(pady=10)

    root.mainloop()

# Combined CLI/GUI entry point

def main():
    print("Welcome to SpeedWave!")
    print("Do you want to run the app in CLI or GUI mode?")
    mode = input("Enter 'cli' for CLI or 'gui' for GUI: ").strip().lower()

    if mode == 'cli':
        main_cli()
    elif mode == 'gui':
        create_gui()
    else:
        print("Invalid mode selected. Exiting.")

if __name__ == "__main__":
    main()
