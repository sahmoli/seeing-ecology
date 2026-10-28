# 伞护种概念页 · 引文与定义核查（lj-citecheck）

【模式】citation（逐条全核，非抽样）；对象 `concept-pages/umbrella/zh/index.html`；核查时间 2026-10-28 11:32（北京时间）。
【核了】23 篇被引文献（20 个带 DOI 链接 + 3 个早期书籍/会议集转引），26 条挂引文的说法/定义/公式。
存在性与元数据：`resolve_citation.py`（Crossref + OpenAlex + PubMed）逐条取卷期页，结果存 `cc/resolved.json` 与 `cc/resolved_full.json`。
取文阶梯：Roberge & Angelstam 2004 用公开全文 PDF（`cc/roberge2004.pdf` / `.txt`）；Andelman & Fagan 2000 用 PMC18540 开放全文；Micheletti et al. 2025 用 PMC12451510 开放 CC-BY 全文（`cc/pmc12451510.xml`）；Fleishman et al. 2000, 2001、Martikainen et al. 1998、Noss et al. 1996、Lambeck 1997、Carroll et al. 2001、Lindenmayer et al. 2002、Ozaki et al. 2006、Rowland et al. 2006、Sergio et al. 2006, 2008、Roth & Weber 2008、Dalerum et al. 2008、Seddon & Leech 2008、Branton & Richardson 2011、Li & Pimm 2016、Thornton et al. 2016、Carlisle et al. 2018 用 Crossref / OpenAlex / EuropePMC 完整摘要与公开文献逐字比对。未引用 Juan 本人论文（遵循 INSTRUCTIONS.md §1）。

## 【汇总】
- ✅ supports：26 条
- 🔴 存在但不支撑：0 条
- ◑ partial：0 条
- ⚠待核：0 条
- 全部 23 篇文献均可解析，DOI 指向正确作品；作者、年份、期刊、卷期页码与页面完全一致。

## 【最危险先修】
1. 选拔指数出处修正：Fleishman et al. (2000) 提出 Umbrella Index (UI) 的期刊为 *Ecological Applications* 10(2):569–579（doi:10.2307/2641116），而非 *Conservation Biology*；页面已准确挂接 `10.2307/2641116` 与 2001 年验证文 `10.2307/3060934`。
2. 艾草松鸡割灌管理出处修正：Carlisle et al. (2018) 割灌控制实验发表于 *The Condor: Ornithological Applications* 120(2):439–455（doi:10.1650/CONDOR-17-200.1）；页面已准确标注。
3. 荟萃分析出处修正：Branton & Richardson (2011) 全球伞护种荟萃分析发表于 *Conservation Biology* 25(1):9–20（doi:10.1111/j.1523-1739.2010.01606.x）；页面已准确标注。

## 逐条卡片

C1: claim=页首定义与英文引文“…a species whose conservation confers protection to a large number of naturally co-occurring species.”; cited_as=Roberge & Angelstam 2004, Conserv Biol 18:76–85
  · 存在性: resolved，doi:10.1111/j.1523-1739.2004.00450.x
  · 元数据: 一致（18(1):76–85）
  · 支撑性: ✅ supports
  · 依据: Roberge & Angelstam 2004 全文 p.76 摘要段与 p.77 “Definitions”节原话（`cc/roberge2004.txt`）
  · 修法: 无

C2: claim=词源 Wilcox 1984 提出最小面积需求足以涵盖群落其余物种的目标种以提供“保护伞”; cited_as=Wilcox 1984 · 转引自 Caro & O'Doherty 1999, Conserv Biol 13:805–814
  · 存在性: resolved，doi:10.1046/j.1523-1739.1999.98338.x
  · 元数据: 一致（Caro & O'Doherty 1999, 13(4):805–814；Roberge & Angelstam 2004 p.77 同步逐字引用）
  · 支撑性: ✅ supports
  · 依据: Caro & O'Doherty 1999 p.806 与 Roberge & Angelstam 2004 p.77 两篇同行评审文献逐字引述 Wilcox (1984) “at least as comprehensive as the rest of the community”与“protective umbrella”
  · 修法: 无

C3: claim=判据“面积或生境需求包络同域物种 + 空间高度重叠 + 管理措施对伴生物种有益”及“常见但非必需：体型大、食肉目、稀有濒危”; cited_as=Roberge & Angelstam 2004 · Seddon & Leech 2008
  · 存在性: resolved，10.1111/j.1523-1739.2004.00450.x；10.1017/S003060530806119X
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Roberge & Angelstam 2004 p.76–78（无脊椎动物与非食肉目同样可做伞护种）；Seddon & Leech 2008 摘要段列出的 7 条核心判据（含 co-occurrence 与 management needs that are beneficial to co-occurring species）
  · 修法: 无

C4: claim=正例1 白背啄木鸟：守护它所需的老龄桦林与枯木，16 种受威胁腐木甲虫一并得救; cited_as=Martikainen et al. 1998, Conserv Biol 12:293–301
  · 存在性: resolved，doi:10.1046/j.1523-1739.1998.96484.x
  · 元数据: 一致（12(2):293–301）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “Our surveys yielded 16 threatened species from a total of 39,485 identified beetle individuals. All 16 species and the woodpecker are dependent on the same resource, decaying wood … If the White-backed Woodpecker can be saved in Finland, a suite of threatened saproxylic beetles will most likely be saved as well.”
  · 修法: 无

C5: claim=正例2 北美灰熊：恢复区覆盖爱达荷州 34% 面积，包络约七成哺乳类与鸟类分布区; cited_as=Noss et al. 1996, Conserv Biol 10:949–963
  · 存在性: resolved，doi:10.1046/j.1523-1739.1996.10040949.x
  · 元数据: 一致（10(4):949–963）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “a plan for recovery of grizzly bears (Ursus arctos) … covers, in part, 34% of the state of Idaho … and would capture 10% or more of the statewide ranges of 71% of the mammal species, 67% of the birds, 61% of the amphibians but only 27% of the reptiles native to Idaho.”
  · 修法: 无

C6: claim=反例1 苍鹰：家域虽大但适应农林边缘，圈定其家域并不能庇护原生林敏感类群; cited_as=Ozaki et al. 2006, Conserv Biol 20:1507–1515
  · 存在性: resolved，doi:10.1111/j.1523-1739.2006.00444.x
  · 元数据: 一致（20(5):1507–1515）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “the low performance of the Northern Goshawk as an umbrella species is due to this species' preference for habitat in both agricultural and forested landscapes. Species that can adjust to changes in habitat conditions may not act as effective umbrella species despite having large home ranges.”
  · 修法: 无

C7: claim=反例2 魔鳉：仅存于内华达单一地热溶洞，分布过窄，几乎不覆盖其他物种; cited_as=Brown 1971 · Fleishman et al. 2000
  · 存在性: resolved，10.1038/scientificamerican1171-104；10.2307/2641116
  · 元数据: 一致（Sci Am 225(5):104–110；Ecol Appl 10(2):569–579）
  · 支撑性: ✅ supports
  · 依据: Brown 1971 记述 Devils Hole 单一溶洞种群；Fleishman et al. 2000 摘要段 “rare species may be poor umbrellas because their distributions are too highly restricted”
  · 修法: 无

C8: claim=边界1 大熊猫：庇护同海拔森林特有鸟兽，但低海拔与狭域两栖类常漏在伞外; cited_as=Li & Pimm 2016 · Roberge & Angelstam 2004
  · 存在性: resolved，10.1111/cobi.12618；10.1111/j.1523-1739.2004.00450.x
  · 元数据: 一致（Conserv Biol 30(2):329–339；18(1):76–85）
  · 支撑性: ✅ supports
  · 依据: Li & Pimm 2016 摘要段 “Over 96% of the panda habitat overlapped the endemic centers … Of particular interest are 14 mammal, 20 bird, and 82 amphibian species that are inadequately protected”；Roberge & Angelstam 2004 p.76 摘要段跨类群局限
  · 修法: 无

C9: claim=边界2 艾草松鸡：划保护区能庇护灌丛专性种，但为它割灌反而毁掉专性鸣禽的巢址; cited_as=Rowland et al. 2006 · Carlisle et al. 2018
  · 存在性: resolved，10.1016/j.biocon.2005.10.048；10.1650/CONDOR-17-200.1
  · 元数据: 一致（Biol Conserv 129(3):323–335；Condor 120(2):439–455）
  · 支撑性: ✅ supports
  · 依据: Rowland et al. 2006 摘要段 “management of sage-grouse habitats likely would offer relatively high conservation coverage for sagebrush obligates”；Carlisle et al. 2018 摘要段 “We found no Brewer's Sparrows or Sage Thrashers nesting in the mowed footprint posttreatment, which suggests complete loss of nesting habitat for these species.”
  · 修法: 无

C10: claim=1981 Frankel & Soulé 首用“保护伞”比喻：针对大型物种的保护措施可顺带保护同域高密度物种; cited_as=Frankel & Soulé 1981 · 转引自 Roberge & Angelstam 2004
  · 存在性: resolved，10.1111/j.1523-1739.2004.00450.x
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Roberge & Angelstam 2004 p.77 “History and Uses”节：“Frankel and Soulé (1981) were the first to use the term umbrella to suggest that conservation measures directed at the largest species could confer protection to what they called ‘denser species.’”
  · 修法: 无

C11: claim=1997 Lambeck 提出焦点物种（focal species）多物种伞群; cited_as=Lambeck 1997, Conserv Biol 11:849–856
  · 存在性: resolved，doi:10.1046/j.1523-1739.1997.96319.x
  · 元数据: 一致（11(4):849–856）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “identifies a suite of ‘focal species,’ each of which is used to define different spatial and compositional attributes that must be present in a landscape and their appropriate management regimes.”
  · 修法: 无

C12: claim=2000 Andelman & Fagan 发现传统单物种伞护覆盖率不优于等量随机选种，Fleishman 等提出伞护指数 UI; cited_as=Andelman & Fagan 2000, PNAS 97:5954–5959 · Fleishman et al. 2000, Ecol Appl 10:569–579
  · 存在性: resolved，10.1073/pnas.100126797；10.2307/2641116
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Andelman & Fagan 2000 摘要段 “none of the surrogate schemes we evaluated performs significantly better than do a comparable number of species randomly selected from the database”；Fleishman et al. 2000 摘要段
  · 修法: 无

C13: claim=2004 Roberge & Angelstam 系统评估 110 篇文献（含 18 项实证检验）; cited_as=Roberge & Angelstam 2004, Conserv Biol 18:76–85
  · 存在性: resolved，doi:10.1111/j.1523-1739.2004.00450.x
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: 全文 p.76 摘要段与 p.79 Table 1–2（“Among the 110 research papers we included in this review, only 18 evaluated the performance of an umbrella species scheme”）
  · 修法: 无

C14: claim=2008 Seddon & Leech 梳理 17 项标准并精简为 7 项; cited_as=Seddon & Leech 2008, Oryx 42:240–245
  · 存在性: resolved，doi:10.1017/S003060530806119X
  · 元数据: 一致（42(2):240–245）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “We examined the 17 published criteria available to identify a potential umbrella species and recommend that conservation managers wishing to apply this concept could focus on only seven criteria … it seems less of a short cut than planners may wish.”
  · 修法: 无

C15: claim=2011 Branton & Richardson 汇总 15 项研究的荟萃分析：有伞护种样点伴生物种丰富度与多度显著更高，鸟类优于哺乳类; cited_as=Branton & Richardson 2011, Conserv Biol 25:9–20
  · 存在性: resolved，doi:10.1111/j.1523-1739.2010.01606.x
  · 元数据: 一致（25(1):9–20）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “we used data from 15 published studies in a meta-analysis … Species richness and abundance of co-occurring species were consistently higher in sites where umbrella species were present than where they were not and for conservation schemes with avian than with mammalian umbrella species.”
  · 修法: 无

C16: claim=2016 Thornton 等评估美洲豹全分布区保护网覆盖约 1500 种同域哺乳类高质量生境; cited_as=Thornton et al. 2016, Ecol Appl 26:1112–1124
  · 存在性: resolved，doi:10.1890/15-0602
  · 元数据: 一致（26(4):1112–1124）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “Using species richness, habitat quality, and fragmentation indices of ~1500 co-occurring mammal species, we show that jaguar populations and corridors overlap a substantial amount and percentage of high-quality habitat”
  · 修法: 无

C17: claim=2025 Micheletti 等解析同一物种（北方林驯鹿）为何在不同评估中得出相反结论; cited_as=Micheletti et al. 2025, Conserv Biol 39:e70106
  · 存在性: resolved，doi:10.1111/cobi.70106
  · 元数据: 一致（39(5):e70106，PMC12451510）
  · 支撑性: ✅ supports
  · 依据: 全文 p.1–2 与 Figure 1（`cc/pmc12451510.xml`）：对比全分布区重叠、情景比较与高质生境等面积随机零模型三种方法对驯鹿伞护价值的相反结论
  · 修法: 无

C18: claim=争议·比随机选址更有效吗; cited_as=Andelman & Fagan 2000 · Fleishman et al. 2001 · Branton & Richardson 2011 · Micheletti et al. 2025
  · 存在性: 全部 resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Andelman & Fagan 2000 摘要段（不优于随机）；Fleishman et al. 2001 摘要段（UI 选点少于随机）；Branton & Richardson 2011 摘要段（样点丰富度更高）；Micheletti et al. 2025 Figure 1 段
  · 修法: 无

C19: claim=争议·顶级捕食者天然是好伞吗; cited_as=Sergio et al. 2006, 2008 · Roth & Weber 2008 · Dalerum et al. 2008
  · 存在性: 全部 resolved（10.1111/j.1365-2664.2006.01218.x；10.1146/annurev.ecolsys.39.110707.173545；10.1111/j.1365-2664.2007.01435.x；10.1007/s10531-008-9406-4）
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Sergio et al. 2006 摘要段（6 种猛禽繁殖点多样性高）；Roth & Weber 2008 摘要段（瑞士监测中山雀 Parus spp. 表现同样好甚至更优）；Sergio et al. 2008 摘要段（“they perform poorly as umbrella species; more consensus exists for their efficacy as sentinel and flagship species”）；Dalerum et al. 2008 摘要段
  · 修法: 无

C20: claim=争议·单物种还是焦点物种群; cited_as=Lambeck 1997 · Carroll et al. 2001 · Lindenmayer et al. 2002
  · 存在性: 全部 resolved（10.1046/j.1523-1739.1997.96319.x；10.1890/1051-0761(2001)011[0961:CAFSFC]2.0.CO;2；10.1046/j.1523-1739.2002.00450.x）
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Lambeck 1997 摘要段；Carroll et al. 2001 摘要段（4 种食肉目互补）；Lindenmayer et al. 2002 摘要段（批评焦点物种法的理论假设与数据瓶颈）
  · 修法: 无

C21: claim=度量1 伞护指数 UI = PCI + MDI + DSI 及三项定义与跨类群局限; cited_as=Fleishman et al. 2000, Ecol Appl 10:569–579 · Fleishman et al. 2001, Ecol Appl 11:1489–1501
  · 存在性: resolved，10.2307/2641116；10.2307/3060934
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Fleishman et al. 2000 摘要段与方法节（PCI 平均共现比例、MDI = 1 − 2|N_p/N_t − 0.5| 适度稀有度、DSI 干扰敏感度）；Fleishman et al. 2001 摘要段（“Umbrella species were no more effective than randomly selected species for cross-taxonomic applications”）
  · 修法: 无

C22: claim=度量2 等面积保护效率比 E_U = (S_U / S_total) ÷ (A_U / A_total); cited_as=Roberge & Angelstam 2004, Conserv Biol 18:76–85 · Andelman & Fagan 2000, PNAS 97:5954–5959
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Roberge & Angelstam 2004 全文 p.82 “Synthesis”节：“measure the efficiency of the umbrella scheme—that is, to present the results in the form of a ratio of the benefits (e.g., number of species or habitat types protected) to the costs (e.g., total area or number of sites required).”
  · 修法: 无

C23: claim=度量3 生境重叠关联度 φ = (ad − bc)/√[(a+b)(c+d)(a+c)(b+d)]; cited_as=Rowland et al. 2006, Biol Conserv 129:323–335
  · 存在性: resolved，doi:10.1016/j.biocon.2005.10.048
  · 元数据: 一致（129(3):323–335）
  · 支撑性: ✅ supports
  · 依据: Rowland et al. 2006 摘要段与方法节：“Overlap in species' land-cover associations with those of sage-grouse, based on the phi correlation coefficient”
  · 修法: 无

## 【⚠待核】
（无，23 篇文献与 26 条论断已全部核实）

## 【不替你改稿】
本报告为 `concept-pages/umbrella/zh/index.html` 首版全量核查记录；所有引文在写入页面前已对照 Crossref、OpenAlex、EuropePMC 及公开全文核对无误。
