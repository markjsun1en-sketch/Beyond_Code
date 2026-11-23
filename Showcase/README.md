# Showcase 固定同步与发布流程

站点：[Beyond Code](https://ai-native-software-engineering.mac1en.chatgpt.site) · [English](https://ai-native-software-engineering.mac1en.chatgpt.site/en)。唯一站点身份与全书双语 23 章、14 幅机制图的范围保存在 [publication.json](publication.json)。最新已验证版本见 [latest-release.json](latest-release.json)，历史发布记录保存在 `releases/`。

中文正文来源是合并后的完整 `OptimizedDocs/` 工作稿。`PolishedDocs/` 的第 1、6、23 章保留为独立成书候选稿。

英文稿存放在 [translations/](translations/)。第 6 章依据 `01faed1` 的[成书候选稿](../PolishedDocs/第6章_Truth与State_Architecture_成书候选稿.md)翻译，保留引言和 6.1–6.10 的节序。其余 22 章依据 `3cdd900` 中的中文工作稿翻译，并沿用其编号小节、案例、证据边界和图号。顶栏语言入口连接对应的目录、图集或同一章。英文目录和前后章导航保持英文，搜索可定位两种语言的正文。英文稿与英文图稿纳入发布来源指纹。

## 默认完成条件

根据作者的持续授权，后续任务修改正文、机制图、图题/图注或阅读器时，同一任务要完成同步、检查、发布和线上回读；无需等待再次提出发布请求。明确要求“仅本地／暂不发布”时遵从，并说明尚未发布及原因。只修改Evidence、修订说明或流程文档，不触发内容发布。规则入口是 [AGENTS.md 第9节](../AGENTS.md)，操作技能是 [showcase-publish](../.agents/skills/showcase-publish/SKILL.md)。

这不是后台监听或定时任务。修改文件本身不会自动上传；执行修改任务的Agent必须完成下面的流程。

## 1. 确认状态并打开原站点源仓库

在书稿仓库执行：

```sh
python3 tools/showcase_workflow.py status --online
```

`current` 表示当前来源与最后一次已验证发布、线上公开指纹一致。`needs_publication` 或非零退出表示需要处理；网络失败表示无法确认，不能称为已同步。`status` 只做轻量新鲜度检查，完整线上逐文件检查在 `finish`。

使用当前安装的 **Sites** 技能：读取原Site及访问范围，取得同一Site的短期源仓库凭据，以source helper打开最新源仓库。已有checkout可复用，路径取工具返回值；不要把临时目录或插件版本当永久配置。保持原网址与访问范围，不新建Site。凭据仅经工具内存和stdin传递，不写文件。

## 2. 图稿来源核对与必要的重渲染

图源保存在相应语种的章节中，由 Mermaid 和相邻图题、图注组成。准备入口核对两种语言的编号、所属章节、图题、图注、Mermaid、SVG 和 PNG 指纹，以及清单完整性。

任何不一致都先处理，不能只改manifest里的哈希。用 `tools/render_mechanism_diagrams.cjs` 的原有渲染方式，传入当前环境实际可用的Mermaid、渲染依赖及浏览器路径。增量更新必须明确所属 `--batch phase-x` 与 `--figures fig-x-y`，并传入所属章节；不带 `--figures` 的部分章节渲染可能覆盖整批清单。渲染失败后停止后续同步，修复并重新核对全部图。

英文导出使用同一脚本加 `--language en`，输入 `Showcase/translations/*.en.md`。图文件和清单写入 `Showcase/translations/diagrams/`。增量导出使用 `--figures fig-x-y-en` 并传入所属英文稿。

图题/图注虽不一定改变像素，也必须更新对应manifest。不得把同一图登记进另一批次。新增或删除章节/图时，同步调整 `publication.json`、构建器中的规模约定和导航，再运行完整检查；不要绕过数量检查发布缺页版本。

## 3. 一条命令准备可发布内容

```sh
python3 tools/showcase_workflow.py prepare --checkout /path/to/site-checkout
```

要求Python 3.12+和 `markdown-it-py==4.0.0`。日期默认为Asia/Shanghai当天；复现指定日期可加 `--date YYYY-MM-DD`。

入口依次执行图稿预检、`sync_showcase.py`、构建和强制带书稿根目录的验证。正文只去除约定的两类编辑Header；内部Evidence链接变成自然语言来源标签，适用边界、代码、表格及正文全部保留。公开目录不包含内部路径、Receipt编号或编辑档案。

检查覆盖两种语言各 23 章、同章切换、前后章导航、代码空白、表格结构、图文件、锚点和搜索索引。每次重新生成 `dist/`。成功后产生 `showcase-prepared.json`，固定本次来源、站点快照及所有公开文件的指纹。来源指纹覆盖正文、图清单、图文件、阅读器和同步逻辑。

## 4. 实际阅读检查

使用支持的浏览器工具检查受影响页面与一条完整阅读路径，保存真实截图：

- 桌面正文及小节/前后章导航；手机320px和390px下的正文、表格、代码及顶部按钮。
- 修改过的机制图、图注和放大视图；图有变化时核对全部分支与箭头。
- 实际关键词命中、正文高亮、跨页与同页定位。搜索逻辑或布局修改时，加测 `AUTH-REVOKE-004`、`QA维护任务`、“工程能力适配”、清空及无结果。
- 图加载后落点仍正确；线上 `.html` 会跳转至无扩展名地址，发布后需验证这个路径。

将观察保存为临时JSON，`output_fingerprint` 必须从本次 `showcase-prepared.json` 原样复制。示例结构（下面的空值不可作为通过记录）：

```json
{
  "output_fingerprint": "",
  "production_url": "",
  "version_id": "",
  "checks": {"desktop": false, "mobile": false, "search": false, "figures": false, "production": false},
  "notes": [],
  "screenshots": []
}
```

只有实际通过才能改为true；截图填写真实本地绝对路径。支持工具不可用时保留未验证原因，不把静态检查写成浏览器已通过。检查中修复源码后重新prepare，绑定新的指纹。

## 5. 推送、打包并更新发布

使用Sites source helper推送并打包本次准备结果。已完成且输入未变的构建/验证无需重复，`commands: []`即可；保留其返回的同一 `project_id`、完整 `commit_sha`、`archive`。

推送后、save/deploy前执行：

```sh
python3 tools/showcase_workflow.py check --checkout /path/to/site-checkout
```

任何源文件、站点快照或构建产物在prepare后变化都会失败。重新prepare后要重新审阅受影响结果，并重新推送打包；不能混用旧archive和新commit。

通过后按Sites技能保存该commit/archive，再部署返回的版本，沿用原访问范围。保留实际 `save_site_version` 与deployment返回JSON，可直接保存工具的 `structuredContent`；不要手写成功状态或凭据。非终态部署继续使用同一deployment ID检查。失败时诊断原部署，避免盲目创建版本或更换Site。

## 6. 发布回读与完成记录

发布成功后先在正式网址回读受影响的导航、搜索落点和图像交互，将真实结果记入review JSON的 `production`，填写实际正式URL和返回的version ID。然后执行（三个JSON均来自上述真实结果）：

```sh
python3 tools/showcase_workflow.py finish \
  --checkout /path/to/site-checkout \
  --version-json /path/to/version.json \
  --deployment-json /path/to/deployment.json \
  --review-json /path/to/browser-review.json
python3 tools/showcase_workflow.py status --online
```

`finish`核对同一Site、版本与部署关系、推送Commit、准备指纹、浏览器记录和截图；然后逐个回读所有公开HTML、搜索索引、manifest、JS/CSS、SVG/PNG，跟随正式站点重定向。正文结构及代码空白必须一致，非HTML文件逐字节比对；平台注入的非阅读器脚本不作为书稿内容。

先记录 `deployed_unverified`，全部通过后才转为 `verified`。回读失败仍保存失败原因，重试历史保存在版本记录的 `history` 中，不抹掉已经发生的部署；修复后对同一部署重试finish。线上回读优先使用系统curl的正常证书验证；没有curl时用Python默认TLS信任库，禁止用跳过证书校验来取得通过。若来源又变化，先处理新版本，不能把旧发布改记成新稿已上线。

若线上出现交互错误，保持production为false，记录问题并修复后重走流程。完成答复给出正式URL、版本、检查结果及实际限制。未完成时明确本地已改、线上处于哪个版本及卡点。

## 已有记录

- [首次完整同步，第3版](release-2026-11-22.json)。
- [读者体验复查，第4版](reader-review-2026-11-22.md)及[版本记录](release-2026-11-22-v4.json)。
- 新发布的自动检查结果见 [最新记录](latest-release.json)及 `releases/vNNNN.json`。

修改流程工具本身时，在prepare成功后运行故障回归测试；普通正文改动无需重复这套工具测试：

```sh
python3 tools/test_showcase_workflow.py --checkout /path/to/site-checkout
```

测试在临时副本中制造陈旧图注、图源、导出文件、阅读器、快照、产物和失败回读，不修改实际书稿或线上站点。
