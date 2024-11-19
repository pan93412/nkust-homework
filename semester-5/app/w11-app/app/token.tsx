import { useAsyncStorage } from "@react-native-async-storage/async-storage";
import { useEffect, useState } from "react";
import { View, Text, Button } from "react-native";

export default function Token() {
  const asyncStorage = useAsyncStorage("token");
  const [token, setToken] = useState<string | null>(null);

  useEffect(() => {
    asyncStorage.getItem().then((result) => {
      console.log("Token retrieved.");
      setToken(result);
    })
  }, []);

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text>Token: {token}</Text>

      <Button
        title="Set token"
        onPress={async () => {
          await asyncStorage.setItem("my-token");
          setToken("my-token");
        }}
      />
      <Button
        title="Remove token"
        onPress={async () => {
          await asyncStorage.removeItem();
          setToken(null);
        }}
      />
    </View>
  );
}
