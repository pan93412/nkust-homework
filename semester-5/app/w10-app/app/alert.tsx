import { Button, Text, View, Alert } from "react-native";

export default function AlertPage() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Button title="Show alert" onPress={() => Alert.alert(
        "測試 Alert",
        "哈囉！",
        [
          { text: "OK", onPress: () => console.log("OK") },
          { text: "Cancel", onPress: () => console.log("Cancel") },
        ]
      )} />
    </View>
  );
}
