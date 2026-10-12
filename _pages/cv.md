---
layout: page
permalink: /cv/
title: 简历
nav: true
nav_order: 4
description: 宣博乐的教育、实践经历、科研项目、论文、学术交流与荣誉。
toc:
  sidebar: left
---

{% assign cv = site.data.cv.cv %}
{% assign sections = cv.sections %}

<div class="cv">
  <a class="anchor" id="contact-information"></a>
  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">联系信息</h3>
    <div class="card-text font-weight-light">
      <table class="table table-cv table-sm table-borderless"><tbody>
        <tr><td><b>姓名</b></td><td>{{ cv.name }}</td></tr>
        <tr><td><b>学术身份</b></td><td>{{ cv.label }}</td></tr>
        <tr><td><b>邮箱</b></td><td><a href="mailto:{{ cv.email }}">{{ cv.email }}</a></td></tr>
      </tbody></table>
    </div>
  </div>

<a class="anchor" id="education"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">教育背景</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">
      {% for entry in sections.Education %}
        <li class="list-group-item"><div class="row">
          <div class="col-sm-2 text-center"><span class="badge font-weight-bold danger-color-dark text-uppercase align-middle">{{ entry.start_date }}<br>{{ entry.end_date }}</span></div>
          <div class="col-sm-10 mt-2 mt-sm-0"><h6 class="title font-weight-bold ml-1 ml-md-4">{{ entry.institution }}</h6><p class="ml-1 ml-md-4">{{ entry.area }} · {{ entry.studyType }}</p><ul class="items">{% for item in entry.highlights %}<li>{{ item }}</li>{% endfor %}</ul></div>
        </div></li>
      {% endfor %}
    </ul>
  </div>

<a class="anchor" id="experience"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">实践经历</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">
      {% for entry in sections.Experience %}
        <li class="list-group-item"><div class="row">
          <div class="col-sm-2 text-center"><span class="badge font-weight-bold danger-color-dark text-uppercase align-middle">{% if entry.date %}{{ entry.date }}{% else %}{{ entry.start_date }}<br>{{ entry.end_date }}{% endif %}</span></div>
          <div class="col-sm-10 mt-2 mt-sm-0"><h6 class="title font-weight-bold ml-1 ml-md-4">{{ entry.position }}</h6><p class="ml-1 ml-md-4"><em>{{ entry.company }}</em></p><p class="ml-1 ml-md-4">{{ entry.summary }}</p>{% if entry.highlights %}<ul class="items">{% for item in entry.highlights %}<li>{{ item }}</li>{% endfor %}</ul>{% endif %}</div>
        </div></li>
      {% endfor %}
    </ul>
  </div>

<a class="anchor" id="projects"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">科研项目</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">
      {% for entry in sections.Projects %}
        <li class="list-group-item"><div class="row">
          <div class="col-sm-2 text-center"><span class="badge font-weight-bold danger-color-dark text-uppercase align-middle">{{ entry.start_date }}<br>{{ entry.end_date }}</span></div>
          <div class="col-sm-10 mt-2 mt-sm-0"><h6 class="title font-weight-bold ml-1 ml-md-4">{{ entry.name }}</h6><p class="ml-1 ml-md-4"><em>{{ entry.position }}</em></p><p class="ml-1 ml-md-4">{{ entry.summary }}</p></div>
        </div></li>
      {% endfor %}
    </ul>
  </div>

<a class="anchor" id="presentations"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">学术交流</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">
      {% for entry in sections["Academic Presentations"] %}
        <li class="list-group-item"><div class="row">
          <div class="col-sm-2 text-center"><span class="badge font-weight-bold danger-color-dark text-uppercase align-middle">{{ entry.date }}</span></div>
          <div class="col-sm-10 mt-2 mt-sm-0"><h6 class="title font-weight-bold ml-1 ml-md-4">{{ entry.title }}</h6><p class="ml-1 ml-md-4">{{ entry.format }}</p></div>
        </div></li>
      {% endfor %}
    </ul>
  </div>

<a class="anchor" id="publications"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">论文与手稿</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">
      {% for entry in sections.Publications %}
        <li class="list-group-item"><div class="row">
          <div class="col-sm-2 text-center"><span class="badge font-weight-bold danger-color-dark text-uppercase align-middle">{{ entry.releaseDate }}</span></div>
          <div class="col-sm-10 mt-2 mt-sm-0"><h6 class="title font-weight-bold ml-1 ml-md-4">{{ entry.title }}</h6>{% if entry.publisher %}<p class="ml-1 ml-md-4"><em>{{ entry.publisher }}</em></p>{% endif %}</div>
        </div></li>
      {% endfor %}
    </ul>
  </div>

<a class="anchor" id="skills"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">研究方法与技能</h3>
    <div class="card-text font-weight-light">{% for entry in sections.Skills %}<p><strong>{{ entry.name }}：</strong>{{ entry.keywords }}</p>{% endfor %}</div>
  </div>

<a class="anchor" id="open-source-projects"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">开源项目</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">{% for entry in sections["Open Source Projects"] %}<li class="list-group-item"><h6 class="title font-weight-bold">{{ entry.name }}</h6><p>{{ entry.summary }}</p><ul class="items">{% for item in entry.highlights %}<li>{% if item contains 'https://' %}<a href="{{ item }}" target="_blank" rel="noopener noreferrer">查看 GitHub</a>{% else %}{{ item }}{% endif %}</li>{% endfor %}</ul></li>{% endfor %}</ul>
  </div>

<a class="anchor" id="awards"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">荣誉与奖励</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">{% for entry in sections.Awards %}<li class="list-group-item"><div class="row"><div class="col-sm-2 text-center"><span class="badge font-weight-bold danger-color-dark text-uppercase align-middle">{{ entry.date }}</span></div><div class="col-sm-10 mt-2 mt-sm-0"><h6 class="title font-weight-bold ml-1 ml-md-4">{{ entry.title }}</h6>{% if entry.awarder != '' %}<p class="ml-1 ml-md-4"><em>{{ entry.awarder }}</em></p>{% endif %}</div></div></li>{% endfor %}</ul>
  </div>

<a class="anchor" id="languages"></a>

  <div class="card mt-3 p-3">
    <h3 class="card-title font-weight-medium">语言能力</h3>
    <ul class="card-text font-weight-light list-group list-group-flush">{% for entry in sections.Languages %}<li class="list-group-item"><strong>{{ entry.name }}：</strong>{{ entry.summary }}</li>{% endfor %}</ul>
  </div>
</div>
