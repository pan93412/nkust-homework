<script setup>
import { ref, watch } from 'vue';
import { Head, Link } from '@inertiajs/vue3';
import axios from 'axios';
import AppLayout from '../Layout.vue';

const props = defineProps({
    initialResults: Array,
    searchTerm: String,
});

const searchQuery = ref(props.searchTerm);
const searchResults = ref(props.initialResults || []);
const isLoading = ref(false);
const errorMessage = ref('');
const debounceTimeout = ref(null);

const searchPodcasts = async () => {
    if (!searchQuery.value || searchQuery.value.length < 2) {
        searchResults.value = [];
        return;
    }

    isLoading.value = true;
    errorMessage.value = '';

    try {
        const response = await axios.get(`/podcasts/search?term=${encodeURIComponent(searchQuery.value)}&limit=20`);

        if (response.data.success) {
            searchResults.value = response.data.data;
        } else {
            errorMessage.value = response.data.message || '搜尋過程發生錯誤';
            searchResults.value = [];
        }
    } catch (error) {
        errorMessage.value = '無法連接到搜尋服務，請稍後再試';
        searchResults.value = [];
        console.error('播客搜尋錯誤:', error);
    } finally {
        isLoading.value = false;
    }
};

// 實作搜尋延遲功能，避免頻繁 API 請求
watch(searchQuery, () => {
    clearTimeout(debounceTimeout.value);
    debounceTimeout.value = setTimeout(() => {
        searchPodcasts();
    }, 500);
});
</script>

<template>
    <AppLayout title="播客搜尋">
        <Head title="播客搜尋" />

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="bg-white overflow-hidden shadow-xl sm:rounded-lg p-6">
                    <h1 class="text-2xl font-bold mb-6">播客搜尋</h1>

                    <div class="mb-8">
                        <label for="search" class="block text-sm font-medium text-gray-700">搜尋播客</label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <input
                                type="text"
                                id="search"
                                v-model="searchQuery"
                                class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-4 pr-12 sm:text-sm border-gray-300 rounded-md"
                                placeholder="請輸入播客名稱或關鍵字"
                                minlength="2"
                            />
                            <div v-if="isLoading" class="absolute inset-y-0 right-0 pr-3 flex items-center">
                                <svg class="animate-spin h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                            </div>
                        </div>
                        <p class="mt-1 text-sm text-gray-500">輸入至少 2 個字元開始搜尋</p>
                    </div>

                    <div v-if="errorMessage" class="bg-red-50 p-4 rounded-md mb-6">
                        <div class="flex">
                            <div class="flex-shrink-0">
                                <svg class="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                                </svg>
                            </div>
                            <div class="ml-3">
                                <h3 class="text-sm font-medium text-red-800">{{ errorMessage }}</h3>
                            </div>
                        </div>
                    </div>

                    <div v-if="searchResults.length > 0" class="space-y-6">
                        <h2 class="text-lg font-semibold">搜尋結果</h2>

                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            <div v-for="podcast in searchResults" :key="podcast.trackId" class="border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition">
                                <Link :href="`/podcasts/${ podcast.trackId }`" class="block h-full">
                                    <img v-if="podcast.artworkUrl600" :src="podcast.artworkUrl600" :alt="podcast.collectionName" class="w-full aspect-square object-cover" />
                                    <div v-else class="w-full aspect-square bg-gray-200 flex items-center justify-center">
                                        <span class="text-gray-400">無圖片</span>
                                    </div>

                                    <div class="p-4">
                                        <h3 class="font-bold text-lg line-clamp-2">{{ podcast.collectionName }}</h3>
                                        <p class="text-gray-600 line-clamp-1">{{ podcast.artistName }}</p>
                                        <div class="mt-2 flex items-center text-sm text-gray-500">
                                            <span>{{ podcast.trackCount }} 集</span>
                                            <span class="mx-2">•</span>
                                            <span>{{ podcast.primaryGenreName }}</span>
                                        </div>
                                    </div>
                                </Link>
                            </div>
                        </div>
                    </div>

                    <div v-else-if="searchQuery && searchQuery.length >= 2 && !isLoading" class="text-center py-12">
                        <svg xmlns="http://www.w3.org/2000/svg" class="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M12 14h.01M19 21a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                        <h3 class="mt-2 text-sm font-medium text-gray-900">沒有找到相符的播客</h3>
                        <p class="mt-1 text-sm text-gray-500">請嘗試不同的搜尋關鍵字</p>
                    </div>

                    <div v-else-if="!searchQuery" class="text-center py-12">
                        <svg xmlns="http://www.w3.org/2000/svg" class="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                        </svg>
                        <h3 class="mt-2 text-sm font-medium text-gray-900">開始搜尋播客</h3>
                        <p class="mt-1 text-sm text-gray-500">在上方輸入框輸入關鍵字來搜尋您喜愛的播客</p>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
