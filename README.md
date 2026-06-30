# 写个故事 / write-a-story

这是一个 Codex/Agentspace 可调用的编剧 skill，内部名称为 `write-a-story`，中文显示名为“写个故事”。

它融合了三本剧本创作书的结构化方法：

- 罗伯特·麦基《故事》
- 悉德·菲尔德《电影剧本写作基础》
- Blake Snyder《Save the Cat!》

适合用于构思、诊断、写作或改写短篇与长篇剧本，尤其是把一个模糊想法推进到 logline、人物欲望、结构、场景卡、高潮和可拍文本。

## 仓库结构

```text
.
├── SKILL.md                  # skill 入口文件
├── chapters/                 # 44 个章节方法卡
├── cheatsheet.md             # 快速创作与诊断表
├── patterns.md               # 可执行工作流
├── glossary.md               # 术语表
├── three-book-synthesis.md   # 三书共识与冲突优先级
├── install.sh                # 本地安装脚本
└── scripts/verify_skill.py   # 离线验证脚本
```

## 在其他设备安装

### 方式 A：Codex Desktop / Codex skills 目录

在目标设备上执行：

```bash
git clone https://github.com/<你的用户名>/<这个仓库名>.git /tmp/write-a-story
bash /tmp/write-a-story/install.sh
```

安装后重启 Codex Desktop，或重新打开一个 Codex 会话。调用时使用：

```text
$write-a-story
```

### 方式 B：手动复制

如果目标设备没有 bash：

1. 下载这个仓库的 zip。
2. 解压后把整个文件夹复制到：
   - macOS/Linux: `~/.codex/skills/write-a-story`
   - Windows: `%USERPROFILE%\.codex\skills\write-a-story`
3. 重启 Codex。
4. 使用 `$write-a-story` 调用。

### 方式 C：Agentspace skills CLI

如果你的环境使用 `npx skills`，可以尝试：

```bash
npx skills add <你的用户名>/<这个仓库名> -g -y
```

不同 skills runtime 对仓库布局的识别规则可能不同；如果 CLI 安装失败，用方式 A 或方式 B。

## 验证

安装后可以运行：

```bash
python3 ~/.codex/skills/write-a-story/scripts/verify_skill.py ~/.codex/skills/write-a-story
```

你应该看到：

```text
OK: write-a-story skill verified.
```

## 使用示例

```text
$write-a-story 我想写一个10秒短片：一个女孩反复观看自己的手机录像，发现背景里有一个未来的自己。
```

```text
$write-a-story 帮我诊断这个剧本中段为什么软。
```

```text
$write-a-story 用三书共识帮我把这个概念整理成 logline、人物欲望、高潮选择和短片结构。
```

## 注意

- `name` 必须保持为 `write-a-story`，否则 Codex 可能无法识别。
- `SKILL.md` 的 frontmatter 只能使用 Codex 支持的字段。
- 这个 skill 是对三本书方法结构的学习提炼，不包含原书全文。
