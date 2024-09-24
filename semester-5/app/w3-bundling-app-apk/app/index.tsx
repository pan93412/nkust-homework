import { Text, View, StyleSheet } from "react-native";

export default function Index() {
  const name = "潘奕濬";
  const sid = "C111156103";
  const department = "智慧商務系";

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{name}</Text>
      <Text>{formatTitle(sid, department)}</Text>

      <View style={styles.demoFlex}>
        <View style={styles.demoFlexCell1}>
          <Text>flex=0.3</Text>
        </View>
        <View style={styles.demoFlexCell2}>
          <Text>flex=0.2</Text>
        </View>
        <View style={styles.demoFlexCell3}>
          <Text>flex=0.5</Text>
        </View>
      </View>
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
  demoFlex: {
    flexDirection: "row",
    borderColor: 'red',
    borderWidth: 2,
  },
  demoFlexCell1: {
    flex: 0.3,
    backgroundColor: '#e2d4b7',
  },
  demoFlexCell2: {
    flex: 0.2,
    backgroundColor: '#9c9583',
  },
  demoFlexCell3: {
    flex: 0.5,
    backgroundColor: '#b0bbbf',
  },
});
