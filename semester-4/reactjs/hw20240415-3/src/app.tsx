import "./app.css";
import { useContext, useState } from "preact/hooks";
import { NameContext } from "./context";
import { NameDisplayer } from "./children";

export function App() {
  const context = useContext(NameContext);
  const [value, setValue] = useState<string | null>(null);

  return (
    <NameContext.Provider value={value ?? context}>
      <NameDisplayer />

      <button onClick={() => setValue("a")}>a</button>
      <button onClick={() => setValue("b")}>b</button>
      <button onClick={() => setValue("c")}>c</button>
    </NameContext.Provider>
  );
}
