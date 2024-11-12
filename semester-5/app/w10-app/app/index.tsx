import { Link } from "expo-router";
import { View } from "react-native";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Link href="/alert">打開作業 1: Alert</Link>
      <Link href="/system-info">打開作業 2: System Information</Link>
      <Link href="/window-dimension">打開作業 3: Window Dimension</Link>
    </View>
  );
}
