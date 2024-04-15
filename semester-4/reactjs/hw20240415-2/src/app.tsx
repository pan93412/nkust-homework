import { signal } from "@preact/signals";
import "./app.css";

export function App() {
  const name = signal("");
  const age = signal(0);
  const color = signal("");
  const birthday = signal("");
  const email = signal("");

  return (
    <form onSubmit={(event) => {
      event.preventDefault();

      console.log("Name:", name.value);
      console.log("Age:", age.value);
      console.log("Color:", color.value);
      console.log("Birthday:", birthday.value);
      console.log("Email:", email.value);
    }}>
      <div>
        <label>
          Name:
          <input type="text" name="name" value={name} onChange={(event) => {
            name.value = event.currentTarget.value;
          }} />
        </label>
      </div>
      <div>
        <label>
          Age:
          <input type="number" name="age" value={age} onChange={(event) => {
            age.value = event.currentTarget.valueAsNumber;
          }} />
        </label>
      </div>
      <div>
        <label>
          Favorite color
          <input type="color" name="color" value={color} onChange={(event) => {
            color.value = event.currentTarget.value;
          }}/>
        </label>
      </div>
      <div>
        <label>
          Birthday
          <input type="date" name="birthday" value={birthday} onChange={(event) => {
            birthday.value = event.currentTarget.value;
          }}/>
        </label>
      </div>
      <div>
        <label>
          Email
          <input type="email" name="email" value={email} onChange={(event) => {
            email.value = event.currentTarget.value;
          }}/>
        </label>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  );
}
