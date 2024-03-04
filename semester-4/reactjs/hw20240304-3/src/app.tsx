import { effect, signal } from "@preact/signals";

export function Timer() {
  const time = signal(new Date().toLocaleTimeString());

  effect(() => {
    const interval = setInterval(() => {
      time.value = new Date().toLocaleTimeString();
    }, 1000);

    return () => clearInterval(interval);
  });

  return <p>Current time: {time}</p>;
}
export function App() {
  return (
    <div>
      <Timer />
    </div>
  );
}
