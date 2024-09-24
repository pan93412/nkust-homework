import { Text, View, StyleSheet } from "react-native";

export default function Index() {
  const name = "潘奕濬";
  const sid = "C111156103";
  const department = "智慧商務系";

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{name}</Text>
      <Text>{formatTitle(sid, department)}</Text>
    </View>
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
  title: {
    fontSize: 36,
    color: "darkblue",
    fontWeight: 'bold',
  },
});
