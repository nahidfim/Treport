import React from 'react';
import {Text, View, StyleSheet } from '@react-pdf/renderer';

const borderColor = '#90e5fc'
const styles = StyleSheet.create({
    container: {
        flexDirection: 'row',
        borderBottomColor: '#bff0fd',
        backgroundColor: '#bff0fd',
        borderBottomWidth: 1,
        alignItems: 'center',
        height: 24,
        textAlign: 'center',
        fontStyle: 'bold',
        flexGrow: 1,
    },
    itemcode: {
        width: '40%',
        borderRightColor: borderColor,
        borderRightWidth: 1,
    },
    itemname: {
        width: '60%',
        borderRightColor: borderColor,
        borderRightWidth: 1,
    },
    totalorder: {
        width: '60%',
        borderRightColor: borderColor,
        borderRightWidth: 1,
    },
    amount: {
        width: '60%'
    },
  });

  const InvoiceTableHeader = () => (
      <View style={styles.container}>
          <Text style={styles.itemcode}>Item Code</Text>
          <Text style={styles.itemname}>Item Name</Text>
        <Text style={styles.totalorder}>Total order</Text>
        <Text style={styles.amount}>Total Amount</Text>
    </View>
  );
  
  export default InvoiceTableHeader
