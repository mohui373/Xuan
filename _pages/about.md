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
        我主要关注人在社会规范、目标受挫与裁员情境中的行为与表现，研究社会线索、个体动机与认知评价如何共同塑造人的判断、态度与后续行为。
      </p>
      <ul class="tag-list hero-tags" aria-label="主要研究方向">
        <li>实验社会心理学</li>
        <li>组织与行为</li>
        <li>动机与目标追求</li>
        <li>道德行为</li>
      </ul>
      <div class="site-actions" aria-label="主要链接">
        <a class="site-action site-action-primary" href="{{ '/research/' | relative_url }}">了解我的研究</a>
        <a class="site-action" href="{{ '/cv/' | relative_url }}">查看简历</a>
      </div>
      <p class="site-profile-links">学术档案：<a href="https://orcid.org/0009-0004-9399-9489" target="_blank" rel="noopener noreferrer">ORCID</a><a href="https://github.com/mohui373" target="_blank" rel="noopener noreferrer">GitHub</a><a href="mailto:huimo7627@gmail.com">Email</a></p>
    </div>
    <figure class="profile-frame">
      <img src="{{ '/assets/img/profile-bole.jpg' | relative_url }}" alt="宣博乐学术头像" width="720" height="900">
      <figcaption>Bole Xuan · Basic Psychology</figcaption>
    </figure>
  </section>

  <section class="research-question-band" aria-labelledby="core-question">
    <p class="section-eyebrow">Core Question</p>
    <h2 id="core-question">当环境影响个体的目标追求时，人会如何重新理解处境，并调整自己的态度与行为？哪些潜在机制起到关键作用呢？</h2>
    <p>社会规范 × 目标承诺 × 行为与决策 × 实验心理学</p>
  </section>

  <section class="site-section" aria-labelledby="streams-title">
    <div class="section-heading">
      <div>
        <p class="section-eyebrow">Research at a Glance</p>
        <h2 id="streams-title">目前三项研究的主要方向</h2>
      </div>
      <a class="section-link" href="{{ '/research/' | relative_url }}">查看完整研究设计 →</a>
    </div>
    <div class="stream-list">
      {% for stream in site.data.research.streams %}
        <article class="stream-row">
          <p class="stream-index">{{ stream.number }}</p>
          <div class="stream-copy">
            <p class="stream-overline">{{ stream.english_title }}</p>
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
      <p class="section-eyebrow">Featured Open-Source Project</p>
      <h2 id="project-title">paper-to-paradigm</h2>
      <p class="project-lede">面向论文阅读、研究理解与实验重建的手术工具。</p>
      <p>
        它对论文进行解剖和仔细分解，将理论、变量、被试体验、研究流程、数据与分析重新连接起来，从被试角度复现论文所研究的内容。
      </p>
      <div class="site-actions">
        <a class="site-action site-action-primary" href="{{ '/projects/' | relative_url }}">了解项目</a>
        <a class="site-action" href="https://github.com/mohui373/paper-to-paradigm">GitHub Repository</a>
      </div>
    </div>
    <div class="project-skills" aria-label="核心 skills">
      <div>
        <span>01</span>
        <h3>paper-anatomy</h3>
        <p>Read & Audit：解剖理论与概念、变量、实验程序、被试体验与证据边界。</p>
      </div>
      <div>
        <span>02</span>
        <h3>paper-reconstruction</h3>
        <p>Reconstruct & Replicate：重建来源、详细程序、材料、数据结构与可复现流程。</p>
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
        <p class="section-eyebrow">Research Methods</p>
        <h2 id="methods-title">研究方法与工具</h2>
      </div>
    </div>
    <div class="method-columns">
      <div>
        <h3>Research Design</h3>
        <p>实验设计、问卷设计、访谈研究、扎根理论</p>
      </div>
      <div>
        <h3>Quantitative Methods</h3>
        <p>方差分析、回归分析、中介与调节分析、结构方程模型</p>
      </div>
      <div>
        <h3>Research Tools</h3>
        <p>R、SPSS、E-Prime、MATLAB、Mplus、AMOS、MAXQDA、NVivo</p>
      </div>
    </div>
  </section>
</main>
