import { Link } from "expo-router";
import React from "react";
import { View, Text, StyleSheet, Image, ScrollView, Button } from "react-native";

export default function ProfileScreen() {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Image
          source={{ uri: "https://placekitten.com/200/200" }}
          style={styles.profileImage}
        />
        <Text style={styles.name}>John Doe</Text>
        <Text style={styles.title}>Software Developer</Text>

        <Link href="/portfollo" asChild>
          <Button title="Go to Portfollo" />
        </Link>
      </View>

      <View style={styles.infoSection}>
        <Text style={styles.sectionTitle}>About Me</Text>
        <Text style={styles.infoText}>
          Passionate software developer with experience in React Native and
          mobile development. Love to create beautiful and functional
          applications.
        </Text>
      </View>

      <View style={styles.infoSection}>
        <Text style={styles.sectionTitle}>Contact Information</Text>
        <Text style={styles.infoText}>Email: john.doe@example.com</Text>
        <Text style={styles.infoText}>Phone: (123) 456-7890</Text>
        <Text style={styles.infoText}>Location: New York, USA</Text>
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
    alignItems: "center",
    padding: 20,
    backgroundColor: "#fff",
  },
  profileImage: {
    width: 150,
    height: 150,
    borderRadius: 75,
    marginBottom: 15,
  },
  name: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 5,
  },
  title: {
    fontSize: 16,
    color: "#666",
    marginBottom: 10,
  },
  infoSection: {
    backgroundColor: "#fff",
    padding: 20,
    marginTop: 20,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "bold",
    marginBottom: 10,
  },
  infoText: {
    fontSize: 16,
    color: "#333",
    marginBottom: 5,
  },
});
