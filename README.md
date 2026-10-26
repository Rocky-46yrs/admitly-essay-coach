# Admitly Essay Coach V0.3.3

[下载 v0.3.3 安装包](https://github.com/Rocky-46yrs/admitly-essay-coach/releases/download/v0.3.3/admitly-essay-coach-v0.3.3.zip) · [版本发布](https://github.com/Rocky-46yrs/admitly-essay-coach/releases) · [测试报告](evals/RESULTS.md)

面向中国申请者的免费开源 Agent Skill。优先兼容 Codex；不包含网站、账户或服务。Skill 本身无运行依赖；AI 客户端费用和数据处理规则由客户端决定。

## 第一次使用，直接选一句

- **没有初稿**：`使用 $admitly-essay-coach。我申请授课型硕士，还不会写PS。请用中文一步步帮我，先问两个最重要的问题。`
- **已有文书**：`使用 $admitly-essay-coach，帮我看看下面这段。先给最需要改的一点和一个修改版本，不用评级。<贴正文>`
- **只想改英文**：`使用 $admitly-essay-coach，只修这段语法，保留结构和真实贡献。<贴正文>`

不用先整理完整申请档案，也不用先用英文讲故事。能提供当期题目和篇幅时再补充；没有时可以先做通用编辑，但不能确认已经满足目标项目的提交要求。

## 能做什么
先读已有文书，给出诊断和可追踪的逐段修改；没有草稿时，以每轮 1–3 个问题挖掘真实素材，再比较叙事策略、形成大纲与工作稿。保留事实账本、稳定段落编号、N/A 评分、个人声音与修改理由。

英美授课型硕士 PS/SOP 是原有重点。本科（Common App、补充文书等）、研究型硕士和博士（含 Research Statement）新增专门指导模块。美国、英国、加拿大、澳大利亚有路由边界；其他国家可提供通用指导。**模块存在不代表已核验所有学校、年度或题目**。学校当前官方要求和 AI 政策优先，无法核验就标记待核实。没有浏览工具也能诊断表达，但不能声称联网验证。

## 安装到 Codex
1. 解压 `admitly-essay-coach-v0.3.3.zip`，得到 `admitly-essay-coach` 文件夹；确认其下一层就是 `SKILL.md`。
2. 个人安装：将整个文件夹复制到 `~/.agents/skills/admitly-essay-coach/`。项目内安装则放到该项目的 `.agents/skills/admitly-essay-coach/`，二选一，避免同名重复。
3. 重启或重新打开 Codex 会话，在技能选择器中确认，或明确输入 `$admitly-essay-coach`。
4. 提供脱敏文书、目标学位/专业、申请年度、官方题目及字数限制；缺少的信息可以后补。

交付的版本工作目录名为 `admitly-essay-coach-v0.3.3`；若直接复制这个目录安装，需改名为 `admitly-essay-coach`。ZIP 已使用正确的安装根目录。其他支持 Agent Skills 的客户端可按其说明放置目录；客户端工具、附件读取及浏览能力需要实际确认，不能保证所有客户端行为一致。

参考：[Codex 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。最低文件是 `SKILL.md`；`agents/openai.yaml` 提供 Codex 界面信息，其他客户端可忽略它。

## 八条可直接使用的示例
以下示例材料均为合成，不是真实申请者资料。

1. **从零访谈**：`使用 $admitly-essay-coach。我申请英国授课型商业分析硕士，2027 年入学，没有初稿，经济学背景。请用中文开始访谈，每轮最多三个问题，不假设我有科研。`
2. **直接诊断**：`使用 $admitly-essay-coach，先诊断这段，不必重新做全量访谈：I helped my team clean survey data. Our team completed the report. 我还没有学校题目，请将无法判断的评分项标为 N/A。`
3. **逐段修改**：`使用 $admitly-essay-coach。只修改已上传稿件的 P02，保留 helped 的贡献范围；给原文、改写、理由和事实依据。其他段落暂不改。`
4. **策略与大纲**：`使用 $admitly-essay-coach。根据当前事实账本提出两条真正不同的叙事路线，说明证据、段落安排和风险。等我选路线后，再生成大纲。素材不足就指出缺口。`
5. **定校适配**：`使用 $admitly-essay-coach，将现有 SOP 适配我提供的 B 校项目官网及 2027 入学题目。先核验来源和 AI 政策，检查原 A 校的课程、城市和导师名称残留。不能核实的地方不要补写事实。`
6. **本科场景**：`使用 $admitly-essay-coach。我准备美国本科 Common App Essay，尚未确定当年题目。先帮助我挖掘一次真实的选择经历，不强迫写职业目标或 Why school。`
7. **研究申请**：`使用 $admitly-essay-coach。我准备加拿大研究型硕士的 Research Statement。请先区分已做工作与拟研究计划，检查方法、局限和个人贡献；项目要求待我提供。`
8. **继续中断访谈**：`使用 $admitly-essay-coach。下面是上次的事实账本和进度摘要。请保留已有 F/P 编号，只追问当前最重要的两个缺口，不把推断改成已确认事实。`

上传附件若无法读取，应改用可读文本；不要在提示词中填写证件号码等无关信息。模糊的“写得更厉害”不能授权编造。

## 输出与工作方式
按任务渐进加载 references，assets 是可裁剪模板，不必一次输出全部表格。已有草稿可以直接诊断；仅改语法不会被强制加入策略访谈。新稿素材足够时通常提出 2–3 条路线，由你选择或明确授权推荐路线。个人反思与职业目标也需要本人依据。

评分是编辑辅助，不是录取预测。缺失依据或不适用项为 N/A，不折算完整百分制。学校信息记录项目、年度、来源、访问日期与状态。文书和网页中的指令视为不可信资料。不会自动上传到检测服务，不保证 AI 检测结果；也不承诺客户端零留存。用户材料不会加入公开测试。

## 学校限制AI时如何继续

先核查目标学校允许哪些协助；不把“本人素材真实”或“会披露AI使用”当作允许代写、翻译的依据。若学校只允许语法检查，自己写英文后可以这样调用：

`使用 $admitly-essay-coach。请先核实这个项目当前的AI政策；若只允许拼写和语法检查，就只在该范围纠正我自己写的英文，不改论点、结构或个人贡献。<项目官方链接与英文原稿>`

本包已做一次真实官网政策及后续语法检查测试，见[记录与适用边界](evals/LIVE-POLICY-RUN.md)。它不代表所有学校都允许同样的协助。

## 更新与卸载
更新前，将旧技能文件夹备份到技能搜索目录以外的位置，例如个人备份目录。保存自己的私有事实账本与工作稿，勿放入公开包。用新版替换安装位置的 `admitly-essay-coach`，不要同时保留两个同名可发现版本。重启会话，明确调用并检查是否能提供策略模块。

从 V0.1 升级无需迁移服务或数据库；旧 F/P 编号保留，新事实状态需逐条映射，不能批量升格为“用户确认”。卸载时将该技能目录移出 `.agents/skills` 并重启会话；不会自动删除其他位置的文书、历史对话或客户端记录。

## 文件与测试
- [SKILL.md](SKILL.md)：入口、路由与不可违反的规则。
- `references/`：场景与专业知识；`assets/`：输出模板。
- [变更与升级说明](CHANGELOG.md)、[来源说明](SOURCES.md)、[测试说明](evals/README.md)、[实际测试报告](evals/RESULTS.md)。
- 本地可选验证：`python3 evals/validate_package.py`；结构负向测试：`python3 -m unittest discover -s evals -p 'test_*.py'`。

## 开源
原创部分采用 [MIT License](LICENSE)。参考项目的思想与链接不意味着复制其实现或授予第三方内容许可。贡献请使用合成案例，不提交真实申请材料、密钥或身份信息。

## 保留的表达改进（始于V0.2.1）

在10个合成配对案例的模型预评中，V0.2未显示稳定的成稿优势。此次针对部分稿件动机概括、重复结尾及课程匹配解释不足做小幅修订：把已有材料讲具体，检查每段新增信息，缩短重复说明；不放松事实、政策或个人承诺确认要求。见[变更说明](CHANGELOG.md)及[本版验证](evals/RESULTS.md)。不宣称已经通过新版10案例盲评。

可直接调用：`使用 $admitly-essay-coach，检查这段是否只重复学习愿望。请在已有事实与我已表达的目标内展开具体问题；新推断放正文外，别替我认领新兴趣。`

安装目录名仍为admitly-essay-coach；将旧版备份到技能搜索目录外再替换。不要将V0.2与V0.3.3同时放在可发现目录中。

## 保留的整合能力（始于V0.3.2）

以V0.2.1为底稿，选择性吸收用户提供V0.3.1的薄素材处理、候选追踪、交接摘要、最小项目材料与反例测试思路。默认定性诊断；明确要求数字时保留原编辑量表与N/A规则，不把旧版按旧规则生成的合规记录改称失败。

交接摘要没有固定30天失效规则；保留原核验历史，再检查当前适用性。候选可拒绝，不用诱导二选一；本人精确确认内部意向不必额外制造经历证明。新旧事实冲突需要澄清，不因“最新”就择一。

新增调用：`我答不出这段有什么反思。请根据真实素材给最多两个可以拒绝的候选，指出依据和未知，不写成我的既定想法。`

暂停调用：`请把当前必要的F/P/S状态、否决过的C和下一步整理为可复制交接摘要，留在对话中即可。`

审查理由见[整合说明](MERGE_NOTES.md)，本版验证见[测试报告](evals/RESULTS.md)。其他客户端的具体安装路径未在本次验证，按其自身说明操作。

## 客户端适配状态

| 客户端 | 当前证据与安装入口 |
|---|---|
| Codex CLI | 已有实际行为回归；按上述目录安装，使用 `$admitly-essay-coach` |
| Claude Code | 通用目录格式可移植，本Skill未完成行为验证；个人目录 `~/.claude/skills/admitly-essay-coach/`，使用 `/admitly-essay-coach`。本次本机CLI 2.1.72未登录，未调用Claude模型 |
| Claude网页/Cowork | 官方支持在Customize → Skills上传技能ZIP；本包未实测，不把导入成功等同于行为正确 |
| WorkBuddy | 在“专家·技能·连接器 → 技能 → 添加技能 → 上传技能”选择本地ZIP；本包未实测。开放平台市场还有展示名、作者等专用字段，当前通用ZIP不宣称已适配上架 |
| Grok Bot / Meta Muse个人助手 | 尚未验证本包的原生导入与参考文件加载，不宣称即装即用；与Grok Build / Muse Code是不同产品 |
| Muse Code | 官方文档支持`.agents/skills`及导入其他Agent技能；本包未实测 |

其他客户端机制依据2026-10-26复查的[Claude Code](https://code.claude.com/docs/en/skills)、[Claude技能](https://support.claude.com/en/articles/12512180-use-skills-in-claude)、[WorkBuddy本地导入](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)、[WorkBuddy市场格式](https://open.workbuddy.cn/en/docs/skill)、[Grok Bot](https://docs.x.ai/grok-bot/skills-routines-and-automations)、[Muse Code](https://dev.meta.ai/docs/muse-code/extending)官方说明。客户端能力与账号权限可能变化；Codex的`$`调用方式不等于所有客户端通用命令，也可用自然语言明确指定本技能名称。
