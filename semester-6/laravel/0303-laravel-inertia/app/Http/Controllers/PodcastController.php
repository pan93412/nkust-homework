<?php

namespace App\Http\Controllers;

use App\Http\Services\AppleMusicApi;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Inertia\Inertia;
use Inertia\Response;

class PodcastController extends Controller
{
    protected AppleMusicApi $appleMusicApi;

    public function __construct(AppleMusicApi $appleMusicApi)
    {
        $this->appleMusicApi = $appleMusicApi;
    }

    /**
     * 顯示播客搜尋頁面
     */
    public function index(): Response
    {
        return Inertia::render('Podcasts/Index', [
            'initialResults' => [],
            'searchTerm' => '',
        ]);
    }

    /**
     * 搜尋播客
     */
    public function search(Request $request): JsonResponse
    {
        $request->validate([
            'term' => 'required|string|min:2|max:100',
            'limit' => 'sometimes|integer|min:1|max:50',
        ]);

        $term = $request->input('term');
        $limit = $request->input('limit', 10);

        try {
            $results = $this->appleMusicApi->searchPodcasts($term, $limit);

            return response()->json([
                'success' => true,
                'data' => $results,
                'count' => count($results)
            ]);
        } catch (\Exception $e) {
            Log::error('播客搜尋失敗', [
                'term' => $term,
                'error' => $e->getMessage()
            ]);

            return response()->json([
                'success' => false,
                'message' => '無法完成搜尋，請稍後再試',
            ], 500);
        }
    }

    /**
     * 顯示單一播客詳細資訊
     */
    public function show(string $id): Response|JsonResponse
    {
        try {
            $podcast = $this->appleMusicApi->findPodcast($id);

            if (!$podcast) {
                return response()->json([
                    'success' => false,
                    'message' => '找不到指定的播客',
                ], 404);
            }

            return Inertia::render('Podcasts/Show', [
                'podcast' => $podcast
            ]);
        } catch (\Exception $e) {
            Log::error('取得播客資訊失敗', [
                'podcast_id' => $id,
                'error' => $e->getMessage()
            ]);

            return response()->json([
                'success' => false,
                'message' => '無法取得播客資訊，請稍後再試',
            ], 500);
        }
    }

    /**
     * API端點：取得播客資訊
     */
    public function getPodcast(string $id): JsonResponse
    {
        try {
            $podcast = $this->appleMusicApi->findPodcast($id);

            if (!$podcast) {
                return response()->json([
                    'success' => false,
                    'message' => '找不到指定的播客',
                ], 404);
            }

            return response()->json([
                'success' => true,
                'data' => $podcast
            ]);
        } catch (\Exception $e) {
            Log::error('API取得播客資訊失敗', [
                'podcast_id' => $id,
                'error' => $e->getMessage()
            ]);

            return response()->json([
                'success' => false,
                'message' => '無法取得播客資訊，請稍後再試',
            ], 500);
        }
    }
}
