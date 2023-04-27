!(function (o, n) {
  "object" == typeof exports && "object" == typeof module
    ? (module.exports = n())
    : "function" == typeof define && define.amd
    ? define([], n)
    : "object" == typeof exports
    ? (exports.DocsifyPluginToc = n())
    : (o.DocsifyPluginToc = n());
})(this, () =>
  (() => {
    "use strict";
    var o = {};
    function n(o, n) {
      let e = ['<div class="page_toc">'];
      const t = [];
      return (
        (o = document.querySelectorAll(
          `#main ${window.$docsify.toc.target}`
        )) &&
          o.forEach(function (o) {
            const n = (function (o, n) {
              if (o >= 1 && o <= window.$docsify.toc.tocMaxLevel) {
                return ['<div class="lv' + o + '">', n, "</div>"].join("");
              }
              return "";
            })(o.tagName.replace(/h/gi, ""), o.innerHTML);
            n && t.push(n);
          }),
        t.length > 0 ? ((e = e.concat(t)), e.push("</div>"), e.join("")) : ""
      );
    }
    const e = () => {
      const o = window.innerHeight,
        n = document.querySelectorAll(`#main ${window.$docsify.toc.target}`);
      let e = [];
      n.forEach((n, t) => {
        const i = n.getBoundingClientRect();
        i.top <= o && i.height + i.top > 0 && e.push(t);
      });
      const t = document.scrollingElement || document.body;
      if (
        (0 === t.scrollTop
          ? (e = [0])
          : t.offsetHeight - window.innerHeight - t.scrollTop < 5 &&
            e.length > 0 &&
            (e = [e[0]]),
        e.length)
      ) {
        document.querySelectorAll(".page_toc>div").forEach((o, n) => {
          n === e[0] ? o.classList.add("active") : o.classList.remove("active");
        });
      }
    };
    return (
      window.$docsify || (window.$docsify = {}),
      (window.$docsify.plugins = (window.$docsify.plugins || []).concat(
        function (o, t) {
          o.mounted(function () {
            const o = window.Docsify.dom.find(".content");
            if (o) {
              const n = window.Docsify.dom.create("aside", "");
              window.Docsify.dom.toggleClass(n, "add", "toc-nav"),
                window.Docsify.dom.before(o, n);
            }
          }),
            o.doneEach(function () {
              const o = window.Docsify.dom.find(".toc-nav");
              o &&
                ((o.innerHTML = n().trim()),
                "" === o.innerHTML
                  ? (window.Docsify.dom.toggleClass(o, "add", "nothing"),
                    window.document.removeEventListener("scroll", e))
                  : (window.Docsify.dom.toggleClass(o, "remove", "nothing"),
                    e(),
                    window.document.addEventListener("scroll", e)));
            });
        }
      )),
      (o = o.default)
    );
  })()
);
