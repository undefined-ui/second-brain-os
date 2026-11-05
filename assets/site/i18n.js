// Shared UI language support. English source strings are the fallback keys.
// This script is independent of the graph/CDN so navigation remains usable.
(function () {
  'use strict';
  const storageKey = 'sbos:language';
  const supported = ['en', 'zh-CN'];
  const messages = { 'zh-CN': {
    'Switch to Chinese': '切换为中文',
    'Switch to English': 'Switch to English',
    'Second Brain OS - guides and resources for AI engineers': 'Second Brain OS - AI 工程师的指南与资源',
    'Guides and resources for AI engineers': 'AI 工程师的指南与资源',
    'the whole site, as one graph': '用一张图谱探索整个网站',
    'A course on building agents from a single prompt to production, five handbooks that go deep on one layer each, a hands-on second-brain project, and the links worth your time. Free, plain markdown.': '从一句提示词到生产环境的智能体开发课程、深入各个层面的五本手册、第二大脑实战项目，以及值得阅读的精选资源。免费开放，以 Markdown 编写。',
    'Every page, term and tool on this site is a bubble. The lines are the real links between them. Click one to see what it leans on.': '每个气泡代表一篇文章、一个术语或一项工具，连线对应它们之间的实际关联。点击气泡，探索相关内容。',
    'Back to the whole map': '返回完整图谱',
    'Contents': '目录',
    'search pages, terms, tools': '搜索文章、术语和工具',
    'Search the site': '搜索全站',
    'Switch between light and dark theme': '切换浅色或深色主题',
    'Resources': '资源', 'Tree': '组件树', 'Repo': '代码仓库', 'Map': '图谱',
    'drag': '拖动', 'orbit': '旋转', 'scroll': '滚动', 'zoom': '缩放',
    'click': '点击', 'open': '打开', 'back': '返回', 'made by': '作者',
    'Selected item': '所选项目', 'Reader': '阅读器',
    'Back to the graph (Esc)': '返回图谱（Esc）', 'graph': '图谱',
    'Close (Esc)': '关闭（Esc）', 'Close the reader': '关闭阅读器',
    'Show or hide layers': '显示或隐藏图层',
    'Pause the rotation': '暂停旋转', 'Resume the rotation': '继续旋转',
    'Whole map': '完整图谱', 'drawing the map…': '正在绘制图谱…',
    'Course': '课程', 'Handbooks': '专题手册', 'Second brain': '第二大脑',
    'Glossary': '术语表', 'Toolkit': '工具箱',
    'home': '首页', 'collection': '合集', 'section': '章节', 'page': '文章',
    'term': '术语', 'group': '分组', 'skill': '技能', 'command': '命令',
    'subagent': '子智能体', 'script': '脚本', 'resource': '资源',
    '+ {count} more': '+ 另外 {count} 项',
    '{count} words': '{count} 个英文词', '{count} pages': '{count} 篇文章',
    'words': '英文词', 'pages': '文章', 'terms': '术语', 'tools': '工具',
    'connections': '关联', 'sections': '章节', 'min': '分钟',
    '{count}m': '{count} 分钟',
    'links out': '个出站链接', 'linked from': '个入站链接',
    'Read the page': '阅读文章', 'Source': '源文件',
    'On this page': '本文目录', 'Links to': '链接至', 'Linked from': '被以下内容引用',
    'Terms on this page': '本文术语', 'Toolkit and sources': '工具与来源',
    'previous': '上一篇', 'next': '下一篇', 'Start reading': '开始阅读',
    'Pages': '文章', 'The module it deepens': '对应课程模块', 'Its handbook': '配套手册',
    'Leans on': '参考章节', 'Leaned on by': '引用本章的章节', 'Sections': '章节',
    'Start at the beginning': '从头开始', 'Terms, by reach': '按覆盖范围排列的术语',
    'Inside': '包含内容', 'glossary': '术语表',
    'on {count} pages': '出现于 {count} 篇文章', 'mentions': '次提及',
    'Read where it is defined': '阅读术语定义', 'Leans on it hardest': '主要相关文章',
    'Often alongside': '常见相关术语', 'Open {host}': '访问 {host}',
    'Cited in': '引用文章', 'Related terms': '相关术语',
    'resources': '资源', 'toolkit': '工具箱', 'tools:': '工具：',
    'ingestion': '资料导入', 'structuring': '组织结构', 'retrieval': '检索',
    'maintenance': '维护', 'outputs': '知识输出', 'projects': '项目',
    'safety': '安全', 'setup': '搭建', 'plugin': '插件',
    'View on GitHub': '在 GitHub 上查看', 'Follows the skill': '调用的技能',
    'Called by': '由以下命令调用', 'Mentioned in': '提及文章',
    'page {position} of {count}': '第 {position} 篇，共 {count} 篇',
    'This page did not load. Try reloading.': '文章加载失败，请刷新重试。',
    'terms on this page': '本文术语', 'source:': '源文件：',
    'This article is available in English.': '本文正文暂为英文。',
    'The agents course': '智能体开发课程',
    'Seven modules from a single prompt to a production agent.': '七个模块，从一句提示词到可用于生产的智能体。',
    'One layer at a time, each ending in a build you can finish in an evening.': '逐层深入，每本手册都以一个可在一晚完成的实践项目收尾。',
    'A hands-on project: a knowledge base an agent builds and maintains for you.': '动手实践：让智能体为你构建和维护知识库。',
    'Show or hide: {layer}': '显示或隐藏：{layer}',
    'the agents course': '智能体开发课程', 'handbooks': '专题手册', 'second brain': '第二大脑',
    'nothing on the site matches that': '未找到匹配内容',
    'Light theme': '浅色主题', 'Dark theme': '深色主题',
    'The 3D map needs WebGL, which is not available here.': '三维图谱需要 WebGL，当前环境暂不支持。',
    'Read the guide on GitHub': '在 GitHub 上阅读指南',
  } };
  let saved;
  try { saved = JSON.parse(localStorage.getItem(storageKey)); } catch { /* Storage may be disabled. */ }
  const preferred = (navigator.languages && navigator.languages[0]) || navigator.language || 'en';
  let locale = supported.includes(saved) ? saved : /^zh(?:-|$)/i.test(preferred) ? 'zh-CN' : 'en';
  const originalLabels = new WeakMap();

  function t(source, params = {}, language = locale) {
    const catalog = messages[language];
    const value = catalog && Object.prototype.hasOwnProperty.call(catalog, source) ? catalog[source] : source;
    return String(value).replace(/\{(\w+)\}/g, (match, key) => Object.prototype.hasOwnProperty.call(params, key) ? String(params[key]) : match);
  }
  function register(language, catalog) {
    if (supported.includes(language)) Object.assign(messages[language] || (messages[language] = {}), catalog);
  }
  function translate(root = document) {
    const attributes = ['title', 'placeholder', 'aria-label', 'content'];
    const selector = ['[data-i18n]', '[data-language-toggle]', '[data-node-label]', '[data-node-description]', ...attributes.map(a => `[data-i18n-${a}]`)].join(',');
    const elements = [...root.querySelectorAll(selector)];
    if (root.matches && root.matches(selector)) elements.unshift(root);
    for (const el of elements) {
      let params = {};
      try { params = JSON.parse(el.getAttribute('data-i18n-params') || '{}') || {}; } catch { /* Ignore malformed optional parameters. */ }
      if (el.hasAttribute('data-i18n')) el.textContent = t(el.getAttribute('data-i18n'), params);
      for (const attr of attributes) {
        const key = el.getAttribute('data-i18n-' + attr);
        if (key !== null) el.setAttribute(attr, t(key, params));
      }
      if (el.hasAttribute('data-node-label') || el.hasAttribute('data-node-description')) {
        if (!originalLabels.has(el)) originalLabels.set(el, el.textContent);
        const field = el.hasAttribute('data-node-description') ? 'desc' : 'label';
        const id = el.getAttribute(field === 'desc' ? 'data-node-description' : 'data-node-label');
        const translated = window.SBOS_NODE_ZH?.[id]?.[field];
        el.textContent = locale === 'zh-CN' && translated ? translated : originalLabels.get(el);
      }
      if (el.hasAttribute('data-language-toggle')) {
        el.textContent = locale === 'en' ? '中文' : 'English';
        el.setAttribute('lang', locale === 'en' ? 'zh-CN' : 'en');
        const label = t(locale === 'en' ? 'Switch to Chinese' : 'Switch to English');
        el.setAttribute('aria-label', label);
        el.setAttribute('title', label);
      }
    }
    document.documentElement.lang = locale;
  }
  function setLocale(next) {
    if (!supported.includes(next) || next === locale) return;
    locale = next;
    try { localStorage.setItem(storageKey, JSON.stringify(locale)); } catch { /* Keep the in-memory preference. */ }
    translate();
    window.dispatchEvent(new CustomEvent('sbos:languagechange', { detail: { locale } }));
  }
  window.SBOS_I18N = { t, register, translate, setLocale, get locale() { return locale; } };
  document.documentElement.lang = locale;
  document.addEventListener('click', event => {
    if (event.target.closest('[data-language-toggle]')) setLocale(locale === 'en' ? 'zh-CN' : 'en');
  });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', () => translate());
  else translate();
}());
