# UPGRADE_PLAN.md

## 未来升级计划

### 1. Shadow DOM 隔离版组件
- 将放大缩放交互封装为 Web Component，内部用 Shadow DOM 实现样式与事件100%隔离。
- 彻底杜绝外部容器、全局CSS/JS对组件行为的影响。
- 兼容所有现代浏览器和主流WebView。

### 2. 桌面端/移动端适配
- Electron、Tauri、QtWebEngine等桌面Web容器适配，保证交互体验一致。
- 移动端主流浏览器、混合App（如Cordova、Capacitor、uni-app等）兼容性适配。
- 老旧WebView自动降级为class隔离方案。

### 3. iframe沙箱与CSP安全增强
- 支持将组件运行在iframe沙箱中，进一步提升安全隔离级别。
- 配置严格的CSP策略，防止XSS、脚本注入等安全风险。

### 4. 多端统一与自动检测
- 自动检测运行环境，选择最佳隔离与兼容方案。
- 维护一套核心组件代码，多端复用，降低维护成本。

---

> 以上升级计划将在下一个大版本逐步实现，具体进度和路线详见项目主页与CHANGELOG。 