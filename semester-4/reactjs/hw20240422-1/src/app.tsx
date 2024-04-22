import "./app.css";
import { useEffect, useRef, useState } from "preact/hooks";
import { ContextChildrenDemo } from "./children";
import { AgeContext, ColorContext, UsernameContext } from "./context";

export function App() {
  const [username, setUsername] = useState("");
  const [age, setAge] = useState(0);
  const [color, setColor] = useState("black");

  // only triggered for the first render
  const timeout = useRef<number>();
  useEffect(() => {
    timeout.current = setTimeout(() => {
      alert("First render");
    }, 50);

    return () => {
      clearTimeout(timeout.current);
    };
  }, []);

  return (
    <UsernameContext.Provider value={username}>
      <AgeContext.Provider value={age}>
        <ColorContext.Provider value={color}>
          <ContextChildrenDemo
            Title={({ children }) => <h1>{children}</h1>}
            mark="1"
          >
            <ContextChildrenDemo
              Title={({ children }) => <h2>{children}</h2>}
              mark="1.1"
            >
              <ContextChildrenDemo
                Title={({ children }) => <h3>{children}</h3>}
                mark="1.1.1"
              ></ContextChildrenDemo>
              <ContextChildrenDemo
                Title={({ children }) => <h3>{children}</h3>}
                mark="1.1.2"
              ></ContextChildrenDemo>
              <ContextChildrenDemo
                Title={({ children }) => <h2>{children}</h2>}
                mark="1.1"
              ></ContextChildrenDemo>
              <ContextChildrenDemo
                Title={({ children }) => <h2>{children}</h2>}
                mark="1.2"
              ></ContextChildrenDemo>
            </ContextChildrenDemo>
            <ContextChildrenDemo
              Title={({ children }) => <h1>{children}</h1>}
              mark="2"
            >
              <ContextChildrenDemo
                Title={({ children }) => <h2>{children}</h2>}
                mark="2.1"
              >
                <ContextChildrenDemo
                  Title={({ children }) => <h2>{children}</h2>}
                  mark="2.1.1"
                ></ContextChildrenDemo>
              </ContextChildrenDemo>
              <ContextChildrenDemo
                Title={({ children }) => <h2>{children}</h2>}
                mark="2.2"
              >
                <ContextChildrenDemo
                  Title={({ children }) => <h2>{children}</h2>}
                  mark="2.2.1"
                ></ContextChildrenDemo>
              </ContextChildrenDemo>
            </ContextChildrenDemo>
          </ContextChildrenDemo>
          <input
            type="input"
            value={username}
            onInput={(e) => setUsername(e.currentTarget.value)}
            placeholder="Username…"
          />
          <input
            type="number"
            value={age}
            onInput={(e) => setAge(e.currentTarget.valueAsNumber)}
            placeholder="Age…"
          />
          <input
            type="color"
            value={color}
            onInput={(e) => setColor(e.currentTarget.value)}
            placeholder="Color…"
          />
        </ColorContext.Provider>
      </AgeContext.Provider>
    </UsernameContext.Provider>
  );
}
