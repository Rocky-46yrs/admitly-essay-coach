# 未发布修订：解释与备选稿事实保真

2026-11-01核查。基于9acfa18，只修改revision-protocol.md的终审规则，入口与其他运行指南未变。测试使用冻结的候选技能目录、gpt-6-astra/high及现有Codex执行器；按需读取技能，禁用联网。输入见[三条合成案例](provenance-cases.json)。本报告为开发者逐项核查，不是独立盲评，也不是同模型旧版对照。

P02首次调用完成；P03首次调用因账户额度限制失败，未产生答案，P04当时未启动。保留失败事件，之后仅续跑P03/P04，两条均完成。完整执行记录位于本地work/provenance-regression/candidate及candidate-resumed。本报告没有把额度失败计作模型答题失败，也未覆盖旧记录。

## 结果判断

- P02：保留六段老师提供的录音及转录动作，不把录音推定为访谈；说明指出每项可补充行动须确实完成。
- P03：保留五人实习小组、18份文件及日期排序，不推测文件内容/来源，不追问用户已拒绝透露的信息。
- P04：保留三段同学录制的课堂讨论、转录和主题编码，没有以保守为由删掉已确认贡献。

三例按预设must人工核查符合要求。包验证通过；现有11项结构测试通过。结构检查不证明行为可靠。未重跑E01–E48、完整文书旅程或配对盲评；未在WorkBuddy/DeepSeek上测试候选规则，故不能宣称其原问题已修复。候选尚未发布新版本，V0.3.3 ZIP和WorkBuddy安装文件均未修改。

## 实际最终回答及执行证据

### P02

**英文修改稿**
> I transcribed six audio recordings provided by my teacher.

**理由（P01）**
原句“I conducted six interviews and analysed the findings.”把转录写成了主持访谈和分析，夸大了职责。修改稿保留“六段”及老师提供材料的来源，用 *transcribed* 准确表达实际工作，也不假定录音内容属于访谈。

依据 F01：你自述只转录了老师提供的六段录音，没有访谈或分析。已据此核对修改稿，未作独立核实；当前版本无待确认项。

若要进一步增强细节，可补充实际做过的核对、说话人标注或时间戳记录；每项都须确实完成才能加入。现有事实不支持增加分析、研究发现或能力提升的表述。

执行完成：21.82秒，exit_code=0；输入SHA-256 `7a52f64db0b9869f89e5597c9b120ffa3950a8f851d07623a0fb1d94ebdd3f8e`；响应SHA-256 `15ef9a967490b71294cb58530bd562ed2397134f7145f594220ac6df2dddf630`。

### P03

**原句（P01）**
> I managed a database and identified customer trends.

**建议稿**
> As part of a five-person internship team, I organized 18 files by date.

**修改说明**
“Managed a database”超出了按日期整理文件的职责；“identified customer trends”也没有事实支持，因此删除。改稿保留团队背景，并明确你个人完成的动作和数量，不推测文件内容、来源或工作成效。

依据：F01＝五人实习小组；F02＝你按日期整理了18份文件，均来自你的自述。已核对改稿与这些信息一致，未作独立核实；本次修改无待确认项。

执行完成：24.02秒，exit_code=0；输入SHA-256 `0712f0ee7491789ddf169b09a14c0890ebbfac1cd3842920483305e35a96240b`；响应SHA-256 `18b8df13bb6aacf91e9427d009222fb252a2630c57b09eb8a06f87675bc6d564`。

### P04

I transcribed three audio recordings of classroom discussions made by classmates and thematically coded the transcripts.

理由：这句话准确区分了同学录音与你转录、编码的贡献，未添加采访经历或效果评估。

执行完成：14.12秒，exit_code=0；输入SHA-256 `e33ddc85f0e432bb3ef04a8d7c6b63edbaffe645126acb18ad2768c137dc219a`；响应SHA-256 `2d0b476c0eb2b7b9684b6314de603d56ed7404f17609d0d8c922802c37bb6cad`。

## V0.3.4打包说明

2026-11-01将上述已测运行规则打包为V0.3.4；打包仅更新版本标识和发布说明，未继续修改运行规则。上述“未发布”描述为测试时状态。旧48案例与5条旅程仍保留原始0.3.3元数据，不能当作本版重新执行的证据。WorkBuddy已安装版仍为0.3.3。
