// Simplified Chinese navigation and glossary metadata, keyed by stable graph IDs.
// Keep source documents, file names, URLs and graph topology in their original form.
// New upstream nodes fall back to the English metadata in graph-data.js.
window.SBOS_NODE_ZH = {
  'root': { label: 'Second Brain OS', desc: '面向 AI 工程师的指南与资源：从一条提示词到生产环境的智能体开发课程、深入各个层面的五本手册、第二大脑实战项目、工具箱，以及值得阅读的资料。' },
  'col:course': { label: '智能体开发课程', desc: '七个模块，带你从一条提示词走向生产级智能体：理论来自白皮书，每个模块都有实战。建议按顺序学习。' },
  'col:handbook': { label: '专题手册', desc: '围绕课程中的某一层，汇集技术、工具与实战项目，供你随时查阅。可以从任意主题开始。' },
  'col:guide': { label: '第二大脑', desc: '一个实战项目：让智能体用纯 Markdown 为你建立并维护知识库。一个晚上即可搭建。' },
  'col:glossary': { label: '术语表', desc: '全站反复出现的核心概念。每个术语都链接到最依赖它的页面。' },
  'col:toolkit': { label: '工具箱', desc: '可安装使用的智能体技能、斜杠命令、子智能体、脚本、课程插件，以及知识库入门模板。' },
  'col:resources': { label: '资源', desc: '经过筛选的论文、工具、Obsidian 插件、代码仓库与阅读资料。' },

  'sec:course-0-map': { label: '0 · 全景图', desc: '什么是智能体，模型周围的五个层次，以及何时工作流比循环更合适。' },
  'sec:course-1-context': { label: '1 · 上下文', desc: '模型能看到什么：注意力、缓存、四个位置、会话与记忆。' },
  'sec:course-2-loop': { label: '2 · 循环', desc: '谁来决定下一步：目标、检查器、停止规则、预算，以及能在生产环境中运行的混合模式。' },
  'sec:course-3-gate': { label: '3 · 决策关卡', desc: '在高成本模型之前先做低成本决策：从分类器开始，在合适的场景使用系统一模型。' },
  'sec:course-4-harness': { label: '4 · 运行框架', desc: '模型周围的工作环境：隔离、指南、监测与权限，由外向内逐层搭建。' },
  'sec:course-5-evals': { label: '5 · 评估', desc: '每月运行同一套测试：检查运行轨迹中的行为、校验评审器，并建立包含失败案例的基准集。' },
  'sec:course-6-production': { label: '6 · 生产环境', desc: '从演示走向部署：网关、追踪、成本与安全，以及覆盖五个层次的首日行动计划。' },
  'sec:track-graph': { label: '知识图谱', desc: '用图谱构建智能体记忆：GraphRAG、提取流程与存储，然后花一个晚上为自己的知识库搭建图谱层。' },
  'sec:track-jev': { label: 'Jev 工程', desc: '决策关卡是系统的一层，Jev 是实现它的一种方式。返回带置信度的类型化决策，并在获得 Jev 使用权限前先搭建可运行的系统。' },
  'sec:track-harness': { label: '智能体运行框架', desc: '模型周围的运行机制：循环、工具、上下文工程与框架选型，用约 150 行代码在一个晚上搭建可用的运行框架。' },
  'sec:track-loop': { label: '循环工程', desc: '智能体的控制系统：停止条件、评审器与上下文整理，以及一个可放心运行到次日清晨的循环。' },
  'sec:track-evals': { label: '评估工程', desc: '以测量规范 AI 产品：基准集、可靠的评审器与智能体轨迹，并在一个下午搭建第一套评估。' },
  'sec:01-concepts': { label: '基本概念', desc: '为什么由大语言模型维护的知识库比被你弃用的笔记系统更有效，以及这种模式究竟是什么。' },
  'sec:02-setup': { label: '搭建', desc: '一个晚上，从零搭建由智能体维护的知识库。首次使用请依次完成九个步骤：约二十分钟的输入操作，另加第四步访谈所需的时间。' },
  'sec:03-ingestion': { label: '资料导入', desc: '尽可能顺畅地把阅读、观看和写作的内容收进 raw/，再有序整理到 Wiki 中。' },
  'sec:04-structuring': { label: '组织结构', desc: '决定知识库成为知识图谱还是资料堆的规则。' },
  'sec:05-graphs': { label: '图谱', desc: '深入大多数第二大脑指南一带而过的部分：图谱视图背后的结构与用途。' },
  'sec:06-agents': { label: '智能体', desc: '让一次性的搭建变成可以自行维护的系统。' },
  'sec:07-retrieval': { label: '检索', desc: '如何向知识库提问，并获得值得信任的回答。' },
  'sec:08-outputs': { label: '知识输出', desc: '当知识库能够产出成果，它才真正发挥价值。' },
  'sec:09-maintenance': { label: '维护', desc: '新鲜感过去后，让系统持续运转的方法。' },
  'sec:10-troubleshooting': { label: '故障排查', desc: '具体问题与对应的解决方法。' },

  'course-0-map/what-an-agent-is': { label: '什么是智能体' },
  'course-0-map/five-layers': { label: '五个层次，一个系统' },
  'course-0-map/agents-or-workflows': { label: '智能体还是工作流' },
  'course-1-context/how-models-read': { label: '模型如何读取上下文' },
  'course-1-context/the-four-places': { label: '上下文的四个位置' },
  'course-1-context/context-practice': { label: '上下文实战' },
  'course-2-loop/loops-vs-workflows': { label: '循环与工作流' },
  'course-2-loop/the-four-parts': { label: '循环的四个组成部分' },
  'course-2-loop/loop-practice': { label: '循环实战：筛选、循环与回退' },
  'course-3-gate/cheap-decisions': { label: '低成本决策' },
  'course-3-gate/gates-in-practice': { label: '决策关卡的实际应用' },
  'course-3-gate/gate-practice': { label: '决策关卡实战' },
  'course-4-harness/the-office': { label: '模型的工作环境' },
  'course-4-harness/the-four-rings': { label: '四层防护' },
  'course-4-harness/harness-practice': { label: '运行框架实战' },
  'course-5-evals/two-kinds-of-checks': { label: '两类检查' },
  'course-5-evals/judges-and-golden-sets': { label: '评审器与基准集' },
  'course-5-evals/evals-practice': { label: '评估实战' },
  'course-6-production/from-prototype': { label: '从原型到生产环境' },
  'course-6-production/operating-agents': { label: '智能体运维' },
  'course-6-production/day-one-plan': { label: '首日行动计划' },

  'track-graph/why-graphs': { label: '为什么使用知识图谱' },
  'track-graph/graphrag': { label: 'GraphRAG' },
  'track-graph/building-graphs-with-llms': { label: '用大语言模型构建图谱' },
  'track-graph/graph-stores': { label: '图谱存储' },
  'track-graph/tools': { label: '工具' },
  'track-graph/build-extract': { label: '实战：提取图谱' },
  'track-graph/build-query': { label: '实战：查询图谱' },
  'track-graph/build-use': { label: '实战：将图谱接入循环' },
  'track-graph/resources': { label: '资源' },
  'track-jev/system-one-models': { label: '系统一模型' },
  'track-jev/what-jev-is-good-for': { label: 'Jev 的适用场景' },
  'track-jev/jev-in-an-agent-stack': { label: '智能体技术栈中的 Jev' },
  'track-jev/getting-started': { label: 'Jev 入门' },
  'track-jev/build-decision-endpoint': { label: '实战：类型化决策接口' },
  'track-jev/build-router': { label: '实战：基于置信度的路由器' },
  'track-jev/build-swap-in-jev': { label: '实战：切换到 Jev' },
  'track-jev/resources': { label: 'Jev 资源' },
  'track-harness/what-a-harness-is': { label: '什么是运行框架' },
  'track-harness/claude-code-as-harness': { label: '用 Claude Code 作为运行框架' },
  'track-harness/context-engineering': { label: '上下文工程' },
  'track-harness/tools-and-mcp': { label: '工具与 MCP' },
  'track-harness/harness-landscape': { label: '运行框架全览' },
  'track-harness/build-the-loop': { label: '实战：搭建循环' },
  'track-harness/build-guardrails': { label: '实战：权限与上下文' },
  'track-harness/build-graduate': { label: '实战：何时升级运行框架' },
  'track-harness/resources': { label: '资源' },
  'track-loop/what-loop-engineering-is': { label: '什么是循环工程' },
  'track-loop/stop-conditions': { label: '停止条件' },
  'track-loop/critics-and-verification': { label: '评审器与验证' },
  'track-loop/context-hygiene': { label: '上下文整理' },
  'track-loop/patterns': { label: '循环模式' },
  'track-loop/build-goal-test': { label: '实战：目标完成检查' },
  'track-loop/build-critic': { label: '实战：评审器' },
  'track-loop/build-overnight': { label: '实战：通宵运行的循环' },
  'track-loop/resources': { label: '资源' },
  'track-evals/why-evals': { label: '为什么需要评估' },
  'track-evals/designing-evals': { label: '设计评估' },
  'track-evals/llm-as-judge': { label: '用大语言模型担任评审器' },
  'track-evals/agent-evals': { label: '智能体评估' },
  'track-evals/tooling': { label: '评估工具' },
  'track-evals/build-traces': { label: '实战：阅读运行轨迹' },
  'track-evals/build-suite': { label: '实战：评估套件' },
  'track-evals/build-ci': { label: '实战：评估关卡' },
  'track-evals/resources': { label: '评估资源' },

  '01-concepts/what-is-a-second-brain': { label: '第二大脑究竟是什么' },
  '01-concepts/the-save-for-later-paradox': { label: '稍后再看的悖论' },
  '01-concepts/llm-wiki-pattern': { label: 'LLM Wiki 模式' },
  '01-concepts/two-layers': { label: '两个层次' },
  '01-concepts/why-markdown-and-plain-text': { label: '为什么使用 Markdown 与纯文本' },
  '01-concepts/pkm-lineage': { label: '卡片盒、PARA 与常青笔记' },
  '01-concepts/wiki-vs-rag': { label: 'Wiki 与 RAG' },
  '01-concepts/what-good-looks-like': { label: '运行良好的知识库是什么样' },
  '02-setup/obsidian-install-and-vault': { label: 'Obsidian 与你的第一个知识库' },
  '02-setup/claude-code-setup': { label: '在知识库中使用 Claude Code' },
  '02-setup/mcp-obsidian': { label: 'Obsidian 的 MCP 接入' },
  '02-setup/claude-md': { label: '编写 CLAUDE.md' },
  '02-setup/vault-structure': { label: '知识库结构' },
  '02-setup/project-scoping': { label: '限定项目范围' },
  '02-setup/live-data': { label: '实时数据连接器' },
  '02-setup/obsidian-plugins': { label: '值得安装的插件' },
  '02-setup/git-and-sync': { label: 'Git、同步与备份' },
  '03-ingestion/web-clipper': { label: '网页文章' },
  '03-ingestion/youtube-transcripts': { label: 'YouTube 与播客' },
  '03-ingestion/pdfs-and-books': { label: 'PDF、论文与书籍' },
  '03-ingestion/chat-exports': { label: '聊天记录导出' },
  '03-ingestion/voice-and-meetings': { label: '语音笔记与会议' },
  '03-ingestion/newsletters-and-email': { label: '电子简报与邮件' },
  '03-ingestion/bulk-backfill': { label: '批量导入多年积累的资料' },
  '04-structuring/atomic-pages': { label: '一页一个想法' },
  '04-structuring/page-types': { label: '四种页面类型' },
  '04-structuring/linking-rules': { label: '链接规则' },
  '04-structuring/frontmatter-schema': { label: 'Frontmatter 元数据结构' },
  '04-structuring/naming-and-aliases': { label: '命名与别名' },
  '04-structuring/dedupe-and-merge': { label: '去重与合并' },
  '04-structuring/contradictions-and-supersession': { label: '矛盾与观点更替' },
  '04-structuring/index-and-log': { label: 'index.md 与 log.md' },
  '05-graphs/graph-basics': { label: '知识库的图谱基础' },
  '05-graphs/obsidian-graph-view': { label: '读懂 Obsidian 图谱视图' },
  '05-graphs/typed-links': { label: '带类型的链接' },
  '05-graphs/graph-vs-vectors': { label: '图谱与向量嵌入' },
  '05-graphs/graphrag': { label: 'GraphRAG 及其适用场景' },
  '05-graphs/exporting-your-graph': { label: '导出图谱' },
  '05-graphs/metrics': { label: '值得追踪的图谱指标' },
  '06-agents/agent-roles': { label: '智能体角色' },
  '06-agents/scheduled-maintenance': { label: '定时调度' },
  '06-agents/subagents': { label: '子智能体与并行工作' },
  '06-agents/hooks': { label: '钩子' },
  '06-agents/skills-and-commands': { label: '技能与斜杠命令' },
  '06-agents/safety-and-guardrails': { label: '安全防护' },
  '07-retrieval/asking-questions': { label: '向知识库提问' },
  '07-retrieval/query-patterns': { label: '查询模式' },
  '07-retrieval/search-tools': { label: '搜索工具' },
  '07-retrieval/rag-on-top': { label: '按需添加 RAG' },
  '07-retrieval/context-budget': { label: '上下文预算' },
  '08-outputs/writing-from-the-vault': { label: '基于知识库写作' },
  '08-outputs/research-reports': { label: '研究报告' },
  '08-outputs/publishing-and-export': { label: '发布与导出' },
  '08-outputs/teaching-yourself': { label: '从自己的知识库中学习' },
  '09-maintenance/lint-and-health': { label: '知识库检查' },
  '09-maintenance/review-cadence': { label: '定期回顾' },
  '09-maintenance/versioning-with-git': { label: '版本管理' },
  '09-maintenance/backups-and-portability': { label: '备份与可迁移性' },
  '09-maintenance/privacy-and-secrets': { label: '隐私' },
  '09-maintenance/scaling': { label: '扩展到上千个页面' },
  '10-troubleshooting/common-failures': { label: '常见问题' },
  '10-troubleshooting/agent-writes-garbage': { label: '智能体写出的内容质量差' },
  '10-troubleshooting/broken-links': { label: '失效链接与孤立页面' },
  '10-troubleshooting/vault-too-big': { label: '知识库过于庞大' },
  '10-troubleshooting/faq': { label: '常见问答' },

  'hub:skills': { label: '技能', desc: '第二大脑项目中的每个工作流对应一个技能。智能体只在任务匹配时加载对应技能。' },
  'hub:commands': { label: '斜杠命令', desc: '通过 /name 输入，进入限定范围的技能操作。' },
  'hub:agents': { label: '子智能体', desc: '六个子智能体，其中四个按设计仅允许读取。' },
  'hub:scripts': { label: '脚本', desc: '无需第三方依赖的 Python 脚本，用于链接检查、统计、图谱导出与聊天记录导入。' },
  'hub:plugin': { label: 'agents-course 插件', desc: '智能体开发课程的配套工具：审计上下文、用脚本定义完成条件、搭建评估套件，以及评审循环结果的智能体。' },
  'hub:vault': { label: '知识库入门模板', desc: 'vault-template/：包含 Wiki 结构、项目流程、CLAUDE.md 与页面模板，可直接复制使用。' },
  'rcat:papers': { label: '论文', desc: '与知识库检索和推理相关的研究。阅读这些论文，自己判断是否需要向量数据库。' },
  'rcat:tools': { label: '工具', desc: 'Obsidian 插件目录以外的工具。插件请参阅 plugins.md。Star 数来自 2026 年 9 月的 GitHub 数据。' },
  'rcat:plugins': { label: 'Obsidian 插件', desc: '按 Obsidian 官方社区统计的安装量排序，数据截至 2026 年 9 月。从超过 7,400 个插件中，筛选适合由智能体维护的知识库的插件。' },
  'rcat:repositories': { label: '代码仓库', desc: '值得了解的图谱、检索与记忆项目。Star 数来自 2026 年 9 月的 GitHub API。智能体技能见 skills.md，Obsidian 插件见 plugins.md。' },
  'rcat:skills': { label: '技能目录', desc: '按单个技能计数：包含十六个技能的仓库计为十六项，因为实际安装的就是这些技能。统计来自对 2026 年 9 月各仓库文件树的检查。' },
  'rcat:reading': { label: '阅读资料', desc: 'Karpathy 于 2026 年 4 月 4 日发布的 llm-wiki gist。本仓库以其中的模式为基础。' },

  'term:second-brain': { label: '第二大脑', desc: '一个由智能体读写的本地纯文本文件夹，保存你阅读和理解过的知识，并能回答你的问题。' },
  'term:llm-wiki': { label: 'LLM Wiki', desc: 'Karpathy 提出的模式：模型将来源资料整理成相互链接的 Wiki，后续提问时直接使用这些成果。' },
  'term:vault': { label: '知识库', desc: '智能体维护的 Markdown 文件夹。Obsidian 称它为仓库（Vault），对智能体来说它就是一组文件。' },
  'term:obsidian': { label: 'Obsidian', desc: '用于阅读知识库、浏览图谱和剪藏来源资料的 Markdown 编辑器。智能体工作时无需运行它。' },
  'term:claude-code': { label: 'Claude Code', desc: '负责整理资料的智能体：读取原始来源、编写并链接页面、执行维护。' },
  'term:claude-md': { label: 'CLAUDE.md', desc: '智能体在每次会话开始时读取的常驻指令：你是谁、页面规范，以及知识库规则。' },
  'term:mcp': { label: 'MCP', desc: '模型上下文协议（Model Context Protocol）：连接智能体与工具、数据的标准接口，例如从不同环境访问你的知识库。' },
  'term:raw': { label: 'raw/', desc: '收件箱与原始档案：剪藏文章、转录文本和 PDF。只写入一次，之后不再修改，也很少重新阅读。' },
  'term:two-layers': { label: '两个层次', desc: 'Wiki 保存已知的知识，项目层承载正在做的事情。分开管理，让两者都保持有用。' },
  'term:ingest': { label: '资料导入', desc: '将一份原始来源转化为带链接的 Wiki 页面。只有新页面与已有知识建立连接，导入才算完成。' },
  'term:wikilink': { label: 'Wiki 链接', desc: '笔记之间的 [[页面名称]] 链接。它是最简单的图谱边，也是知识库不断积累价值的基础。' },
  'term:backlinks': { label: '反向链接', desc: '指向某个页面的链接。无需搜索，就能找到所有引用这个想法的页面。' },
  'term:atomic-pages': { label: '原子化页面', desc: '每页只讲一个想法，让链接的含义明确，并让页面能够在各种相关场景中复用。' },
  'term:page-types': { label: '页面类型', desc: '来源、概念、实体与综合：每种类型都有自己的内容要求和链接规则。' },
  'term:frontmatter': { label: 'Frontmatter 元数据', desc: '页面顶部的 YAML 区块：类型、来源、日期与状态。它让知识库无需数据库也能被查询。' },
  'term:aliases': { label: '别名', desc: '同一页面的其他名称，让链接和搜索指向已有页面，避免重复创建。' },
  'term:contradictions': { label: '矛盾', desc: '当新来源提出不同观点时，保留双方立场、日期与来源，记录你曾经相信什么以及原因。' },
  'term:index-log': { label: 'index.md 与 log.md', desc: '智能体首先读取的目录，以及每次运行记录一行的日志，让知识库的每次改动都可审计。' },
  'term:knowledge-graph': { label: '知识图谱', desc: '页面是节点，链接是边。在这套方案中，图谱就是文件系统，无需服务器或独立存储。' },
  'term:typed-links': { label: '带类型的链接', desc: '明确两个页面如何关联的链接，例如支持、矛盾或扩展。只有来源明确表达了关系，才标注类型。' },
  'term:orphans': { label: '孤立页面', desc: '没有任何页面链接到的页面。它们很快会被遗忘，也是观察知识库衰退时首先要关注的指标。' },
  'term:hubs': { label: '枢纽与桥梁', desc: '枢纽是大量页面共同链接的页面；桥梁连接原本分离的群组。两者都能揭示知识结构中的关键位置。' },
  'term:clusters': { label: '群组', desc: '链接密集的页面集合。未经刻意规划而自然形成的群组，往往能带来新的发现。' },
  'term:graphrag': { label: 'GraphRAG', desc: '基于提取的实体图谱与社区摘要进行检索，适合回答关于整个语料库的全局问题。' },
  'term:rag': { label: 'RAG', desc: '检索增强生成：提问时按相似度检索文本片段。不同问题之间不会自动积累成果。' },
  'term:vectors': { label: '向量嵌入', desc: '基于文本片段嵌入的相似度搜索。当结构化、相互链接的知识库已无法满足检索需求时，再考虑加入。' },
  'term:context-window': { label: '上下文窗口', desc: '模型一次能够看到的内容范围。智能体在当前会话中掌握的一切都要占用这份预算。' },
  'term:lost-in-middle': { label: '中间信息丢失', desc: '模型对长上下文开头和结尾的记忆远好于中间部分。这也是把所有信息塞进上下文容易失败的原因。' },
  'term:skills': { label: '技能', desc: '包含 SKILL.md 的文件夹，提供智能体仅在任务匹配时加载的指令。每个工作流对应一个技能。' },
  'term:slash-commands': { label: '斜杠命令', desc: '以 /name 输入的简短命令，进入限定范围的技能操作，是日常使用的直接入口。' },
  'term:subagents': { label: '子智能体', desc: '拥有独立上下文与有限工具集的智能体。本项目中的多数子智能体按设计仅允许读取。' },
  'term:hooks': { label: '钩子', desc: '运行框架在特定事件发生时执行的代码，例如工具调用前或编辑后，用于落实模型无法遗漏的规则。' },
  'term:scheduled': { label: '定时维护', desc: '定时执行检查、链接整理与回顾，让知识库在你休息时自行归档。' },
  'term:lint': { label: '检查与健康状态', desc: '自动检查失效链接、孤立页面、缺失的元数据与过期页面，相当于知识库的测试套件。' },
  'term:git': { label: 'Git', desc: '知识库的版本历史。每次智能体运行都可以审查，出错的改动都可以撤销。' },
  'term:privacy': { label: '隐私与敏感信息', desc: '哪些内容绝不能进入页面、提示词或公开导出，以及防止这些内容泄露的检查。' },
  'term:web-clipper': { label: 'Web Clipper', desc: 'Obsidian 的浏览器扩展，一键将文章保存为 raw/ 中的 Markdown 文件。' },
  'term:transcripts': { label: '转录文本', desc: '将视频、语音与会议转换成文本，便于像其他资料一样导入知识库。' },
  'term:agent': { label: '智能体', desc: '具备工具、在循环中运行的模型，自行决定下一步，直到达成目标或触发停止规则。' },
  'term:five-layers': { label: '五个层次', desc: '课程对模型周围系统的划分：上下文、循环、决策关卡、运行框架与评估。' },
  'term:workflows': { label: '工作流与智能体', desc: '工作流由代码决定下一步，智能体由模型决定下一步。大多数生产系统会结合两者。' },
  'term:context-engineering': { label: '上下文工程', desc: '决定哪些内容进入系统提示词、工具、历史与末尾，以及它们的排列顺序，让模型看到正确的信息。' },
  'term:caching': { label: '提示词缓存', desc: '在多次调用间复用提示词的稳定前缀。合理组织上下文，可以降低成本并加快响应。' },
  'term:memory': { label: '记忆', desc: '跨会话保留的信息。在本项目中，它是智能体重新读取的文件，不是模型的隐藏功能。' },
  'term:loop': { label: '智能体循环', desc: '目标、行动、检查、重复。循环是模型周围的控制系统，也是多数失败发生的位置。' },
  'term:stop-conditions': { label: '停止条件', desc: '循环必须结束的情况：目标达成、预算耗尽或没有进展。缺少停止条件，循环可能持续到造成损害。' },
  'term:critics': { label: '评审器与检查器', desc: '在模型之外判断结果的检查机制，例如测试、编译器或独立评审者。模型自我审查不属于这类检查。' },
  'term:gate': { label: '决策关卡', desc: '在高成本模型之前执行的低成本、范围明确的决策：对每一项提出一个有界问题，根据答案选择处理路径。' },
  'term:system-one': { label: '系统一模型', desc: '小型快速模型，返回带置信度的类型化决策而非自由文本。Jev 是实现决策关卡的一种方式。' },
  'term:harness': { label: '运行框架', desc: '模型周围的工作环境：由外向内搭建的隔离、指南、监测与权限机制。' },
  'term:guardrails': { label: '安全防护与权限', desc: '规定智能体可以操作什么、哪些操作必须征求批准，以及它犯错时仍然有效的边界。' },
  'term:tools-tool-use': { label: '工具使用', desc: '模型请求运行框架代为执行操作。智能体的各种能力都通过这种方式实现。' },
  'term:evals': { label: '评估', desc: '每月运行同一套测试，检查真实行为，避免提示词或模型的变更悄悄破坏功能。' },
  'term:golden-set': { label: '基准集', desc: '每次评估都会使用的固定案例集合，其中包括已经遇到过的失败案例。' },
  'term:llm-judge': { label: '大语言模型评审器', desc: '根据评分标准对输出打分的模型。先用人工标注验证评审器本身，再用它进行评估。' },
  'term:traces': { label: '运行轨迹', desc: '逐步记录智能体全部行为的完整日志，是行为评估与调试共同使用的依据。' },
  'term:production': { label: '生产环境', desc: '从偶尔成功的演示，走向具备追踪、成本控制、安全措施与明确负责人的系统。' },
};

// Keep executable tool names intact; translate their descriptions.
Object.assign(window.SBOS_NODE_ZH, {
  "skill:second-brain-backfill": {
    "label": "second-brain-backfill",
    "desc": "分批、可控地将大型资料归档导入知识库：筛选值得导入的内容，优先处理较早的资料，每批结束后保存检查点，并让费用可见。适用于导入多年书签、其他笔记应用的导出文件、下载文件夹或聊天记录等情况……"
  },
  "skill:second-brain-changed-my-mind": {
    "label": "second-brain-changed-my-mind",
    "desc": "追踪用户记录的观点如何变化：被新观点替代的主张、不同日期来源之间的矛盾，以及促成改变的证据。适用于询问自己在哪些事情上改变了看法、某个主题的思考如何发展，或过去相信什么等情况……"
  },
  "skill:second-brain-chat-import": {
    "label": "second-brain-chat-import",
    "desc": "先检查隐私，再将导出的聊天记录分为需要导入、归档和删除的内容。适用于导入 Claude 或 ChatGPT 历史记录、旧对话，或判断聊天归档中哪些内容值得保留。不用于导入单次粘贴的对话……"
  },
  "skill:second-brain-graph": {
    "label": "second-brain-graph",
    "desc": "分析知识库的链接图谱，报告孤立率、平均度、连通分量、枢纽、桥接节点和聚类，并解释各指标对检索的意义。适用于检查图谱健康状况或结构、获取指标，以及寻找连接最多或最孤立的页面……"
  },
  "skill:second-brain-ingest": {
    "label": "second-brain-ingest",
    "desc": "将第二大脑知识库中的原始资料转化为相互链接的 wiki 页面：阅读来源，拆分概念与实体，创建或更新页面，连接已有页面，并记录运行日志。适用于将文件放入 raw/，或粘贴文章、转录文本、PDF 后请求导入的情况……"
  },
  "skill:second-brain-lint": {
    "label": "second-brain-lint",
    "desc": "审查并修复第二大脑知识库的结构问题：失效 wiki 链接、孤立页面、空白占位页、不符合规范的 frontmatter、近似重复页面和过期索引。适用于结构检查、清理、审计或健康检查等需求……"
  },
  "skill:second-brain-merge": {
    "label": "second-brain-merge",
    "desc": "合并描述同一事物的两个页面，保留每条不同的主张，重定向入站链接，并记录合并过程。适用于用户批准合并重复页面、要求“将 X 合入 Y”，或清理结构检查提出的近似重复页面。不用于合并……"
  },
  "skill:second-brain-metrics": {
    "label": "second-brain-metrics",
    "desc": "记录带日期的知识库健康指标快照，并与历史快照比较，让趋势可见。适用于月度或季度检查、判断知识库是否在改善，或持续跟踪指标。不用于一次性的图谱分析……"
  },
  "skill:second-brain-privacy": {
    "label": "second-brain-privacy",
    "desc": "审查知识库中不应存在的内容：凭据、他人的隐私信息、工作机密，以及用户不希望同步或备份的资料。适用于隐私检查、分享或同步前检查，以及刚导入聊天记录或会议笔记的情况……"
  },
  "skill:second-brain-project": {
    "label": "second-brain-project",
    "desc": "创建或更新知识库中的项目：搭建四阶段文件夹流程，为项目编写只有一个目标的 CLAUDE.md，并链接到所依赖的概念页。适用于开始需要持续推进的新工作、创建项目文件夹或定义项目目标……"
  },
  "skill:second-brain-publish": {
    "label": "second-brain-publish",
    "desc": "准备发布知识库中的一部分内容：检查主动公开标记，查找私密资料，在导出前报告链接可能泄露的内容。适用于将笔记发布为网站或数字花园、检查哪些内容可以公开，或设置导出流程。不用于……"
  },
  "skill:second-brain-query": {
    "label": "second-brain-query",
    "desc": "阅读第二大脑知识库自身的页面来回答问题，引用所用页面，并在知识库没有答案时明确说明。适用于询问自己对某主题知道什么、读过什么、两个想法有什么联系，或在哪些事情上改变了看法……"
  },
  "skill:second-brain-quiz": {
    "label": "second-brain-quiz",
    "desc": "根据用户自己的概念页生成问题，找出保存过却没有学会的内容，并将答案与页面内容比较。适用于自测、复习、从笔记制作记忆卡片，或检查遗忘内容。不用于通用的……"
  },
  "skill:second-brain-rename": {
    "label": "second-brain-rename",
    "desc": "安全重命名页面：更新文件，修复所有入站 wiki 链接，将旧名加入别名，并记录日志。适用于更改规范标题、修正不一致的标题，或处理结构检查发现的命名问题。不用于合并两个页面……"
  },
  "skill:second-brain-report": {
    "label": "second-brain-report",
    "desc": "根据知识库撰写研究报告：对照现有页面界定问题范围，列出空白，并写出包含引用、分歧和局限的发现。适用于研究报告、某主题的深入文章，或利用已收集资料全面理解一个问题……"
  },
  "skill:second-brain-review": {
    "label": "second-brain-review",
    "desc": "定期复盘第二大脑知识库：新增了什么，哪些主题正在增长，存在哪些矛盾，哪些问题仍未解决，以及接下来值得阅读什么。适用于周度或月度复盘、查看知识库变化，或回顾最近学习的主题……"
  },
  "skill:second-brain-transcript": {
    "label": "second-brain-transcript",
    "desc": "在资料导入前清理原始转录文本：添加标点和段落、标记说话者、修正技术术语的误识别，并按主题拆分长录音。适用于自动生成的转录稿、字幕、播客或讲座记录、会议录音文本，以及视频处理请求……"
  },
  "skill:second-brain-write": {
    "label": "second-brain-write",
    "desc": "基于知识库起草文章：从概念页构建提纲，保留用户自身来源的引用，并指出材料中的分歧。适用于根据已收集内容撰写文章、帖子、随笔或通讯，或探讨某个主题可以写什么。不用于……"
  },
  "cmd:aliases": {
    "label": "/aliases",
    "desc": "查找缺失的别名"
  },
  "cmd:archive": {
    "label": "/archive",
    "desc": "将不常用资料移出 wiki"
  },
  "cmd:ask": {
    "label": "/ask",
    "desc": "仅根据知识库回答问题"
  },
  "cmd:audit": {
    "label": "/audit",
    "desc": "审查智能体执行过的操作"
  },
  "cmd:backfill": {
    "label": "/backfill",
    "desc": "分批批量导入历史资料"
  },
  "cmd:bridges": {
    "label": "/bridges",
    "desc": "查找维系图谱连通性的页面"
  },
  "cmd:changed-my-mind": {
    "label": "/changed-my-mind",
    "desc": "查看自己修正过的观点"
  },
  "cmd:claude-md": {
    "label": "/claude-md",
    "desc": "创建或更新 CLAUDE.md"
  },
  "cmd:clusters": {
    "label": "/clusters",
    "desc": "查看知识库实际关注的主题"
  },
  "cmd:commit": {
    "label": "/commit",
    "desc": "提交当前状态，并附上有意义的提交说明"
  },
  "cmd:commitments": {
    "label": "/commitments",
    "desc": "列出尚未履行的承诺"
  },
  "cmd:compare": {
    "label": "/compare",
    "desc": "根据自己的资料比较两件事"
  },
  "cmd:connect": {
    "label": "/connect",
    "desc": "寻找两个想法之间的路径"
  },
  "cmd:contradictions": {
    "label": "/contradictions",
    "desc": "列出尚未解决的矛盾"
  },
  "cmd:contradicts": {
    "label": "/contradicts",
    "desc": "提出反对自己观点的论据"
  },
  "cmd:decisions": {
    "label": "/decisions",
    "desc": "列出已经作出的决定"
  },
  "cmd:dedupe": {
    "label": "/dedupe",
    "desc": "查找近似重复页面"
  },
  "cmd:doctor": {
    "label": "/doctor",
    "desc": "检查配置是否正常工作"
  },
  "cmd:draft": {
    "label": "/draft",
    "desc": "基于知识库起草内容"
  },
  "cmd:dry-run": {
    "label": "/dry-run",
    "desc": "预览运行结果而不写入"
  },
  "cmd:explain": {
    "label": "/explain",
    "desc": "用自己的话解释，并找出理解空白"
  },
  "cmd:export": {
    "label": "/export",
    "desc": "导出一个或一组页面"
  },
  "cmd:gaps": {
    "label": "/gaps",
    "desc": "查找自己理解中缺失的部分"
  },
  "cmd:graph-export": {
    "label": "/graph-export",
    "desc": "导出图谱供外部分析"
  },
  "cmd:graph": {
    "label": "/graph",
    "desc": "报告图谱的结构"
  },
  "cmd:handoff": {
    "label": "/handoff",
    "desc": "准备交接简报"
  },
  "cmd:health": {
    "label": "/health",
    "desc": "快速检查健康状况"
  },
  "cmd:hubs": {
    "label": "/hubs",
    "desc": "查找吞并了过多图谱连接的页面"
  },
  "cmd:index": {
    "label": "/index",
    "desc": "重建索引"
  },
  "cmd:ingest-chats": {
    "label": "/ingest-chats",
    "desc": "导入导出的聊天记录"
  },
  "cmd:ingest-highlights": {
    "label": "/ingest-highlights",
    "desc": "导入书籍或文章中的高亮"
  },
  "cmd:ingest-mine": {
    "label": "/ingest-mine",
    "desc": "导入自己完成的作品"
  },
  "cmd:ingest-newsletter": {
    "label": "/ingest-newsletter",
    "desc": "导入通讯，并避免重复"
  },
  "cmd:ingest-paper": {
    "label": "/ingest-paper",
    "desc": "导入学术论文"
  },
  "cmd:ingest-pdf": {
    "label": "/ingest-pdf",
    "desc": "导入 PDF"
  },
  "cmd:ingest-url": {
    "label": "/ingest-url",
    "desc": "剪藏并导入网页"
  },
  "cmd:ingest-voice": {
    "label": "/ingest-voice",
    "desc": "导入语音笔记"
  },
  "cmd:ingest-youtube": {
    "label": "/ingest-youtube",
    "desc": "导入视频或播客的转录文本"
  },
  "cmd:ingest": {
    "label": "/ingest",
    "desc": "将 raw/ 中的新资料导入 wiki"
  },
  "cmd:init": {
    "label": "/init",
    "desc": "搭建新知识库的初始结构"
  },
  "cmd:install": {
    "label": "/install",
    "desc": "安装技能、命令和智能体"
  },
  "cmd:know": {
    "label": "/know",
    "desc": "查看自己对某个主题知道什么"
  },
  "cmd:link": {
    "label": "/link",
    "desc": "发现并补充缺失的关联"
  },
  "cmd:lint": {
    "label": "/lint",
    "desc": "审查结构并执行可机械完成的修复"
  },
  "cmd:merge": {
    "label": "/merge",
    "desc": "合并两个页面"
  },
  "cmd:metrics": {
    "label": "/metrics",
    "desc": "记录带日期的指标快照"
  },
  "cmd:monthly": {
    "label": "/monthly",
    "desc": "月度结构复盘"
  },
  "cmd:orphans": {
    "label": "/orphans",
    "desc": "查找无法通过链接到达的页面"
  },
  "cmd:outline": {
    "label": "/outline",
    "desc": "根据概念页拟定文章提纲"
  },
  "cmd:privacy": {
    "label": "/privacy",
    "desc": "审查知识库中不应存在的内容"
  },
  "cmd:project-status": {
    "label": "/project-status",
    "desc": "查看项目进展"
  },
  "cmd:project": {
    "label": "/project",
    "desc": "创建项目"
  },
  "cmd:prune": {
    "label": "/prune",
    "desc": "查找可以安全移除的内容"
  },
  "cmd:publish": {
    "label": "/publish",
    "desc": "检查哪些内容可以安全发布"
  },
  "cmd:quiz": {
    "label": "/quiz",
    "desc": "用自己的页面进行自测"
  },
  "cmd:rename": {
    "label": "/rename",
    "desc": "重命名页面并修复所有链接"
  },
  "cmd:report": {
    "label": "/report",
    "desc": "撰写研究报告"
  },
  "cmd:retype": {
    "label": "/retype",
    "desc": "修正页面类型"
  },
  "cmd:review": {
    "label": "/review",
    "desc": "定期复盘知识库学到了什么"
  },
  "cmd:rollback": {
    "label": "/rollback",
    "desc": "撤销上一次运行"
  },
  "cmd:schedule": {
    "label": "/schedule",
    "desc": "设置定时维护"
  },
  "cmd:schema": {
    "label": "/schema",
    "desc": "检查 frontmatter 是否符合结构规范"
  },
  "cmd:scope": {
    "label": "/scope",
    "desc": "将相关知识引入项目"
  },
  "cmd:secrets": {
    "label": "/secrets",
    "desc": "扫描凭据"
  },
  "cmd:sources": {
    "label": "/sources",
    "desc": "查看某条主张的依据"
  },
  "cmd:split": {
    "label": "/split",
    "desc": "拆分承载过多内容的页面"
  },
  "cmd:stale": {
    "label": "/stale",
    "desc": "查找长期无人维护的概念页"
  },
  "cmd:tags": {
    "label": "/tags",
    "desc": "审查标签词汇"
  },
  "cmd:timeline": {
    "label": "/timeline",
    "desc": "查看资料来源随时间如何发展"
  },
  "cmd:trace": {
    "label": "/trace",
    "desc": "显示答案使用了哪些页面"
  },
  "cmd:typed-links": {
    "label": "/typed-links",
    "desc": "在重要关系上添加链接类型"
  },
  "cmd:weekly": {
    "label": "/weekly",
    "desc": "周度复盘"
  },
  "agent:curator": {
    "label": "curator",
    "desc": "建议修剪、归档或合并哪些内容。只读，只提出建议，不执行操作。适合季度复盘，或知识库已超出用户能够掌握的规模时使用。"
  },
  "agent:graph-analyst": {
    "label": "graph-analyst",
    "desc": "分析链接图谱，报告指标、枢纽、桥接节点和聚类。只读。适合月度检查，或知识库变得难以导航时使用。"
  },
  "agent:ingestor": {
    "label": "ingestor",
    "desc": "将 raw/ 中的新资料处理为相互链接的 wiki 页面。存在待处理来源时使用。"
  },
  "agent:linker": {
    "label": "linker",
    "desc": "发现并补充现有 wiki 页面之间缺失的关联。适合批量导入后或按计划运行。"
  },
  "agent:researcher": {
    "label": "researcher",
    "desc": "根据知识库回答研究问题，并指出缺失的信息。适用于涉及多个页面的问题。"
  },
  "agent:reviewer": {
    "label": "reviewer",
    "desc": "定期复盘知识库学到了什么。适合每周运行，或在用户询问变化时使用。"
  },
  "script:chat_export_to_md.py": {
    "label": "chat_export_to_md.py",
    "desc": "将导出的聊天记录 JSON 转换为每个对话一个 Markdown 文件。"
  },
  "script:graph_export.py": {
    "label": "graph_export.py",
    "desc": "将知识库的 wiki 链接图谱导出为 CSV 边列表或 GraphML。"
  },
  "script:link_check.py": {
    "label": "link_check.py",
    "desc": "检查第二大脑知识库中的失效 wiki 链接、孤立页面和占位页。"
  },
  "script:vault_stats.py": {
    "label": "vault_stats.py",
    "desc": "输出第二大脑知识库的健康指标。"
  },
  "plug:context-audit": {
    "label": "context-audit",
    "desc": "按四个位置审查智能体的上下文布局：系统提示词、工具、历史记录和末尾。适用于检查或修复上下文、提示词缓存、每轮 token 开销，或 CLAUDE.md / AGENTS.md 布局。只读，仅报告发现和修复清单，不修改内容。不用于编写……"
  },
  "plug:evals-bootstrap": {
    "label": "evals-bootstrap",
    "desc": "为智能体搭建第一套评估：从真实失败中提取案例，编写轨迹行为检查，并生成运行器。适用于评估、回归测试、黄金集，以及确认提示词或模型变更没有破坏行为。不用于单个任务的完成检查……"
  },
  "plug:gate-check": {
    "label": "gate-check",
    "desc": "找出流程中无需昂贵模型处理的决策，为其建议规则、传统分类器或小模型，并采用失败时关闭的路由。适用于降低模型成本或延迟、解决所有任务都交给大模型的问题，或增加前置分流、路由与过滤层……"
  },
  "plug:goal-test": {
    "label": "goal-test",
    "desc": "将模糊任务转化为可测试的完成定义，并生成可执行的目标测试脚本；可选地，在无界面智能体外添加有次数上限的重试循环。适用于循环运行智能体、判断任务何时结束，或将“改进 X”之类的目标变为……"
  },
  "plug:harness-audit": {
    "label": "harness-audit",
    "desc": "按四层防线审查智能体运行框架：隔离、指南、传感器和权限。适用于检查配置是否安全、审查沙箱、权限、钩子与 AGENTS.md 防护，或评估一次糟糕运行可能破坏什么。只读，报告影响范围和加固建议……"
  },
  "plug:loop-critic": {
    "label": "loop-critic",
    "desc": "在全新上下文中审查智能体循环某一轮的结果：对照目标检查声称完成的工作，寻找投机捷径与未测试的路径，并给出包含具体缺陷的结论。在工作会话或循环尝试结束后、接受结果前使用。"
  }
});
