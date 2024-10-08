import { StatusBar } from "expo-status-bar";
import { useState } from "react";
import { Text, View, StyleSheet, SafeAreaView, TextInput, Button, Alert } from "react-native";

export default function Index() {
  const [account, setAccount] = useState('');
  const [password, setPassword] = useState('');

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.header}>你好，{account || "匿名者"}！</Text>
      <TextInput style={styles.textInput} onChangeText={setAccount} value={account} placeholder="請輸入帳號" />
      <TextInput style={styles.textInput} onChangeText={setPassword} value={password} secureTextEntry placeholder="請輸入密碼" />
      <Button title="忘記密碼" onPress={() => Alert.alert("忘記密碼", `你的密碼是 ${password}`, [
        {text: '好'},
      ])} />
      <StatusBar hidden />
    </SafeAreaView>
  );
}

export function formatTitle(sid: string, department: string): string {
  return `${sid} ${department}`
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    gap: 12,
    alignItems: 'center',
    justifyContent: 'center',
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  textInput: {
    height: 30,
    width: 200,
    borderWidth: 1,
    borderColor: 'rgba(0, 0, 0, 0.4)',
    overlayColor: 'darkgray',
    borderRadius: 4,
    paddingHorizontal: 4,
  }
});
