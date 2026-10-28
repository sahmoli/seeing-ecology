# 关键种概念页 · 引文与定义核查（lj-citecheck）

【模式】citation（逐条全核，非抽样）；对象 `concept-pages/keystone/zh/index.html`；核查时间 2026-10-28 11:00（北京时间）。
【核了】22 篇被引文献（含 2026-10-28 11:20 补核新增的 Paine 1980）（15 个带 DOI 链接 + 6 个仅作者年份引用），30 条挂引文的说法/定义/公式。
存在性与元数据：`resolve_citation.py`（Crossref + OpenAlex）+ Crossref 逐条取卷期页，结果在 `cc/resolved.json`。
取文阶梯：Power 1996、Simberloff 1998 用 Zenodo/Plazi 公开 CC-BY 全文；Mills 1993 用 Zenodo 8204920 公开 CC-BY 全文（`cc/mills1993.pdf`）；Valls 2015 用 Archimer 公开全文（`cc/valls.pdf`，全文已读）；Jordán 2009 用 PMC2685432 全文（`cc/jordan.html/.txt`）；Paine 1980 用公开课程全文（摘录见 `cc/paine1980_excerpt.txt`）；Jones 1994 用作者机构公开扫描本；Cottee-Jones 2012 用 eScholarship CC-BY 全文片段；其余用摘要（OpenAlex/出版社/HERO）。未检索 Juan 的 Zotero（本次未授权）。

## 【汇总】
- ✅ supports：16 条
- 🔴 存在但不支撑（已改）：1 条（Cottee-Jones & Whittaker 2012）
- ◑ partial（已改写或改引）：8 条
- ◑ 已软化措辞（无具体引文挂靠的推论）：2 条
- 补核后变化：C6 换成真实物种并 ✅；C26 ◑→✅（全文）；C12 由转引改为全文核实，◑ 已改写；C10 原话由两篇同行评审文献逐字确认
- ⚠待核：0 条（2026-10-28 11:20 补核全部解决，见文末【补核记录】）
- 21 篇文献全部可解析，DOI 指向正确作品；作者/年/刊/卷期页与页面一致，无误引。Davic 2003 = Conserv Ecol 7(1): r11 复核无误。

## 【最危险先修】
1. 2012 时间线：原文“系统评述：概念被滥用、证据不足，主张回到可检验的定义”。原文结论正相反：作者认为难以建立带定量阈值的稳健定义，提议宽定义 “a keystone species is a species that is of demonstrable importance for ecosystem function”，并说该词的价值可能更多在隐喻；且文章是 perspective，不是系统评述。已改为“批判性评述：定义太多、太含糊，难有统一的定量阈值；提议宽定义‘对生态系统功能有可证实重要性的物种’”。

2. 1993 时间线（补核）：原文“几乎任何重要物种都叫关键种”Mills 1993 没有；原文核心主张是不再给物种贴关键种标签、改测互作强度（p.223）。已改为“批评这个词用得太宽、定义含糊；主张不再给物种贴‘关键种’标签，改测互作强度。”

## 逐条卡片

C1: claim=页首定义与英文引文“one whose impact … disproportionately large relative to its abundance”; cited_as=Power et al. 1996, BioScience 46:609–620
  · 存在性: resolved，doi:10.2307/1312990
  · 元数据: 一致（10 位作者，46(8):609–620）
  · 支撑性: ✅ supports
  · 依据: Power 1996 全文 p.609 定义段（Zenodo 10.5281/zenodo.19668411）；中文译文忠实
  · 修法: 无

C2: claim=判据“移走它变化大 + 影响远大于丰度所能解释”; cited_as=Power et al. 1996
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: p.609 “effects are much larger than would be predicted from their abundance”；“常见但非必需”与 p.611 “not always of high trophic status”一致
  · 修法: 无

C3: claim=赭色海星：移走后加州贻贝占满岩礁（图注：物种数 15→8）; cited_as=Paine 1966, 1969
  · 存在性: resolved，10.1086/282400；10.1086/282586
  · 元数据: 一致（Am Nat 100(910):65–75；103(929):91–93）
  · 支撑性: ✅ supports
  · 依据: Paine 1966 “Changes resulting from the removal of the top carnivore”段：“from a 15 to an eight-species system”，“eventually … dominated by Mytilus”（课程公开 PDF 片段）；1969 p.92 称 Pisaster 为 keystone
  · 修法: 无

C4: claim=海獭吃海胆；海獭消失，海胆啃光海带林; cited_as=Estes & Palmisano 1974
  · 存在性: resolved，10.1126/science.185.4156.1058
  · 元数据: 一致（Science 185:1058–1060）
  · 支撑性: ✅ supports（abstract-level）
  · 依据: 摘要段 “Removal of sea otters causes increased herbivory and ultimately results in the destruction of macrophyte associations”
  · 修法: 无

C5: claim=加州贻贝：影响大、数量也大，是优势种; cited_as=Power et al. 1996
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ◑ partial：Power 1996 给出“优势种”定义（Fig.3 例子是树、巨藻、草原禾草、造礁珊瑚），但全文未点名贻贝为优势种
  · 依据: Power 1996 p.611 Fig.3 图注；Paine 1974 Oecologia 15:93–120（10.1007/BF00345739）标题即称 Mytilus californianus 为 “dominant competitor”
  · 修法: 引注改为“Paine 1974 · Power et al. 1996”

C6: claim=（2026-10-28 已换真实物种）白帽笠螺：移走半年，群落几乎不变：弱互作种; cited_as=Paine 1980, J Anim Ecol 49:667–685
  · 存在性: resolved，doi:10.2307/4220（Crossref：Paine, J Anim Ecol 49(3), 1980）
  · 元数据: 一致（正文 667–685；Crossref 首页 666 含 JSTOR 肖像页）
  · 支撑性: ✅ supports（全文）
  · 依据: pp.677–678 移除实验段：1979 年 6 月在 Tatoosh 岛 15 m² 平台移走 Acmaea mitra，6 个月后 “no apparent compensatory changes in the abundances of other grazers, no differences in the cover of Hedophyllum … and two shifts in the relative abundance of the coralline algae”；结论 “Acmaea mitra clearly is a weakly interacting species”；p.668 弱互作定义 “Removal of a weakly interacting species will yield no or slight change”
  · 注意: 原文说它 “moderately abundant”（1.2–6.1 只/m²），不是“稀有”，所以文案不写“稀有”；动画丰度条设低（0.1）、影响条近零。画法依据 p.679 “A. mitra is often encrusted with corallines”（壳上粉色珊瑚藻斑）
  · 修法: 原示意反例“一种稀有的岩礁螺 / 稀有本身不等于关键”整体替换

C7: claim=同一种海星换个海岸，浪小处控制作用明显减弱; cited_as=Menge et al. 1994
  · 存在性: resolved，10.2307/2937163
  · 元数据: Ecol Monogr 64(3):249–286，作者 5 位（Menge, Berlow, Blanchette, Navarrete, Yamada）
  · 支撑性: ✅ supports（abstract-level）
  · 依据: 摘要段 “strong keystone predation … at wave-exposed headlands; less-strong diffuse predation … at a wave-protected cove”
  · 修法: 无

C8: claim=河狸“筑坝改造整条河”; cited_as=Jones et al. 1994
  · 存在性: resolved，10.2307/3545850（Oikos 69:373–386）
  · 元数据: 一致
  · 支撑性: ◑ partial：原文是筑坝改变水文、造出湿地，没有“整条河”
  · 依据: Jones 1994 p.373 “By cutting trees and using them to construct dams they alter hydrology, creating wetlands”；另有 p.381 “many engineers are keystone species”段
  · 修法: 改为“筑坝成塘，改变河流水文。”

C9: claim=1966 华盛顿州岩岸持续移走海星，多样性下降; cited_as=Paine 1966
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: 摘要段 “experimentally removed, the systems become less diverse”；正文 Mukkaw Bay 段
  · 修法: 无

C10: claim=1969 借“拱心石”提出 keystone species; cited_as=Paine 1969
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports（原文 PDF 仍未取到；同一句由两篇同行评审文献逐字引用，一致）
  · 依据: p.92 “These individual populations are the keystone of the community's structure …”；Mills, Soulé & Doak 1993 p.219 逐字引用此段并注明 Paine 1969（`cc/mills1993.pdf`）；Am Nat 174(3) 10.1086/605920 亦逐字引用。同页还写 “Pisaster is abundant …; Charonia is rare and a food specialist”，支持判据区“稀有、濒危＝常见但非必需”。“拱心石”是词源，不是 Paine 的原话
  · 修法: 无

C11: claim=1974 “关键种从岩礁走向更大的海洋系统”; cited_as=Estes & Palmisano 1974
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ◑ partial：该文是阿留申岛屿有无海獭的比较，同为近岸岩礁系统，摘要未用 keystone 一词
  · 依据: 摘要段首句 “A comparison of western Aleutian Islands with and without sea otter populations”
  · 修法: 改为“比较有无海獭的阿留申岛屿：海獭控制海胆，海带林得以保存。”

C12: claim=1993 词被用得太宽，定义开始模糊; cited_as=Mills, Soulé & Doak 1993
  · 存在性: resolved，10.2307/1312122（Crossref 作者只列 Mills, Doak；OpenAlex 题录与 Power 1996 参考文献均含 Soulé，页面写法正确）
  · 元数据: 一致（43(4):219–224）
  · 支撑性: ◑ partial → 已改（原文全文已读）。“几乎任何重要物种都叫关键种”原文没有；原文的核心主张漏掉了
  · 依据: p.219 “we argue that the term is broadly applied, poorly defined, and nonspecific in meaning”；p.221 “applied to a plethora of species with very different effects”；Conclusions p.223 “neither the science of ecology nor the protection of biodiversity is advanced by continuing to label certain species as keystone. Instead, we advocate the study of interaction strengths”
  · 修法: 改为“批评这个词用得太宽、定义含糊；主张不再给物种贴‘关键种’标签，改测互作强度。”（index.html 与 keystone_body.html 同步）

C13: claim=1996 “影响与丰度不成比例”成为判据并给出 CI 公式; cited_as=Power et al. 1996
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: p.609–610 定义与 CI 公式段
  · 修法: 无

C14: claim=1998 反思旗舰种、伞护种、关键种能否代表整体; cited_as=Simberloff 1998
  · 存在性: resolved，10.1016/S0006-3207(97)00081-5
  · 元数据: 一致（Biol Conserv 83(3):247–257）
  · 支撑性: ◑ partial：文章批评的是指示种、伞护种、旗舰种和生态系统管理；对关键种是相对正面：可能连接单物种与生态系统管理，但不是万能药
  · 依据: 摘要段 “Keystone species may not be a panacea”；正文 “Keystone species management”节 “may combine some attractive features of single-species management and ecosystem management”
  · 修法: 改为“检讨单物种管理：指示种、伞护种、旗舰种各有缺陷；关键种或能连接单物种与生态系统管理，但不是万能药。”

C15: claim=1999 鼠兔洞穴供鸟类和蜥蜴栖身，又是“多数”食肉动物的猎物; cited_as=Smith & Foggin 1999
  · 存在性: resolved，10.1111/j.1469-1795.1999.tb00069.x
  · 元数据: 一致（Anim Conserv 2(4):235–240）
  · 支撑性: ◑ partial：原文是“nearly all … principal prey”，页面写弱了
  · 依据: 摘要段第 (iii) 点 “serves as the principal prey for nearly all of the plateau's predator species”
  · 修法: “多数食肉动物的猎物”→“几乎所有食肉动物的主要猎物”

C16: claim=2003 影响要“远大于”它在功能群中的生物量占比; cited_as=Davic 2003
  · 存在性: resolved，10.5751/ES-00502-0701r11
  · 元数据: 一致（7(1): r11）
  · 支撑性: ◑ partial：原文是 top-down effect … “large relative to” biomass dominance，没有“远大于”
  · 依据: 摘要段定义句
  · 修法: 改为“自上而下的影响，相对它在所属功能群中的生物量占比很大。”

C17: claim=2005 “提出”强互作种; cited_as=Soulé et al. 2005
  · 存在性: resolved
  · 元数据: 一致（55(2):168–176，10.1641/0006-3568(2005)055[0168:SISCPM]2.0.CO;2）
  · 支撑性: ◑ partial：摘要把 strongly interacting species 当作已有概念使用，不能说是此文“提出”；保护目标（维持生态有效密度）支持
  · 依据: 摘要段 “maintaining population densities … of strongly interactive species above estimable thresholds for ecological effectiveness”
  · 修法: “提出”→“聚焦”

C18: claim=2006 用食物网模型算关键性指数，不做移除实验也能排序; cited_as=Libralato et al. 2006
  · 存在性: resolved，10.1016/j.ecolmodel.2005.11.029
  · 元数据: 一致（195(3–4):153–171）
  · 支撑性: ✅ supports（abstract-level）
  · 依据: 摘要段 “the results allow us to rank functional groups by their keystoneness”（HERO 2515447）
  · 修法: 无

C19: claim=2010 “狼救山杨”受质疑，“关键作用的证据之争公开化”; cited_as=Kauffman, Brodie & Jules 2010
  · 存在性: resolved，10.1890/09-1949.1
  · 元数据: 一致（Ecology 91(9):2742–2755）
  · 支撑性: ◑ partial：检验对象是行为介导的营养级联，不是“关键作用”；“公开化”是推论
  · 依据: 摘要段 “has never been adequately tested … aspen are not currently recovering … not diminished in sites where elk are at higher risk”
  · 修法: 改为“‘狼回归救活黄石山杨’接受景观尺度检验，结果不支持这一说法。”

C20: claim=2011 顶级消费者减少引发跨生态系统连锁变化; cited_as=Estes et al. 2011
  · 存在性: resolved，10.1126/science.1205106
  · 元数据: 一致（333(6040):301–306）
  · 支撑性: ✅ supports
  · 依据: 摘要段 “extensive cascading effects of their disappearance in marine, terrestrial, and freshwater ecosystems”
  · 修法: 无

C21: claim=2012 系统评述：概念被滥用、证据不足，主张回到可检验的定义; cited_as=Cottee-Jones & Whittaker 2012
  · 存在性: resolved，10.21425/F5FBG12533
  · 元数据: 一致（Front Biogeogr 4(3):117–127）
  · 支撑性: 🔴 存在但不支撑：结论段说难以建立带阈值的稳健定义，提议宽定义；文章类型是 perspective
  · 依据: Conclusion 段 “little prospect of developing a robust definition with the required thresholds … ‘a keystone species is a species that is of demonstrable importance for ecosystem function’”（eScholarship qt15d2b65t）
  · 修法: 改为“批判性评述：定义太多、太含糊，难有统一的定量阈值；提议宽定义‘对生态系统功能有可证实重要性的物种’。”

C22: claim=2018 关键类群驱动微生物群落结构与功能; cited_as=Banerjee, Schlaeppi & van der Heijden 2018
  · 存在性: resolved，10.1038/s41579-018-0024-1
  · 元数据: 一致（16(9):567–576）
  · 支撑性: ✅ supports
  · 依据: 题名页 “Keystone taxa as drivers of microbiome structure and functioning”
  · 修法: 无

C23: claim=争议·定义该多宽（窄=影响/丰度；宽=强互作种、工程师、基础种）; cited_as=Power 1996 · Jones 1994 · Ellison 2005 · Cottee-Jones 2012
  · 存在性: 全部 resolved（Ellison 10.1890/1540-9295(2005)003[0479:LOFSCF]2.0.CO;2，3(9):479–486）
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Power p.611 把 ecosystem engineers 列为可能的 keystone modifiers；Jones p.381 “many engineers are keystone species”段；Cottee-Jones Tables 1–2；Ellison 摘要段定义 foundation species
  · 修法: 无

C24: claim=争议·证据从哪来（大型动物难做移除实验；黄石之争）; cited_as=Ripple & Beschta 2004 · Kauffman et al. 2010
  · 存在性: resolved（Ripple 10.1641/0006-3568(2004)054[0755:WATEOF]2.0.CO;2，54(8):755–766）
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Ripple 摘要段（狼 1995 重引入后的级联效应）与 Kauffman 摘要段结论相反；Power p.613 “spatial or temporal contrasts … (Estes and Palmisano 1974)”
  · 修法: 无

C25: claim=争议·属于物种还是情境; cited_as=Menge 1994 · Power 1996
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: Menge 摘要段 “suggest it is not universal”；Power “Are there traits that make species keystones?”节 “context dependent”段
  · 修法: 无

C26: claim=争议·模型能否代替实验（结果取决于模型结构和参数，不同指数挑出的物种未必一致）; cited_as=Libralato 2006 · Jordán 2009 · Valls 2015
  · 存在性: resolved（Jordán 10.1098/rstb.2008.0335，364:1733–1741；Valls 10.1890/14-0306.1，85(1):29–47）
  · 元数据: 一致
  · 支撑性: ✅ supports（全文）
  · 依据: Valls 2015 Discussion 段 “inconsistent results were obtained when both KS1 and KS2 indices were used”，“KS1 index frequently attributed high keystoneness to functional groups with high biomass”；案例模型中 KS1 头名落在高影响高生物量组，KS2 头名为过路虎鲸和鸟类捕食者。Jordán 2009（PMC2685432）Table 1 与 Fig. 3 段，Kuosheng Bay 食物网：TI5 选出第 14 组，TI10 选出第 4 组，TF 下第 9 组从第 7 名跳到第 2 名，“degree (D) predicts very similar, but somewhat different results”
  · 修法: 无

C27: claim=CI 公式 CI_i = [(t_N − t_D)/t_N]·(1/p_i) 及各项含义; cited_as=Power et al. 1996
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports
  · 依据: p.609–610 公式段：t_N 为完整群落中的性状，t_D 为删除物种 i 后的性状，p_i 为物种 i 的比例丰度（多数情况用生物量）
  · 修法: 无

C28: claim=CI 局限“或改用生物量算丰度，结果就变”; cited_as=无单独引注（推论）
  · 存在性: 不适用
  · 元数据: 不适用
  · 支撑性: ◑ 推论；原句暗示默认不用生物量，与 Power p.609 “in most cases, proportional biomass”不符
  · 依据: Power 1996 p.609 公式段
  · 修法: 改为“换一个性状，或换一种丰度算法，结果就变”

C29: claim=Paine 1992 PI = (N − D)/D · 1/Y，N/D 为“捕食者”在/不在时“猎物”数量，Y 为捕食者密度; cited_as=Paine 1992, Nature 355:73–75
  · 存在性: resolved，10.1038/355073a0
  · 元数据: 一致（355(6355):73–75）
  · 支撑性: ◑ partial：公式正确；但 Paine 1992 测的是 7 种植食性动物对海带幼孢子体的作用，原文用 consumer/grazer，不是捕食者-猎物
  · 依据: Power 1996 p.610 对 Paine 指数的复述 “[(t_N − t_D)/t_D](1/n) … abundance of the prey in the presence of the consumer … number of consumer individuals”
  · 修法: 标签改为“消费者在时，被食者的数量 / 移走消费者后，被食者的数量 / 消费者的密度”

C30: claim=Libralato KS_i = log[ε_i·(1 − p_i)]，ε_i 来自混合营养影响矩阵，p_i 为生物量占比; cited_as=Libralato et al. 2006
  · 存在性: resolved
  · 元数据: 一致
  · 支撑性: ✅ supports（secondary）
  · 依据: Valls 2015 正文公式 (1)–(3) 段复述 KS1 = log[ε_i × (1 − p_i)]，ε_i 为对其他各组 MTI 的平方和开方；Libralato 摘要段
  · 修法: 无

## 【⚠待核】
（已全部解决，见下）

## 【补核记录】2026-10-28 11:20（北京时间）
- ✅ C12 Mills 1993：Zenodo 公开全文（CC-BY）已读；页面措辞已改，补上作者“改测互作强度”的核心主张。
- ✅ C26：Valls 2015 Archimer 全文 + Jordán 2009 PMC 全文都支持“不同指数挑出的物种未必一致”。
- ✅ Paine 1969 p.92 原话：Mills 1993 p.219 与 Am Nat 2009 两篇同行评审文献逐字引用一致。原文 PDF 仍未取到：OceanRep 公开条目实际要 GEOMAR 机构登录；Sci-Hub 镜像弹出人机验证，未绕过。如 Juan 有 JSTOR/学校账号，可补存原 PDF 到 `cc/`。
- ✅ C6 换成真实物种：白帽笠螺 Acmaea mitra（Paine 1980 移除实验），卡片文字、引注、物种画（exviz/sp.js `limpet`）和场景（exviz/script.js `S.limpet`）已同步更新。
- 所有取到的 PDF 只存 `cc/`，用于核对，不在页面链接或转发。

## 【不替你改稿】（以下为首轮记录；补核轮另改了 C6、C12，备份 `zh/index.pre_c6_footer.bak.html`）
本次是按委托直接改页面：只改了上面列出的 13 处文字/引注，未动版式和动画；改前备份 `zh/index.pre_citecheck.bak.html`、`../keystone_body.pre_citecheck.bak.html`。C6 示意反例、C12、C26 未改，留给 Juan 判断。
注意：`keystone_body.html` 已落后于 index.html（例子区和度量区还是旧版），本次只同步了两边都存在的 9 处文字。
