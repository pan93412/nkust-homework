const BUY_REWARD = 0.001425;
const SELL_REWARD = 0.004425;

/**
 * Calculate the rewards.
 */
export function calculateRewards(buy: number, sell: number): number {
  return (sell - buy - BUY_REWARD * buy - SELL_REWARD * sell) / buy;
}
