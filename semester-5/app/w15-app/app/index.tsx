import { Link, Stack } from "expo-router";
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
      <Stack.Screen options={{ title: "首頁" }} />
      <Link href="/card" asChild>
        <Button title="Homework 1: Card" />
      </Link>
      <Link href="/dialog" asChild>
        <Button title="Homework 2: Dialog" />
      </Link>
    </View>
  );
}
