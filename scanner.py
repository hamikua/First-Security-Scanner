import os

def network_scanner():
    # 假設你的區域網路開頭是 192.168.1
    base_ip = "192.168.1." 
    print(f"開始掃描網路範圍: {base_ip}0 到 {base_ip}255...")

    for i in range(1, 255):
        ip = base_ip + str(i)
        # 使用系統的 ping 指令，-n 1 代表只 ping 一次，-w 100 代表等待 100 毫秒
        response = os.system(f"ping -n 1 -w 100 {ip} > nul")
        
        if response == 0:
            print(f"[+] 發現裝置在線: {ip}")

if __name__ == "__main__":
    network_scanner()
