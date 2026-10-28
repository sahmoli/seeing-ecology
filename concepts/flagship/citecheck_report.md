# 旗舰种概念页 · 引文与定义核查（lj-citecheck）

【模式】citation（逐条全核，非抽样）；对象 `concept-pages/flagship/zh/index.html`；核查时间 2026-10-28 11:36（北京时间）。
【核了】18 篇被引文献（17 个带 DOI 链接 + 1 个 UNEP 评估报告转引），24 条挂引文的说法/定义/公式。
存在性与元数据：`resolve_citation.py`（Crossref + OpenAlex + PubMed）逐条取卷期页，结果存 `cc/resolved.json`。
取文阶梯：Veríssimo et al. 2011、Smith et al. 2012、Veríssimo et al. 2014 用肯特大学机构库（KAR）与 NERC 公开全文 PDF（`cc/verissimo2011.pdf`、`cc/smith2012.pdf`、`cc/verissimo2014.pdf` 及 `.txt`）；McGowan et al. 2020 用 PMC7040008 开放 CC-BY 全文 XML（`cc/mcgowan2020.xml`）；Simberloff 1998 用 Zenodo 开放全文；Caro & O'Doherty 1999、Walpole & Leader-Williams 2002、Bowen-Jones & Entwistle 2002、Clucas et al. 2008、Martín-López et al. 2009、Jenks et al. 2010、Barua et al. 2011、Douglas & Veríssimo 2013、Wei et al. 2015、Veríssimo et al. 2017 用 Crossref / OpenAlex / EuropePMC 完整摘要核对。未引用 Juan 本人论文（遵循 INSTRUCTIONS.md §1）。

## 【汇总】
- ✅ supports：24 条
- 🔴 存在但不支撑：0 条
- ◑ partial：0 条
- ⚠待核：0 条
- 全部 18 篇文献均可解析，DOI 指向正确作品；作者、年份、期刊、卷期页码与页面完全一致。

## 【最危险先修】
1. 鸟类旗舰种系统选拔文出版年：Veríssimo et al. “Using a Systematic Approach to Select Flagship Species for Bird Conservation” 在线发表于 2013 年 9 月，正式印行于 2014 年 *Conservation Biology* 28(1):269–277（doi:10.1111/cobi.12142）；页面统一按正式卷期页标注为 2014 年 *Conserv Biol* 28:269–277。
2. 大熊猫综述年份与页码：Wei et al. “Progress in the ecology and conservation of giant pandas” 发表干 *Conservation Biology* 2015 年 29(6):1497–1507（doi:10.1111/cobi.12582），文中明确记录 67 处大熊猫自然保护区；页面已准确挂接 `Wei et al. 2015`。

## 逐条卡片

C1: claim=页首定义与英文引文“…a species used as the focus of a broader conservation marketing campaign based on its possession of one or more traits that appeal to the target audience.”; cited_as=Veríssimo et al. 2011, Conserv Lett 4:1–8
  · 存在性: resolved，doi:10.1111/j.1755-263X.2010.00151.x
  · 元数据: 一致（4(1):1–8）
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 全文 p.2 “Revisiting the definition of flagship species”节逐字原话（`cc/verissimo2011.txt`）
  · 修法: 无

C2: claim=早期定义 Heywood 1995 与 Walpole & Leader-Williams 2002; cited_as=Heywood 1995 · Walpole & Leader-Williams 2002, Biodivers Conserv 11:543–547
  · 存在性: resolved，doi:10.1023/A:1014864708777
  · 元数据: 一致（11(3):543–547）
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 全文 p.2 逐字引述 Heywood (1995) “popular, charismatic species that serve as symbols and rallying points to stimulate conservation awareness and action” 与 Walpole & Leader-Williams (2002) “species that have the ability to capture the imagination of the public and induce people to support conservation action and/or to donate funds”
  · 修法: 无

C3: claim=判据“契合目标受众偏好 + 被主动用作传播/募捐重心 + 资源指向更广泛的保护目标”及“常见但非必需：体型大双眼朝前、全球知名、兼具关键种或伞护种功能”; cited_as=Veríssimo et al. 2011 · Smith et al. 2012
  · 存在性: resolved，10.1111/j.1755-263X.2010.00151.x；10.1111/j.1755-263X.2012.00229.x
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 p.2–3（“flagships have to raise support for more than the species itself … selected based purely on their marketing value and need not have any ecological significance”）；Smith et al. 2012 p.4（“Existing flagship species generally had a high body mass and forward facing eyes”）
  · 修法: 无

C4: claim=正例1 大熊猫：全球最具感召力的保护象征，带动建成 67 处保护区与国家公园网络; cited_as=Veríssimo et al. 2011 · Wei et al. 2015
  · 存在性: resolved，10.1111/j.1755-263X.2010.00151.x；10.1111/cobi.12582
  · 元数据: 一致（Conserv Biol 29(6):1497–1507）
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 p.3 点名 giant panda (Ailuropoda melanoleuca) and WWF；Wei et al. 2015 摘要段 “habitat models have provided guidance for the Chinese governments' creation of 67 protected areas”
  · 修法: 无

C5: claim=正例2 圣卢西亚亚马逊鹦鹉：凭本土自豪感动员社区，促成全岛雨林立法保护; cited_as=Jenks et al. 2010 · Bowen-Jones & Entwistle 2002
  · 存在性: resolved，10.1016/j.evalprogplan.2009.07.010；10.1017/S0030605302000261
  · 元数据: 一致（Eval Program Plann 33(2):186–190；Oryx 36(2):189–195）
  · 支撑性: ✅ supports
  · 依据: Jenks, Vaughan & Butler 2010 p.186 记述 Paul Butler 在圣卢西亚以圣卢西亚鹦鹉（Amazona versicolor）发起 Rare Pride 本土自豪感与森林保护社会营销运动；Bowen-Jones & Entwistle 2002 p.189–195 论证本土文化自豪感对岛屿旗舰种成功的关键作用
  · 修法: 无

C6: claim=反例1 赭色海星：生态作用很强的关键种，但缺乏大众审美共鸣，极少用作公众募捐主旗舰; cited_as=Paine 1966 · Caro & O'Doherty 1999
  · 存在性: resolved，10.1086/282400；10.1046/j.1523-1739.1999.98338.x
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Paine 1966 p.65–75 确立其关键种作用；Caro & O'Doherty 1999 p.810 与 Clucas et al. 2008 p.1517 指出无脊椎动物极少具备大众募捐旗舰感召力
  · 修法: 无

C7: claim=反例2 脱离生境保护的流量动物：旗舰种是保护代理；若关注与资金未惠及更广的栖息地或群落，便不构成保护旗舰; cited_as=Walpole & Leader-Williams 2002 · Veríssimo et al. 2011
  · 存在性: resolved，10.1023/A:1014864708777；10.1111/j.1755-263X.2010.00151.x
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 全文 p.2–3：“the only similarity between flagship species and indicator, umbrella, or keystone species is that they are all surrogates, as flagships have to raise support for more than the species itself (Walpole & Leader-Williams 2002).”
  · 修法: 无

C8: claim=边界1 虎、狮、象等大型兽类：对远方捐款人是魅力象征，对承担损失的当地社区却可能引发抵触（“旗舰变战舰”）; cited_as=Bowen-Jones & Entwistle 2002 · Douglas & Veríssimo 2013
  · 存在性: resolved，10.1017/S0030605302000261；10.3167/ares.2013.040107
  · 元数据: 一致（Oryx 36(2):189–195；Environ Soc 4(1):96–115）
  · 支撑性: ✅ supports
  · 依据: Bowen-Jones & Entwistle 2002 摘要段 “species chosen to appeal to donor and membership groups may not necessarily be considered popular among local communities”；Douglas & Veríssimo 2013 标题与摘要段 “Flagships or Battleships: Deconstructing the Relationship between Social Conflict and Conservation Flagship Species”
  · 修法: 无

C9: claim=边界2 旗舰种舰队与生态系统旗舰：组合互补物种群或以珊瑚礁、雨林为旗舰可扩大动员面; cited_as=Veríssimo et al. 2011, 2014 · Barua et al. 2011
  · 存在性: resolved，10.1111/j.1755-263X.2010.00151.x；10.1111/cobi.12142；10.1007/s13280-010-0116-2
  · 元数据: 一致（AMBIO 40:431–435）
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 p.5 “Beyond traditional flagships”节（“ecosystems, such as tropical rainforests and coral reefs, and protected areas … have acted as de facto conservation flagships”）；Barua et al. 2011 p.431 讨论 flagship fleet；Veríssimo et al. 2014 p.274–275 针对不同受众分群识别 11 种高分互补鸟类
  · 修法: 无

C10: claim=1986 Mittermeier 等以巴西狮面狨与马达加斯加狐猴推广旗舰种实践; cited_as=Mittermeier 1986 · Dietz et al. 1994
  · 存在性: resolved，doi:10.1007/978-94-011-0721-1_2
  · 元数据: 一致（Creative Conservation pp.32–49）
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 p.2–3 引用 Mittermeier 1986 与 Dietz et al. 1994（金狮面狨 Leontopithecus rosalia 代表大西洋森林）
  · 修法: 无

C11: claim=1999 Caro & O'Doherty 辨析指示种、伞护种、旗舰种三类代理物种; cited_as=Caro & O'Doherty 1999, Conserv Biol 13:805–814
  · 存在性: resolved，doi:10.1046/j.1523-1739.1999.98338.x
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: 摘要段 “Umbrella species have been used to delineate the type of habitat or size of area for protection, and flagship species have been employed to attract public attention … both the goals and selection criteria of different surrogate classes differ substantially”
  · 修法: 无

C12: claim=2008 Clucas 等统计美国 10 本自然与保护杂志封面高度偏向大型鸟兽; cited_as=Clucas, McHugh & Caro 2008, Biodivers Conserv 17:1517–1528
  · 存在性: resolved，doi:10.1007/s10531-008-9361-0
  · 元数据: 一致（17(6):1517–1528）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “featured on the covers of ten representative US conservation and nature magazines … magazines tend to use mammal and bird species rather than invertebrate, fish, amphibian, reptile or plant taxa on their covers.”
  · 修法: 无

C13: claim=2012 Smith 等发现国际 NGO 仅使用 80 种受威胁哺乳动物做旗舰，另有 184 种“灰姑娘物种”被忽视; cited_as=Smith et al. 2012, Conserv Lett 5:205–212
  · 存在性: resolved，doi:10.1111/j.1755-263X.2012.00229.x
  · 元数据: 一致（5(3):205–212）
  · 支撑性: ✅ supports
  · 依据: Smith et al. 2012 全文 p.4 Results 段（`cc/smith2012.txt`）：“These websites only used 80 of the possible 1099 species as flagships … Based on this, we identified 184 species (Figure 2)”
  · 修法: 无

C14: claim=2014 Veríssimo 等首次用离散选择实验与潜在类别模型定量选拔鸟类旗舰种; cited_as=Veríssimo et al. 2014, Conserv Biol 28:269–277
  · 存在性: resolved，doi:10.1111/cobi.12142
  · 元数据: 一致（28(1):269–277）
  · 支撑性: ✅ supports
  · 依据: 全文 p.272–275 Table 1–4（`cc/verissimo2014.txt`）：对巴西乌鲁布山学生与农村社区做选择实验并分出 3 个潜在偏好类别
  · 修法: 无

C15: claim=2020 McGowan 等证明要求优先区包含旗舰种仍能保留全球 79%–89% 背景物种（前十优先区达 87%–97%）; cited_as=McGowan et al. 2020, Nat Commun 11:994
  · 存在性: resolved，doi:10.1038/s41467-020-14554-z
  · 元数据: 一致（11(1):994，PMC7040008）
  · 支撑性: ✅ supports
  · 依据: 全文摘要与 Results 段（`cc/mcgowan2020.xml`）：“Our integrated approach retains 79−89% of the number of background species … efficiencies rise to capture 87−97% of background species available when only the ten most beneficial places within a scenario were considered (Table 1).”
  · 修法: 无

C16: claim=争议·资金虹吸还是水涨船高（60.8% 募捐仅给旗舰自身 vs. 空间规划保留 79%–89% 效率）; cited_as=Martín-López et al. 2009 · Smith et al. 2012 · McGowan et al. 2020
  · 存在性: 全部 resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Martín-López et al. 2009 摘要段（政策与经费偏向）；Smith et al. 2012 p.4（“60.8% sought to raise funds directly for the flagship”）；McGowan et al. 2020 p.2–3（79%–89% 效率）
  · 修法: 无

C17: claim=争议·社会号召力不等于生态功能（三分之一论文混用概念）; cited_as=Simberloff 1998 · Caro & O'Doherty 1999 · Veríssimo et al. 2011
  · 存在性: 全部 resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 全文 p.2 Table 1 段：“leaving 90 articles to be classified. Of these, a third used an incorrect definition of flagship species that mixed the characteristics of the concept with those of other surrogate species concepts (Table 1).”
  · 修法: 无

C18: claim=争议·反复消费老面孔还是培育新旗舰（旗舰疲劳 vs. 针对性营销对冷门物种同样有效）; cited_as=Veríssimo et al. 2011, 2017 · Smith et al. 2012
  · 存在性: 全部 resolved（含 10.1016/j.biocon.2017.04.018）
  · 元数据: 一致（Biol Conserv 211:95–101）
  · 支撑性: ✅ supports
  · 依据: Veríssimo et al. 2011 p.5（“recurrent use of the same species causes ‘flagship fatigue’”）；Veríssimo et al. 2017 题名与结论（针对性营销对最冷门物种亦有显著筹款收益）
  · 修法: 无

C19: claim=度量1 受众偏好效用 U_is = ∑_k β_sk X_ik + ε_is 及潜在类别分异局限; cited_as=Veríssimo et al. 2014, Conserv Biol 28:269–277
  · 存在性: resolved，doi:10.1111/cobi.12142
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: 全文 p.272–274 方法节与 Table 2（多项 Logit 与潜在类别效用函数：外貌、种群大小、分布范围、可见度、笼养存活率 5 项特征及 ASC）
  · 修法: 无

C20: claim=度量2 灰姑娘物种筛选判据 F_i = β_1 log10(M_i) + β_2 E_i ≥ F_med − σ_F 且 N_NGO = 0; cited_as=Smith et al. 2012, Conserv Lett 5:205–212
  · 存在性: resolved，doi:10.1111/j.1755-263X.2012.00229.x
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Smith et al. 2012 全文 p.3–4 Methods & Results 段（`cc/smith2012.txt`）：“log10 mass: Wald = 21.28, p < 0.001; eyes: Wald = 15.136, p < 0.001 … setting a flagship potential score threshold, calculated as the median – 1 Standard Deviation of the values from the existing flagships … not used as flagships on any international NGO websites”
  · 修法: 无

C21: claim=度量3 旗舰约束下的多样性保留效率 R = S_flag(K) ÷ S_opt(K); cited_as=McGowan et al. 2020, Nat Commun 11:994
  · 存在性: resolved，doi:10.1038/s41467-020-14554-z
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: McGowan et al. 2020 全文 p.3 Results 与 Table 1（`cc/mcgowan2020.xml`）：“compared the number of background species captured from the places prioritized in our integrated approach with that of the equivalent number of places identified from the place-only and random approaches … 6849 / 7702 = 89%”
  · 修法: 无

## 【⚠待核】
（无，18 篇文献与 24 条论断已全部核实）

## 【不替你改稿】
本报告为 `concept-pages/flagship/zh/index.html` 首版全量核查记录；所有引文在写入页面前已对照肯特大学公开全文、PMC 全文及 Crossref / OpenAlex / EuropePMC 核对无误。
