import React from "react";
import { View, ScrollView, StyleSheet, Image } from "react-native";
import { Text, Card, Button, Icon } from "@rneui/themed";
import { Stack } from "expo-router";

const users = [
  {
    name: "小明",
    avatar: "https://uifaces.co/our-content/donated/1H_7AxP0.jpg",
  },
  {
    name: "阿中",
    avatar:
      "https://images.pexels.com/photos/598745/pexels-photo-598745.jpeg?crop=faces&fit=crop&h=200&w=200&auto=compress&cs=tinysrgb",
  },
  {
    name: "佳欣",
    avatar: "https://uifaces.co/our-content/donated/bUkmHPKs.jpg",
  },
  {
    name: "建廷",
    avatar: "https://randomuser.me/api/portraits/men/4.jpg",
  },
  {
    name: "安迪",
    avatar: "https://uifaces.co/our-content/donated/NY9hnAbp.jpg",
  },
  {
    name: "凱蒂",
    avatar:
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgxMTc1MTYzM15BMl5BanBnXkFtZTgwNzI5NjMwOTE@._V1_UY256_CR16,0,172,256_AL_.jpg",
  },
];

const Cards: React.FunctionComponent = () => {
  return (
    <>
      <Stack.Screen options={{ title: "卡片" }} />
      <ScrollView>
        <View style={styles.container}>
          {/* 第一個卡片 - 使用者清單 */}
          <Card>
            <Card.Title>好友列表</Card.Title>
            <Card.Divider />
            {users.map((u, i) => {
              return (
                <View key={i} style={styles.user}>
                  <Image
                    style={styles.image}
                    resizeMode="cover"
                    source={{ uri: u.avatar }}
                  />
                  <Text style={styles.name}>{u.name}</Text>
                </View>
              );
            })}
          </Card>

          {/* 第二個卡片 - 字體示範 */}
          <Card containerStyle={{ marginTop: 15 }}>
            <Card.Title>字體範例</Card.Title>
            <Card.Divider />
            <Text style={styles.fonts} h1>
              標題 h1
            </Text>
            <Text style={styles.fonts} h2>
              標題 h2
            </Text>
            <Text style={styles.fonts} h3>
              標題 h3
            </Text>
            <Text style={styles.fonts} h4>
              標題 h4
            </Text>
            <Text style={styles.fonts}>這是一般文字範例。</Text>
          </Card>

          {/* 第三個卡片 - 介紹與按鈕 */}
          <Card>
            <Card.Title>你好，世界！</Card.Title>
            <Card.Divider />
            <Card.Image
              style={{ padding: 0, borderRadius: 8 }}
              source={{
                uri: "https://awildgeographer.files.wordpress.com/2015/02/john_muir_glacier.jpg",
              }}
            />
            <Text style={{ marginBottom: 10, textAlign: "center" }}>
              使用 React Native Elements 能輕鬆建構良好結構的 UI 元件。
            </Text>
            <Button
              icon={
                <Icon
                  name="visibility"
                  color="#ffffff"
                  iconStyle={{ marginRight: 10 }}
                />
              }
              buttonStyle={styles.button}
              title="查看詳情"
            />
          </Card>
        </View>
      </ScrollView>
    </>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f4f4f4",
    paddingBottom: 10,
  },
  fonts: {
    marginBottom: 8,
    fontFamily: "PingFang TC", // 適合繁體中文的字體
  },
  user: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 8,
  },
  image: {
    width: 50,
    height: 50,
    borderRadius: 25,
    marginRight: 12,
  },
  name: {
    fontSize: 18,
    color: "#333",
    fontWeight: "500",
  },
  button: {
    borderRadius: 8,
    backgroundColor: "#4a90e2",
    marginLeft: 0,
    marginRight: 0,
    marginBottom: 0,
  },
});

export default Cards;
