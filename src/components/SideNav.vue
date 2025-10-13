<template>
  <nav
    class="side-nav"
    :class="{ 'is-hovered': isHovered }"
    @mouseenter="isHovered = true"
    @mouseleave="isHovered = false"
  >
    <!-- 弧线 -->
    <div class="nav-line"></div>

    <!-- 导航项 -->
    <ul class="nav-list">
      <li class="nav-item">
        <a
          href="#about"
          class="nav-link"
          @click="scrollToSection('about', $event)"
        >
          <span class="nav-dot"></span>
          <span class="nav-text">About Me</span>
        </a>
      </li>
      <li v-for="category in categories" :key="category" class="nav-item">
        <a
          :href="`#${getCategoryId(category)}`"
          class="nav-link"
          @click="scrollToSection(getCategoryId(category), $event)"
        >
          <span class="nav-dot"></span>
          <span class="nav-text">{{ category }}</span>
        </a>
      </li>
      <li class="nav-item">
        <a
          href="#footer"
          class="nav-link"
          @click="scrollToSection('footer', $event)"
        >
          <span class="nav-dot"></span>
          <span class="nav-text">Special Thanks</span>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  categories: {
    type: Array,
    default: () => [],
  },
});

const isHovered = ref(false);

const getCategoryId = (category) => {
  return category.toLowerCase().replace(/\s+/g, "-");
};

const scrollToSection = (id, event) => {
  event.preventDefault();
  const element = document.getElementById(id);
  if (element) {
    const offset = 80; // 偏移量，避免被顶部遮挡
    const elementPosition =
      element.getBoundingClientRect().top + window.pageYOffset;
    const offsetPosition = elementPosition - offset;

    window.scrollTo({
      top: offsetPosition,
      behavior: "smooth",
    });
  }
};
</script>

<style scoped>
.side-nav {
  position: fixed;
  right: 3rem;
  top: 50%;
  transform: translateY(-50%);
  z-index: 100;
  opacity: 0.6;
  transition: opacity 0.3s ease;
  height: 450px;
  width: 200px;
}

.side-nav.is-hovered {
  opacity: 1;
}

/* 弧形竖线 */
.nav-line {
  position: absolute;
  right: 0;
  top: 0;
  width: 3px;
  height: 100%;
  background: linear-gradient(
    180deg,
    transparent 0%,
    rgba(102, 126, 234, 0.3) 10%,
    rgba(102, 126, 234, 0.8) 50%,
    rgba(102, 126, 234, 0.3) 90%,
    transparent 100%
  );
  border-radius: 50px;
}

.side-nav.is-hovered .nav-line {
  background: linear-gradient(
    180deg,
    transparent 0%,
    rgba(102, 126, 234, 0.5) 10%,
    rgba(102, 126, 234, 1) 50%,
    rgba(102, 126, 234, 0.5) 90%,
    transparent 100%
  );
  box-shadow: 0 0 20px rgba(102, 126, 234, 0.4);
}

.nav-list {
  position: relative;
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.nav-item {
  position: relative;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0;
  text-decoration: none;
  color: #2c3e50;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
  white-space: nowrap;
  position: relative;
  padding-right: 0;
}

.nav-link:hover {
  color: #667eea;
}

/* 导航圆点 */
.nav-dot {
  position: absolute;
  right: -7px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: white;
  border: 3px solid #667eea;
  transition: all 0.3s ease;
  flex-shrink: 0;
  box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
  z-index: 2;
}

.nav-link:hover .nav-dot {
  transform: scale(1.4);
  background: #667eea;
  border-color: white;
  box-shadow: 0 0 20px rgba(102, 126, 234, 0.6);
}

.nav-text {
  position: relative;
  right: 1.5rem;
  opacity: 0;
  transform: translateX(10px);
  transition: all 0.3s ease;
  white-space: nowrap;
  background: rgba(255, 255, 255, 0.95);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  pointer-events: none;
}

.side-nav.is-hovered .nav-text {
  opacity: 1;
  transform: translateX(0);
  pointer-events: auto;
}

/* 响应式：平板及以下隐藏侧边导航 */
@media (max-width: 1024px) {
  .side-nav {
    display: none;
  }
}

/* 大屏幕优化 */
@media (min-width: 1400px) {
  .side-nav {
    right: 4rem;
  }
}

/* 小屏幕调整 */
@media (max-width: 1280px) {
  .side-nav {
    right: 2rem;
  }
}
</style>
