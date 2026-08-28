---
layout: default
title: 研究
permalink: /research/
description: 宣博乐的研究方向、研究设计与研究进展。
nav: true
nav_order: 1
---

<main class="editorial-page research-page">
  <header class="page-intro wide">
    <p class="section-eyebrow">Research</p>
    <h1>人在选择空间改变后，如何重新理解环境并调整行为？</h1>
    <p>
      我的研究关注人在规范、受挫、受限选择和组织变革情境中，如何通过动机与认知过程调整后续判断、态度与行为。
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
<p class="research-question">{{ stream.question }}</p>
<p>{{ stream.summary }}</p>

      <div class="research-detail-grid">
        <div>
          <h3>研究设计与当前关注</h3>
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
      <p class="research-note">{{ stream.note }}</p>
      {% if stream.osf_url %}
        <p class="research-resource"><a href="{{ stream.osf_url }}" target="_blank" rel="noopener noreferrer">{{ stream.osf_label }}</a></p>
      {% endif %}
    </article>

{% endfor %}

</main>
