import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import ProjectDetail from "../views/ProjectDetail.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/project/:id",
    name: "ProjectDetail",
    component: ProjectDetail,
  },
  // 404 fallback
  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

export default router;

