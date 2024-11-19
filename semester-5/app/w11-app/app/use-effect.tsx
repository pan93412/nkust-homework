import { useEffect } from "react";
import { View, Text } from "react-native";

export default function UseEffect() {
    console.log("on component created");

    useEffect(() => {
        console.log("on component mounted");

        return () => {
            console.log("on component unmounted");
        };
    });

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
        <Text>see console for details</Text>
    </View>
  );
}
