<template>
  <div class="project-item">
    <div class="project-main">
      <div v-for="(item, index) in project.main" :key="index" class="main-item">
        <div class="image-container" @click="openLightbox(item.image)">
          <img
            :src="item.image"
            :alt="item.title"
            class="main-image"
            loading="lazy"
            referrerpolicy="no-referrer"
            crossorigin="anonymous"
            @error="handleImageError"
          />
          <div class="image-overlay">
            <span class="zoom-icon">🔍</span>
          </div>
        </div>
        <div class="content">
          <h3 class="item-title">{{ item.title }}</h3>
          <p class="item-description">{{ item.description }}</p>
          <a
            v-if="item.link"
            :href="item.link"
            target="_blank"
            rel="noopener noreferrer"
            class="item-link"
          >
            查看原文 →
          </a>
        </div>
      </div>
    </div>

    <!-- 图片灯箱 Lightbox -->
    <Teleport to="body">
      <Transition name="lightbox">
        <div
          v-if="lightboxImage"
          class="lightbox-overlay"
          @click="closeLightbox"
        >
          <div class="lightbox-content">
            <button class="close-button" @click="closeLightbox">✕</button>
            <img
              :src="lightboxImage"
              alt="大图预览"
              class="lightbox-image"
              referrerpolicy="no-referrer"
              crossorigin="anonymous"
              @click.stop
            />
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  project: {
    type: Object,
    required: true,
  },
});

const lightboxImage = ref(null);

const openLightbox = (imageUrl) => {
  lightboxImage.value = imageUrl;
  document.body.style.overflow = "hidden";
};

const closeLightbox = () => {
  lightboxImage.value = null;
  document.body.style.overflow = "";
};

const handleImageError = (event) => {
  console.warn("图片加载失败，可能是防盗链限制：", event.target.src);
  // 可以设置一个默认占位图
  // event.target.src = '/placeholder.jpg'
};
</script>

<style scoped>
.project-item {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.project-main {
  display: grid;
  gap: 2rem;
}

.main-item {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.main-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

/* 交替布局 */
.main-item:nth-child(even) {
  grid-template-columns: 1fr 1fr;
}

.main-item:nth-child(even) .image-container {
  order: 2;
}

.main-item:nth-child(even) .content {
  order: 1;
}

.image-container {
  position: relative;
  overflow: hidden;
  cursor: pointer;
  aspect-ratio: 16 / 9;
  background: #f5f5f5;
}

.main-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.image-container:hover .main-image {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-container:hover .image-overlay {
  opacity: 1;
}

.zoom-icon {
  font-size: 2rem;
  color: white;
}

.content {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.item-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #2c3e50;
}

.item-description {
  font-size: 1rem;
  line-height: 1.6;
  color: #555;
  margin-bottom: 1.5rem;
  flex-grow: 1;
}

.item-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #42b883;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
  align-self: flex-start;
}

.item-link:hover {
  color: #349469;
}

/* 灯箱样式 */
.lightbox-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  cursor: zoom-out;
}

.lightbox-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-image {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
  cursor: default;
}

.close-button {
  position: absolute;
  top: -3rem;
  right: 0;
  background: rgba(255, 255, 255, 0.2);
  border: 2px solid rgba(255, 255, 255, 0.5);
  color: white;
  font-size: 2rem;
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  line-height: 1;
  padding: 0;
}

.close-button:hover {
  background: rgba(255, 255, 255, 0.3);
  border-color: rgba(255, 255, 255, 0.8);
  transform: rotate(90deg);
}

/* 动画 */
.lightbox-enter-active,
.lightbox-leave-active {
  transition: opacity 0.3s ease;
}

.lightbox-enter-active .lightbox-image,
.lightbox-leave-active .lightbox-image {
  transition: transform 0.3s ease;
}

.lightbox-enter-from,
.lightbox-leave-to {
  opacity: 0;
}

.lightbox-enter-from .lightbox-image,
.lightbox-leave-to .lightbox-image {
  transform: scale(0.8);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .main-item {
    grid-template-columns: 1fr !important;
    gap: 0;
  }

  .main-item:nth-child(even) .image-container,
  .main-item:nth-child(even) .content {
    order: 0;
  }

  .content {
    padding: 1.5rem;
  }

  .item-title {
    font-size: 1.25rem;
  }

  .item-description {
    font-size: 0.9rem;
  }

  .close-button {
    top: 1rem;
    right: 1rem;
  }
}
</style>
