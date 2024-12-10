import React, { useState } from "react";
import { BottomSheet, Button, ListItem } from "@rneui/themed";
import { StyleSheet } from "react-native";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { Stack } from "expo-router";

type BottomSheetComponentProps = {};

const BottomSheetComponent: React.FunctionComponent<
    BottomSheetComponentProps
> = () => {
    const [isVisible, setIsVisible] = useState(false);
    const list = [
        { title: "選項 1" },
        { title: "選項 2" },
        {
            title: "取消",
            containerStyle: { backgroundColor: "#ff4444" },
            titleStyle: { color: "white" },
            onPress: () => setIsVisible(false),
        },
    ];

    return (
        <SafeAreaProvider>
            <Stack.Screen options={{ title: "底部彈出視窗" }} />
            <Button
                title="開啟底部選單"
                onPress={() => setIsVisible(true)}
                buttonStyle={styles.button}
            />
            <BottomSheet modalProps={{}} isVisible={isVisible}>
                {list.map((l, i) => (
                    <ListItem
                        key={i}
                        containerStyle={[styles.listItem, l.containerStyle]}
                        onPress={l.onPress}
                    >
                        <ListItem.Content>
                            <ListItem.Title style={[styles.listItemTitle, l.titleStyle]}>
                                {l.title}
                            </ListItem.Title>
                        </ListItem.Content>
                    </ListItem>
                ))}
            </BottomSheet>
        </SafeAreaProvider>
    );
};

const styles = StyleSheet.create({
    button: {
        margin: 10,
        backgroundColor: "#2089dc",
        borderRadius: 8,
        paddingVertical: 12,
    },
    listItem: {
        paddingVertical: 15,
        borderBottomWidth: 1,
        borderBottomColor: "#e0e0e0",
    },
    listItemTitle: {
        fontSize: 16,
        textAlign: "center",
    },
});

export default BottomSheetComponent;
