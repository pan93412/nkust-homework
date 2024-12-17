import React, { useState } from "react";
import { Button, Dialog, CheckBox, ListItem, Avatar } from "@rneui/themed";
import { View, Text, StyleSheet } from "react-native";

type DialogComponentProps = {};

const Dialogs: React.FunctionComponent<DialogComponentProps> = () => {
  const [visible1, setVisible1] = useState(false);
  const [visible2, setVisible2] = useState(false);
  const [visible3, setVisible3] = useState(false);
  const [visible4, setVisible4] = useState(false);
  const [visible5, setVisible5] = useState(false);
  const [visible6, setVisible6] = useState(false);
  const [checked, setChecked] = useState(1);

  // 控制 Dialog 開關
  const toggleDialog = (setter: React.Dispatch<React.SetStateAction<boolean>>) =>
    setter((prev) => !prev);

  const userlist = [
    {
      name: "陳小明",
      avatar_url: "https://uifaces.co/our-content/donated/XdLjsJX_.jpg",
      subtitle: "小明@example.com",
    },
    {
      name: "李大中",
      avatar_url: "https://uifaces.co/our-content/donated/KtCFjlD4.jpg",
      subtitle: "大中@example.com",
    },
    {
      name: "王佳欣",
      avatar_url:
        "https://images.unsplash.com/photo-1498529605908-f357a9af7bf5?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=047fade70e80ebb22ac8f09c04872c40",
      subtitle: "佳欣@example.com",
    },
  ];

  return (
    <View style={styles.container}>
      <View style={styles.buttonContainer}>
        <Button
          title="打開簡易對話框"
          onPress={() => toggleDialog(setVisible1)}
          buttonStyle={styles.button}
        />
        <Button
          title="多按鈕對話框"
          onPress={() => toggleDialog(setVisible2)}
          buttonStyle={styles.button}
        />
        <Button
          title="載入中對話框"
          onPress={() => toggleDialog(setVisible3)}
          buttonStyle={styles.button}
        />
        <Button
          title="無按鈕對話框"
          onPress={() => toggleDialog(setVisible4)}
          buttonStyle={styles.button}
        />
        <Button
          title="客製選擇框 1"
          onPress={() => toggleDialog(setVisible5)}
          buttonStyle={styles.button}
        />
        <Button
          title="選擇帳號對話框"
          onPress={() => toggleDialog(setVisible6)}
          buttonStyle={styles.button}
        />
      </View>

      {/* 簡易對話框 */}
      <Dialog isVisible={visible1} onBackdropPress={() => toggleDialog(setVisible1)}>
        <Dialog.Title title="提示" />
        <Text style={styles.dialogText}>這是一個簡易的對話框。</Text>
      </Dialog>

      {/* 多按鈕對話框 */}
      <Dialog isVisible={visible2} onBackdropPress={() => toggleDialog(setVisible2)}>
        <Dialog.Title title="操作確認" />
        <Text style={styles.dialogText}>請選擇您的操作：</Text>
        <Dialog.Actions>
          <Dialog.Button
            title="確認"
            onPress={() => console.log("已確認")}
          />
          <Dialog.Button
            title="取消"
            onPress={() => console.log("已取消")}
          />
        </Dialog.Actions>
      </Dialog>

      {/* 載入中對話框 */}
      <Dialog isVisible={visible3} onBackdropPress={() => toggleDialog(setVisible3)}>
        <Dialog.Loading />
      </Dialog>

      {/* 無按鈕對話框 */}
      <Dialog isVisible={visible4} onBackdropPress={() => toggleDialog(setVisible4)}>
        <Dialog.Title title="通知" />
        <Text style={styles.dialogText}>此對話框無操作按鈕。</Text>
      </Dialog>

      {/* 客製選擇框 */}
      <Dialog isVisible={visible5} onBackdropPress={() => toggleDialog(setVisible5)}>
        <Dialog.Title title="請選擇您的偏好" />
        {["選項一", "選項二", "選項三"].map((option, index) => (
          <CheckBox
            key={index}
            title={option}
            containerStyle={styles.checkbox}
            checkedIcon="dot-circle-o"
            uncheckedIcon="circle-o"
            checked={checked === index + 1}
            onPress={() => setChecked(index + 1)}
          />
        ))}
        <Dialog.Actions>
          <Dialog.Button
            title="確認"
            onPress={() => {
              console.log(`您選擇了選項 ${checked}`);
              toggleDialog(setVisible5);
            }}
          />
          <Dialog.Button title="取消" onPress={() => toggleDialog(setVisible5)} />
        </Dialog.Actions>
      </Dialog>

      {/* 帳號選擇對話框 */}
      <Dialog isVisible={visible6} onBackdropPress={() => toggleDialog(setVisible6)}>
        <Dialog.Title title="選擇您的帳號" />
        {userlist.map((user, i) => (
          <ListItem
            key={i}
            containerStyle={styles.listItem}
            onPress={() => {
              console.log(`選擇了帳號：${user.name}`);
              toggleDialog(setVisible6);
            }}
          >
            <Avatar rounded source={{ uri: user.avatar_url }} />
            <ListItem.Content>
              <ListItem.Title style={styles.userName}>
                {user.name}
              </ListItem.Title>
              <ListItem.Subtitle style={styles.userSubtitle}>
                {user.subtitle}
              </ListItem.Subtitle>
            </ListItem.Content>
          </ListItem>
        ))}
      </Dialog>
    </View>
  );
};

// 樣式設置
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    backgroundColor: "#f8f9fa",
  },
  buttonContainer: {
    margin: 20,
    alignItems: "center",
  },
  button: {
    borderRadius: 8,
    width: 240,
    marginVertical: 10,
    backgroundColor: "#4a90e2",
  },
  dialogText: {
    fontSize: 16,
    color: "#333",
    marginVertical: 10,
  },
  checkbox: {
    backgroundColor: "white",
    borderWidth: 0,
  },
  listItem: {
    marginHorizontal: -10,
    borderRadius: 10,
    marginVertical: 5,
    backgroundColor: "#f0f0f0",
  },
  userName: {
    fontWeight: "bold",
    fontSize: 16,
  },
  userSubtitle: {
    color: "gray",
    fontSize: 14,
  },
});

export default Dialogs;
