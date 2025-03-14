<div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
    <div class="p-8 bg-white rounded-lg shadow-md">
        <h1 class="text-4xl font-bold text-center mb-6">Counter</h1>

        <div class="flex items-center justify-center space-x-6">
            <button
                wire:click="decrement2"
                class="px-6 py-2 text-2xl font-bold text-white bg-red-700 rounded-lg hover:bg-red-800 transition-colors"
            >
                -2
            </button>

            <button
                wire:click="decrement"
                class="px-6 py-2 text-2xl font-bold text-white bg-red-500 rounded-lg hover:bg-red-600 transition-colors"
            >
                -1
            </button>

            <span class="text-5xl font-bold text-gray-700">{{ $count }}</span>

            <button
                wire:click="increment"
                class="px-6 py-2 text-2xl font-bold text-white bg-green-500 rounded-lg hover:bg-green-600 transition-colors"
            >
                +1
            </button>
            <button
                wire:click="increment2"
                class="px-6 py-2 text-2xl font-bold text-white bg-green-700 rounded-lg hover:bg-green-800 transition-colors"
            >
                +2
            </button>
        </div>
    </div>
</div>
