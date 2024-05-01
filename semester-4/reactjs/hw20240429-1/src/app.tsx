import "./app.css";
import { useEffect, useState } from "preact/hooks";

export function App() {
  const [number1, setNumber1] = useState(0);
  const [number2, setNumber2] = useState(0);
  const [number3, setNumber3] = useState(0);

  useEffect(() => {
    console.log("Appending number 2 %d to number 1", number2);
    setNumber1((number1) => number1 + number2);
  }, [number2]);

  useEffect(() => {
    console.log("Number 1 (%d) or Number 3 (%d) has been changed.", number1, number3)
  }, [number1, number3])

  return (
    <section>
      <div style={{
        color: number1 > 100 ? "red" : "black"
      }}>
        Number 1: {number1}
        <button onClick={() => setNumber1((number1) => number1 + 1)}>+1</button>
      </div>
      <div>
        Number 2: {number2}
        <button onClick={() => setNumber2((number2) => number2 + 1)}>+1</button>
      </div>
      <div>
        Number 3: {number3}
        <button onClick={() => setNumber3((number3) => number3 + 1)}>+1</button>
      </div>
    </section>
  );
}
