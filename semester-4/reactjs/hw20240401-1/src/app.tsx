import { signal } from "@preact/signals";
import { IntroCard, NegativeButton, PositiveButton, Title } from "./components/intro.tsx";
import { StarIdentifier } from "./components/star.tsx";

export function App() {
  const n = signal(0);
  const star = signal(0);

  return (
    <main>
      <IntroCard>
        <Title>{n}</Title>
        <div>
          <PositiveButton onClick={() => n.value++}>+1</PositiveButton>
          <NegativeButton onClick={() => n.value--}>-1</NegativeButton>
        </div>

        <StarIdentifier activeStar={star} onSelectedStar={(selectedStar) => {
          star.value = selectedStar
        }} />
      </IntroCard>
    </main>
  );
}
