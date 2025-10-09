<template>
  <div class="about-me">
    <div class="about-content">
      <!-- 个人照片 -->
      <div class="photo-section">
        <div class="photo-frame">
          <img
            :src="profile.photo"
            :alt="profile.name"
            class="profile-photo"
            referrerpolicy="no-referrer"
          />
        </div>
      </div>

      <!-- 关于我 -->
      <div class="info-section">
        <h1 class="name">{{ profile.name }}</h1>
        <p class="name-en">{{ profile.nameEn }}</p>
        <div class="divider"></div>
        <p class="education">{{ profile.school }} · {{ profile.major }}</p>
        <div class="about-text">
          <h2 class="about-title">ABOUT ME</h2>
          <p
            v-for="(paragraph, index) in aboutParagraphs"
            :key="index"
            class="about-paragraph"
          >
            {{ paragraph }}
          </p>
        </div>

        <!-- 社交媒体 -->
        <div
          v-if="profile.social && profile.social.length"
          class="social-section"
        >
          <h3 class="connect-title">Connect Me</h3>
          <div class="social-links">
            <a
              v-for="social in profile.social"
              :key="social.name"
              :href="social.url"
              target="_blank"
              rel="noopener noreferrer"
              class="social-link"
              :title="social.name"
            >
              <span class="social-icon">{{ social.icon }}</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  profile: {
    type: Object,
    required: true,
  },
});

// 将关于我的文本按换行符分段
const aboutParagraphs = computed(() => {
  return props.profile.aboutMe
    ? props.profile.aboutMe.split("\n\n").filter((p) => p.trim())
    : [];
});
</script>

<style scoped>
.about-me {
  max-width: 1200px;
  margin: 0 auto;
  padding: 3rem 2rem;
}

.about-content {
  display: grid;
  grid-template-columns: 400px 1fr;
  gap: 4rem;
  align-items: start;
  background: white;
  border-radius: 20px;
  padding: 3rem;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
}

/* 照片区域 */
.photo-section {
  position: sticky;
  top: 2rem;
}

.photo-frame {
  position: relative;
  width: 100%;
  aspect-ratio: 3 / 4;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.photo-frame::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    rgba(102, 126, 234, 0.1) 0%,
    rgba(118, 75, 162, 0.1) 100%
  );
  pointer-events: none;
  z-index: 1;
}

.profile-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* 信息区域 */
.info-section {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.name {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2c3e50;
  margin: 0;
  letter-spacing: -0.5px;
}

.name-en {
  font-size: 1.2rem;
  color: #7f8c8d;
  font-weight: 300;
  letter-spacing: 1px;
  margin: -0.5rem 0 0 0;
}

.divider {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  border-radius: 2px;
  margin: 0.5rem 0;
}

.education {
  font-size: 1.1rem;
  color: #5d6d7e;
  margin: 0;
}

.about-text {
  margin-top: 1rem;
}

.about-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.about-paragraph {
  font-size: 1.05rem;
  line-height: 1.8;
  color: #555;
  margin-bottom: 1rem;
  text-align: justify;
}

.about-paragraph:last-child {
  margin-bottom: 0;
}

/* 社交媒体 */
.social-section {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #ecf0f1;
}

.connect-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 1rem 0;
  letter-spacing: 0.5px;
}

.social-links {
  display: flex;
  gap: 1rem;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  background: #f8f9fa;
  border-radius: 50%;
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 1.5rem;
}

.social-link:hover {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  transform: translateY(-3px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.social-link:hover .social-icon {
  transform: scale(1.1);
}

.social-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease;
}

/* 响应式设计 */
@media (max-width: 968px) {
  .about-content {
    grid-template-columns: 1fr;
    gap: 2rem;
    padding: 2rem;
  }

  .photo-section {
    position: relative;
    top: 0;
  }

  .photo-frame {
    max-width: 400px;
    margin: 0 auto;
  }

  .name {
    font-size: 2rem;
  }
}

@media (max-width: 640px) {
  .about-me {
    padding: 1.5rem 1rem;
  }

  .about-content {
    padding: 1.5rem;
  }

  .name {
    font-size: 1.8rem;
  }

  .name-en {
    font-size: 1rem;
  }

  .about-title {
    font-size: 1.3rem;
  }

  .about-paragraph {
    font-size: 1rem;
  }

  .social-link {
    width: 44px;
    height: 44px;
    font-size: 1.3rem;
  }
}
</style>
