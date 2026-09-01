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
    <p>按研究状态分类展示。未确认的 DOI、期刊、预印本与公开材料链接不会显示。</p>
  </header>

  <section class="publication-group" aria-labelledby="under-review-title">
    <div class="section-heading compact">
      <h2 id="under-review-title">Manuscripts Under Review</h2>
    </div>
    <div class="publications">{% bibliography --query @*[status=under_review] %}</div>
    <p class="publication-resource">该研究的公开预注册与材料：<a href="https://osf.io/uke2j" target="_blank" rel="noopener noreferrer">在 OSF 查看</a></p>
  </section>

  <section class="publication-group" aria-labelledby="preparation-title">
    <div class="section-heading compact">
      <h2 id="preparation-title">Manuscripts in Preparation</h2>
    </div>
    <div class="publications">{% bibliography --query @*[status=in_preparation] %}</div>
  </section>

  <section class="publication-group" aria-labelledby="published-title">
    <div class="section-heading compact">
      <h2 id="published-title">Peer-Reviewed Publications</h2>
    </div>
    <div class="publications">{% bibliography --query @*[status=published] %}</div>
  </section>
</div>
