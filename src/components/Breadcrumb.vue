<script setup lang="ts">
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb'

defineProps<{
  path: string[]
}>()
</script>

<template>
  <Breadcrumb>
    <BreadcrumbList>
      <BreadcrumbItem v-for="part, index in path" :key="part">
        <BreadcrumbSeparator class="hidden md:block" />
        <component :is="index === path.length - 1 ? BreadcrumbPage : 'span'">
          {{ part }}
        </component>
      </BreadcrumbItem>
    </BreadcrumbList>
  </Breadcrumb>
</template>
