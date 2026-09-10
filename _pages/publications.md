---
layout: page
permalink: /publications/
title: 论文
description: 宣博乐的论文、在审手稿与准备中研究。
nav: true
nav_order: 2
---

<div class="editorial-page publications-page">
  <header class="page-intro">
    <p class="section-eyebrow">Publications & Manuscripts</p>
    <p>论文与手稿按当前状态列出，相关开放材料见条目下方链接。</p>
  </header>

  <section class="publication-group" aria-labelledby="under-review-title">
    <div class="section-heading compact">
      <h2 id="under-review-title">审稿中</h2>
    </div>
    <div class="publications">{% bibliography --query @*[status=under_review] %}</div>
    <p class="publication-resource">说服研究的预注册与材料：<a href="https://osf.io/uke2j" target="_blank" rel="noopener noreferrer">在 OSF 查看</a></p>
  </section>

  <section class="publication-group" aria-labelledby="preparation-title">
    <div class="section-heading compact">
      <h2 id="preparation-title">准备中</h2>
    </div>
    <div class="publications">{% bibliography --query @*[status=in_preparation] %}</div>
  </section>

  <section class="publication-group" aria-labelledby="published-title">
    <div class="section-heading compact">
      <h2 id="published-title">已发表成果</h2>
    </div>
    <div class="publications">{% bibliography --query @*[status=published] %}</div>
  </section>
</div>
