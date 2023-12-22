import React, { Fragment } from 'react';
import {Text, View, StyleSheet } from '@react-pdf/renderer';

const styles = StyleSheet.create({
    invoiceNoContainer: {
        flexDirection: 'row',
        marginTop:20,
        justifyContent: 'flex-left'
    },
    invoiceDateContainer: {
        flexDirection: 'row',
        marginTop:20,
        justifyContent: 'flex-right'
    },
    invoiceDate: {
            fontSize: 12,
            fontStyle: 'bold',
    },
    label: {
        width: 35
    },
    labelreport: {
        width: 100
    },
    
  });


  const InvoiceNo = ({invoice}) => (
        <Fragment>
            {/* <View style={styles.invoiceDateContainer}>
                <Text style={styles.label}>Date: </Text>
              <Text >{invoice.trans_date}</Text>
          </View > */}
          <View style={styles.invoiceNoContainer}>
                <Text style={styles.labelreport}>Report Issus Date:</Text>
                <Text style={styles.invoiceDate}>{invoice.report_issus_date}</Text>
            </View >
        </Fragment>
  );
  
  export default InvoiceNo
