# 机制简图导出

Mermaid 源保存在所属章节，SVG、PNG、预览页及指纹文件均由源生成，不应手工修改导出图。

| 图 | 所属正文 | 静态图 |
|---|---|---|
| 图4-1 目标到行动选择 | [第4章 4.5](../第4章_Intent与Agent_Input对象边界回接稿.md) | [SVG](fig-4-1.svg) · [PNG](fig-4-1.png) |
| 图5-1 渐进检索与缺口处置 | [第5章 5.4](../第5章_Context对象边界回接稿.md) | [SVG](fig-5-1.svg) · [PNG](fig-5-1.png) |
| 图9-1 旧证据与当前用途 | [第9章 9.11](../第9章_Evidence_Use与Decision_Disposition边界稿.md) | [SVG](fig-9-1.svg) · [PNG](fig-9-1.png) |
| 图10-1 审阅继续与停止 | [第10章 10.14](../第10章_Review_Engineering_首轮修订稿.md) | [SVG](fig-10-1.svg) · [PNG](fig-10-1.png) |
| 图12-1 决策信息汇合 | [第12章 12.9](../第12章_Cognitive_Compression与Human_Decision_Interface_首轮修订稿.md) | [SVG](fig-12-1.svg) · [PNG](fig-12-1.png) |
| 图14-1 产品检查与 QA 适用性 | [第14章 14.9](../第14章_Observability与Intervention_首轮修订稿.md) | [SVG](fig-14-1.svg) · [PNG](fig-14-1.png) |
| 图15-1 查询条件与原文核对 | [第15章 15.16](../第15章_Memory_Engineering_首轮修订稿.md) | [SVG](fig-15-1.svg) · [PNG](fig-15-1.png) |
| 图21-1 记录与验证路径裁剪 | [第21章 21.29](../第21章_AI_Native_SDLC_首轮修订稿.md) | [SVG](fig-21-1.svg) · [PNG](fig-21-1.png) |
| 图23-1 不同决定对象 | [第23章 23.19](../第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md) | [SVG](fig-23-1.svg) · [PNG](fig-23-1.png) |
| 图8-1 恢复目标与前置条件 | [第8章 8.10](../第8章_Agent_Reliability_Engineering_首轮修订稿.md) | [SVG](fig-8-1.svg) · [PNG](fig-8-1.png) |
| 图18-1 按用途保留与退役 | [第18章 18.21](../第18章_Traceability_and_Accountability_首轮修订稿.md) | [SVG](fig-18-1.svg) · [PNG](fig-18-1.png) |
| 图20-1 测量合同与有限处置 | [第20章 20.8](../第20章_AgentOps_成本与模型漂移_首轮修订稿.md) | [SVG](fig-20-1.svg) · [PNG](fig-20-1.png) |
| 图16-1 方法比较与无优势结果 | [第16章 16.24](../第16章_Self_Evolution_Engineering_首轮修订稿.md) | [SVG](fig-16-1.svg) · [PNG](fig-16-1.png) |
| 图23-2 隔离奖励路径与冷恢复 | [第23章 23.44.3](../第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md) | [SVG](fig-23-2.svg) · [PNG](fig-23-2.png) |

可直接查看[阶段 A 预览页](phase-a-preview.html)、[阶段 B 预览页](phase-b-preview.html)、[阶段 C 预览页](phase-c-preview.html)、[阶段 D 预览页](phase-d-preview.html)或[阶段 E 预览页](phase-e-preview.html)。默认按窗口显示完整关系，支持原尺寸滚动及打开SVG查看细节；正文与完整证据边界仍以所属章节为准。

本轮使用 Mermaid 11.12.1、Playwright 和本地 Chrome 渲染；[阶段 A manifest](phase-a-manifest.json)、[阶段 B manifest](phase-b-manifest.json)、[阶段 C manifest](phase-c-manifest.json)、[阶段 D manifest](phase-d-manifest.json)与[阶段 E manifest](phase-e-manifest.json)分别保存库文件、Mermaid 源及导出物 SHA-256。没有将外部渲染库复制进书稿仓库。

从仓库根目录使用[导出脚本](../../tools/render_mechanism_diagrams.cjs)，向三个路径参数提供本机实际路径。`--batch`默认为`phase-a`，也支持`phase-b`、`phase-c`、`phase-d`与`phase-e`，各阶段清单与预览分开生成：

```sh
node tools/render_mechanism_diagrams.cjs \
  --mermaid-js /path/to/mermaid-11.12.1.min.js \
  --playwright-module /path/to/node_modules/playwright \
  --browser-path /path/to/chrome \
  OptimizedDocs/第12章_Cognitive_Compression与Human_Decision_Interface_首轮修订稿.md \
  OptimizedDocs/第14章_Observability与Intervention_首轮修订稿.md \
  OptimizedDocs/第23章_AI_Game_Dev_OS纵向案例_首轮修订稿.md
```

脚本只读章节，在本目录写导出物，使用独立临时浏览器上下文。对Mermaid输出中不能独立解析的HTML换行标签，脚本从已渲染DOM序列化为有效XML后再保存SVG；PNG仍来自同一渲染内容。修改任一源图后重新生成，并核对语义与实际排版；指纹一致不能代替视觉检查或作者审阅。

阶段 B 使用相同渲染参数，加上 `--batch phase-b` 并将输入章节换为第4、5、15章；阶段 C 使用 `--batch phase-c`，输入第9、10、21章。不要混用阶段输入，以免覆盖相应预览和清单；章节中图号决定 SVG／PNG 文件名。阶段 B、C 的图为教学或建议机制，具体实现与限制见正文，不能从图推断为自动化能力或已经验证的效果。


阶段D输入第8、18、20章，使用`--batch phase-d`。阶段E输入第16、23章，并使用`--batch phase-e --figures fig-16-1,fig-23-2`，以保留阶段A的图23-1原导出不变。图16-1解释建议比较路径，图23-2概括具名保存机器运行；不得把后者当作所有异常路径、人工体验或主项目采用的证据。

RR-040修订图8-1、16-1、18-1的分支和图注，仍使用原有机制简图。`--figures`只更新选中图，并保留同批次其他已有清单项；不要把其他批次的图选入当前批次。仅刷新预览样式时可运行`node tools/render_mechanism_diagrams.cjs --preview-only all`，它从五份已有清单生成HTML，不启动浏览器或改写SVG／PNG。书页排版另行检查，窗口缩放不代表最终印刷字号。

[RR-041](../../RevisedResult/RR-041_RR-040实施后书稿与配图复查.md)进一步修订图9-1的可评价负面结果／未知分支、图18-1的联合退役条件和图20-1的探针未确认及停止出口。仅重导这三图并同步阶段C、D预览与清单：阶段C选`--figures fig-9-1`，阶段D选`--figures fig-18-1,fig-20-1`。其余11图保留，图源、图注、导出及受影响预览已完成针对性复查。
