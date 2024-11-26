import { Link } from 'expo-router';
import React from 'react';
import { StyleSheet, ScrollView, View, Text, Image, Button } from 'react-native';

const Portfolio = () => {
    return (
        <ScrollView style={styles.container}>
            {/* Header Section */}
            <View style={styles.header}>
                <Image
                    source={{ uri: 'https://via.placeholder.com/150' }}
                    style={styles.profileImage}
                />
                <Text style={styles.name}>John Doe</Text>
                <Text style={styles.title}>Software Developer</Text>

                <Link href="/profile" asChild>
                    <Button title="Go to Profile" />
                </Link>
            </View>

            {/* About Section */}
            <View style={styles.section}>
                <Text style={styles.sectionTitle}>About Me</Text>
                <Text style={styles.sectionText}>
                    Passionate software developer with experience in mobile and web development.
                    Specialized in React Native and modern JavaScript frameworks.
                </Text>
            </View>

            {/* Skills Section */}
            <View style={styles.section}>
                <Text style={styles.sectionTitle}>Skills</Text>
                <View style={styles.skillsContainer}>
                    {['React Native', 'JavaScript', 'TypeScript', 'Node.js', 'Git'].map((skill) => (
                        <View key={skill} style={styles.skillItem}>
                            <Text style={styles.skillText}>{skill}</Text>
                        </View>
                    ))}
                </View>
            </View>

            {/* Projects Section */}
            <View style={styles.section}>
                <Text style={styles.sectionTitle}>Projects</Text>
                <View style={styles.projectItem}>
                    <Text style={styles.projectTitle}>Mobile App Project</Text>
                    <Text style={styles.projectDesc}>
                        Developed a cross-platform mobile application using React Native.
                    </Text>
                </View>
                <View style={styles.projectItem}>
                    <Text style={styles.projectTitle}>Web Development Project</Text>
                    <Text style={styles.projectDesc}>
                        Created a responsive website using modern web technologies.
                    </Text>
                </View>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f5f5f5',
    },
    header: {
        alignItems: 'center',
        padding: 20,
        backgroundColor: '#fff',
    },
    profileImage: {
        width: 150,
        height: 150,
        borderRadius: 75,
        marginBottom: 15,
    },
    name: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 5,
    },
    title: {
        fontSize: 18,
        color: '#666',
    },
    section: {
        margin: 20,
        padding: 15,
        backgroundColor: '#fff',
        borderRadius: 10,
    },
    sectionTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    sectionText: {
        fontSize: 16,
        color: '#444',
        lineHeight: 24,
    },
    skillsContainer: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        gap: 10,
    },
    skillItem: {
        backgroundColor: '#e0e0e0',
        padding: 8,
        borderRadius: 5,
    },
    skillText: {
        fontSize: 14,
    },
    projectItem: {
        marginBottom: 15,
    },
    projectTitle: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 5,
    },
    projectDesc: {
        fontSize: 14,
        color: '#666',
    },
});

export default Portfolio;
