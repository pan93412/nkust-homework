import { StyleSheet, View, Image } from "react-native";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        flexWrap: 'wrap',
        gap: 40,
      }}
    >
      <Image source={require('../assets/images/react-logo.png')} style={styles.image} />
      <Image source={require('../assets/images/icon.png')} style={styles.image} />
      <Image source={require('../assets/images/react-logo.png')} style={styles.image} />
    </View>
  );
}

const styles = StyleSheet.create({
  image: {
    width: 120,
    height: 120,
    padding: 40,
  }
})
