import { Link } from "expo-router";
import { Text, View } from "react-native";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Link href="/buttons">Hw1: Component Style, Button</Link>
      <Link href="/bottom-sheet">Hw2: Bottom Sheet</Link>
      <Link href="/badge">Hw3: Badge</Link>
    </View>
  );
}
