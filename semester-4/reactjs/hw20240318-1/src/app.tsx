import { Avatar, IntroCard, Title } from "./components/intro.tsx";

export function App() {
  return (
    <main>
      <IntroCard>
        <Avatar src="https://pan93.com/avatar.png" />
        <Title color="blue">潘奕濬</Title>
        <p>智商二甲 C111156103</p>
      </IntroCard>
    </main>
  );
}
