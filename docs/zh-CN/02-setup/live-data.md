# 实时数据连接器

静态笔记只是半个大脑。另一半是不断变化的内容：日历、收件箱，以及真正产生决策的沟通渠道。

MCP 连接这些来源的方式，与连接 Obsidian 相同。

<a id="calendar"></a>

## 日历

```bash
claude mcp add google-workspace uvx workspace-mcp --tools calendar
```

浏览器会打开 OAuth 登录页面。授予读取权限。

随后，知识库就可以据此工作：

```
Read my calendar for today, log what I committed to in each meeting into my
tasks project, and flag anything without a clear next step.
```

电子邮件、Slack 和 Notion 通过各自的 MCP 服务器连接，注册方式相同。

<a id="grant-read-not-write"></a>

## 授予读取权限，不授予写入权限

给每个连接器提供完成任务所需的最小权限范围，只要可以选择，就优先使用只读权限。第二大脑应该读取你的数据，而不是删除它，或者代你发送内容。

<a id="the-rule-that-matters-most"></a>

## 最重要的规则

**依靠密钥权限，而不是提示词。**

告诉智能体“不要删除这个”，只是一条建议，不是安全设置。只要智能体在技术上能够删除文件、清空文件夹或发送邮件，未来某一天，在某个你未曾预料的上下文中，它就可能这样做。

在权限层面控制哪些操作可行：只读令牌、限定范围的密钥、每个连接器独立的凭据。这样，`CLAUDE.md` 中的指令就成了安全边界之上的偏好，而不是隔开你的收件箱与一次错误运行的唯一屏障。

这一点同样适用于你自己的知识库。请参阅[防护措施](../06-agents/safety-and-guardrails.md)。

<a id="what-is-worth-connecting"></a>

## 哪些来源值得连接

连接那些承载决策和承诺的来源：先接日历，再接你实际用于工作的电子邮件或聊天工具。

跳过那些只产生大量内容、却没有有效信息的来源。一个向知识库灌满通知的连接器，会让之后的每次查询变差，因为智能体必须穿过这些杂讯才能找到有用内容。

<a id="next"></a>

## 下一篇

[值得安装的插件](obsidian-plugins.md)
