<template>
  <table role="presentation" aria-label="price table">
    <tr>
      <td>小明擁有</td>
      <td colspan="2">
        <input
          id="current-have"
          v-model="currentHave"
          class="b-green-700 text-pink-8 b-2 w-1/2"
        />
      </td>
    </tr>

    <tr class="text-left">
      <th></th>
      <th>單價</th>
      <th>數量</th>
    </tr>

    <tr v-for="(price, name) in priceTable" :key="name">
      <td>{{ name }}</td>
      <td>{{ price }}</td>
      <td>
        <input
          id="current-have"
          v-model="quantityTable[name]"
          class="b-green-700 text-pink-8 b-2 w-full"
        />
      </td>
    </tr>

    <tr>
      <td>小明</td>
      <td v-if="remainings < 0" class="text-red">不足 {{ -remainings }}</td>
      <td v-else></td>
      <td v-if="remainings > 0" class="text-blue">剩下 {{ remainings }}</td>
      <td v-else></td>
    </tr>
  </table>
</template>

<script setup lang="ts">
import { computed, reactive, ref } from "vue";

const currentHave = ref(200);

const priceTable = {
  鉛筆: 20,
  橡皮擦: 15,
};

const quantityTable = reactive<typeof priceTable>({
  鉛筆: 5,
  橡皮擦: 10,
});

const remainings = computed(() => {
  let total = 0;

  for (const key in priceTable) {
    // type-guard
    if (key === "鉛筆" || key === "橡皮擦")
      total += priceTable[key] * quantityTable[key];
  }

  return currentHave.value - total;
});
</script>

<style scoped>
td,
th {
  padding: 2px 4px;
}

th {
  font-weight: inherit;
}

th,
td {
  width: 8rem;
}
</style>
