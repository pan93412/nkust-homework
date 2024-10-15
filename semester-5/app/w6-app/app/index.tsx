import { useState } from "react";
import {
  View,
  StyleSheet,
  SafeAreaView,
  TextInput,
  Button,
} from "react-native";

export default function Index() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  return (
    <SafeAreaView style={styles.container}>
      <TextInput
        style={styles.textInput}
        placeholder="請輸入帳號"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.textInput}
        secureTextEntry
        placeholder="請輸入密碼"
        value={password}
        onChangeText={setPassword}
      />

      <View style={styles.buttonGroup}>
        <Button title="登入" onPress={() => {}} />
        <Button
          title="清除"
          onPress={() => {
            setUsername("");
            setPassword("");
          }}
        />
      </View>
    </SafeAreaView>
  );
}

var styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    gap: 4,
    margin: 16,
  },
  textInput: {
    borderWidth: 1,
    borderColor: "rgba(0, 0, 0, 0.6)",
    width: 200,
    height: 24,
  },
  buttonGroup: {
    flex: 1,
    flexDirection: "row",
  },
});
