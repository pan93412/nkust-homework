import { test, expect } from "@playwright/test";

test.beforeEach(async ({ page }) => {
  await page.goto("/");
});

test("should have a form to fill values", async ({ page }) => {
  const ui = page.getByLabel("rewards ui");
  await expect(ui).toBeVisible();
});
