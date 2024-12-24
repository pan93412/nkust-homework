import React from "react";
import { View, Text } from "react-native";
import { FAB } from "@rneui/themed";

export default function FabPage() {
  const [visible, setVisible] = React.useState(true);

  return (
    <>
      <View
        style={{
          alignItems: "center",
          paddingVertical: 10,
          flexGrow: 1,
          backgroundColor: "#f0f0f0",
        }}
      >
        <Text style={{ color: "#397af8", paddingVertical: 10, fontSize: 18 }}>
          小尺寸
        </Text>
        <FAB
          loading
          visible={visible}
          icon={{ name: "add", color: "white" }}
          size="small"
        />
        <Text style={{ color: "#397af8", paddingVertical: 10, fontSize: 18 }}>
          大尺寸
        </Text>
        <FAB
          visible={visible}
          icon={{ name: "add", color: "white" }}
          color="green"
        />
        <Text style={{ color: "#397af8", paddingVertical: 10, fontSize: 18 }}>
          主要顏色
        </Text>
        <FAB
          visible={visible}
          title="導航"
          upperCase
          icon={{ name: "place", color: "white" }}
        />

        <Text style={{ color: "#397af8", paddingVertical: 10, fontSize: 18 }}>
          停用
        </Text>

        <FAB
          visible={visible}
          disabled
          title="擴展"
          icon={{
            name: "place",
            color: "white",
          }}
        />
        <FAB
          visible={visible}
          onPress={() => setVisible(!visible)}
          placement="right"
          title="隱藏"
          icon={{ name: "delete", color: "white" }}
          color="red"
        />
        <FAB
          visible={!visible}
          onPress={() => setVisible(!visible)}
          placement="left"
          title="顯示"
          icon={{ name: "edit", color: "white" }}
          color="green"
        />
      </View>
    </>
  );
}
