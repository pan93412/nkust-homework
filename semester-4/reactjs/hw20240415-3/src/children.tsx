import { useContext } from "preact/hooks";
import { NameContext } from "./context";

export function NameDisplayer() {
    const context = useContext(NameContext);
    return <h1 style={{ textAlign: 'center' }}>{context}</h1>;
}
