<template>
  <div class="project-detail">
    <!-- Back Button -->
    <div class="back-button-container">
      <router-link to="/" class="back-button">
        <span class="back-icon">←</span>
        <span>Back to Home</span>
      </router-link>
    </div>

    <!-- Project Not Found -->
    <div v-if="!project" class="not-found">
      <h2>Project Not Found</h2>
      <p>The project you're looking for doesn't exist.</p>
      <router-link to="/" class="home-link">Go back to home</router-link>
    </div>

    <!-- Project Content -->
    <div v-else class="project-content">
      <!-- Project Header -->
      <div class="project-header">
        <div class="header-image">
          <img
            :src="project.titleImage"
            :alt="project.title"
            referrerpolicy="no-referrer"
            crossorigin="anonymous"
          />
        </div>
        <div class="header-info">
          <span v-if="project.category" class="category-badge">{{
            project.category
          }}</span>
          <h1 class="project-title">{{ project.title }}</h1>
          <p class="project-description">{{ project.description }}</p>
        </div>
      </div>

      <!-- Project Main Content -->
      <div class="project-main">
        <h2 class="section-title">Project Details</h2>
        <ProjectItem :project="project" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import ProjectItem from "../components/ProjectItem.vue";
import projectsData from "../assets/projects/example.json";

const route = useRoute();
const router = useRouter();

const projects = ref(projectsData.projects || []);

// Find project by ID
const project = computed(() => {
  const id = parseInt(route.params.id);
  return projects.value.find((p) => p.id === id);
});

// Scroll to top when component mounts
onMounted(() => {
  window.scrollTo(0, 0);
});
</script>

<style scoped>
.project-detail {
  min-height: 100vh;
  background: #f8f9fa;
}

.back-button-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem 2rem 1rem 2rem;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: white;
  color: #2c3e50;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.back-button:hover {
  background: #667eea;
  color: white;
  transform: translateX(-4px);
}

.back-icon {
  font-size: 1.25rem;
}

.not-found {
  max-width: 600px;
  margin: 4rem auto;
  padding: 3rem 2rem;
  text-align: center;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.not-found h2 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.not-found p {
  color: #666;
  margin-bottom: 2rem;
}

.home-link {
  display: inline-block;
  padding: 0.75rem 2rem;
  background: #667eea;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.home-link:hover {
  background: #5568d3;
  transform: translateY(-2px);
}

.project-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem 4rem 2rem;
}

.project-header {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  margin-bottom: 3rem;
}

.header-image {
  width: 100%;
  height: 400px;
  overflow: hidden;
  background: #f5f5f5;
}

.header-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.header-info {
  padding: 2.5rem;
}

.category-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: 1rem;
}

.project-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2c3e50;
  margin: 0 0 1rem 0;
  line-height: 1.2;
}

.project-description {
  font-size: 1.15rem;
  color: #555;
  line-height: 1.7;
  margin: 0;
}

.project-main {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.section-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid #e9ecef;
}

@media (max-width: 768px) {
  .back-button-container {
    padding: 1rem;
  }

  .project-content {
    padding: 0 1rem 2rem 1rem;
  }

  .header-image {
    height: 250px;
  }

  .header-info {
    padding: 1.5rem;
  }

  .project-title {
    font-size: 1.75rem;
  }

  .project-description {
    font-size: 1rem;
  }

  .project-main {
    padding: 1.5rem;
  }

  .section-title {
    font-size: 1.5rem;
  }
}
</style>
