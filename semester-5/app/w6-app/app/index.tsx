import {
  Text,
  TouchableHighlight,
  TouchableOpacity,
  View,
  StyleSheet,
  TouchableWithoutFeedback,
  TouchableNativeFeedback,
  Pressable,
  ScrollView,
  Image,
  SafeAreaView,
} from "react-native";
import { FlatList, GestureHandlerRootView } from "react-native-gesture-handler";

export default function Index() {
  const data = (new Array(2000)).fill(null).map(
    (_, index) => ({ key: index, data: `Data ${Math.ceil(Math.random() * 600_000_000_000)}` })
  );

  return (
    <GestureHandlerRootView>
      <SafeAreaView style={styles.container}>
        <FlatList
          data={data}
          renderItem={({ item }) => (
            <View style={{ marginTop: 10, alignItems: "center" }}>
              <Text>{item.key}</Text>
              <Text>{item.data}</Text>
            </View>
          )}
        />
      </SafeAreaView>
    </GestureHandlerRootView>
  );
}

var styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    gap: 4,
  },
});
