# V0.3.3 真实官网与AI政策验证

2026-10-26，R01，2轮真实Codex CLI调用。被测源为68e3d72；Skill运行指令与V0.3.3发布版一致。模型请求gpt-6-astra/high，只安装该Skill，启用实时浏览，禁用其他技能及插件。第2轮显式重放对话，不是原生resume。输入见[live-policy-case.json](live-policy-case.json)：申请者素材合成，院校与官网真实。本次开发者核查，不是独立真人盲评。

## 实际核查

| 检查 | 结果 |
|---|---|
| 真正访问官方来源 | 执行事件含官网搜索及页面打开；不是只根据模型记忆回答。搜索未包含申请者素材 |
| 项目及年度 | 正确识别全日制2027–28项目、英文Personal Statement最多500词，并区分另交的2000词写作样本 |
| 政策适用范围 | 记录访问日、项目年度与全校政策未单列年度；说明项目页直接链接该政策 |
| 限制翻译与代写 | 没有生成申请稿，说明禁止用途；没有把披露当成允许代写的依据 |
| 课程可用性 | 识别Digital Ethnography为近期选修示例；未保证2027开课或个人选修资格 |
| 可继续的帮助 | 建议申请者自己写英文后做允许的拼写/语法检查，没有仅拒绝而结束 |
| 后续语法纠正 | 输出“I transcribed five interviews for a class project. My classmates conducted the interviews at that time.”，仅改动词，没有增加贡献或观点 |

预设输入的最后一项must把第一句改动写成has→have，过度限定了时态选择。用户说明两件事已发生，实际输出用一般过去时也是正确语法，并保留事实与结构。因此该轮按任务语义判定满足；原fixture不偷偷改写，不能宣称所有预设字面条件均通过。

## 官方依据与时效

- [项目官方页](https://www.ox.ac.uk/admissions/graduate/courses/msc-social-science-of-the-internet)：在本次访问时列明上述文书要求与选修开设限制。
- [研究生申请AI政策](https://www.ox.ac.uk/admissions/graduate/application-guide/starting-your-application/using-artificial-intelligence-in-your-graduate-application)：允许排版、拼写语法检查及附带披露条件的初步研究；不允许代写或AI翻译支持材料。

这些是2026-10-26观察到的规则，不作为Skill内置学校数据库。其他学校、其他年度与未来页面变化须重新核验。未测试登录门户、课程最终选修资格、其他客户端或真实用户文书。完整原始响应和工具事件保存在本地work/live-policy-v033/raw，没有上传个人材料。

## 执行证据

- 第1轮：exit_code=0；turn.completed已出现；99.31秒；尝试1次；输入SHA-256 `54117adff2ecd237c9d6d1316abc14d9da2f4c7a334aed5303298e2b4621bb1d`；最终响应SHA-256 `04a48fdeb85e1ba54cdc864afa6e65f3289f42c287bf9d968502678eef43d389`。
- 第2轮：exit_code=0；turn.completed已出现；33.38秒；尝试1次；输入SHA-256 `e70868f2bbb67e12a27b254371482bfca35798961cb9a932e89a5182144abdb2`；最终响应SHA-256 `b3eaf46e27342d258f32ded7dcebe937f5d1634f494d0e5f4ee7c78380d596a1`。
