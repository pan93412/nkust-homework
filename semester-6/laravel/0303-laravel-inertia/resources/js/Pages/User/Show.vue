<script setup lang="ts">
import Layout from '../Layout.vue'
import { Head, Link } from '@inertiajs/vue3'

defineProps<{ user: { name?: string } }>();
</script>

<template>
    <Layout>
        <Head title="Welcome" />
        <div class="flex flex-col items-center justify-center min-h-screen py-12 bg-gradient-to-br from-blue-50 to-indigo-100">
            <div class="w-full max-w-md p-8 mx-auto bg-white rounded-xl shadow-md overflow-hidden">
                <h1 class="text-3xl font-extrabold text-center text-indigo-600 mb-6">
                    Welcome
                </h1>
                <div class="flex items-center justify-center">
                    <div class="text-center">
                        <p class="text-lg text-gray-700">
                            Hello <span class="font-semibold text-indigo-500">{{ user.name ?? 'Guest' }}</span>,
                            welcome to your first Inertia app!
                        </p>
                        <div class="mt-6" v-if="!user.name">
                            <Link href="/users/1">
                                <button class="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition-colors duration-300">
                                    Sign In
                                </button>
                            </Link>
                        </div>
                        <div class="mt-6 flex justify-center gap-4" v-else>
                            <Link href="/users">
                                <button class="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition-colors duration-300">
                                    Dashboard
                                </button>
                            </Link>
                            <Link href="/users">
                                <button class="px-4 py-2 border border-indigo-300 text-indigo-600 rounded-md hover:bg-indigo-50 transition-colors duration-300">
                                    Sign Out
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </Layout>
</template>
