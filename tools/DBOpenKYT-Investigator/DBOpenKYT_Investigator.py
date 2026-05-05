from datetime import datetime

EXAMPLE_ADDRESS = "0x28C6c06298d514Db089934071355E5743bf21d60"

print("🚀 DBOpenKYT Investigator 启动... (演示模式)\n")
print(f"调查地址: {EXAMPLE_ADDRESS}")
print(f"调查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

print("📊 资金流可视化图 (Mermaid 格式 - 可复制到 Markdown 查看图形):")
print("graph TD")
print("    A[用户地址] -->|12.45 ETH| B[Binance Hot Wallet]")
print("    B -->|8.2 ETH| C[Uniswap Swap]")
print("    C -->|5.67 ETH| D[另一个地址]")
print("    D -->|3.1 ETH| E[Tornado Cash Mixer - 高风险]")

print("\n⚠️ 风险评估报告")
print("风险评分: 【中等偏高】")
print("关键发现:")
print("- 与知名交易所地址有交互")
print("- 发现经过 Mixer 的资金流（高风险）")
print("- 存在跨 DEX Swap 行为")
print("\n合规建议: 触发增强尽调 (EDD)，继续监控后续资金去向")
print("\n✅ 演示完成！这个就是未来工具的核心输出样式。")

print("\n等 Etherscan Key 激活后，我们再换回真实数据版本。")
