import type { Nominal } from "nominal-types";

export type Height = Nominal<"height-cm", number>;
export type Weight = Nominal<"weight-kg", number>;
export type Bmi = Nominal<"bmi", number>

export function calculateBmi(height: Height, weight: Weight): Bmi {
  const heightM = height / 100;

  const bmi = weight / (heightM * heightM);

  return bmi as Bmi;
}

export function renderBmi(bmi: Bmi): string {
  return bmi.toFixed(2);
}
