import { useCounter2Store, useCounterStore } from "./store";
import "./counter.css";

export function Counter() {
  const count = useCounterStore((state) => state.count);
  const increment = useCounterStore((state) => state.increment);
  const decrement = useCounterStore((state) => state.decrement);
  const incrementByAmount = useCounterStore((state) => state.incrementByAmount);

  const count2 = useCounter2Store((state) => state.count);
  const increment2 = useCounter2Store((state) => state.incrementTwo);
  const decrement2 = useCounter2Store((state) => state.decrementTwo);

  return (
    <div className="counter-block">
      <section className="counter">
        <div>
          <button onClick={() => increment()}>+1</button>
        </div>
        <div>{count}</div>
        <div>
          <button onClick={() => decrement()}>-1</button>
        </div>
      </section>
      <section className="counter-increment">
        <form onSubmit={(e) => {
          e.preventDefault();
          const form = new FormData(e.currentTarget);

          const amount = form.get("amount");
          if (!amount || typeof amount !== "string") {
            return;
          }

          incrementByAmount(parseInt(amount));
          e.currentTarget.reset();
        }}>
          <input name="amount" type="number" placeholder="Amount to add…" />
        </form>
      </section>
      <section className="counter2">
        <div>
          <button onClick={() => increment2()}>+2</button>
        </div>
        <div>{count2}</div>
        <div>
          <button onClick={() => decrement2()}>-2</button>
        </div>
      </section>
    </div>
  );
}
