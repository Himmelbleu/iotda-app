import { createRouter, createWebHashHistory } from "vue-router";

const router = createRouter({
  routes: [
    {
      name: "Home",
      path: "/",
      meta: { title: "首页" },
      redirect: "/data",
      component: () => import("@/views/Home.vue"),
      children: [
        {
          name: "DataScreen",
          path: "data",
          meta: { title: "大数据屏" },
          component: () => import("@/views/DataScreen.vue")
        },
        {
          name: "Cover",
          path: "cover",
          redirect: '/cover/base',
          meta: { title: "井盖数据" },
          component: () => import("@/views/cover/Cover.vue"),
          children: [
            {
              name: "CoverBase",
              path: "base",
              meta: { title: "基本信息" },
              component: () => import("@/views/cover/CoverBase.vue")
            }
          ]
        },
        {
          name: "Smoke",
          path: "smoke",
          redirect: '/smoke/base',
          meta: { title: "烟感数据" },
          component: () => import("@/views/smoke/Smoke.vue"),
          children: [
            {
              name: "SmokeBase",
              path: "base",
              meta: { title: "基本信息" },
              component: () => import("@/views/smoke/SmokeBase.vue")
            }
          ]
        }
      ]
    }
  ],
  history: createWebHashHistory(),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { el: "#app", top: 0, behavior: "smooth" };
    }
  }
});

export default router;
