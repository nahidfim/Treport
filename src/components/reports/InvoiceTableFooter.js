import React from 'react';
import {Text, View, StyleSheet } from '@react-pdf/renderer';

const borderColor = '#90e5fc'
const styles = StyleSheet.create({
    row: {
        flexDirection: 'row',
        borderBottomColor: '#bff0fd',
        borderBottomWidth: 1,
        alignItems: 'center',
        height: 24,
        fontSize: 12,
        fontStyle: 'bold',
       
    },
    border: {
        width: '40%',
        textAlign: 'center',
        borderRightColor: borderColor,
        borderRightWidth: 1,
        paddingRight: 8,
    },
    total: {
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


const InvoiceTableFooter = ({items}) => {
    // const total = items.map(item => item.qty * item.rate)
    //     .reduce((accumulator, currentValue) => accumulator + currentValue , 0)
    return(    
        <View style={styles.row}>
            <Text style={styles.border}></Text>
           <Text style={styles.total}>Total</Text>
            <Text style={styles.totalorder}>999,999</Text>
            <Text style={styles.totalamount}>999,999,999</Text>
            {/* <Text style={styles.total}>{ Number.parseFloat(total).toFixed(2)}</Text> */}
        </View>
    )
};
  
  export default InvoiceTableFooter
