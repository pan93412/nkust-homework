import React from "react";
import { View, Text, StyleSheet } from "react-native";
import { Icon } from "@rneui/themed";

export default function IconPage() {
    return (
        <View style={styles.container}>
            <Icon name="rowing" style={styles.icon} />
            <Text>Rowing</Text>

            <Icon name="g-translate" color="#00aced" style={styles.icon} />
            <Text>Google Translate</Text>

            <Icon name="sc-telegram" type="evilicon" color="#517fa4" style={styles.icon} />
            <Text>Telegram</Text>

            <Icon
            reverse
            name="ios-american-football"
            type="ionicon"
            color="#517fa4"
            />
            <Text>American Football</Text>

            <Icon
            raised
            name="heartbeat"
            type="font-awesome"
            color="#f50"
            onPress={() => console.log("hello")}
            />
            <Text>Heartbeat</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        padding: 20,
        backgroundColor: "#f0f0f0",
    },
    icon: {
        margin: 10,
    },
});
