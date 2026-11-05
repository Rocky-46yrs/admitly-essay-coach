# 语义范围修订：候选测试

2026-11-05核查。基于cbc9dfb，在风格指南增加一条规则：区分掌握技能与项目实用，保持否定命题的原始范围，并检查连接词和指代是否新增关系。入口、其他运行模块未改。合成输入见[案例](semantic-scope-cases.json)。

使用冻结候选目录及现有Codex执行器，gpt-6-astra/high；本地原始记录在work/semantic-scope及work/semantic-scope-resumed。首次S01读到指南后因额度限制失败，没有最终答案，S02当时未运行。此次续跑保留原失败记录，两个调用均完成；冻结指南逐字节匹配待提交文件。以下判断由开发者逐项检查，不是独立盲评或旧版配对实验。

## 判定

- S01：62词，独立按空白计数与回答一致；Python回归作为已学习内容，与项目中Excel按月汇总明确分开。保留三人团队、24条记录；未评估促销因果效果没有被扩大成“未做促销”或“促销无效”。事实、范围及字数条件满足。
- S01的表达仍可更紧凑：grouping by month与monthly sales summary重复，受到60词下限与素材量的共同约束。本测试不证明文风已最优，也不鼓励靠重复填满篇幅。
- S02：保留已确认的显微镜使用、双人课堂、八张制片和笔记，没有加入患者、疾病或效果。未把没有长期随访扩写为没有其他观察；省略与该经历句无关的随访否定不改变所述贡献。符合本例事实及输出要求。

包结构校验通过。未重跑长文L01、旧48例或WorkBuddy；本次短例通过不能证明长文中的两处问题已消失。该改动暂为未发布修订，V0.3.4 ZIP与各客户端安装不变。

## 实际回答

### S01

I have studied regression analysis using Python. In a marketing class project, I worked as part of a team of three students. My contribution was to use Excel to summarize a dataset containing a total of 24 sales records, grouping the records by month to produce a monthly sales summary. I did not evaluate the causal effects of promotions in this project.

修改理由：本段共62词，区分了学过的Python回归分析与项目中实际使用的Excel月度汇总，保留三人团队及24条记录的事实，未添加因果结论、反思或新经历。

执行：84.32秒，exit_code=0、turn.completed；输入SHA-256 `4d19b51584e1a0e4e8cf12c6acab4cc4e3efca64fab0d3f59f680df2daa24980`；响应SHA-256 `a6122b4d9d58d0bb3c4fa3e414cbf05b6d8806d402304bec2974993ddfd2052a`。

### S02

During a paired laboratory class, I used my microscopy skills to examine eight slides and recorded my observations in notes.

理由：这句话保留了已确认的显微镜操作能力、双人实验课情境、八张制片及观察笔记，未添加长期随访、疾病、疗效或病人经历。

执行：46.93秒，exit_code=0、turn.completed；输入SHA-256 `a269881dad9b97af0adca16fe6d8427fe7b89984a77152bea3135a643414decc`；响应SHA-256 `d9ecbf13636cccfb2dde17e85921f8c1904572783991fdabfde411b89e492f0d`。
