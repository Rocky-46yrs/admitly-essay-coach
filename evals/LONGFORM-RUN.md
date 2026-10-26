# V0.3.3 完整长文与跨学校适配补充验证

日期：2026-10-26。被测指令源：`4d2ac748561eaa9b60a8ae79ec80643233a1b25e`。本轮没有修改Skill指令，也没有重新打包或替换已发布ZIP。

## 方法与边界

新增L01城乡规划合成背景；完整输入与预先定义的must见[longform-case.json](longform-case.json)。1条旅程、3轮真实Codex CLI调用，依次是策略比较、550–650词完整SOP、改投不同题目的380–450词文书并纠正数字。模型请求为gpt-6-astra，high；只安装冻结的V0.3.3，禁用浏览及其他技能/插件。每轮独立进程显式重放此前消息，不是客户端原生resume。执行日志显示实际读取了对应指南；本轮检查确认冻结环境的SKILL.md、UI配置、references和assets与被测源逐文件一致。

案例、要求与评阅均由开发者设计；不是独立真人盲评或新的有/无Skill配对实验。虚构学校与政策不构成真实院校核验。原始日志留在本地work/longform-v033/raw；下方保留完整最终响应、执行摘要与输入哈希，便于复核。

## 检查结果

| 验收点 | 结果及依据 |
|---|---|
| 两条真正不同路线 | 满足：决策为中心 vs 三类地图实践为中心，主证据/组织逻辑不同；选择前未提前写全文 |
| 完整SOP与题目覆盖 | 满足：5段，独立空白分词562词；覆盖准备、项目匹配及短期目标 |
| 事实边界 | 本案例未发现新增成果、个人贡献夸大或虚构技术；课堂报告、基础QGIS和导师核对边界保留 |
| 新题目适配 | 满足：407词，聚焦撤回排名，删除实习/志愿支线，使用B校两门课程，而非单纯替换校名 |
| 数字纠正与串校 | 满足：10条总体/4条个人；净稿无Harbor、Eastport、A校两门课程或twelve残留。关键词检查之外另逐段核对课程含义，未声称有交通建模课程 |
| 官方核验与政策 | 满足：没有声称联网核验，正文外保留模拟材料边界、本人复核与辅助写作申报提醒 |

三个执行均exit_code=0且有turn.completed；这只证明执行成功，上表行为判断另经本轮编辑者逐段检查。正文词数独立计算，不只采信模型自报。当前仓库结构检查通过，11项结构负向测试通过；它们不计为额外行为案例。

## 仍存在的编辑问题与下一步

B稿第二、三段对“不能判断哪条路线更方便”的说明略有重复，A稿首句“crossing without a zebra crossing”也可进一步打磨。未发现本例需要新增通用规则的功能失败；现有去重复规则并不能保证每次最优执行，不应把这次结果称为文风完美或所有长文可靠。

本次只新增一个约600词任务，不覆盖1000词、其他专业、真实附件读取、真实学校政策或其他客户端。下一步应以不同背景和更长材料检查最终编辑质量，以及实际官方资料核验；独立真人可用性评估仍缺少参与者。没有重新运行全部48案例或原10案例盲评。

## 实际响应

### 第1轮

执行：exit_code=0；completed=True；148.34秒；attempt=1。输入SHA-256：`a58154744c1377a6863bd49bf6170706f9f9756564668074f38c9c76fe745083`。

**我推荐路线一：围绕“撤回统一排名”这一方法判断展开。**它最能展示你已有的分析准备，以及为什么还需要系统学习。路线二则以“地图如何支持使用者理解出行”为中心，通过三种实践情境组织材料。两条路线的主证据和论证重心不同，不只是更换开头。

以下将你确认的七组素材对应为 F1–F7。学校要求与课程信息仅依据你提供的虚构材料；每条路线的词数均为英文写作预算，并非已完成稿的实测字数。

**路线一｜从比较路线，到判断证据支持怎样的比较**

核心主张：课程项目中，你既能发现地图表达的问题、补充现场证据，也能在依据不足时调整分析方式。由此连接你已经确认的学习需求：更系统的空间分析，以及将使用者经验纳入分析的方法。

主证据是 F1–F3；F4、F6证明基础准备，F7连接学习与职业方向。

| 段落 | 内容与作用 | 预计英文词数 |
|---|---|---:|
| P01 | 从没有斑马线的过街点切入，说明地图最短路径与实际通行条件的差别。交代四人小组走访12条路段，你独立复走其中4条，并用QGIS对应观察点与路段；小组最终保留最短路径图、增加障碍注释层。建立具体问题与个人贡献。 | 145 |
| P02 | 展开核心决策：原想按障碍数量统一排名，但工作日下午的观察范围与轮椅使用者的缺席，使这一排序依据不足；你撤回建议，改为展示不同障碍类型。相较上一段，新增“如何决定分析可以得出什么结论”，并由此引出尚缺的方法。 | 120 |
| P03 | 说明学习准备：城市规划、统计学与GIS课程，以及图层编辑、基础空间连接能力。简述六周实习中对照两版公交站点底图、提交疑似不一致条目，补充对基础资料准确性的认识。区分数据版本问题与现场观察问题，避免重复反思。 | 105 |
| P04 | 回答为什么选择该项目：Transport Accessibility Studio对应从基础图层操作走向系统的可达性比较；Public Engagement Methods对应访谈设计与利益相关方沟通，回应项目中缺少使用者参与的问题。说明希望学习什么，以及它如何补足现有实践。 | 155 |
| P05 | 落到短期目标：在城市规划咨询团队从事交通可达性分析。说明上述训练与这一工作的联系；长期方向仍在探索，无需补出宏大承诺。 | 65 |

总预算约 **590词**，为后续衔接和修改留出空间。

这条路线的个体性来自一组连贯决策：发现最短路径表达不足、提出补充现场注释、再撤回证据不支持的统一排名。读者能看到你的判断如何改变了报告呈现方式。

主要风险是把全文写成“我没有做什么”。处理时应让具体行动占主导，仅在解释排名决策时集中交代观察边界。撤回排名也不能写成已经建立了更准确的评价体系；已知成果是调整呈现方式、完成课堂报告。图书馆经历可以不放入这条路线，避免再次论述地图的局限。

**路线二｜从地图使用现场，追问信息、分析与使用者经验如何衔接**

核心主张：你接触过地图的解释、底图资料核对和现场空间分析，逐渐明确希望学习如何将交通可达性分析与使用者经验结合。这条路线围绕不同工作环节展开，重点是申请动机与能力组合。

主证据是 F5、F4、F1–F3；F6嵌入学术准备，F7贯穿学习目标。段落按论证需要排列，不暗示三段经历之间存在未经确认的时间顺序或因果关系。

| 段落 | 内容与作用 | 预计英文词数 |
|---|---|---:|
| P01 | 从图书馆活动中居民询问“为什么不标电梯”切入。交代你六次周末协助解释图例与换乘标记，当时无法回答，后来才明确这张图只覆盖线路信息。提出地图所呈现的信息与使用者提出的问题可能并不重合。 | 100 |
| P02 | 转向信息基础：规划院实习中，你按清单核对两版底图的站名和位置，将疑似不一致条目交导师确认。新增问题是“信息是否准确、一致”，呈现与居民沟通之外的另一种准备。 | 105 |
| P03 | 转向分析环节：以诊所步行路线项目说明，即使有了空间资料，也仍需判断距离、现场障碍与比较结论的关系。突出你的复走、QGIS对应、方法段与注释贡献，简述撤回排名；嵌入相关课程基础。 | 160 |
| P04 | 把前面的经验连接到具体学习需求：Transport Accessibility Studio支持系统比较可达性；Public Engagement Methods提供访谈设计和沟通训练，让你有机会学习如何了解使用者经验，而不凭一条提问或自己的观察认定需求。 | 160 |
| P05 | 说明短期希望进入规划咨询团队从事可达性分析，将已有的基础资料处理与空间分析能力继续发展，并保持长期方向开放。 | 65 |

总预算约 **590词**。

这条路线的个体性来自你在三个具体位置接触地图：向居民解释信息、核对底图资料、参与路线分析。各段分别回答“信息覆盖什么”“资料是否一致”“分析能支持什么判断”，因此有机会形成层层推进的动机说明。

主要风险是写成三段经历罗列，或把居民的问题扩大为已发现的普遍需求。写作时必须保留这只是一次提问的事实边界，不能延伸成电梯调查、参与式研究或出行改善成果。这条路线适合你更希望突出实践动机、沟通意识与分析兴趣的情况，但需要严格压缩每段职责描述。

**推荐路线一，理由有三点：**

- **个人贡献最清楚。**复走、记录、QGIS对应、提出注释层与撤回排名，都有明确事实支持。
- **学习需求衔接最直接。**空间比较与使用者参与的两个缺口，分别对应两门已提供的课程。
- **650词内更容易形成论证深度。**一个项目承担主要分析，课程与实习补充准备，无需让三段经历争夺篇幅。

本轮已完成两条候选路线及段落安排，并按素材核对了个人贡献、题目覆盖和事实边界；尚未选定路线或撰写全文，也未进行外部核验。下一步只需选择：**路线一、路线二，或指定希望组合的部分**。不需要重新做全量访谈。

### 第2轮

执行：exit_code=0；completed=True；114.4秒；attempt=1。输入SHA-256：`147cef8d84287008c25e6503c8dbc301784963c3382e035f1d5449951e876f1f`。

<essay>
A crossing without a zebra crossing complicated our group's assumption that the shortest route was the most convenient. In a third-year urban planning project, our four-person team examined walking routes between campus and a nearby community clinic. We visited twelve road segments, and I independently revisited four, recording slopes, waiting at junctions and kerb conditions. Using QGIS, I linked observation points to the corresponding segments. The crossing prompted me to distinguish route length from the conditions affecting passage along it. After discussion, we retained the shortest-path map and added a layer of annotations describing observed barriers. I wrote the methods section and prepared the field annotations for our classroom report; other members handled the final layout.

I initially proposed ranking the routes by the number of barriers recorded. However, our observations covered only weekday afternoons, and no wheelchair users had participated. A single ranking would therefore have implied a comparison that our evidence could not adequately support. I withdrew the proposal, and we presented different types of barriers instead. Our teacher also asked us to explain the limitations of the observation periods. The resulting report documented conditions we had observed, without establishing which route would be most convenient for different users. This decision made me pay more attention to describing the boundaries of evidence, rather than simply producing a tidy map. My interest is in how accessibility analysis can be combined with users' experiences without assigning needs to people who have not been involved.

My undergraduate courses in urban planning principles, introductory statistics and GIS provide a foundation for further study. I can edit layers and perform basic spatial joins in QGIS, and the walking-route project gave me experience connecting field observations with mapped information. During a six-week internship at a municipal planning institute, I worked with a different aspect of mapping: the consistency of source materials. Following my supervisor's checklist, I organised two versions of bus-stop base maps, compared stop names and locations, and referred suspected discrepancies to my supervisor for verification. This work showed me how planning recommendations depend on accurate underlying information. Managing versions of practical planning data presented a different problem from deciding how to represent observations in a classroom map.

Harbor University's MSc Urban Mobility offers two courses that directly address my learning needs. Transport Accessibility Studio uses spatial analysis to compare transport accessibility. It would help me progress from basic layer operations towards the more systematic spatial analysis I want to learn. In my project, annotating barriers made observed conditions visible, but did not resolve how accessibility should be compared. The studio's focus on comparison is therefore particularly relevant to the gap between my current skills and the analysis I hope to undertake. Public Engagement Methods, with its training in interview design and stakeholder communication, addresses the other part of my interest. Our route observations did not include patients' accounts or wheelchair users' perspectives. Learning to design interviews would support my aim of bringing users' experiences into accessibility analysis rather than treating my own observations as sufficient evidence of their needs.

After the master's degree, I hope to work on transport accessibility analysis in an urban planning consultancy team. This would connect my planning background and GIS foundation with the spatial analysis and engagement training I am seeking. My longer-term direction remains open; my immediate goal is to develop the analytical preparation needed for this work.
</essay>

**净稿实测：562词。**按空白分隔计数，连字符词计为一词，不含标签及正文外说明，符合550–650词要求。

已逐段对照你确认的素材，覆盖学习准备、项目选择和毕业方向；保留个人与团队贡献的区别，未加入新的情绪、成长故事或实践成效。项目与课程信息仅依据你提供的虚构材料，未进行外部核验。

请最后核对英文是否准确表达你的本意；若模拟提交，按所给政策在提交表披露辅助写作使用情况。

### 第3轮

执行：exit_code=0；completed=True；92.44秒；attempt=1。输入SHA-256：`3d709ae6d1374049e3791d1fca9606b0c2c98382021f3680c24a8f355e338fed`。

<essay>
In a third-year urban planning project, I withdrew my proposal to rank walking routes by the number of barriers we recorded. Our four-person team had examined ten road segments between campus and a nearby community clinic. I independently revisited four, recording slopes, waiting at junctions and kerb conditions, then linked the observation points to road segments in QGIS. These observations provided concrete details about the routes, but their scope limited the comparisons we could make.

All our observations took place on weekday afternoons, and no wheelchair users participated. Counting barriers could describe what we recorded, but it could not establish how different users would experience those routes. A single ranking would have treated an incomplete set of observations as a sufficient basis for judging convenience. I therefore withdrew the ranking proposal, and we presented different types of barriers instead. Our report retained the shortest-path map alongside a layer of field annotations. I wrote the methods section and prepared those annotations; other team members handled the final layout.

Our teacher asked us to explain the limitations of the observation periods. The report documented observed conditions, without establishing which route would be most convenient for different users. Withdrawing the ranking made me pay more attention to describing the boundaries of evidence instead of pursuing a tidy map. It also left a methodological gap: displaying barrier types did not supply the user perspectives missing from our analysis.

My interest is in combining transport accessibility analysis with users' experiences, and I want to learn interview design without assigning needs to people who have not been involved. Meadow University's MA Participatory Urban Planning offers relevant support through Participatory Inquiry Workshop, which focuses on interview design and participatory workshops. Its interview training directly addresses my need to learn how to ask users about their experiences. The workshop component would provide a further setting for learning about participation beyond the field observations used in our project.

Planning Evidence Seminar, which compares the use and limitations of evidence across cases, would complement this training. My project involved a specific judgement about what a limited observation record could support; examining other cases would offer a broader basis for considering such judgements. My undergraduate grounding in planning principles, introductory statistics and GIS would support this study. Together, these courses connect to my aim of working on accessibility analysis in a planning consultancy team, where I hope to combine analytical preparation with a clearer understanding of users' experiences.
</essay>

**净稿实测407词**：按空白分隔，连字符词计一词，不含标签，符合380–450词范围。

主要修改与终审结果：

- 围绕“撤回统一排名”组织全文，依次说明证据局限、具体调整及仍未解决的问题；删除实习与志愿经历。
- 小组路段数已更正为 **10**，个人复走仍为 **4**；保留个人与团队贡献的区别。
- 项目联系改为访谈与参与式工作坊、案例证据比较；未将其写成交通建模训练，未残留目标A名称或课程。
- 已核对题目覆盖、事实边界及重复表述，未新增情绪或成长故事。

学校、课程与政策仅依据你提供的虚构材料，未进行外部核验。仍需你最终确认英文表达符合本人意思；模拟提交时须按所给政策申报辅助写作情况。
