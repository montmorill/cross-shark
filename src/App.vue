<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRoute } from 'vue-router'

import AppSidebar from '@/components/AppSidebar.vue'
import Breadcrumb from '@/components/Breadcrumb.vue'
import { Separator } from '@/components/ui/separator'
import { SidebarInset, SidebarProvider, SidebarTrigger } from '@/components/ui/sidebar'

const { t } = useI18n()
const route = useRoute()

const breadcrumb = computed(() => {
  const parts = route.path.split('/').filter(Boolean)
  if (parts.length === 2) {
    return [t(`${parts[0]}.title`), t(`${parts[0]}.${parts[1]}`)]
  }
  return parts
})
</script>

<template>
  <SidebarProvider>
    <AppSidebar />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
        <div class="flex items-center gap-2 px-4">
          <SidebarTrigger class="-ml-1" />
          <Separator
            orientation="vertical"
            class="mr-2 data-[orientation=vertical]:h-4"
          />
          <Breadcrumb :path="breadcrumb" />
        </div>
      </header>
      <RouterView />
    </SidebarInset>
  </SidebarProvider>
</template>
