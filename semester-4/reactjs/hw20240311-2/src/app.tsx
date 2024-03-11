import { signal } from "@preact/signals";

export function App() {
  const base = signal(50);
  const balance = signal(0);

  const addBalance = () => {
    balance.value = balance.value + base.value;
  };

  const subtractBalance = () => {
    if (balance.value < base.value) {
      alert("You don't have enough balance");
      return;
    }

    balance.value = balance.value - base.value;
  };

  return (
    <div className="font-sans p-8 text-2xl">
      <section className="text-center">
        <h1>Deposit</h1>
        <p>Balance: {balance}</p>

        <div>
          <input
            type="range"
            min="10"
            max="200"
            step="5"
            value={base}
            onChange={(e) => base.value = parseInt(e.currentTarget.value)}
          />
          <span>${base}</span>
          <br />
          <button className="text-xl" onClick={addBalance}>
            Deposit
          </button>
          <button className="text-xl" onClick={subtractBalance}>
            Withdraw
          </button>
        </div>
      </section>
    </div>
  );
}
