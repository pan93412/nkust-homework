import { useContext, useEffect } from "preact/hooks";
import { AgeContext, ColorContext, UsernameContext } from "./context";
import { ComponentChildren, FunctionComponent } from "preact";

export function ContextChildrenDemo({
  mark,
  children,
  Title,
}: {
  mark: string;
  children?: ComponentChildren;
  Title: FunctionComponent;
}) {
  const username = useContext(UsernameContext);
  const color = useContext(ColorContext);
  const age = useContext(AgeContext);

  console.log(`ContextChildrenDemo ${mark} render`);
  useEffect(() => {
    console.log(`ContextChildrenDemo ${mark} mounted`);
    return () => {
      console.log(`ContextChildrenDemo ${mark} unmounted`);
    };
  });

  return (
    <section>
      <Title>Children {mark}</Title>
      <p
        style={{
          color: color,
        }}
      >
        {username} (Age {age})
      </p>
      <section>
        {children}
      </section>
    </section>
  );
}
