import { Link } from "expo-router";
import { Button, View } from "react-native";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Link href="/profile" asChild><Button title="Go to Profile" /></Link>
      <Link href="/portfollo" asChild><Button title="Go to Portfollo" /></Link>
    </View>
  );
}
