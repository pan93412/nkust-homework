import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { Drawer } from 'expo-router/drawer';
import { Stack } from 'expo-router';

export default function Layout() {
  return (
    <GestureHandlerRootView style={{ flex: 1 }}>
      <Stack>
        <Stack.Screen
          name="index" // This is the name of the page and must match the url from root
          options={{
            title: 'Overview',
          }}
        />
        <Stack.Screen
          name="demo" // This is the name of the page and must match the url from root
          options={{
            presentation: 'modal',
          }}
        />
      </Stack>
    </GestureHandlerRootView>
  );
}
