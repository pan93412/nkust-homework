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
        </Container>
      </AppShell.Main>
    </AppShell>
  );
}
