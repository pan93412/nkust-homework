import { StatusBar } from "expo-status-bar";
import { useState } from "react";
import {
  Button,
  Text,
  View,
} from "react-native";

export default function StatusBarPage() {
  const styleTypes = ['auto', 'inverted', 'light', 'dark'] as const;

  const [visibleStatusBar, setVisibleStatusBar] = useState(false);
  const [styleStatusBar, setStyleStatusBar] = useState<typeof styleTypes[number]>(styleTypes[0]);

  return (
    <View
      style={{
        flex: 1,
        gap: 4,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <StatusBar style={styleStatusBar} hidden={!visibleStatusBar} />
      <View>
        <Text>StatusBar style: {styleStatusBar}</Text>
        <Text>StatusBar Visibliity: {visibleStatusBar ? 'Visible' : 'Invisible'}</Text>
      </View>
      <View>
        <Button
          title="Toggle StatusBar"
          onPress={() => setVisibleStatusBar(!visibleStatusBar)}
        />
        <Button
          title="Change StatusBar Style"
          onPress={() => {
            const index = styleTypes.indexOf(styleStatusBar);
            setStyleStatusBar(styleTypes[(index + 1) % styleTypes.length]);
          }}
        />
      </View>
    </View>
  );
}
