import { ReactNode, useState } from "react";
import { ActivityIndicator, Modal, StyleSheet, Switch, Text, View } from "react-native";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
      }}
    >
      <View style={{ flexDirection: "row", flex: 1 }}>
        <View style={{ flex: 1, backgroundColor: "powderblue" }}></View>
        <View style={{ flex: 2, backgroundColor: "skyblue" }}></View>
        <View style={{ flex: 3, backgroundColor: "steelblue" }}></View>
      </View>
      <View style={{ flexDirection: "row-reverse", flex: 2 }}>
        <View style={{ flex: 1, backgroundColor: "powderblue" }}></View>
        <View style={{ flex: 2, backgroundColor: "skyblue" }}></View>
        <View style={{ flex: 3, backgroundColor: "steelblue" }}></View>
      </View>
      <View style={{ flexDirection: "row", flex: 3 }}>
        <View style={{ flex: 1, backgroundColor: "powderblue" }}></View>
        <View style={{ flex: 2, backgroundColor: "skyblue" }}></View>
        <View style={{ flex: 3, backgroundColor: "steelblue" }}></View>
      </View>
    </View>
  );
}

export interface ComponentPracticeProps {
  children: ReactNode;
  onPress: () => void;
  fontSize?: number;
}

export function ComponentPractice({
  fontSize = 20,
  ...props
}: ComponentPracticeProps) {
  return (
    <Text
      style={{
        color: "red",
        fontSize: fontSize,
        fontWeight: "bold",
        textAlign: "center",
      }}
      onPress={props.onPress}
    >
      {props.children}
    </Text>
  );
}

const styles = StyleSheet.create({
  red: {
    color: "red",
  },
  bigBlue: {
    color: "blue",
    fontWeight: "bold",
    fontSize: 30,
  }
})
