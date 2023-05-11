<template>
  <form aria-label="rewards ui" @submit="handleSubmit">
    <label for="buy-price">股票買入價格：</label>
    <input id="buy-price" v-model="buyPrice" type="number" />

    <label for="sell-price">股票賣出價格：</label>
    <input id="sell-price" v-model="sellPrice" type="number" />

    <button type="submit">計算</button>

    <label>
      報酬率：
      <input v-model="rewardRate" type="number" readonly />
    </label>
  </form>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { calculateRewards } from "./rewards";

const buyPrice = ref(0);
const sellPrice = ref(0);
const rewardRate = ref(0);

const handleSubmit = (e: Event) => {
  e.preventDefault();
  rewardRate.value = calculateRewards(buyPrice.value, sellPrice.value);
};
</script>
