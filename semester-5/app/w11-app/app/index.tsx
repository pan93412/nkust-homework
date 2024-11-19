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
      <Link href="/use-effect">打開作業 1: useEffect</Link>
      <Link href="/fetch">打開作業 2: fetch</Link>
    </View>
  );
}
