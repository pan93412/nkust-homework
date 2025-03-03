<script setup>
import {Link} from '@inertiajs/vue3'
</script>

<template>
    <main class="min-h-screen bg-gray-50">
        <header class="bg-white shadow-sm">
            <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex h-16 items-center justify-between">
                    <Link href="/public" class="text-gray-900 hover:text-gray-600 font-medium">Home</Link>
                </div>
            </nav>
        </header>
        <article class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <slot/>
        </article>
    </main>
</template>
