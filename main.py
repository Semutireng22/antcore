import requests
import json
import time
import random
from fake_useragent import UserAgent
import datetime
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Header Banner ASCII Berwarna
BANNER = f"""                                                             
{Fore.CYAN} _   _  ____ ____       _    ___ ____  ____  ____   ___  ____  
{Fore.CYAN}| | | |/ ___|  _ \     / \  |_ _|  _ \|  _ \|  _ \ / _ \|  _ \ 
{Fore.CYAN}| | | | |  _| | | |   / _ \  | || |_) | | | | |_) | | | | |_) |
{Fore.CYAN}| |_| | |_| | |_| |  / ___ \ | ||  _ <| |_| |  _ <| |_| |  __/ 
{Fore.CYAN} \___/ \____|____/  /_/   \_|___|_| \_|____/|_| \_\\___/|_|    

{Fore.YELLOW}  Channel: {Fore.BLUE}t.me/ugdairdrop
"""

def read_wallet_addresses(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"{Fore.RED}Error: File wallet tidak ditemukan ({str(e)})")
        return []

def send_task_completion(session, wallet_address, task_id):
    url = "https://portal.antcore.xyz/api/complete-task"
    payload = {
        "walletAddress": wallet_address,
        "taskId": task_id
    }
    
    try:
        response = session.post(
            url,
            data=json.dumps(payload),
            timeout=10,
            verify=True
        )
        return response.status_code
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")
        return None

def main():
    # Tampilkan banner
    print(BANNER)
    
    wallet_addresses = read_wallet_addresses('address.txt')
    if not wallet_addresses:
        print(f"{Fore.RED}Tidak ada wallet address yang valid.")
        return

    ua = UserAgent()
    with requests.Session() as session:
        while True:
            print(f"\n{Fore.GREEN}[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Memulai tugas untuk {len(wallet_addresses)} wallet...")
            
            # Update headers dengan User-Agent acak
            session.headers.update({
                'User-Agent': ua.random,
                'Content-Type': 'application/json'
            })
            
            for wallet in wallet_addresses:
                print(f"\n{Fore.MAGENTA}🔄 Memproses wallet: {Fore.CYAN}{wallet[:6]}...{wallet[-4:]}")
                
                for task_id in [9, 10]:
                    status = send_task_completion(session, wallet, task_id)
                    if status == 200:
                        print(f"  {Fore.GREEN}✅ Task {task_id} berhasil")

                    elif status == 400:
                        print(f"  {Fore.YELLOW}⚠️ Task {task_id} sudah selesai")
                    else:
                        print(f"  {Fore.RED}❌ Task {task_id} gagal (Status: {status})")
                    
                    # Delay acak antara task
                    time.sleep(random.randint(2, 5))
                
                # Delay acak antara wallet
                time.sleep(random.randint(5, 10))
            
            next_run = datetime.datetime.now() + datetime.timedelta(hours=24, minutes=random.randint(-60, 60))
            print(f"\n{Fore.YELLOW}⏳ Eksekusi berikutnya: {Fore.CYAN}{next_run.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Delay sampai waktu eksekusi berikutnya
            time.sleep((next_run - datetime.datetime.now()).total_seconds())

if __name__ == "__main__":
    main()
