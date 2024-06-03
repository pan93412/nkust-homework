export function App() {
  return (
    <main style={{
      margin: "20px",
      fontFamily: "sans-serif",
    }}>
      <form>
        <div style={{
          marginBottom: "12px",
        }}>
          <label htmlFor="username">Username:</label>
          <input type="text" id="username" name="username" />
        </div>

        <div style={{
          marginBottom: "12px",
        }}>
        <label htmlFor="age">Age:</label>
        <input type="number" id="age" name="age" min="1" max="200" />
        </div>

        <div style={{
          marginBottom: "12px",
        }}>
          <label htmlFor="country">Country or Region:</label>
          <select id="country" name="country">
            <option value="taiwan">Taiwan</option>
            <option value="usa">USA</option>
            <option value="uk">UK</option>
          </select>
        </div>

        <div>
          <input type="submit" value="Submit" />
        </div>
      </form>
    </main>
  );
}
