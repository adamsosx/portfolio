---
layout: default
title: Blog
---

# Blog
Przemyślenia o technologii, rozwoju i ludzkiej naturze

<div class="posts">
  {% for post in site.posts %}
    <article class="post">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <div class="post-meta">
        {{ post.date | date: "%d.%m.%Y" }} • {{ post.category }} • {{ post.readTime }}
      </div>
      <div class="post-excerpt">
        {{ post.excerpt }}
      </div>
      <a href="{{ post.url }}" class="read-more">Czytaj więcej →</a>
    </article>
  {% endfor %}
</div>
