<template>
  <div class="home">
    <!-- Side Navigation -->
    <SideNav :categories="categories" />

    <!-- About Me Section -->
    <section id="about" class="about-section">
      <h2 class="section-title">
        <span class="title-icon">👋</span>
        About Me
      </h2>
      <AboutMe :profile="profile" />
    </section>

    <!-- Projects Section -->
    <section class="projects-section">
      <h2 class="section-title">
        <span class="title-icon">🎨</span>
        My Projects
      </h2>

      <!-- Projects by Category -->
      <div
        v-for="category in categories"
        :key="category"
        :id="getCategoryId(category)"
        class="category-section"
      >
        <h3 class="category-title">{{ category }}</h3>
        <div class="projects-grid">
          <ProjectCard
            v-for="project in getProjectsByCategory(category)"
            :key="project.id"
            :project="project"
          />
        </div>
      </div>

      <!-- No Projects Message -->
      <div v-if="projects.length === 0" class="no-projects">
        <p>No projects yet. Stay tuned!</p>
      </div>
    </section>

    <!-- Special Thanks Footer -->
    <SpecialThanks />
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import AboutMe from "../components/AboutMe.vue";
import ProjectCard from "../components/ProjectCard.vue";
import SideNav from "../components/SideNav.vue";
import SpecialThanks from "../components/SpecialThanks.vue";
import profileData from "../assets/profile.json";
import projectsData from "../assets/projects/example.json";

const profile = ref(profileData);
const projects = ref(projectsData.projects || []);

// Get unique categories
const categories = computed(() => {
  const cats = projects.value.map((p) => p.category);
  return [...new Set(cats)].filter(Boolean);
});

// Get projects by category
const getProjectsByCategory = (category) => {
  return projects.value.filter((p) => p.category === category);
};

// Convert category to id
const getCategoryId = (category) => {
  return category.toLowerCase().replace(/\s+/g, "-");
};
</script>

<style scoped>
.home {
  min-height: 100vh;
}

.about-section {
  margin-bottom: 4rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin: 3rem 0 2rem 0;
  color: #2c3e50;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
}

.title-icon {
  font-size: 2.5rem;
}

.projects-section {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.category-section {
  margin-bottom: 4rem;
}

.category-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 3px solid #667eea;
  display: inline-block;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
}

.no-projects {
  text-align: center;
  padding: 4rem 2rem;
  color: #999;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .projects-section {
    padding: 1rem;
  }

  .section-title {
    font-size: 2rem;
    margin: 2rem 0 1.5rem 0;
  }

  .title-icon {
    font-size: 2rem;
  }

  .category-title {
    font-size: 1.5rem;
  }

  .projects-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .category-section {
    margin-bottom: 3rem;
  }
}
</style>
