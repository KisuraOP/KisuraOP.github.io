/*
 * Vercount 兼容跳板
 * Fluid 主题会加载 {static_prefix.busuanzi}/busuanzi.pure.mini.js，
 * 这里动态注入 Vercount 的计数脚本；Vercount 会填充页面里
 * #busuanzi_container_page_pv / #busuanzi_value_page_pv 等节点。
 * 项目：https://github.com/EvanNotFound/vercount
 */
(function () {
  var script = document.createElement('script');
  script.src = 'https://events.vercount.one/js';
  script.defer = true;
  document.head.appendChild(script);
})();
