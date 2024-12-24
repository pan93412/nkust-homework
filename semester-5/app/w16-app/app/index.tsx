import { Link } from "expo-router";
import { ActivityIndicator, Button, Text, View } from "react-native";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Link href="/fab" asChild><Button title="HW1: FAB"></Button></Link>
      <Link href="/icon" asChild><Button title="HW2: Icon"></Button></Link>
      <Link href="/text-input" asChild><Button title="HW3: Text Input"></Button></Link>
      <Link href="/linear-progress" asChild><Button title="HW4: Linear Progress"></Button></Link>
    </View>
  );
}
