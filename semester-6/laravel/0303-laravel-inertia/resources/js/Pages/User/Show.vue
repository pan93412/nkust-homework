<script setup lang="ts">
import Layout from '../Layout.vue'
import { Head } from '@inertiajs/vue3'

defineProps<{ user: { name?: string } }>();
</script>

<template>
  <Layout>
    <Head title="Welcome" />
    <h1>Welcome</h1>
    <p>Hello {{ user.name ?? 'not logged in' }}, welcome to your first Inertia app!</p>
  </Layout>
</template>
