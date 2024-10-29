import { ReactNode, useState } from "react";
import { ActivityIndicator, Modal, Switch, Text, View } from "react-native";

export default function Index() {
  const [switchOp, setSwitchOp] = useState(false);

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        gap: 8,
      }}
    >
      <Modal visible={switchOp} animationType="slide">
        <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
          <Text>Modal</Text>
          <Switch value={switchOp} onValueChange={setSwitchOp} />
        </View>
      </Modal>

      <ComponentPractice fontSize={36} onPress={() => alert(`Hello, ${switchOp ? 'world' : 'owo'}!`)}>
        Hello, World!
      </ComponentPractice>

      <Switch value={switchOp} onValueChange={setSwitchOp} />

      <ActivityIndicator />
      <ActivityIndicator size="large" />
      <ActivityIndicator size="small" />
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
