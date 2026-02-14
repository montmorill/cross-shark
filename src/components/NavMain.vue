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
          <SidebarMenuButton :tooltip="$t(`${item.slug}.title`)" :is-active="$route.path === `/${item.slug}` ">
            <RouterLink :to="`/${item.slug}`" class="flex items-center gap-2">
              <component :is="item.icon" v-if="item.icon" class="size-4 shrink-0" />
              <span>{{ $t(`${item.slug}.title`) }}</span>
            </RouterLink>
            <CollapsibleTrigger class="grow pl-auto">
              <ChevronRight class="size-4 ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
            </CollapsibleTrigger>
          </SidebarMenuButton>
          <CollapsibleContent>
            <SidebarMenuSub>
              <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.slug">
                <SidebarMenuSubButton as-child :is-active="$route.path === `/${item.slug}/${subItem.slug}`">
                  <RouterLink :to="`/${item.slug}/${subItem.slug}`">
                    <component :is="subItem.icon" v-if="subItem.icon" />
                    <span>{{ $t(`${item.slug}.${subItem.slug}`) }}</span>
                  </RouterLink>
                </SidebarMenuSubButton>
              </SidebarMenuSubItem>
            </SidebarMenuSub>
          </CollapsibleContent>
        </SidebarMenuItem>
      </Collapsible>
    </SidebarMenu>
  </SidebarGroup>
</template>
