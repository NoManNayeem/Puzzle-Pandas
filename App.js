import React from 'react';
import { StyleSheet, View } from 'react-native';
import { WebView } from 'react-native-webview';

export default function App() {
  return (
    <View style={styles.container}>
      <WebView
        style={styles.webview} // Use the dedicated webview style
        source={{ uri: 'http://192.168.1.105:8000/' }}
        originWhitelist={['*']} // Allow all URLs to be loaded
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  webview: {
    width: '100%',
    height: '95%',
  },
});
