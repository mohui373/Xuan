---
layout: default
title: 首页
permalink: /
description: 宣博乐的个人学术主页：社会规范、目标受挫、组织与行为、道德行为及 AI 与员工行为。
---

<main class="site-home">
  <section class="site-hero" aria-labelledby="home-title">
    <div class="site-hero-copy">
      <p class="site-kicker">实验社会心理学 · 组织与行为</p>
      <h1 id="home-title">宣博乐</h1>
      <p class="site-role">基础心理学硕士研究生｜闽南师范大学</p>
      <p class="site-lede">
        本人研究人在目标受挫、面对社会规范或经历组织裁员时，如何判断处境并作出回应。研究侧重社会线索、个体动机与认知评价对态度和行为的影响。
      </p>
      <ul class="tag-list hero-tags" aria-label="主要研究方向">
        <li>实验社会心理学</li>
        <li>组织与行为</li>
        <li>动机与目标追求</li>
        <li>道德行为</li>
      </ul>
      <div class="site-actions" aria-label="主要链接">
        <a class="site-action site-action-primary" href="{{ '/research/' | relative_url }}">了解研究方向</a>
        <a class="site-action" href="{{ '/cv/' | relative_url }}">查看简历</a>
      </div>
      <p class="site-profile-links">学术档案：<a href="https://orcid.org/0009-0004-9399-9489" target="_blank" rel="noopener noreferrer">ORCID</a><a href="https://github.com/mohui373" target="_blank" rel="noopener noreferrer">GitHub</a><a href="mailto:huimo7627@gmail.com">Email</a></p>
    </div>
    <figure class="profile-frame">
      <img src="{{ '/assets/img/profile-bole.webp' | relative_url }}" alt="宣博乐学术头像" width="720" height="720" fetchpriority="high" decoding="async">
      <figcaption>Bole Xuan · 基础心理学</figcaption>
    </figure>
  </section>

  <section class="research-question-band" aria-labelledby="core-question">
    <p class="section-eyebrow">贯穿研究的问题</p>
    <h2 id="core-question">当环境改变了追求目标的方式，人会如何理解处境、调整行动？</h2>
    <p>从调剂后的目标投入，到道德提醒下的规则遵从，再到 AI 裁员后的员工反应。</p>
  </section>

  <section class="site-section" aria-labelledby="streams-title">
    <div class="section-heading">
      <div>
        <p class="section-eyebrow">Research at a Glance</p>
        <h2 id="streams-title">当前研究</h2>
      </div>
      <a class="section-link" href="{{ '/research/' | relative_url }}">研究设计与进展 →</a>
    </div>
    <div class="stream-list">
      {% for stream in site.data.research.streams %}
        <article class="stream-row">
          <p class="stream-index">{{ stream.number }}</p>
          <div class="stream-copy">
            <h3>{{ stream.title }}</h3>
            <p>{{ stream.question }}</p>
          </div>
          <span class="status status-{{ stream.status_key }}">{{ stream.status }}</span>
        </article>
      {% endfor %}
    </div>
  </section>

  <section class="site-section project-feature" aria-labelledby="project-title">
    <div class="project-feature-copy">
      <p class="section-eyebrow">开放研究工具</p>
      <h2 id="project-title">paper-to-paradigm</h2>
      <p class="project-lede">面向论文阅读、研究理解与实验重建的研究工具箱。</p>
      <p>
        从被试会经历什么出发，梳理论文的理论、变量与实验流程，再核对材料、数据和分析之间的关系，为重建研究提供依据。
      </p>
      <div class="site-actions">
        <a class="site-action site-action-primary" href="{{ '/projects/' | relative_url }}">了解项目</a>
        <a class="site-action" href="https://github.com/mohui373/paper-to-paradigm">查看 GitHub</a>
      </div>
    </div>
    <div class="project-skills" aria-label="核心 skills">
      <div>
        <span>01</span>
        <h3>paper-anatomy</h3>
        <p>阅读与核查：梳理理论、变量、实验程序和被试体验，辨明证据边界。</p>
      </div>
      <div>
        <span>02</span>
        <h3>paper-reconstruction</h3>
        <p>实验重建：追溯来源，整理程序、材料与数据结构，形成可复现流程。</p>
      </div>
    </div>
  </section>

  <section class="site-section" aria-labelledby="publications-title">
    <div class="section-heading">
      <div>
        <p class="section-eyebrow">Selected Publications</p>
        <h2 id="publications-title">论文与手稿</h2>
      </div>
      <a class="section-link" href="{{ '/publications/' | relative_url }}">查看完整列表 →</a>
    </div>
    <div class="publications publication-strip">
      {% bibliography --query @*[selected=true] %}
    </div>
  </section>

  <section class="site-section" aria-labelledby="methods-title">
    <div class="section-heading">
      <div>
        <h2 id="methods-title">研究方法与工具</h2>
      </div>
    </div>
    <div class="method-columns">
      <div>
        <h3>研究设计</h3>
        <p>实验设计、问卷设计、访谈研究、扎根理论</p>
      </div>
      <div>
        <h3>定量方法</h3>
        <p>方差分析、回归分析、中介与调节分析、结构方程模型</p>
      </div>
      <div>
        <h3>研究工具</h3>
        <p>R、SPSS、E-Prime、MATLAB、Mplus、AMOS、MAXQDA、NVivo、Excel</p>
      </div>
    </div>
  </section>
</main>
