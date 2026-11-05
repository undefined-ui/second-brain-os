# Obsidian 的 MCP 连接

MCP 是 Claude 与其他应用通信的标准方式。对于知识库，它提供的是通往 Obsidian 本身的入口，而不是底层文件夹的入口。这意味着智能体可以从任何会话中使用知识库，而不必只从该目录内启动。

刚开始不需要它。当你需要定时任务，或使用桌面应用而不是知识库目录中的终端时，再添加即可。

<a id="two-routes"></a>

## 两条路径

[Local REST API 插件](https://github.com/coddingtonbear/obsidian-local-rest-api)现在已在 `/mcp/` 提供内置 MCP 服务器，因此不再必须另装服务器。先检查它的 README：如果内置服务器能满足需求，就直接在客户端中注册，并跳过下面的第 2 步。

这里描述的第三方路径，是通过插件的 REST API 运行 `mcp-obsidian`。它仍然是文档最丰富、也是大多数指南介绍的方案。两条路径最终都能达到相同目的。

<a id="step-1-enable-the-plugin"></a>

## 第 1 步：启用插件

在 Obsidian 中依次打开：**设置**（左下角齿轮）→ **第三方插件** → **启用第三方插件** → **浏览** → 搜索 `Local REST API` → **安装** → **启用**。

打开插件设置。那里有一个 **API Key**，是一长串字母和数字。复制它。

Obsidian 显示密钥时，会在前面加上 `Bearer`。这个词不是密钥的一部分，只复制它后面的字符串。这是首次连接失败最常见的原因。

<a id="step-2-register-the-server"></a>

## 第 2 步：注册服务器

在 Claude Code 标签页或终端中执行以下命令，将 `PASTE-YOUR-KEY-HERE` 替换为你的密钥：

```bash
claude mcp add-json obsidian-vault '{
  "type": "stdio",
  "command": "uvx",
  "args": ["mcp-obsidian"],
  "env": {
    "OBSIDIAN_API_KEY": "PASTE-YOUR-KEY-HERE",
    "OBSIDIAN_HOST": "127.0.0.1",
    "OBSIDIAN_PORT": "27124"
  }
}'
```

`uvx` 会在不永久安装的情况下运行服务器。如果找不到这个命令，请先安装 `uv`。

<a id="step-3-test-it"></a>

## 第 3 步：测试连接

```
List every file in my Obsidian vault.
```

如果智能体能读取并列出你的笔记，说明连接成功。

<a id="when-it-does-not-work"></a>

## 无法连接时

- **Obsidian 已关闭。** 插件在应用内部提供 API，因此只有 Obsidian 运行时才能连接。
- **密钥中包含 `Bearer`。** 删除它。
- **端口错误。** 对照插件设置显示的端口，检查配置中的值。默认端口是 27124。
- **插件已禁用。** 更新后重新开启受限模式，会关闭第三方插件。

<a id="do-you-need-this-at-all"></a>

## 你究竟是否需要它

一个曾经持续维护的 `mcp-obsidian` 分支已归档，理由是：知识库本来就是磁盘上的 Markdown 文件，再绕经 REST 插件只会增加复杂性。这与本指南建议先使用文件系统的理由一致，值得认真考虑：只有当你确实需要从知识库目录之外的会话访问它时，MCP 才值得引入。

<a id="security"></a>

## 安全

这会启动一个本地 HTTP 服务器，而密钥提供对笔记的完整读写权限。将地址保持为 `127.0.0.1`，不要将端口暴露出去，并像保护密码一样保护密钥。如果把密钥粘贴到任何公开位置，请在插件设置中轮换它。

<a id="next"></a>

## 下一篇

[编写你的 CLAUDE.md](claude-md.md)
