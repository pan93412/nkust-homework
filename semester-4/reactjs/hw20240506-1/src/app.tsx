import "./app.css";
import { store } from "./storage";
import { Provider } from "react-redux";
import { Counter } from "./counter";

export function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  )
}
