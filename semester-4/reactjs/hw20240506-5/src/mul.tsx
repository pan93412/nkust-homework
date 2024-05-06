import { useMulStore } from "./store";
import "./mul.css";

export function Counter() {
  const a = useMulStore((state) => state.a);
  const b = useMulStore((state) => state.b);
  const c = useMulStore((state) => state.c);

  const result = useMulStore((state) => state.result);
  const multiply = useMulStore((state) => state.multiply);

  return (
      <section className="multiply">
        <input type="number" value={a} onChange={(e) => multiply("a", e.target.valueAsNumber)} />
        <div>×</div>
        <input type="number" value={b} onChange={(e) => multiply("b", e.target.valueAsNumber)} />
        <div>×</div>
        <input type="number" value={c} onChange={(e) => multiply("c", e.target.valueAsNumber)} />
        <div>=</div>
        <input type="number" value={result()} readOnly />
      </section>
  );
}
