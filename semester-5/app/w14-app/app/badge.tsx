import React from 'react';
import { Text, View, ScrollView, StyleSheet } from 'react-native';
import { Avatar, Badge, Icon, withBadge } from '@rneui/themed';

const BadgedIcon = withBadge(15)(Icon);

const BadgeComponent = () => {
return (
    <>
        <ScrollView style={styles.container}>
            <Text style={styles.subHeader}>標準徽章</Text>
            <View
                style={{
                    flexDirection: 'row',
                    justifyContent: 'space-around',
                    marginTop: 20,
                    marginBottom: 40,
                }}
            >
                <Badge value="3" status="success" />
                <Badge value="99+" status="error" />
                <Badge value="500" status="primary" />
                <Badge value="10" status="warning" />
            </View>
            <Text style={styles.subHeader}>迷你徽章</Text>
            <Text style={styles.description}>
                這種類型的徽章在未提供數值時顯示。這種形式適合用於顯示狀態。
            </Text>
            <View
                style={{
                    flexDirection: 'row',
                    justifyContent: 'space-around',
                    marginTop: 20,
                    marginBottom: 20,
                }}
            >
                <Badge status="success" />
                <Badge status="error" />
                <Badge status="primary" />
                <Badge status="warning" />
            </View>
            <View
                style={{
                    flexDirection: 'row',
                    justifyContent: 'space-around',
                    marginBottom: 20,
                }}
            >
                <Text style={styles.statusText}>成功</Text>
                <Text style={styles.statusText}>錯誤</Text>
                <Text style={styles.statusText}>主要</Text>
                <Text style={styles.statusText}>警告</Text>
            </View>

            <Text style={styles.subHeader}>指示器徽章</Text>
            <View
                style={{
                    flexDirection: 'row',
                    justifyContent: 'space-around',
                    marginTop: 20,
                    marginBottom: 40,
                }}
            >
                <View>
                    <Avatar
                        rounded
                        source={{ uri: 'https://randomuser.me/api/portraits/men/41.jpg' }}
                        size="medium"
                    />
                    <Badge
                        status="success"
                        containerStyle={{ position: 'absolute', top: 5, left: 40 }}
                    />
                </View>
                <BadgedIcon type="ionicon" name="ios-chatbubbles" />
                <View>
                    <Avatar
                        rounded
                        source={{
                            uri: 'https://randomuser.me/api/portraits/women/40.jpg',
                        }}
                        size="large"
                    />
                    <Badge
                        status="primary"
                        value={10}
                        containerStyle={{ position: 'absolute', top: 5, left: 60 }}
                    />
                </View>
            </View>
        </ScrollView>
    </>
);
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
    },
    subHeader: {
        backgroundColor: "#1976d2",
        color: "white",
        textAlign: "center",
        paddingVertical: 8,
        marginBottom: 15,
        fontSize: 16,
        fontWeight: 'bold',
        borderRadius: 5,
    },
    description: {
        textAlign: "center",
        paddingHorizontal: 20,
        color: '#666',
        fontSize: 14,
        lineHeight: 20,
    },
    statusText: {
        color: '#1976d2',
        paddingVertical: 10,
        fontSize: 14,
        fontWeight: '500',
    }
})

export default BadgeComponent;
