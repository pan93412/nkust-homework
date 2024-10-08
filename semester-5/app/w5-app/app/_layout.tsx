import { Stack } from "expo-router";

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="index" options={{ title: "哈囉！", headerLargeTitle: true }} />
    </Stack>
  );
}
