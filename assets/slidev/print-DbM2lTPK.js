import{f as _,$ as u,y as f,o as i,e as r,g as e,t as a,F as h,Z as g,a0 as v,d as x,j as b}from"../modules/vue-pLxyOTZ-.js";import{u as N,j as y,c as m,b as k}from"../index-DIhmbxhQ.js";import{N as S}from"./NoteDisplay-BtmfLOpG.js";import"../modules/shiki-BnGJND2h.js";const D=_({__name:"print",setup(p,{expose:n}){n();const{slides:l,total:o}=N();u(`
@page {
  size: A4;
  margin-top: 1.5cm;
  margin-bottom: 1cm;
}
* {
  -webkit-print-color-adjust: exact;
}
html,
html body,
html #app,
html #page-root {
  height: auto;
  overflow: auto !important;
}
`),y({title:`Notes - ${m.title}`});const d=f(()=>l.value.map(t=>{var s;return(s=t.meta)==null?void 0:s.slide}).filter(t=>t!==void 0&&t.noteHTML!=="")),c={slides:l,total:o,slidesWithNote:d,get configs(){return m},NoteDisplay:S};return Object.defineProperty(c,"__isScriptSetup",{enumerable:!1,value:!0}),c}}),j={id:"page-root"},w={class:"m-4"},L={class:"mb-10"},T={class:"text-4xl font-bold mt-2"},V={class:"opacity-50"},B={class:"text-lg"},C={class:"font-bold flex gap-2"},H={class:"opacity-50"},W={key:0,class:"border-main mb-8"};function z(p,n,l,o,d,c){return i(),r("div",j,[e("div",w,[e("div",L,[e("h1",T,a(o.configs.title),1),e("div",V,a(new Date().toLocaleString()),1)]),(i(!0),r(h,null,g(o.slidesWithNote,(t,s)=>(i(),r("div",{key:s,class:"flex flex-col gap-4 break-inside-avoid-page"},[e("div",null,[e("h2",B,[e("div",C,[e("div",H,a(t==null?void 0:t.no)+"/"+a(o.total),1),v(" "+a(t==null?void 0:t.title)+" ",1),n[0]||(n[0]=e("div",{class:"flex-auto"},null,-1))])]),x(o.NoteDisplay,{"note-html":t.noteHTML,class:"max-w-full"},null,8,["note-html"])]),s<o.slidesWithNote.length-1?(i(),r("hr",W)):b("v-if",!0)]))),128))])])}const O=k(D,[["render",z],["__file","C:/Users/Somto/Documents/mcda-dataviz-tutorial/slides/node_modules/@slidev/client/pages/presenter/print.vue"]]);export{O as default};
