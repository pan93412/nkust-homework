import {
  Appearance,
  Text,
  View,
} from "react-native";

export default function AppearancePage() {
  const colorScheme = Appearance.getColorScheme();

  return (
    <View
      style={{
        flex: 1,
        gap: 4,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text style={{ fontSize: 20 }}>偏好色彩資訊</Text>
      <Text>使用者偏好 {colorScheme === 'light' ? '亮色' : '暗色'} 背景。</Text>
    </View>
  );
}
