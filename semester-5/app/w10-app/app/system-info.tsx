import { Button, Text, View, Alert, Platform, TextInput } from "react-native";

export default function SystemInfoPage() {
  return (
    <View
      style={{
        flex: 1,
        gap: 4,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text style={{fontSize: 20}}>系統資訊</Text>

      <Text>平台：{Platform.OS}</Text>
      <Text>版本：{Platform.Version}</Text>
      <Text>電視平台？{Platform.isTV}</Text>

      <Text>所有屬性：</Text>
      <TextInput multiline style={{
        fontSize: 12,
        fontFamily: "Courier New",
      }} value={JSON.stringify(Platform.constants, null, 4)} readOnly />
    </View>
  );
}
