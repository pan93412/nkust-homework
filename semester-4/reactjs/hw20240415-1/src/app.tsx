import "./app.css";
import { useRef } from "preact/hooks";

export function App() {
  const $name = useRef<HTMLInputElement | null>(null);
  const $age = useRef<HTMLInputElement | null>(null);
  const $color = useRef<HTMLInputElement | null>(null);
  const $birthday = useRef<HTMLInputElement | null>(null);
  const $email = useRef<HTMLInputElement | null>(null);

  return (
    <form onSubmit={(event) => {
      event.preventDefault();

      console.log("Name:", $name.current?.value);
      console.log("Age:", $age.current?.value);
      console.log("Color:", $color.current?.value);
      console.log("Birthday:", $birthday.current?.value);
      console.log("Email:", $email.current?.value);
    }}>
      <div>
        <label>
          Name:
          <input type="text" name="name" ref={$name} />
        </label>
      </div>
      <div>
        <label>
          Age:
          <input type="number" name="age" ref={$age} />
        </label>
      </div>
      <div>
        <label>
          Favorite color
          <input type="color" name="color" ref={$color} />
        </label>
      </div>
      <div>
        <label>
          Birthday
          <input type="date" name="birthday" ref={$birthday} />
        </label>
      </div>
      <div>
        <label>
          Email
          <input type="email" name="email" ref={$email} />
        </label>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  );
}
