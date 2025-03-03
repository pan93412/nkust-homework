<script setup>
import { ref, onMounted } from 'vue';
import { Head, Link } from '@inertiajs/vue3';
import axios from 'axios';
import AppLayout from '../Layout.vue';

const props = defineProps({
    podcast: Object,
});

const isLoadingEpisodes = ref(false);
const episodes = ref([]);
const errorMessage = ref('');

const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('zh-TW', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
};

const formatDuration = (milliseconds) => {
    if (!milliseconds) return '';
    const totalSeconds = Math.floor(milliseconds / 1000);
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    if (hours > 0) {
        return `${hours}時${minutes}分${seconds}秒`;
    } else if (minutes > 0) {
        return `${minutes}分${seconds}秒`;
    } else {
        return `${seconds}秒`;
    }
};

const loadEpisodes = async () => {
    if (!props.podcast?.feedUrl) {
        errorMessage.value = '無法載入集數資訊：缺少播客 Feed URL';
        return;
    }

    isLoadingEpisodes.value = true;

    try {
        // 這裡假設你有一個 API 端點可以解析播客 Feed
        // 若實際開發中需要實作此功能，可考慮使用後端解析 RSS
        const response = await axios.get(`/podcasts/${props.podcast.trackId}/episodes`);
        if (response.data.success) {
            episodes.value = response.data.data;
        } else {
            errorMessage.value = response.data.message || '無法載入集數資訊';
        }
    } catch (error) {
        console.error('載入播客集數失敗:', error);
        errorMessage.value = '載入集數資訊時發生錯誤，請稍後再試';
    } finally {
        isLoadingEpisodes.value = false;
    }
};

onMounted(() => {
    // 如果需要載入集數資料，可取消下面這行的註解
    // loadEpisodes();
});
</script>

<template>
    <AppLayout :title="podcast?.collectionName || '播客詳情'">
        <Head :title="podcast?.collectionName || '播客詳情'" />

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <!-- 返回按鈕 -->
                <div class="mb-6">
                    <Link href="/podcasts" class="inline-flex items-center text-indigo-600 hover:text-indigo-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L4.414 9H17a1 1 0 010 2H4.414l5.293 5.293a1 1 0 010 1.414z" clip-rule="evenodd" />
                        </svg>
                        返回播客列表
                    </Link>
                </div>

                <!-- 播客不存在提示 -->
                <div v-if="!podcast" class="bg-white shadow overflow-hidden sm:rounded-lg p-8 text-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M12 14h.01M19 21a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                    <h3 class="mt-2 text-lg font-medium text-gray-900">找不到指定的播客</h3>
                    <p class="mt-1 text-gray-500">此播客可能不存在或已被移除</p>
                    <div class="mt-6">
                        <Link href="/podcasts" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700">
                            返回搜尋頁面
                        </Link>
                    </div>
                </div>

                <!-- 播客詳細資訊 -->
                <div v-else class="bg-white shadow overflow-hidden sm:rounded-lg">
                    <!-- 播客頭部資訊 -->
                    <div class="p-6 md:p-8 border-b border-gray-200">
                        <div class="flex flex-col md:flex-row md:items-start">
                            <div class="flex-shrink-0 mb-6 md:mb-0 md:mr-8">
                                <img
                                    v-if="podcast.artworkUrl600"
                                    :src="podcast.artworkUrl600"
                                    :alt="podcast.collectionName"
                                    class="w-full md:w-64 h-auto rounded-lg shadow-md"
                                />
                                <div v-else class="w-full md:w-64 h-64 bg-gray-200 rounded-lg shadow-md flex items-center justify-center">
                                    <span class="text-gray-500">無圖片</span>
                                </div>

                                <!-- 外部連結 -->
                                <div class="mt-4 space-y-2">
                                    <a v-if="podcast.collectionViewUrl" :href="podcast.collectionViewUrl" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-sm text-gray-600 hover:text-gray-900">
                                        <svg class="h-5 w-5 mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M11 3a1 1 0 100 2h2.586l-6.293 6.293a1 1 0 101.414 1.414L15 6.414V9a1 1 0 102 0V4a1 1 0 00-1-1h-5z"></path>
                                            <path d="M5 5a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2v-3a1 1 0 10-2 0v3H5V7h3a1 1 0 000-2H5z"></path>
                                        </svg>
                                        在 Apple Podcasts 中查看
                                    </a>
                                    <a v-if="podcast.feedUrl" :href="podcast.feedUrl" target="_blank" rel="noopener noreferrer" class="inline-flex items-center text-sm text-gray-600 hover:text-gray-900">
                                        <svg class="h-5 w-5 mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                            <path fill-rule="evenodd" d="M5 5a3 3 0 015-2.236A3 3 0 0114.83 6H16a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h1.17A3 3 0 015 5zm4 1V5a1 1 0 10-2 0v1H4a1 1 0 00-1 1v8a1 1 0 001 1h12a1 1 0 001-1V8a1 1 0 00-1-1h-3v1z" clip-rule="evenodd"></path>
                                        </svg>
                                        RSS Feed
                                    </a>
                                </div>
                            </div>

                            <div class="flex-grow">
                                <h1 class="text-2xl md:text-3xl font-bold text-gray-900 mb-2">
                                    {{ podcast.collectionName }}
                                </h1>
                                <p class="text-lg text-gray-700 mb-4">
                                    {{ podcast.artistName }}
                                </p>

                                <div class="flex flex-wrap gap-x-6 gap-y-2 mb-6">
                                    <div class="flex items-center text-sm text-gray-500">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" />
                                        </svg>
                                        {{ podcast.primaryGenreName || '未分類' }}
                                    </div>
                                    <div class="flex items-center text-sm text-gray-500">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
                                        </svg>
                                        {{ podcast.trackCount }} 集
                                    </div>
                                    <div v-if="podcast.releaseDate" class="flex items-center text-sm text-gray-500">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                        </svg>
                                        {{ formatDate(podcast.releaseDate) }}
                                    </div>
                                    <div v-if="podcast.country" class="flex items-center text-sm text-gray-500">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9" />
                                        </svg>
                                        {{ podcast.country }}
                                    </div>
                                </div>

                                <!-- 播客描述 -->
                                <div v-if="podcast.description" class="prose prose-indigo max-w-none">
                                    <h2 class="text-lg font-semibold mb-2">播客簡介</h2>
                                    <p class="text-gray-700 whitespace-pre-line">{{ podcast.description }}</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 集數列表區塊 -->
                    <div class="p-6 md:p-8">
                        <h2 class="text-xl font-bold mb-6 flex items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                            </svg>
                            節目集數
                        </h2>

                        <div v-if="isLoadingEpisodes" class="py-10 text-center">
                            <svg class="animate-spin h-10 w-10 text-gray-400 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            <p class="mt-4 text-gray-600">正在載入集數資訊...</p>
                        </div>

                        <div v-else-if="errorMessage" class="bg-red-50 p-4 rounded-md">
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

                        <div v-else-if="episodes.length > 0" class="space-y-4">
                            <div v-for="(episode, index) in episodes" :key="index" class="border border-gray-200 rounded-lg p-4 hover:bg-gray-50">
                                <h3 class="font-bold text-lg">{{ episode.title }}</h3>
                                <div class="mt-2 text-sm text-gray-500 flex items-center space-x-3">
                                    <span>{{ formatDate(episode.publishDate) }}</span>
                                    <span v-if="episode.duration">• {{ formatDuration(episode.duration) }}</span>
                                </div>
                                <p v-if="episode.description" class="mt-2 text-gray-600 line-clamp-3">{{ episode.description }}</p>
                                <div v-if="episode.audioUrl" class="mt-3">
                                    <audio controls class="w-full" preload="none">
                                        <source :src="episode.audioUrl" type="audio/mpeg">
                                        您的瀏覽器不支援音訊播放功能
                                    </audio>
                                </div>
                            </div>
                        </div>

                        <div v-else class="text-center py-10 border border-dashed border-gray-300 rounded-lg">
                            <svg xmlns="http://www.w3.org/2000/svg" class="mx-auto h-12 w-12 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
                            </svg>
                            <h3 class="mt-2 text-sm font-medium text-gray-900">暫無集數資訊</h3>
                            <p class="mt-1 text-sm text-gray-500">
                                此播客沒有提供集數資訊或集數資訊無法載入
                            </p>
                            <p class="mt-6">
                                <a v-if="podcast.feedUrl" :href="podcast.feedUrl" target="_blank" rel="noopener noreferrer" class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700">
                                    前往原始 RSS Feed
                                </a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </AppLayout>
</template>
