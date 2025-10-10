<template>
  <router-link :to="`/project/${project.id}`" class="project-card">
    <div class="card-image">
      <img
        :src="project.titleImage"
        :alt="project.title"
        referrerpolicy="no-referrer"
        crossorigin="anonymous"
        @error="handleImageError"
      />
      <div class="card-overlay">
        <span class="view-icon">👁️</span>
        <span class="view-text">View Details</span>
      </div>
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ project.title }}</h3>
      <div
        class="card-description"
        v-html="parseMarkdown(project.description)"
      ></div>
    </div>
  </router-link>
</template>

<script setup>
import { parse } from "marked";

const props = defineProps({
  project: {
    type: Object,
    required: true,
  },
});

const handleImageError = (event) => {
  console.warn("Image loading failed:", event.target.src);
};

// Parse markdown content
const parseMarkdown = (content) => {
  if (!content) {
    return "";
  }
  try {
    return parse(content);
  } catch (error) {
    console.error("Error parsing markdown:", error);
    return content;
  }
};
</script>

<style scoped>
.project-card {
  display: block;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  text-decoration: none;
  color: inherit;
}

.project-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

.card-image {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #f5f5f5;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.project-card:hover .card-image img {
  transform: scale(1.05);
}

.card-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.project-card:hover .card-overlay {
  opacity: 1;
}

.view-icon {
  font-size: 2rem;
  color: white;
}

.view-text {
  color: white;
  font-weight: 500;
  font-size: 1rem;
}

.card-content {
  padding: 1.5rem;
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 0.75rem 0;
  line-height: 1.4;
}

.card-description {
  font-size: 0.95rem;
  color: #666;
  line-height: 1.6;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Markdown content styles for card descriptions */
.card-description :deep(p) {
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description :deep(strong) {
  font-weight: 600;
  color: #2c3e50;
}

.card-description :deep(em) {
  font-style: italic;
}

.card-description :deep(a) {
  color: #667eea;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: all 0.3s ease;
}

.card-description :deep(a:hover) {
  color: #764ba2;
  border-bottom-color: #764ba2;
}

.card-description :deep(ul),
.card-description :deep(ol) {
  margin: 0.5em 0;
  padding-left: 1.5em;
}

.card-description :deep(li) {
  margin: 0.25em 0;
}

.card-description :deep(code) {
  background: #f5f5f5;
  padding: 0.2em 0.4em;
  border-radius: 3px;
  font-family: "Courier New", monospace;
  font-size: 0.9em;
}

.card-description :deep(blockquote) {
  border-left: 3px solid #667eea;
  padding-left: 1em;
  margin: 1em 0;
  color: #666;
  font-style: italic;
}

@media (max-width: 640px) {
  .card-content {
    padding: 1rem;
  }

  .card-title {
    font-size: 1.1rem;
  }

  .card-description {
    font-size: 0.9rem;
  }
}
</style>
