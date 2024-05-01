import "./app.css";
import { useMemo, useState } from "preact/hooks";

export function App() {
  const [number1, setNumber1] = useState(0);

  const memoGlobal = useMemo(() => {
    console.log("Memo with empty dependencies");
    return Math.random();
  }, []);
  const memoByNumber1 = useMemo(() => {
    console.log("Memo with number 1 (%d) as dependency", number1);
    return Math.random() + number1;
  }, [number1]);

  return (
    <section>
      <ul>
        <li>Memo with empty dependencies: {memoGlobal}</li>
        <li>Memo with number 1 as dependency: {memoByNumber1}</li>
      </ul>
      <div>
        Number 1: {number1}
        <button onClick={() => setNumber1((number1) => number1 + 1)}>+1</button>
      </div>
    </section>
  );
}
