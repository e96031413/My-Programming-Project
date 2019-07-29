import React, { Component } from 'react';

import { StyleSheet, WebView, Platform} from 'react-native';

export default class MainActivity extends Component {

      render() {

        return (

          <WebView
          style={styles.WebViewStyle}
          source={{uri: 'https://books.com.tw'}}
          javaScriptEnabled={true}
          domStorageEnabled={true}  />

        );
      }
    }



const styles = StyleSheet.create(
{

 WebViewStyle:
 {
    justifyContent: 'center',
    alignItems: 'center',
    flex:1,
    marginTop: (Platform.OS) === 'ios' ? 20 : 0
 }
});