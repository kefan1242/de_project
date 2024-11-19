import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../components/HomePage.vue";
import DoubanPage from "../components/DoubanPage.vue";
import RottenTomatoesPage from "../components/RottenTomatoesPage.vue";
import AmazonBooksPage from "../components/AmazonBooksPage.vue";
import WinePage from "../components/WinePage.vue";

const routes = [
  { path: "/", 
    component: HomePage 
  },
  {
    path: "/douban",
    component: DoubanPage,
  },
  {
    path: "/rottenTomatoes",
    component: RottenTomatoesPage,
  },
  {
    path: "/amazonBooks",
    component: AmazonBooksPage,
  },
  {
    path: "/wine",
    component: WinePage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
