<script setup lang="ts">
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb'

defineProps<{
  parts: {
    name: string
    path: string
  }[]
}>()
</script>

<template>
  <Breadcrumb>
    <BreadcrumbList>
      <BreadcrumbItem v-for="part, index in parts" :key="part.path">
        <BreadcrumbSeparator class="hidden md:block" />
        <a :href="part.path">
          <component :is="index === parts.length - 1 ? BreadcrumbPage : 'span'">
            {{ part.name }}
          </component>
        </a>
      </BreadcrumbItem>
    </BreadcrumbList>
  </Breadcrumb>
</template>
