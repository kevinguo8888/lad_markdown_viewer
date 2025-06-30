# TECH_LIMITS_AND_SECURITY.md

## 技术限制

- 组件当前未采用 Shadow DOM，样式与事件已最大限度隔离，但极端情况下仍可能被外部全局CSS/JS影响。
- 未来版本将支持 Shadow DOM，进一步提升隔离性。
- 依赖前端 mermaid.js、github-markdown-css，需保证CDN可用。
- 兼容性依赖于现代浏览器/主流WebView，老旧环境可能降级为class隔离方案。

## 安全风险

- 全局JS仍可通过 DOM API 操作组件内部结构，未来Shadow DOM可缓解但无法100%杜绝。
- 外部脚本可通过 window.onMarkdownLinkClick 等接口与组件通信，需校验来源和参数。
- 依赖的第三方库（如mermaid.js）如被污染或篡改，可能带来XSS等安全风险。
- 建议生产环境配置严格的 CSP（内容安全策略），禁止外部脚本注入和跨域资源。
- Markdown内容如含有恶意代码，建议后端做安全过滤。

## 安全建议

- 仅信任官方CDN和已审查的第三方依赖。
- 配置 CSP，限制脚本、样式、img等资源来源。
- 对用户输入的Markdown内容做XSS过滤。
- 未来版本将支持iframe沙箱和多重隔离。

---

如有更高安全需求，建议结合Shadow DOM、iframe、CSP等多重隔离手段。 