import { countAtom } from "@/atoms/countAtom";
import { Link } from "expo-router";
import { useAtom } from "jotai";
import React from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Button,
} from "react-native";

export default function Home() {
  const [count, setCount] = useAtom(countAtom);

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>Welcome to My App</Text>
      </View>

      <View style={styles.content}>
        <Text style={styles.paragraph}>
          This is a demo React Native page with some basic styling and
          components.
        </Text>

        <Link href="/demo">
          <Text style={styles.button}>Open Modal</Text>
        </Link>

        <Text style={styles.paragraph}>Count: {count}</Text>
        <Button title="+1" onPress={() => setCount((c) => c + 1)} />
        <Button title="-1" onPress={() => setCount((c) => c - 1)} />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
  },
  header: {
    padding: 20,
    backgroundColor: "#2196F3",
    alignItems: "center",
  },
  headerText: {
    fontSize: 24,
    color: "white",
    fontWeight: "bold",
  },
  content: {
    padding: 20,
    alignItems: "center",
  },
  paragraph: {
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 20,
    textAlign: "center",
  },
  button: {
    backgroundColor: "#4CAF50",
    padding: 15,
    borderRadius: 8,
    width: 200,
    alignItems: "center",
  },
  buttonText: {
    color: "white",
    fontSize: 16,
    fontWeight: "bold",
  },
});
