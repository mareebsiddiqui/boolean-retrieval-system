(this.webpackJsonpgui=this.webpackJsonpgui||[]).push([[0],{10:function(e,t,c){},11:function(e,t,c){},13:function(e,t,c){"use strict";c.r(t);var n=c(1),s=c.n(n),o=c(5),a=c.n(o),i=(c(10),c(2)),l=(c(11),c(4)),r=c.n(l),j=c(0);var h=function(){var e=Object(n.useState)(),t=Object(i.a)(e,2),c=t[0],s=t[1],o=Object(n.useState)([]),a=Object(i.a)(o,2),l=a[0],h=a[1],u=Object(n.useState)([]),d=Object(i.a)(u,2),b=d[0],f=d[1],O=Object(n.useState)(!1),p=Object(i.a)(O,2),x=p[0],g=p[1],m=Object(n.useState)(),v=Object(i.a)(m,2),N=v[0],y=v[1],_=Object(n.useState)({}),S=Object(i.a)(_,2),w=S[0],C=S[1];function F(e){if(e){var t=e.replace(/([A-Z])/g,"$1");return t.charAt(0).toUpperCase()+t.slice(1)}}return Object(n.useEffect)((function(){N&&fetch("http://localhost:5000/document?doc_id="+N).then((function(e){return e.json()})).then((function(e){console.log(e),C(e)})).catch((function(e){console.log(e)}))}),[N]),Object(j.jsx)("div",{className:"App",children:Object(j.jsxs)("header",{className:"App-header",children:[Object(j.jsx)("h1",{class:"display-4",children:"Short Stories"}),!x&&Object(j.jsxs)("div",{className:"col-lg-8 content",children:[Object(j.jsxs)("div",{className:"form-floating mb-3",children:[Object(j.jsx)("input",{type:"text",className:"form-control",id:"floatingInput",onKeyDown:function(e){"Enter"===e.key&&fetch("http://localhost:5000/query?query="+c).then((function(e){return e.json()})).then((function(e){h(e.results),f(e.search_words)})).catch((function(e){console.log(e)}))},onChange:function(e){return s(e.target.value)},autoFocus:!0}),Object(j.jsx)("label",{style:{color:"#282c34"},htmlFor:"floatingInput",children:"query + enter"})]}),l.length>0?l.map((function(e,t){return Object(j.jsxs)("div",{className:"result mb-4",children:[Object(j.jsxs)("p",{className:"lead text-white",href:"#",children:[e.doc_id,".",Object(j.jsx)("a",{href:"#",className:"text-white",onClick:function(t){t.preventDefault(),g(!0),y(e.doc_id)},children:F(e.doc_name)})]}),e.doc_snippet&&Object(j.jsx)("span",{className:"snippet text-white",children:Object(j.jsx)(r.a,{searchWords:b,textToHighlight:"...".concat(e.doc_snippet,"...")})})]})})):Object(j.jsx)("p",{className:"text-white",children:"No results."})]}),x&&w.doc_name&&Object(j.jsxs)(j.Fragment,{children:[Object(j.jsx)("a",{className:"text-white",href:"#",onClick:function(e){e.preventDefault(),g(!1),C({doc_name:"",doc:""})},children:"Back"}),Object(j.jsx)("h3",{children:w.doc_name}),Object(j.jsx)("div",{className:"col-lg-10 content",children:Object(j.jsx)("p",{style:{textAlign:"justify"},children:Object(j.jsx)(r.a,{searchWords:b,textToHighlight:"".concat(w.doc)})})})]}),x&&!w.doc_name&&Object(j.jsx)("p",{children:"Loading.."})]})})},u=function(e){e&&e instanceof Function&&c.e(3).then(c.bind(null,14)).then((function(t){var c=t.getCLS,n=t.getFID,s=t.getFCP,o=t.getLCP,a=t.getTTFB;c(e),n(e),s(e),o(e),a(e)}))};a.a.render(Object(j.jsx)(s.a.StrictMode,{children:Object(j.jsx)(h,{})}),document.getElementById("root")),u()}},[[13,1,2]]]);
//# sourceMappingURL=main.66fe126c.chunk.js.map