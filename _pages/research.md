---
layout: default
title: 研究
permalink: /research/
description: 宣博乐的研究方向、研究设计与研究进展。
nav: true
nav_order: 1
---

<link rel="stylesheet" href="{{ '/assets/css/research-motion.css' | relative_url }}">
<script defer src="{{ '/assets/js/research-motion.js' | relative_url }}"></script>

<main class="editorial-page research-page research-motion">
  <header class="page-intro wide">
    <svg class="research-compass" viewBox="0 0 100 100" fill="none" aria-hidden="true" focusable="false">
      <circle cx="50" cy="50" r="40" /><circle cx="50" cy="50" r="29" stroke-dasharray="2 6" />
      <path d="M50 3v14M50 83v14M3 50h14M83 50h14M20 20l9 9M71 71l9 9M20 80l9-9M71 29l9-9" />
      <path class="compass-needle" d="m50 23 8 27-8 27-8-27 8-27Zm-27 27h54" />
      <circle cx="50" cy="50" r="3" />
    </svg>
    <p class="section-eyebrow">Research</p>
    <h1>当环境改变了追求目标的方式，人会如何理解处境、调整行动？</h1>
    <p>
      这些研究关注人在面对社会规范、目标受挫、受限选择或组织变革时，动机与认知评价如何影响判断、态度和后续行为。
    </p>
  </header>

  <nav class="research-index" aria-label="研究方向索引">
    {% for stream in site.data.research.streams %}
      <a href="#{{ stream.slug }}"><span>{{ stream.number }}</span>{{ stream.title }}</a>
    {% endfor %}
  </nav>

{% for stream in site.data.research.streams %}

<article id="{{ stream.slug }}" class="research-detail">
<header class="research-detail-header">
<div>
<p class="stream-overline">{{ stream.number }} · {{ stream.english_title }}</p>
<h2>{{ stream.title }}</h2>
</div>
<span class="status status-{{ stream.status_key }}">{{ stream.status }}</span>
</header>
{% if stream.study_title %}<h3>{{ stream.study_title }}</h3>{% endif %}
<h3>核心问题</h3>
<p class="research-question">{{ stream.question }}</p>
<p>{{ stream.summary }}</p>

      <div class="research-detail-grid">
        <div>
          <h3>研究设计</h3>
          <ul class="clean-list">
            {% for item in stream.design %}<li>{{ item }}</li>{% endfor %}
          </ul>
        </div>
        <div>
          <h3>{% if stream.status_key == 'ongoing' %}概念路径（持续更新）{% else %}研究逻辑{% endif %}</h3>
          <ol class="diagram-flow {% if stream.status_key == 'ongoing' %}diagram-conceptual{% endif %}">
            {% for item in stream.diagram %}<li>{{ item }}</li>{% endfor %}
          </ol>
        </div>
      </div>
      {% if stream.findings %}
        <section aria-labelledby="{{ stream.slug }}-findings">
          <h3 id="{{ stream.slug }}-findings">主要发现</h3>
          <ul class="clean-list">
            {% for finding in stream.findings %}<li>{{ finding }}</li>{% endfor %}
          </ul>
        </section>
      {% endif %}
      {% if stream.limitations %}<h3>研究边界</h3><p class="research-note">{{ stream.limitations }}</p>{% endif %}
      <h3>当前状态</h3>
      <p class="research-note">{{ stream.note }}</p>
      {% if stream.osf_url %}
        <p class="research-resource"><a href="{{ stream.osf_url }}" target="_blank" rel="noopener noreferrer">{{ stream.osf_label }}</a></p>
      {% endif %}
    </article>

{% endfor %}

</main>
