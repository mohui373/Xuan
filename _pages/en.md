---
layout: default
title: EN
permalink: /en/
description: Bole Xuan's English academic profile, research, publications, projects, and curriculum vitae.
nav: true
nav_order: 5
lang: en
---

{% assign en = site.data.en %}

<main class="site-home english-site" lang="en">
  <section class="site-hero" aria-labelledby="english-home-title">
    <div class="site-hero-copy">
      <p class="site-kicker">{{ en.profile.kicker }}</p>
      <h1 id="english-home-title">{{ en.profile.name }}</h1>
      <p class="site-role">{{ en.profile.role }}</p>
      <p class="site-lede">{{ en.profile.lede }}</p>
      <ul class="tag-list hero-tags" aria-label="Primary research interests">
        {% for tag in en.profile.tags %}<li>{{ tag }}</li>{% endfor %}
      </ul>
      <div class="site-actions" aria-label="Primary links">
        <a class="site-action site-action-primary" href="#research">Explore Research</a>
        <a class="site-action" href="#cv">View CV</a>
        <a class="site-action" href="{{ '/' | relative_url }}">中文版</a>
      </div>
      <p class="site-profile-links">Academic profiles: <a href="https://orcid.org/0009-0004-9399-9489" target="_blank" rel="noopener noreferrer">ORCID</a><a href="https://github.com/mohui373" target="_blank" rel="noopener noreferrer">GitHub</a><a href="mailto:huimo7627@gmail.com">Email</a></p>
    </div>
    <figure class="profile-frame">
      <img src="{{ '/assets/img/profile-bole.jpg' | relative_url }}" alt="Academic portrait of Bole Xuan" width="720" height="900">
      <figcaption>Bole Xuan · Basic Psychology</figcaption>
    </figure>
  </section>

  <nav class="english-section-nav" aria-label="English page sections">
    <a href="#research">Research</a>
    <a href="#publications">Publications</a>
    <a href="#projects">Projects</a>
    <a href="#cv">CV</a>
  </nav>

  <section class="research-question-band" aria-labelledby="english-core-question">
    <p class="section-eyebrow">Core Question</p>
    <h2 id="english-core-question">{{ en.core_question.title }}</h2>
    <p>{{ en.core_question.keywords }}</p>
  </section>

  <section id="research" class="site-section english-anchor-section" aria-labelledby="english-research-title">
    <div class="section-heading">
      <div>
        <p class="section-eyebrow">Research</p>
        <h2 id="english-research-title">Research Program</h2>
      </div>
    </div>
    <p class="english-section-intro">{{ en.research.intro }}</p>

    <nav class="research-index" aria-label="Research stream index">
      {% for stream in en.research.streams %}
        <a href="#en-{{ stream.slug }}"><span>{{ stream.number }}</span>{{ stream.title }}</a>
      {% endfor %}
    </nav>

    {% for stream in en.research.streams %}
      <article id="en-{{ stream.slug }}" class="research-detail">
        <header class="research-detail-header">
          <div>
            <p class="stream-overline">{{ stream.number }} · {{ stream.title }}</p>
            <h2>{{ stream.title }}</h2>
          </div>
          <span class="status status-{{ stream.status_key }}">{{ stream.status }}</span>
        </header>
        <p class="research-question">{{ stream.question }}</p>
        <p>{{ stream.summary }}</p>
        <div class="research-detail-grid">
          <div>
            <h3>Research Design & Current Focus</h3>
            <ul class="clean-list">
              {% for item in stream.design %}<li>{{ item }}</li>{% endfor %}
            </ul>
          </div>
          <div>
            <h3>{% if stream.status_key == 'ongoing' %}Conceptual Pathway{% else %}Research Logic{% endif %}</h3>
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

  </section>

  <section id="publications" class="site-section english-anchor-section" aria-labelledby="english-publications-title">
    <div class="section-heading">
      <div>
        <p class="section-eyebrow">Publications & Manuscripts</p>
        <h2 id="english-publications-title">Selected Work</h2>
      </div>
    </div>
    <p class="english-section-intro">Items are grouped by current research status. Unconfirmed journals, DOIs, preprints, and links are not displayed.</p>

    {% for group in en.publications %}
      <section class="publication-group" aria-labelledby="en-publication-group-{{ forloop.index }}">
        <div class="section-heading compact">
          <h3 id="en-publication-group-{{ forloop.index }}">{{ group.group }}</h3>
        </div>
        <div class="english-publication-list">
          {% for entry in group.entries %}
            <article class="english-publication-entry">
              <h4>{{ entry.title }}</h4>
              <p>{{ entry.authors }}</p>
              {% if entry.venue %}<p><em>{{ entry.venue }}</em></p>{% endif %}
              {% if entry.note %}<p>{{ entry.note }}</p>{% endif %}
              {% if entry.resource_url %}<a href="{{ entry.resource_url }}" target="_blank" rel="noopener noreferrer">{{ entry.resource_label }}</a>{% endif %}
            </article>
          {% endfor %}
        </div>
      </section>
    {% endfor %}

  </section>

  <section id="projects" class="site-section project-feature english-anchor-section" aria-labelledby="english-project-title">
    <div class="project-feature-copy">
      <p class="section-eyebrow">Featured Open-Source Project</p>
      <h2 id="english-project-title">{{ en.project.name }}</h2>
      <p class="project-lede">{{ en.project.lede }}</p>
      <p>{{ en.project.summary }}</p>
      <ul class="tag-list">
        {% for tag in en.project.tags %}<li>{{ tag }}</li>{% endfor %}
      </ul>
      <div class="site-actions">
        <a class="site-action site-action-primary" href="https://github.com/mohui373/paper-to-paradigm" target="_blank" rel="noopener noreferrer">GitHub Repository</a>
        <a class="site-action" href="{{ '/projects/paper-to-paradigm/' | relative_url }}">Chinese Project Page</a>
      </div>
    </div>
    <div class="project-skills" aria-label="Core skills">
      {% for skill in en.project.skills %}
        <div>
          <span>{{ skill.number }}</span>
          <h3>{{ skill.name }}</h3>
          <p>{{ skill.label }}: {{ skill.summary }}</p>
        </div>
      {% endfor %}
    </div>
  </section>

  <section class="site-section" aria-labelledby="english-methods-title">
    <div class="section-heading">
      <div>
        <p class="section-eyebrow">Research Methods</p>
        <h2 id="english-methods-title">Methods & Tools</h2>
      </div>
    </div>
    <div class="method-columns">
      {% for method in en.methods %}
        <div>
          <h3>{{ method.title }}</h3>
          <p>{{ method.summary }}</p>
        </div>
      {% endfor %}
    </div>
  </section>

  <section id="cv" class="site-section english-cv english-anchor-section" aria-labelledby="english-cv-title">
    <div class="section-heading">
      <div>
        <p class="section-eyebrow">Curriculum Vitae</p>
        <h2 id="english-cv-title">Academic & Professional Profile</h2>
      </div>
    </div>
    <p class="english-section-intro">{{ en.cv.summary }}</p>

    <section class="english-cv-section">
      <h3>Education</h3>
      <div class="english-entry-list">
        {% for entry in en.cv.education %}
          <article class="english-entry">
            <p class="english-entry-date">{{ entry.start_date }} — {{ entry.end_date }}</p>
            <div>
              <h4>{{ entry.degree }}</h4>
              <p class="english-entry-meta">{{ entry.institution }}</p>
              <ul class="clean-list">{% for item in entry.highlights %}<li>{{ item }}</li>{% endfor %}</ul>
            </div>
          </article>
        {% endfor %}
      </div>
    </section>

    <section class="english-cv-section">
      <h3>Professional Experience</h3>
      <div class="english-entry-list">
        {% for entry in en.cv.experience %}
          <article class="english-entry">
            <p class="english-entry-date">{% if entry.date %}{{ entry.date }}{% else %}{{ entry.start_date }} — {{ entry.end_date }}{% endif %}</p>
            <div>
              <h4>{{ entry.role }}</h4>
              <p class="english-entry-meta">{{ entry.organization }}</p>
              <p>{{ entry.summary }}</p>
              {% if entry.highlights %}<ul class="clean-list">{% for item in entry.highlights %}<li>{{ item }}</li>{% endfor %}</ul>{% endif %}
            </div>
          </article>
        {% endfor %}
      </div>
    </section>

    <section class="english-cv-section">
      <h3>Research Projects</h3>
      <div class="english-entry-list">
        {% for entry in en.cv.projects %}
          <article class="english-entry">
            <p class="english-entry-date">{{ entry.start_date }} — {{ entry.end_date }}</p>
            <div>
              <h4>{{ entry.title }}</h4>
              <p class="english-entry-meta">{{ entry.role }}</p>
              <p>{{ entry.summary }}</p>
            </div>
          </article>
        {% endfor %}
      </div>
    </section>

    <section class="english-cv-section">
      <h3>Publications & Manuscripts</h3>
      <div class="english-entry-list compact-list">
        {% for entry in en.cv.publications %}
          <article class="english-entry">
            <p class="english-entry-date">{{ entry.status }}</p>
            <div><h4>{{ entry.title }}</h4></div>
          </article>
        {% endfor %}
      </div>
    </section>

    <section class="english-cv-section">
      <h3>Research Methods & Skills</h3>
      <div class="method-columns">
        {% for entry in en.cv.skills %}
          <div>
            <h4>{{ entry.title }}</h4>
            <p>{{ entry.detail }}</p>
          </div>
        {% endfor %}
      </div>
    </section>

    <section class="english-cv-section">
      <h3>Open-Source Projects</h3>
      {% for entry in en.cv.open_source %}
        <article class="english-simple-entry">
          <h4>{{ entry.title }}</h4>
          <p>{{ entry.detail }}</p>
          <a href="{{ entry.url }}" target="_blank" rel="noopener noreferrer">View on GitHub</a>
        </article>
      {% endfor %}
    </section>

    <section class="english-cv-section">
      <h3>Honors & Awards</h3>
      <div class="english-honors-grid">
        {% for entry in en.cv.honors %}
          <article><span>{{ entry.date }}</span><p>{{ entry.title }}</p></article>
        {% endfor %}
      </div>
    </section>

    <section class="english-cv-section">
      <h3>Languages</h3>
      <div class="english-language-list">
        {% for entry in en.cv.languages %}<p><strong>{{ entry.title }}:</strong> {{ entry.detail }}</p>{% endfor %}
      </div>
    </section>

  </section>

  <footer class="english-page-footer">
    <a class="site-action site-action-primary" href="{{ '/' | relative_url }}">View Chinese Version</a>
    <a class="site-action" href="https://github.com/mohui373/Xuan/blob/main/README_EN.md">English Editing Guide</a>
  </footer>
</main>
