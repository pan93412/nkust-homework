import {
  Button,
  Text,
  View,
  Alert,
  Platform,
  TextInput,
  useWindowDimensions,
} from "react-native";

export default function WindowDimensionPage() {
  const windowDimension = useWindowDimensions();

  return (
    <View
      style={{
        flex: 1,
        gap: 4,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text style={{ fontSize: 20 }}>視窗資訊</Text>

      <Text>視窗寬度：{windowDimension.height}</Text>
      <Text>視窗高度：{windowDimension.width}</Text>
      <Text>縮放比例：{windowDimension.scale}</Text>
      <Text>文字縮放比例：{windowDimension.fontScale}</Text>
    </View>
  );
}
