<template>
  <footer id="footer" class="special-thanks">
    <div class="thanks-content">
      <h2 class="thanks-title">
        <span class="title-icon">💖</span>
        Special Thanks
      </h2>
      <p class="thanks-description">
        I would like to express my gratitude to the following people for their
        support and inspiration.
      </p>
      <div class="thanks-list">
        <a
          v-for="(person, index) in thanksData"
          :key="index"
          :href="person.url"
          target="_blank"
          rel="noopener noreferrer"
          class="thanks-card"
        >
          <div class="card-avatar">
            <img
              v-if="person.avatar"
              :src="person.avatar"
              :alt="person.name"
              class="avatar-image"
              referrerpolicy="no-referrer"
            />
            <div v-else class="card-icon">🙏</div>
          </div>
          <div class="card-info">
            <div class="card-name">{{ person.name }}</div>
            <div class="card-link">
              <span class="link-icon">🔗</span>
              <span class="link-text">Visit Profile</span>
            </div>
          </div>
        </a>
      </div>
      <div class="footer-copyright">
        <p>© 2025 Clarisse Mai. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import thanksJson from "../assets/thanks.json";

const thanksData = thanksJson.thanks || [];
</script>

<style scoped>
.special-thanks {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 2rem;
  margin-top: 4rem;
}

.thanks-content {
  max-width: 1200px;
  margin: 0 auto;
}

.thanks-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  color: white;
}

.title-icon {
  font-size: 2.5rem;
  animation: heartbeat 1.5s ease-in-out infinite;
}

@keyframes heartbeat {
  0%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

.thanks-description {
  text-align: center;
  font-size: 1.1rem;
  opacity: 0.9;
  margin-bottom: 3rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.thanks-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 3rem;
}

.thanks-card {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 1.5rem 1rem;
  text-decoration: none;
  color: white;
  transition: all 0.3s ease;
  border: 2px solid rgba(255, 255, 255, 0.2);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.thanks-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  transition: left 0.5s ease;
}

.thanks-card:hover::before {
  left: 100%;
}

.thanks-card:hover {
  transform: translateY(-5px);
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.4);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
}

.card-avatar {
  position: relative;
  z-index: 1;
}

.avatar-image {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
}

.thanks-card:hover .avatar-image {
  transform: scale(1.1);
  border-color: rgba(255, 255, 255, 0.6);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.card-icon {
  font-size: 3rem;
  transition: transform 0.3s ease;
}

.thanks-card:hover .card-icon {
  transform: scale(1.1);
}

.card-info {
  text-align: center;
  width: 100%;
  z-index: 1;
}

.card-name {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  word-break: break-word;
}

.card-link {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.3rem;
  font-size: 0.85rem;
  opacity: 0.8;
  transition: opacity 0.3s ease;
}

.thanks-card:hover .card-link {
  opacity: 1;
}

.link-icon {
  font-size: 0.9rem;
}

.link-text {
  font-size: 0.85rem;
}

.footer-copyright {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  opacity: 0.8;
  font-size: 0.95rem;
}

.footer-copyright p {
  margin: 0;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .special-thanks {
    padding: 3rem 1.5rem;
  }

  .thanks-title {
    font-size: 2rem;
  }

  .title-icon {
    font-size: 2rem;
  }

  .thanks-description {
    font-size: 1rem;
    margin-bottom: 2rem;
  }

  .thanks-list {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 0.8rem;
  }

  .thanks-card {
    padding: 1.2rem 0.8rem;
  }

  .avatar-image {
    width: 70px;
    height: 70px;
  }

  .card-icon {
    font-size: 2.5rem;
  }

  .card-name {
    font-size: 1rem;
  }

  .link-text {
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .thanks-list {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .avatar-image {
    width: 60px;
    height: 60px;
  }
}
</style>

