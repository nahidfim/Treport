import React, {Fragment} from 'react';
import {Text, View, StyleSheet } from '@react-pdf/renderer';

const borderColor = '#90e5fc'
const styles = StyleSheet.create({
    row: {
        flexDirection: 'row',
        borderBottomColor: '#bff0fd',
        borderBottomWidth: 1,
        alignItems: 'center',
        height: 24,
        fontStyle: 'bold',
    },
    itemcode: {
        width: '40%',
        textAlign: 'center',
        borderRightColor: borderColor,
        borderRightWidth: 1,
        paddingRight: 8,
    },
    itemname: {
        width: '60%',
        textAlign: 'center',
        borderRightColor: borderColor,
        borderRightWidth: 1,
        paddingLeft: 8,
    },
    totalorder: {
        width: '60%',
        borderRightColor: borderColor,
        borderRightWidth: 1,
        textAlign: 'center',
        paddingRight: 8,
    },

    totalamount: {
        width: '60%',
        borderRightColor: borderColor,
        textAlign: 'center',
        paddingRight: 8,
    },
  });


const InvoiceTableRow = ({items}) => {
    const rows = items.map( item => 
        <View style={styles.row} key={item.sno.toString()}>
            <Text style={styles.itemcode}>{item.itemcode}</Text>
            <Text style={styles.itemname}>{item.itemname}</Text>
            <Text style={styles.totalorder}>{item.totalorder}</Text>
            <Text style={styles.totalamount}>{item.totalamount}</Text>
        </View>
    )
    return (<Fragment>{rows}</Fragment> )
};
  
export default InvoiceTableRow