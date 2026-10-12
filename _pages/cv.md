---
layout: default
permalink: /cv/
title: 简历
nav: true
nav_order: 4
description: 宣博乐的教育、实践经历、科研项目、论文、学术交流与荣誉。
---

{% assign cv = site.data.cv.cv %}
{% assign sections = cv.sections %}

<main class="editorial-page cv-editorial">
  <header class="page-intro"><h1>简历</h1><p>{{ cv.name }} · {{ cv.label }}</p></header>
  <nav class="english-section-nav" aria-label="简历栏目索引">
    <a href="#education">教育背景</a><a href="#experience">实践经历</a><a href="#projects">科研项目</a><a href="#presentations">学术交流</a><a href="#publications">论文与手稿</a><a href="#awards">荣誉与奖励</a>
  </nav>

  <section id="contact" class="english-cv-section">
    <h2>联系信息</h2>
    <p>邮箱：<a href="mailto:{{ cv.email }}">{{ cv.email }}</a></p>
    <p><a href="https://orcid.org/0009-0004-9399-9489" target="_blank" rel="noopener noreferrer">ORCID</a> · <a href="https://github.com/mohui373" target="_blank" rel="noopener noreferrer">GitHub</a></p>
  </section>

  <section id="education" class="english-cv-section">
    <h2>教育背景</h2>
    <div class="english-entry-list">
      {% for entry in sections.Education %}
        <article class="english-entry">
          <p class="english-entry-date">{{ entry.start_date }}—{{ entry.end_date }}</p>
          <div><h3>{{ entry.area }} · {{ entry.studyType }}</h3><p class="english-entry-meta">{{ entry.institution }}</p><ul class="clean-list">{% for item in entry.highlights %}<li>{{ item }}</li>{% endfor %}</ul></div>
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="experience" class="english-cv-section">
    <h2>实践经历</h2>
    <div class="english-entry-list">
      {% for entry in sections.Experience %}
        <article class="english-entry">
          <p class="english-entry-date">{% if entry.date %}{{ entry.date }}{% else %}{{ entry.start_date }}—{{ entry.end_date }}{% endif %}</p>
          <div><h3>{{ entry.position }}</h3><p class="english-entry-meta">{{ entry.company }}</p><p>{{ entry.summary }}</p>{% if entry.highlights %}<ul class="clean-list">{% for item in entry.highlights %}<li>{{ item }}</li>{% endfor %}</ul>{% endif %}</div>
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="projects" class="english-cv-section">
    <h2>科研项目</h2>
    <div class="english-entry-list">
      {% for entry in sections.Projects %}
        <article class="english-entry">
          <p class="english-entry-date">{{ entry.start_date }}—{{ entry.end_date }}</p>
          <div><h3>{{ entry.name }}</h3><p class="english-entry-meta">{{ entry.position }}</p><p>{{ entry.summary }}</p></div>
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="presentations" class="english-cv-section">
    <h2>学术交流</h2>
    <div class="english-entry-list">
      {% for entry in sections["Academic Presentations"] %}
        <article class="english-entry">
          <p class="english-entry-date">{{ entry.date }}</p>
          <div><h3>{{ entry.title }}</h3><p class="english-entry-meta">{{ entry.format }}</p></div>
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="publications" class="english-cv-section">
    <h2>论文与手稿</h2>
    <div class="english-entry-list compact-list">
      {% for entry in sections.Publications %}
        <article class="english-entry">
          <p class="english-entry-date">{{ entry.releaseDate }}</p>
          <div><h3>{{ entry.title }}</h3>{% if entry.publisher %}<p class="english-entry-meta">{{ entry.publisher }}</p>{% endif %}</div>
        </article>
      {% endfor %}
    </div>
  </section>

  <section id="skills" class="english-cv-section">
    <h2>研究方法与技能</h2>
    <div class="method-columns">{% for entry in sections.Skills %}<div><h3>{{ entry.name }}</h3><p>{{ entry.keywords }}</p></div>{% endfor %}</div>
  </section>

  <section id="open-source-projects" class="english-cv-section">
    <h2>开源项目</h2>
    {% for entry in sections["Open Source Projects"] %}
      <article class="english-simple-entry"><h3>{{ entry.name }}</h3><p>{{ entry.summary }}</p><ul class="clean-list">{% for item in entry.highlights %}<li>{% if item contains 'https://' %}<a href="{{ item }}" target="_blank" rel="noopener noreferrer">查看 GitHub</a>{% else %}{{ item }}{% endif %}</li>{% endfor %}</ul></article>
    {% endfor %}
  </section>

  <section id="awards" class="english-cv-section">
    <h2>荣誉与奖励</h2>
    <div class="english-honors-grid">{% for entry in sections.Awards %}<article><span>{{ entry.date }}</span><p>{{ entry.title }}{% if entry.awarder != '' %}<br><small>{{ entry.awarder }}</small>{% endif %}</p></article>{% endfor %}</div>
  </section>

  <section id="languages" class="english-cv-section">
    <h2>语言能力</h2>
    <div class="english-language-list">{% for entry in sections.Languages %}<p><strong>{{ entry.name }}：</strong>{{ entry.summary }}</p>{% endfor %}</div>
  </section>
</main>
