<script setup lang="ts">
import type { SidebarProps } from '@/components/ui/sidebar'

import { shark } from '@lucide/lab'
import {
  Flower,
  FolderDown,
  FolderUp,
  Icon,
  Images,
  Video,
} from 'lucide-vue-next'
import {
  siBilibili,
  siInstagram,
  siTiktok,
  siX,
  siXiaohongshu,
} from 'simple-icons'
import { compile, h } from 'vue'

import {
  Sidebar,
  SidebarContent,
  SidebarHeader,
} from '@/components/ui/sidebar'

import NavBrand from './NavBrand.vue'
import NavMain from './NavMain.vue'

const props = withDefaults(defineProps<SidebarProps>(), {
  collapsible: 'icon',
})

const navData = [
  {
    slug: 'source',
    icon: FolderDown,
    items: [
      { slug: 'bilibili', icon: compile(siBilibili.svg) },
      { slug: 'douyin', icon: compile(siTiktok.svg) },
      { slug: 'xiaohongshu', icon: compile(siXiaohongshu.svg) },
    ],
  },
  {
    slug: 'material',
    icon: Flower,
    items: [
      { slug: 'photo', icon: Images },
      { slug: 'video', icon: Video },
    ],
  },
  {
    slug: 'target',
    icon: FolderUp,
    items: [
      { slug: 'instagram', icon: compile(siInstagram.svg) },
      { slug: 'tiktok', icon: compile(siTiktok.svg) },
      { slug: 'twitter', icon: compile(siX.svg) },
    ],
  },
]
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <RouterLink to="/">
        <NavBrand name="Cross Shark" :logo="h(Icon, { iconNode: shark, name: 'shark' })" />
      </RouterLink>
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="navData" />
    </SidebarContent>
  </Sidebar>
</template>
