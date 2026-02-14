<script setup lang="ts">
import type { Component } from 'vue'

import { useStorage } from '@vueuse/core'

import { ChevronRight } from 'lucide-vue-next'

import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible'
import {
  SidebarGroup,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from '@/components/ui/sidebar'

defineProps<{
  items: {
    slug: string
    icon?: Component
    items?: {
      slug: string
      icon?: Component
    }[]
  }[]
}>()

const navMainActive = useStorage<Record<string, boolean>>('navMainActive', {})
</script>

<template>
  <SidebarGroup>
    <SidebarMenu>
      <Collapsible
        v-for="item in items"
        :key="item.slug"
        v-model:open="navMainActive[item.slug]"
        as-child
        class="group/collapsible"
      >
        <SidebarMenuItem>
          <RouterLink :to="`/${item.slug}`">
            <SidebarMenuButton :tooltip="$t(`${item.slug}.title`)">
              <component :is="item.icon" v-if="item.icon" />
              <span>{{ $t(`${item.slug}.title`) }}</span>
              <CollapsibleTrigger class="grow" @click.prevent>
                <ChevronRight class="h-4 ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
              </CollapsibleTrigger>
            </SidebarMenuButton>
          </RouterLink>
          <CollapsibleContent>
            <SidebarMenuSub>
              <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.slug">
                <SidebarMenuSubButton as-child :is-active="$route.path.startsWith(item.slug)">
                  <a :href="`/${item.slug}/${subItem.slug}`">
                    <component :is="subItem.icon" v-if="subItem.icon" />
                    <span>{{ $t(`${item.slug}.${subItem.slug}`) }}</span>
                  </a>
                </SidebarMenuSubButton>
              </SidebarMenuSubItem>
            </SidebarMenuSub>
          </CollapsibleContent>
        </SidebarMenuItem>
      </Collapsible>
    </SidebarMenu>
  </SidebarGroup>
</template>
