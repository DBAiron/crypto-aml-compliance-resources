# 公开链上调查案例研究

本节收集经典的 Crypto 合规/AML 调查案例，重点分析**资金流特点**、**合规风险点** 和 **启示**。适合练习 Reactor / Etherscan 追踪思维。

## 1. Ronin Network Hack (2022.3) - 史上最大 DeFi 黑客事件

**事件概述**：  
Axie Infinity 的 Ronin 跨链桥被黑客攻击，损失约 **6.24 亿美元**（当时价值）。

**资金流关键点**：
- 黑客通过多个新创建的地址分散资金。
- 使用 Tornado Cash Mixer 进行混币。
- 后续通过多个交易所和跨链桥进行洗钱。

**合规启示**：
- 跨链桥是高风险点，必须加强 KYT 监控。
- Mixer（Tornado Cash）属于高风险实体，应触发自动警报 + EDD（增强尽调）。
- Travel Rule 在跨链场景下的执行难度。

**学习练习**：在 Etherscan / Arkham 上搜索 Ronin Bridge 相关地址，尝试追踪资金流向。

---

## 2. Tornado Cash 制裁案例 (2022.8)

**事件概述**：
美国 OFAC 将 Tornado Cash（以太坊混币协议）列入制裁名单。

**合规意义**：
- 即使是开源协议，其智能合约地址也被视为高风险。
- 任何与 Tornado Cash 有交互的地址都会被标记为“Indirect Exposure”。

**合规官实操要点**：
- KYT 系统需要实时更新制裁名单。
- 判断“是否知情”成为重要合规判断标准。
- Reactor 中会自动显示 “Sanctioned Entity” 标签。

**当前状态**（2026）：Tornado Cash 仍被多国监管关注，类似协议需持续监控。

---

## 3. FTX 崩盘相关资金流动 (2022.11)

**事件概述**：
FTX 破产前大量资金异常转移。

**合规风险**：
- 内部人交易（Insider Trading）
- 资金挪用（Misappropriation）
- 大额异常提现触发 AML 警报

**启示**：
- 对交易所/钱包的大额用户必须做定期审查（Ongoing Monitoring）。
- 异常交易模式（短时间内多笔大额转账）是重要红旗（Red Flag）。

---

## 4. 小案例练习推荐（适合新手练习）

1. **知名交易所热钱包追踪**  
   - Binance Hot Wallet 示例地址：`0x28C6c06298d514Db089934071355E5743bf21d60`（Etherscan 搜索）

2. **知名 Mixer 出口地址**  
   - 搜索 Tornado Cash 相关已知出口地址，练习识别混币行为。

3. **跨链桥案例**  
   - Wormhole / Multichain 历史事件。

---

## 贡献方式
- 欢迎提交新的公开案例（PR）
- 每个案例建议包含：事件时间、损失金额、关键技术手段、合规风险点

**更新日期**：2026年5月  
**维护者**：Xiaobo Dai (DB Airon) - C3O Certified
