import { decrement, increment } from "./slices/counter";
import { useAppDispatch, useAppSelector } from "./storage";
import "./counter.css";

export function Counter() {
  const count = useAppSelector((state) => state.counter.value);
  const dispatch = useAppDispatch();

  return (
    <section className="counter">
      <div>
        <button onClick={() => dispatch(increment())}>+1</button>
      </div>
      <div>{count}</div>
      <div>
        <button onClick={() => dispatch(decrement())}>-1</button>
      </div>
    </section>
  );
}
