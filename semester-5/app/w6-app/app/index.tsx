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

export default function Index() {
  return (
    <SafeAreaView>
      <ScrollView>
        <View style={styles.container}>
          <Image
            style={styles.reactLogo}
            source={require("../assets/images/react-logo.png")}
          />
          <Image
            style={styles.reactLogo}
            resizeMode="contain"
            source={require("../assets/images/react-logo.png")}
          />
          <Image
            style={styles.reactLogo}
            resizeMode="center"
            source={require("../assets/images/react-logo.png")}
          />

          <TouchableHighlight
            style={styles.fakeButton}
            underlayColor="gray"
            activeOpacity={0.7}
            onPress={() => console.log("TouchableHighlight")}
          >
            <Text>TouchableHighlight</Text>
          </TouchableHighlight>

          <TouchableOpacity
            style={styles.fakeButton}
            activeOpacity={0.7}
            onPress={() => console.log("TouchableOpacity")}
          >
            <Text>TouchableOpacity</Text>
          </TouchableOpacity>

          <Pressable
            style={styles.fakeButton}
            onPress={() => console.log("Pressable")}
          >
            <Text>Pressable</Text>
          </Pressable>

          <TouchableNativeFeedback
            style={styles.fakeButton}
            onPress={() => console.log("TouchableNativeFeedback")}
            background={TouchableNativeFeedback.Ripple("gray", false)}
          >
            <Text>TouchableNativeFeedback</Text>
          </TouchableNativeFeedback>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

var styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    gap: 4,
  },
  fakeButton: {
    height: 100,
    width: 100,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "lightgray",
  },
  reactLogo: {
    height: 100,
    width: 50,
  },
});
