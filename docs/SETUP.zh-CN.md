# 初代 Oasis 改造记录

这是一份历史过程和复现参考，不是适用于所有 Kindle 的一键脚本。参考设备为初代 Oasis、固件 5.16.2.1.1；不公开设备序列号。安装前先按当前上游文档确认型号、固件、可用越狱方法及恢复步骤。

## 1. 私下备份

通过 USB 将个人书籍、标注和设置备份到**仓库之外**。已经安装 KOReader 时，还应保存它的设置、插件及数据库。备份可能包含微信登录状态、API Key、书名和阅读记录，不能上传到公开仓库。

## 2. 越狱与启动器

本次使用 [WinterBreak2](https://github.com/KindleModding/Winterbreak2) 1.1.0。官方兼容表覆盖参考固件，无需为此注册亚马逊账号。

1. 阅读 [当前安装指南](https://kindlemodding.org/jailbreaking/WinterBreak2/)，包括它要求的自动更新防护。
2. 从官方 release 下载 `wb2.zip`，把其中的 `winterbreak2` 文件夹放到 Kindle USB 根目录。
3. 安全弹出、连接 Wi-Fi，在体验浏览器访问官方指南给出的入口并运行越狱。不要沿用来历不明的镜像入口。
4. 等待完成和重启。参考设备生成的成功标记报告 `jb.sh v2.4.0`。
5. 按所用越狱版本的后续指南安装或确认 hotfix、更新阻止及启动器。不同版本步骤可能不同，不要叠加多个教程的步骤。
6. 本次使用 PEKI/KUAL。临时填充文件仅在越狱完成、确认更新防护后删除；不得误删原有书籍。

这一步需要在 Kindle 屏幕操作，USB 文件拷贝不能代替点击或证明越狱成功。

## 3. KOReader

从 [官方 releases](https://github.com/koreader/koreader/releases/tag/v2026.07.1) 选择 `koreader-kindlepw2-v2026.07.1.zip`，把 `koreader` 和 `extensions` 解压到 USB 根目录。参考固件低于 5.16.3，不能改用 `kindlehf`。

安全弹出后从 KUAL → KOReader → Start KOReader 打开，先验证原生界面、一本普通 EPUB、休眠及唤醒。每次修改插件前正常退出 KOReader，避免运行中的旧进程覆盖配置。

## 4. 微信读书

从 [WeRead releases](https://github.com/finlater/weread.koplugin/releases/tag/v1.6.0) 获取插件，将 `weread.koplugin` 放入 `koreader/plugins`，重启 KOReader。

手机微信读书：我 → 设置 → 微信读书 Skill → 获取 API Key；然后在 KOReader 工具 → 微信读书 → 微信扫码登录，按手机提示确认。这个流程在参考设备上由用户确认可用。密钥、扫码截图、会话文件不能进入仓库。

## 5. 首页、RSS、词典和笔记

- 安装 SimpleUI 3.0.1、RSS Reader 1.21.0 到插件目录。SimpleUI 依赖内置 CoverBrowser；根据上游说明处理冲突插件。
- 在 SimpleUI 中添加微信书架、RSS 的快捷动作，不必复制别人的整份界面设置。
- [RSS 模板](../config/rss/)对应本地中文、英文账户，无需外部账号。源会变化，设备网络需单独验证。先下载每源 5–10 篇并关闭图片测试。
- ECDICT 1.0.28 选择 StarDict 格式；词典文件放到 `koreader/data/dict`。使用上游发布的词典及许可，本仓库不打包词典。
- 在 KOReader 生词本中开启自动添加及上下文；笔记导出选 Markdown，保存到设备 `documents/KOReader-Notes`。这是手动导出，不是自动同步微信云端全部笔记。

## 6. AI 辅助阅读

安装 AI Assistant 1.21。这里的 [DeepSeek 预设](../config/assistant/)使用 UI 可编辑的 provider 记录，Key 为空；地址、模型应再次核对 [DeepSeek 官方文档](https://api-docs.deepseek.com/)。

用户在设备里填写 Key 并点击 Test。只有测试成功才能确认 API 可用。所选文字会发送给配置的模型服务，调用可能收费。本次没有使用真实 Key 做认证测试。

## 7. 本地漫画与 ComicReader

KOReader 本身可以读 CBZ、PDF。ComicReader 0.0.7 增加双页显示、封面分组及方向设置，不提供书源。

该 release 自带 4 个 `statistics.koplugin` 文件，会覆盖阅读统计组件。安装前必须备份当前版本，阅读统计数据库也要保留。若不匹配当前 KOReader，停止安装；不要认为下载包无损就代表兼容。6 英寸屏幕先保留单页。

## 8. 搜索、下载漫画：Rakuyomi

按 [官方构建表](https://tachibana-shin.github.io/rakuyomi/user-guide/installation/choosing-a-build.html)，初代 Oasis 选择 `rakuyomi-kindlea9.zip`。本次记录版本为 1.44.3。

1. 将 `rakuyomi.koplugin` 放进 `koreader/plugins`。Unix 安装时确保随包的 `server`、`uds_http_request` 和 `cbz_metadata_reader` 可执行。
2. 参考 [settings 示例](../config/rakuyomi/settings.example.json)，合并至设备 `koreader/rakuyomi/settings.json`。
3. 重启 KOReader，在文件管理界面顶部菜单进入 Rakuyomi。
4. Manage Sources 添加所需源；目录可用不等于里面每个源都可用。本次只记录 MangaDex 的电脑后端验证，不声称所有源可用。
5. Search mangas 搜索标题，选择章节，先下载一章，再断网打开确认。

本次用同版本官方 macOS 后端和 MangaDex 扩展，完成搜索、章节查询、整章下载和 12 张图片校验；这不能替代 Kindle 的 ARM 执行、TLS、当前 Wi-Fi、渲染和唤醒测试。

## 9. 白屏恢复记录

使用期间报告过休眠唤醒后白屏。日志出现没有可用界面实例的屏保提示；根因没有确认，不能据此归咎某个插件。

本次私下备份日志和设置，安全弹出、拔线后持续按住电源键 40 秒再松开；用户确认完整重启后恢复。不要以恢复出厂作为首个处理手段。

若再次出现：记录触发步骤，私下保存并脱敏日志，先验证原生主页，再逐个开启插件。需要回退 ComicReader 时恢复与原版本匹配的统计组件。重启后恢复不代表根因已经修复。

## 10. 验收

- 原生主页、KOReader、普通 EPUB 正常；休眠唤醒不白屏。
- 微信扫码成功、书架和章节可读。
- 每个 RSS 源可加载一篇，下载后断网重读。
- AI 在本人填 Key 后完成短段落翻译测试。
- CBZ 翻页与单双页切换正常，阅读统计无报错。
- Rakuyomi 搜索、章节、图片和整章离线打开均在设备上通过。

未实际完成的项目应保留为“待验证”，不写成已通过。


## 11. 中文漫画源与书库扩容（2026-11 追加）

以下中文源在 2026-11-07 已用 Rakuyomi **同版本 macOS 后端**实际跑通：

| 源 ID | 名称 | 实测状态 |
|---|---|---|
| `zh.baozimanhua` | 包子漫畫 | ✅ 搜索、章节、图片下载全通 |
| `zh.manhuagui` | 漫画柜 | ✅ 搜索、路由通；偶尔刷新慢 30s+ |
| `zh.dm5` | 动漫屋 | ✅ 搜索、章节通 |
| `zh.mangabz` | Māngabz | ⚠️ 搜索通；章节列表混入「X 話試看版」，下前确认 |

> 实测机器之心 (jiqizhixin.com/rss)、36氪 (36kr.com/feed) 因 XML 结构损坏不通过 RSS Reader 原版解析器，**未加入**；酷壳 coolshell.cn 在国内网络下响应超时 >10s，**未加入**。

### Rakuyomi 中文源接入步骤

```bash
# 前置: koreader/rakuyomi/settings.json 的 languages 必须包含 "zh"
# 使用 Kindle 时，.aix 源文件会被我倒到 `koreader/rakuyomi/sources/`，配合 `.id.source` marker
# 4 个实测可用源的 ID（放在 settings.json 里的 source_lists 之外的本地发现才搜索得到）
# zh.baozimanhua, zh.manhuagui, zh.dm5, zh.mangabz

# 也可以让 Kindle 自动从 source_lists 里找到它们并 Install；
# 慢 WiFi 下建议先在电脑上验证，再 Kindle 一次性下载
```

### Kindle 实际预inject 的漫画（供列表参考，版权归原作）

以下已刷入书库，可在 Kindle 直接点开继续下载：

- 海贼王（包子漫畫，1187 话）、一拳超人（437）、葬送的芙莉莲（131）
- 电锯人（255）、迷宫饭（dm5，119）、进击的巨人（186）、火影忍者（360）
- 鬼灭之刃（212）、龙珠（519）、灌篮高手（31）、全职猎人（184）
- 咒术回战（299）、间谍过家家（194）、怪兽8号（150）

> 全部章节数经过 `refresh-chapters` + `GET /chapters` 双验。若某部在你网络下 refresh 慢，说明该源在自己的源站受限，不影响其它源可用性。

### 坑洞备忘

- `zh.mangabz` 在 2026-11-07 实测章节列表混入「X 話試看版」，下载前确认标题是否带「試看」；`試看版 （13P）` vs 完整 `（30P）`。
- 海贼王包子漫畫源偶尔会返回 reqwest 解码误报，CBZ zip 文件本身完整，用 `unzip -l` + `PIL.Image.verify()` 复核即可。
- 删除一台 Kindle 的漫画时（长按 → 移除出图书馆），CBZ 默认**保留**在 `downloads/`，不会同步删除，见 `delete_downloaded_on_remove: false`。
