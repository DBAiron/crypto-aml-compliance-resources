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

### 🌍 全球加密监管友好度地图（2026年概览）

以下是主要司法管辖区的监管态度分类（基于友好程度）：

| 颜色 | 监管态度 | 代表国家/地区 | 特点 |
|------|----------|---------------|------|
| **🟢 极度友好** | 全面支持 + 清晰牌照 | 阿联酋（Dubai VARA）、新加坡、香港 | 积极发牌、Web3 友好政策 |
| **🟡 友好** | 许可制 + 创新友好 | 瑞士、日本、澳大利亚、加拿大 | 明确监管框架，支持创新 |
| **🟠 中性/严格** | 全面监管但可合规 | 欧盟（MiCA）、美国、英国 | 牌照要求高、合规成本较高 |
| **🔴 严格限制** | 禁止或重度限制 | 中国大陆、印度（部分限制） | ICO/交易所禁止或严格管控 |

**推荐互动地图（强烈建议点击查看）**：

- **[Atlantic Council Crypto Regulation Tracker](https://www.atlanticcouncil.org/programs/geoeconomics-center/cryptoregulationtracker/)** —— 最权威的全球加密监管互动地图（覆盖75+国家，可点击查看详情）
- **[Notabene Travel Rule Adoption Map](https://notabene.id/jurisdictions)** —— 专注于 Travel Rule 全球实施情况
- **[PwC Global Crypto Regulation Report 2026](https://www.pwc.com/gx/en/industries/financial-services/publications/global-crypto-regulation-report.html)** —— 最新报告与地图

**小贴士**：对于中文背景的合规从业者，**香港、新加坡、迪拜** 是目前最现实的友好辖区。

## 2. 区域与国家监管

### MiCA（欧盟 Markets in Crypto-Assets）
- **生效时间**：2024年全面实施。
- **核心内容**：统一许可制度、稳定币监管、透明度要求、市场操纵禁止。
- **对 VASP 的影响**：必须在欧盟获得牌照才能服务欧盟用户。
- **链接**： [MiCA 官方文本](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1114)

### OFAC Sanctions（美国财政部外国资产控制办公室）
- **核心要求**：必须筛查并禁止与 SDN（Specially Designated Nationals）制裁名单上的实体进行任何交易，包括**间接暴露**（Indirect Exposure）。
- **合规重点**：地址/钱包筛查、制裁规避识别、资金冻结报告。
- **对 Crypto 的特殊意义**：OFAC 已多次将特定地址（如 Tornado Cash）列入制裁名单，是 VASP 日常 KYT 的必做事项。

**重要官方链接**：
- [OFAC Virtual Currency Sanctions Compliance Guidance](https://ofac.treasury.gov/media/913571/download?inline) （虚拟资产制裁合规指南，主文档）
- [OFAC Sanctions List Search（实时查询工具）](https://sanctionssearch.ofac.treas.gov/)
- [OFAC 官网 - Virtual Currency 专题](https://ofac.treasury.gov/faqs/topic/1626)

### 美国其他监管

- **FinCEN（Financial Crimes Enforcement Network，金融犯罪执法网络）**
  - **核心要求**：从事虚拟资产交换、转账等业务的实体需注册为 **Money Services Business (MSB)**。
  - **合规重点**：AML 程序、KYC、可疑活动报告（SAR）。
  - **重要链接**：
    - [FinCEN MSB 注册官方页面](https://www.fincen.gov/resources/money-services-business-msb-registration)
    - [FinCEN 虚拟货币指导意见](https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-certain-business-models)

### SEC（U.S. Securities and Exchange Commission，美国证券交易委员会）
- **核心要求**：如果加密资产被认定为“证券”（Howey Test），则需遵守证券发行、注册、披露和交易监管。
- **合规重点**：证券型代币（Security Tokens）、ICO/IDO、Staking、代币发行等活动的合规性判断。
- **2026年最新进展**：SEC 发布了《联邦证券法对某些加密资产及交易的适用》解释性指引，提供更清晰的代币分类框架。

**重要官方链接**：
- [SEC Crypto Assets and Federal Securities Laws 主页](https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/crypto-assets-federal-securities-laws)
- [SEC 2026 Crypto Assets 解释性指引新闻稿](https://www.sec.gov/newsroom/press-releases/2026-30-sec-clarifies-application-federal-securities-laws-crypto-assets)
- [完整指引 PDF](https://www.sec.gov/files/rules/interp/2026/33-11412.pdf)

### 亚洲重点监管（对中文背景从业者特别重要）

亚洲是目前 Web3 合规最活跃的区域之一，以下是中文背景转型者最值得关注的辖区：

#### 香港（Hong Kong）
- **监管机构**：SFC（证券及期货事务监察委员会）
- **核心制度**：虚拟资产交易平台（VATP）牌照 + VASP 监管
- **重点要求**：Travel Rule、客户资产隔离、投资者保护
- **最新进展**（2026）：持续扩展牌照范围至 VA 咨询和管理服务
- **链接**：
  - [SFC 虚拟资产交易平台列表](https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/Virtual-assets/Virtual-asset-trading-platforms-operators/Lists-of-virtual-asset-trading-platforms)
  - [SFC AML Guideline for VASPs](https://www.sfc.hk/-/media/EN/files/LSD/Gazette/GN-3120-of-2023.pdf)

#### 新加坡（Singapore）
- **监管机构**：MAS（货币管理局）
- **核心制度**：Digital Payment Token (DPT) 服务牌照（Payment Services Act）
- **重点要求**：资本要求、AML/CTF、本地实体要求
- **链接**：
  - [MAS DPT 服务许可指南](https://www.mas.gov.sg/regulation/guidelines/guidelines-on-licensing-for-dtsps)
  - [MAS Payment Services Act](https://www.mas.gov.sg/regulation/acts/payment-services-act)

#### 迪拜（Dubai） - VARA
- **监管机构**：VARA（Virtual Assets Regulatory Authority）
- **核心制度**：全面 VASP 牌照制度（全球最友好之一）
- **特点**：对零售和机构都友好，支持衍生品，监管灵活
- **链接**：
  - [VARA 官网](https://www.vara.ae/en/)
  - [VARA Rulebooks](https://rulebooks.vara.ae/)

#### 阿布扎比（Abu Dhabi） - ADGM
- **监管机构**：FSRA（Financial Services Regulatory Authority）
- **核心制度**：Virtual Asset Framework（全球最早且最成熟的虚拟资产全面监管框架之一）
- **特点**：支持交易所、托管、Staking 等多种业务，对机构投资者非常友好，规则与传统金融高度接轨。
- **重要链接**：
  - [Guidance – Regulation of Virtual Asset Activities in ADGM (2025更新)](https://en.adgm.thomsonreuters.com/rulebook/guidance-regulation-virtual-asset-activities-adgm-10-june-2025)
  - [ADGM Virtual Asset Framework 官方页面](https://www.adgm.com/business-areas/digital-assets)

#### 日本（Japan）
- **监管机构**：FSA（金融厅）
- **核心制度**：Crypto Asset Exchange Service Provider 注册制（即将转向金融工具交易法监管）
- **重点要求**：严格的 AML、客户资产保护、网络安全、投资者保护。
- **重要链接**：
  - [FSA Crypto Asset Exchange Service Providers 注册列表](https://www.fsa.go.jp/en/regulated/licensed/en_kasoutuka.xlsx)
  - [Guideline for Supervision of Crypto-Asset Exchange Service Providers](https://www.fsa.go.jp/common/law/guide/kaisya/e016.pdf)
  - [FSA 加密资产监管页面](https://www.fsa.go.jp/en/policy/cryptocurrency.html)

**中文背景从业者建议**：优先考虑 **香港、新加坡、迪拜 VARA、阿布扎比 ADGM** 这四个友好辖区，作为职业发展和项目落地首选。

## 3. 其他重要国际标准与认证

### ISO 37001：反贿赂管理体系
- **核心内容**：国际标准化组织发布的反贿赂管理体系标准，适用于所有组织（包括 VASP）。
- **合规意义**：帮助机构建立系统化的反贿赂政策、尽职调查、举报机制等，是大型机构和银行级合规的重要认证。
- **重要链接**：
  - [ISO 37001 官方介绍](https://www.iso.org/standard/65034.html)
  - [ISO 37001 中文简介](https://www.iso.org/obp/ui/#iso:std:iso:37001:ed-1:v1:zh)

### Wolfsberg Group 虚拟资产原则
- **核心内容**：由全球领先银行组成的 Wolfsberg Group 发布的《Wolfsberg Virtual Asset Service Providers Principles》（VASP 原则）。
- **合规意义**：提供金融机构与 VASP 合作时的 AML/CTF 最佳实践指引，重点包括 KYC、Travel Rule、制裁筛查和高风险客户管理。
- **重要链接**：
  - [Wolfsberg Group VASP Principles 官方文件](https://wolfsberg-group.org/wp-content/uploads/2024/02/Wolfsberg-Group-VASP-Principles.pdf)
  - [Wolfsberg Group 官网](https://wolfsberg-group.org/)

### C3O（Certified Crypto Compliance Officer）
- **核心内容**：由 Global Association of Certified Crypto Compliance Officers 颁发的专业认证。
- **合规意义**：目前 Crypto 领域最直接的对标认证，证明持证人具备虚拟资产风险管理、金融犯罪防控、监管合规等实战能力。
- **重要链接**：
  - [AC3O 官网](https://ac3o.org/)
  - [C3O 认证详情](https://ac3o.org/certification/c3o/)

## 4. 合规实践建议
- 优先关注 **FATF Travel Rule + OFAC Sanctions**（几乎所有 VASP 必做）
- 建立 **风险-based approach**（风险分级）
- 定期更新制裁名单 + 监控监管动态

---

**最后更新**：2026年5月5日  
**维护者**：Xiaobo Dai (DB Airon) - C3O Certified

欢迎 PR 补充最新监管动态！
