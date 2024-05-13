import "./app.css";
import { Counter } from "./calc";
import { useDivStore, useMinusStore, useMulStore, usePlusStore } from "./store";

export function App() {
  return (
    <div className="counters">
      <Counter useStore={usePlusStore} symbol="+" />
      <Counter useStore={useMinusStore} symbol="-" />
      <Counter useStore={useMulStore} symbol="×" />
      <Counter useStore={useDivStore} symbol="÷" />
    </div>
  );
}
