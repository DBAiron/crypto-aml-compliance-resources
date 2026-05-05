# 主要加密资产监管框架（2026最新）

本文件整理了 Web3 / Crypto Compliance 领域最重要的监管框架，重点针对 **VASP（虚拟资产服务商）** 的合规要求。持续更新。

## 1. 全球标准（FATF 框架）

**FATF（金融行动特别工作组）** 是全球反洗钱和反恐怖融资的标准制定者，其标准被 200+ 个司法管辖区采用，是加密合规的**事实上的全球基准**。

### FATF Recommendations（40+9 项建议）
- 2012 年发布并持续更新，将**虚拟资产（VA）和虚拟资产服务商（VASP）** 纳入 AML/CTF 监管框架。
- **最核心的两项**：
  - **Recommendation 15**：新科技与虚拟资产（VASP 需注册、实施 AML 措施）
  - **Recommendation 16**：**Travel Rule（旅行规则）**

### FATF Travel Rule（旅行规则 / Recommendation 16）
- **核心要求**：VASP 在进行虚拟资产转账时，必须收集并安全传输**发送方（Originator）** 和 **接收方（Beneficiary）** 的身份信息（姓名、账号、地址等）。
- **适用场景**：跨境及一定金额以上的转账。
- **当前全球实施情况**（2026）：已有 85+ 个司法管辖区通过或正在实施相关立法。
- **合规意义**：这是 VASP 必须遵守的最重要全球标准之一，直接影响 KYT、尽调和跨链转账流程。

**重要链接**：
- [FATF 40 Recommendations 官方全文](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html)
- [FATF Virtual Assets Guidance](https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-assets.html)
- [Travel Rule 全球实施地图（Notabene）](https://notabene.id/jurisdictions)

---

### 关于**全球监管地图**的想法

**非常好的想法！** 视觉化地图会让这个文件**生动很多**，读者一眼就能看懂不同国家的态度。

**实现建议**（两种方案）：

1. **最简单方案**（推荐先做这个）：
   在上面 Travel Rule 部分后面加一段文字 + 外部链接（不用自己画图）：

   ```markdown
   ### 全球加密监管友好度概览（2026）
   - **极度友好（绿色）**：阿联酋（Dubai VARA）、新加坡、香港
   - **友好（浅绿）**：瑞士、加拿大、澳大利亚
   - **中性/严格监管（黄色）**：欧盟（MiCA）、美国、英国
   - **严格限制（红色）**：中国大陆（禁止 ICO 和交易所）
   - **其他**：印度、俄罗斯等正在动态调整

   **推荐查看互动地图**：
   - [Atlantic Council Crypto Regulation Tracker](https://www.atlanticcouncil.org/programs/geoeconomics-center/cryptoregulationtracker/)
   - [Notabene Travel Rule 全球实施地图](https://notabene.id/jurisdictions)

## 2. 区域与国家监管

### MiCA（欧盟 Markets in Crypto-Assets）
- **生效时间**：2024年全面实施。
- **核心内容**：统一许可制度、稳定币监管、透明度要求、市场操纵禁止。
- **对 VASP 的影响**：必须在欧盟获得牌照才能服务欧盟用户。
- **链接**： [MiCA 官方文本](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1114)

### OFAC Sanctions（美国财政部外国资产控制办公室）
- **核心**：制裁名单筛查（SDN List），禁止与制裁实体交易。
- **合规重点**：地址筛查 + 间接暴露风险（Indirect Exposure）。
- **链接**： [OFAC SDN List](https://sanctionssearch.ofac.treas.gov/) | [OFAC Crypto Guidance](https://home.treasury.gov/policy-issues/financial-sanctions/recent-actions)

### 美国其他监管
- FinCEN（货币服务业务 MSB 注册）
- SEC（证券型代币监管）

### 亚洲重点监管（中文背景特别重要）
- **香港**：SFC VASP 牌照制度 + Travel Rule
- **新加坡**：MAS 数字支付代币服务（DPT）牌照
- **迪拜**：VARA 全面监管框架（对 Web3 非常友好）
- **日本**：FSA 加密资产交易所注册制

## 3. 其他重要标准

- **ISO 37001**：反贿赂管理体系
- ** Wolfsberg Group** 虚拟资产原则
- **C3O（Certified Crypto Compliance Officer）**：专业认证，证明具备 crypto 合规实战能力

## 4. 合规实践建议
- 优先关注 **FATF Travel Rule + OFAC Sanctions**（几乎所有 VASP 必做）
- 建立 **风险-based approach**（风险分级）
- 定期更新制裁名单 + 监控监管动态

---

**最后更新**：2026年5月5日  
**维护者**：Xiaobo Dai (DB Airon) - C3O Certified

欢迎 PR 补充最新监管动态！
