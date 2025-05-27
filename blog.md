---
layout: default
title: Blog
---

# Blog
Przemyślenia o technologii, rozwoju i ludzkiej naturze

{% assign posts = site.posts | where: "published", true %}
{% if posts.size > 0 %}
  {% for post in posts %}
  <article class="post">
    {% if post.image %}
      <div class="post-thumbnail">
        <img src="{{ post.image }}" alt="{{ post.title }}">
      </div>
    {% endif %}
    
    <div class="post-content">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
      <div class="post-meta">
        {{ post.date | date: "%d.%m.%Y" }} • {{ post.category }} • {{ post.readTime }}
      </div>
      <div class="post-excerpt">
        {{ post.excerpt }}
      </div>
      <a href="{{ post.url }}" class="read-more">Czytaj więcej →</a>
    </div>
  </article>
  {% endfor %}
{% else %}
  <p>Brak postów do wyświetlenia.</p>
{% endif %}

<section class="newsletter">
  <h3>Otrzymuj powiadomienia o nowych artykułach</h3>
  <form name="newsletter" method="POST" data-netlify="true">
    <input type="email" name="email" placeholder="Twój email" required>
    <button type="submit">Zapisz się</button>
    <div style="display: none;">
      <input name="bot-field">
    </div>
  </form>
</section>
