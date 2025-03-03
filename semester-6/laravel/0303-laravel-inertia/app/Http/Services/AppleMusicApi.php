<?php

namespace App\Http\Services;

use Illuminate\Support\Facades\Http;
use Illuminate\Http\Client\RequestException;

class AppleMusicApi
{
    /**
     * 根據ID查找播客
     * 使用公開的iTunes API搜尋，不需要認證
     *
     * @param string $id 播客ID (iTunes/Apple Podcast ID)
     * @return array|null 播客資訊，若找不到則返回null
     * @throws \Exception 當API請求失敗時
     */
    public function findPodcast(string $id): ?array
    {
        try {
            $response = Http::get('https://itunes.apple.com/lookup', [
                'id' => $id,
                'entity' => 'podcast',
                'country' => 'TW',
            ]);

            if ($response->successful() && isset($response['resultCount']) && $response['resultCount'] > 0) {
                return $response['results'][0];
            }

            return null;
        } catch (RequestException $e) {
            throw new \Exception('無法取得播客資訊: ' . $e->getMessage());
        }
    }

    /**
     * 搜尋播客
     *
     * @param string $term 搜尋關鍵字
     * @param int $limit 結果數量限制
     * @return array 播客搜尋結果
     * @throws \Exception 當API請求失敗時
     */
    public function searchPodcasts(string $term, int $limit = 10): array
    {
        try {
            $response = Http::get('https://itunes.apple.com/search', [
                'term' => $term,
                'media' => 'podcast',
                'entity' => 'podcast',
                'limit' => $limit,
                'country' => 'TW',
            ]);

            if ($response->successful()) {
                return $response->json('results', []);
            }

            return [];
        } catch (RequestException $e) {
            throw new \Exception('無法搜尋播客: ' . $e->getMessage());
        }
    }
}
