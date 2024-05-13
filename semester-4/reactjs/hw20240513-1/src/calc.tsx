import { CalculateStoreHook } from "./store";
import "./calc.css";

export interface CounterProps {
  useStore: CalculateStoreHook;
  symbol: string;
}

export function Counter({ useStore, symbol }: CounterProps) {
  const a = useStore((state) => state.a);
  const b = useStore((state) => state.b);
  const c = useStore((state) => state.c);

  const result = useStore((state) => state.result);
  const pushValue = useStore((state) => state.pushValue);

  return (
      <section className="calc">
        <input type="number" value={a} onChange={(e) => pushValue("a", e.target.valueAsNumber)} />
        <div>{symbol}</div>
        <input type="number" value={b} onChange={(e) => pushValue("b", e.target.valueAsNumber)} />
        <div>{symbol}</div>
        <input type="number" value={c} onChange={(e) => pushValue("c", e.target.valueAsNumber)} />
        <div>=</div>
        <input type="number" value={result()} readOnly />
      </section>
  );
}
