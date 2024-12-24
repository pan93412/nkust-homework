import React from "react";
import { View, StyleSheet } from "react-native";
import { Input, Icon } from "@rneui/themed";

export default function TextInputView() {
    const [text, setText] = React.useState("");

    return (
        <View style={styles.container}>
            <Input
                placeholder="基本輸入"
                inputContainerStyle={styles.inputContainer}
                inputStyle={styles.input}
            />

            <Input
                placeholder="帶圖示的輸入"
                leftIcon={<Icon type="font-awesome" name="chevron-left" style={styles.icon} />}
                inputContainerStyle={styles.inputContainer}
                inputStyle={styles.input}
            />

            <Input
                placeholder="評論"
                leftIcon={<Icon type="font-awesome" name="comment" color={text ? "darkgreen" : "darkred"} style={styles.icon} />}
                value={text}
                onChangeText={(text) => setText(text)}
                inputContainerStyle={styles.inputContainer}
                inputStyle={styles.input}
            />

            <Input
                placeholder="帶錯誤訊息的輸入"
                errorStyle={{ color: "red" }}
                errorMessage="請輸入有效的錯誤訊息"
                inputContainerStyle={styles.inputContainer}
                inputStyle={styles.input}
            />

            <Input
                placeholder="密碼"
                secureTextEntry={true}
                inputContainerStyle={styles.inputContainer}
                inputStyle={styles.input}
            />
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
    inputContainer: {
        borderBottomWidth: 1,
        borderBottomColor: "#ccc",
        marginBottom: 20,
        width: "100%",
    },
    input: {
        paddingLeft: 10,
        paddingRight: 10,
        height: 40,
        fontSize: 16,
        color: "#333",
    },
    icon: {
        marginRight: 10,
    },
});
