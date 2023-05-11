import { test, expect } from "@playwright/experimental-ct-vue";
import RewardsUI from "./rewards-ui.vue";

test("should work when pressing [計算]", async ({ mount }) => {
  const component = await mount(RewardsUI);

  const buy = component.getByLabel("股票買入價格：");
  const sell = component.getByLabel("股票賣出價格：");
  const submit = component.getByRole("button", {
    name: "計算",
  });
  const rewards = component.getByLabel("報酬率：");

  await buy.fill("1");
  await sell.fill("2");
  await submit.click();
  expect(await rewards.inputValue()).toBe("0.989725");
});

test("should work when entering on sell", async ({ mount }) => {
  const component = await mount(RewardsUI);

  const buy = component.getByLabel("股票買入價格：");
  const sell = component.getByLabel("股票賣出價格：");
  const rewards = component.getByLabel("報酬率：");

  await buy.fill("1");
  await sell.fill("2");
  await sell.press("Enter");
  expect(await rewards.inputValue()).toBe("0.989725");
});
