import { AppShell, Container } from "@mantine/core";
import TanstackForm from "./form";

export function App() {
  return (
    <AppShell
      header={{ height: 60 }}
      padding="md"
    >
      <AppShell.Main>
        <Container>
          <TanstackForm />
          <footer>C111156103, 潘奕濬</footer>
        </Container>
      </AppShell.Main>
    </AppShell>
  );
}
