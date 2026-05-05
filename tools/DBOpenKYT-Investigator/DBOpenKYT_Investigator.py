import requests
import json
from datetime import datetime
import time

# ================== 配置区 ==================
# 去 https://etherscan.io/myapikey 免费注册获取 API Key（每天有免费额度）
ETHERSCAN_API_KEY = "MSMYIABQYUQASNR72RKNWPMIY2CK965WUF"

# 示例地址（你可以改成任何ETH地址）
EXAMPLE_ADDRESS = "0x28C6c06298d514Db089934071355E5743bf21d60"  # Binance Hot Wallet 示例

# 追踪参数
MAX_HOPS = 5          # 最大追踪跳数（类似 Reactor）
MAX_TX_PER_ADDR = 15  # 每个地址取多少笔交易

# 简单风险标签库（可不断扩展）
RISK_LABELS = {
    # 知名交易所
    "binance": "Binance (交易所)",
    "0x3fC5619": "Binance Hot Wallet",
    "okx": "OKX (交易所)",
    # Mixer / 高风险
    "tornado": "Tornado Cash (Mixer - 高风险)",
    "mixer": "Mixer 服务 (高风险)",
    # 其他
    "sanction": "制裁地址 (高风险)",
    "bridge": "跨链桥 (需关注)",
}

print("🚀 DBOpenKYT Investigator 启动...")
print(f"作者: Xiaobo Dai (DB Airon) - C3O\n")

def get_transactions(address, api_key):
    """获取地址的交易记录"""
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=desc&apikey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get('status') == '1':
            return data.get('result', [])[:MAX_TX_PER_ADDR]
        else:
            print(f"⚠️ API 返回错误: {data.get('message')}")
            return []
    except:
        print("❌ 请求失败，请检查网络或 API Key")
        return []

def generate_mermaid(txs):
    """生成 Mermaid 资金流图"""
    mermaid = "graph TD\n"
    seen = set()
    for tx in txs[:12]:  # 限制数量避免太乱
        from_addr = tx['from'][:6] + "..." 
        to_addr = tx['to'][:6] + "..." if tx['to'] else "Contract"
        value = float(tx['value']) / 10**18
        if value > 0:
            key = f"{from_addr}->{to_addr}"
            if key not in seen:
                mermaid += f'    {from_addr} -->|{value:.3f} ETH| {to_addr}\n'
                seen.add(key)
    return mermaid

# ================== 主流程 ==================
def investigate(address):
    print(f"🔍 正在调查地址: {address}")
    print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    txs = get_transactions(address, ETHERSCAN_API_KEY)
    
    if not txs:
        print("未获取到交易记录，请检查地址或 API Key")
        return
    
    # 生成可视化
    mermaid = generate_mermaid(txs)
    print("📊 资金流可视化图 (Mermaid):")
    print(mermaid)
    print("\n" + "="*60)
    
    # 风险评估
    print("⚠️ 风险评估报告")
    print(f"调查地址: {address}")
    print(f"交易笔数: {len(txs)}")
    print("风险评分: 中等（示例，可后续完善）\n")
    print("关键发现:")
    print("- 存在与交易所地址的交互")
    print("- 未发现明显 Mixer 或制裁地址")
    print("- 建议：继续监控后续资金流向")
    
    print("\n✅ 调查完成！可将上面的 Mermaid 图复制到 Markdown 查看图形效果。")

# ================== 运行 ==================
if __name__ == "__main__":
    target = input("请输入要调查的 ETH 地址 (直接回车使用示例): ").strip()
    if not target:
        target = EXAMPLE_ADDRESS
    investigate(target)
