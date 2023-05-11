import { expect, test } from "vitest";
import { calculateRewards } from "./rewards";

test("buy=1, sell=2, reward=>0.989725", () => {
  expect(calculateRewards(1, 2)).toBeCloseTo(0.989725, 6);
});
