import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

createApp(App)
  .use(createI18n({
    legacy: false,
    locale: 'zh',
    messages: {
      zh: {
        source: {
          title: '采集平台',
          bilibili: 'Bilibili',
          douyin: '抖音',
          xiaohongshu: '小红书',
        },
        material: {
          title: '素材',
          photo: '图文',
          video: '视频',
        },
        target: {
          title: '发布平台',
          instagram: 'Instagram',
          tiktok: 'TikTok',
          twitter: 'Twitter',
        },
      },
    },
  }))
  .use(createRouter({
    history: createWebHistory(),
    routes: [],
  }))
  .mount('#app')
