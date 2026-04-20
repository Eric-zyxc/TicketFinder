import { createRouter, createWebHistory } from "vue-router";

import Login from "@/components/contents/Login.vue";
import Home from "@/components/homepage/Home.vue";
import SearchFlight from "@/components/contents/SearchFlight.vue";
import searchHotel from "@/components/contents/SearchHotel.vue";
import signup from "@/components/contents/Signup.vue";

const routes = [
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/home",
    name: "home",
    component: Home,
  },
  {
    path: "/searchFlight",
    name: "searchFlight",
    component: SearchFlight,
  },
  {
    path: "/searchHotel",
    name: "searchHotel",
    component: searchHotel,
  },
  {
    path: "/signup",
    name: "signup",
    component: signup,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
