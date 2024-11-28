

// frappe.ui.form.on('Purchase Receipt', {
//     refresh: function(frm) {
//         // Make sure to use frm inside the refresh handler
//         frm.add_custom_button(__('Extract Text from Image'), function() {
//             // Debug: log frm.doc.image to the console
//             console.log(frm.doc.custom_image);
            
//             // Check if the image field has a value
//             if (frm.doc.custom_image) {
//                 frappe.call({
//                     method: 'custom_ocr_app.api.extract_text_from_temp_image',
//                     args: { file_url: frm.doc.custom_image },
//                     callback: function(r) {
//                         if (r.message.success) {
//                             frappe.msgprint(__('Extracted Text: ' + r.message.text));
//                         } else {
//                             frappe.msgprint(__('Error: ' + r.message.error));
//                         }
//                     }
//                 });
//             } else {
//                 frappe.msgprint(__('Please upload an image before extracting text.'));
//             }
//         });
//     }
// });

//in extracted data

// frappe.ui.form.on('Purchase Receipt', {
//     refresh: function (frm) {
//         // Add a custom button to trigger the text extraction
//         frm.add_custom_button(__('Extract Text from Image'), function () {
//             // Check if the image field has a value
//             if (frm.doc.custom_image) {
//                 // Call the server-side method to extract text
//                 frappe.call({
//                     method: 'custom_ocr_app.api.extract_text_from_temp_image',
//                     args: { file_url: frm.doc.custom_image },
//                     callback: function (r) {
//                         if (r.message.success) {
//                             const extractedText = r.message.text;

//                             // Set the extracted text into the custom_extracted_data field
//                             frm.set_value('custom_extracted_data', extractedText);

//                             // Display a message to the user
//                             frappe.msgprint(__('Text extracted successfully!'));

//                             // Optionally, refresh the field to update the UI
//                             frm.refresh_field('custom_extracted_data');
//                         } else {
//                             // Display error if extraction failed
//                             frappe.msgprint(__('Error: ' + r.message.error));
//                         }
//                     }
//                 });
//             } else {
//                 // Show a message if no image is uploaded
//                 frappe.msgprint(__('Please upload an image before extracting text.'));
//             }
//         });
//     }
// });


// frappe.ui.form.on('Purchase Receipt', {
//     refresh: function (frm) {
//         frm.add_custom_button(__('Extract Text for Lot No.'), function () {
//             if (frm.doc.custom_image) {
//                 // Call server-side method to extract text
//                 frappe.call({
//                     method: 'custom_ocr_app.api.extract_text_from_temp_image',
//                     args: { file_url: frm.doc.custom_image },
//                     callback: function (r) {
//                         if (r.message.success) {
//                             const extractedText = r.message.text;

//                             // Extract the 6-digit Lot No. using regex
//                             const lotNoMatch = extractedText.match(/\b\d{6}\b/);

//                             if (lotNoMatch) {
//                                 const lotNo = lotNoMatch[0]; // First match
                                
//                                 // Update all items in the child table
//                                 frm.doc.items.forEach(item => {
//                                     frappe.model.set_value(item.doctype, item.name, 'custom_lot_no', lotNo);
//                                 });

//                                 // Display success message
//                                 frappe.msgprint(__('Lot No. extracted and set: ' + lotNo));

//                                 // Refresh the child table to reflect changes
//                                 frm.refresh_field('items');
//                             } else {
//                                 frappe.msgprint(__('No 6-digit Lot No. found in the extracted text.'));
//                             }
//                         } else {
//                             frappe.msgprint(__('Error: ' + r.message.error));
//                         }
//                     }
//                 });
//             } else {
//                 frappe.msgprint(__('Please upload an image before extracting text.'));
//             }
//         });
//     }
// });




// frappe.ui.form.on('Purchase Receipt', {
//     refresh: function (frm) {
//         frm.add_custom_button(__('Extract Data from Image'), function () {
//             if (frm.doc.custom_image) {
//                 frappe.call({
//                     method: 'custom_ocr_app.api.extract_text_from_temp_image',
//                     args: { file_url: frm.doc.custom_image },
//                     callback: function (r) {
//                         if (r.message.success) {
//                             const { lot_no, reel_size, weight } = r.message;

//                             if (lot_no || reel_size || weight) {
//                                 // Populate extracted data into item-level fields
//                                 frm.doc.items.forEach(item => {
//                                     if (lot_no) frappe.model.set_value(item.doctype, item.name, 'custom_lot_no', lot_no);
//                                     if (reel_size) frappe.model.set_value(item.doctype, item.name, 'custom_reel_size', reel_size);
//                                     if (weight) frappe.model.set_value(item.doctype, item.name, 'received_qty', weight);
//                                 });

//                                 // Refresh the child table to show changes
//                                 frm.refresh_field('items');

//                                 frappe.msgprint(__('Data extracted and populated successfully!'));
//                             } else {
//                                 frappe.msgprint(__('Could not extract relevant numerical data from the image.'));
//                             }
//                         } else {
//                             frappe.msgprint(__('Error: ' + r.message.error));
//                         }
//                     }
//                 });
//             } else {
//                 frappe.msgprint(__('Please upload an image before extracting data.'));
//             }
//         });
//     }
// });




//main
// frappe.ui.form.on('Purchase Receipt', {
//     refresh: function (frm) {
//         frm.add_custom_button(__('Extract Data from Image'), function () {
//             if (frm.doc.custom_image) {
//                 frappe.call({
//                     method: 'custom_ocr_app.api.extract_text_from_temp_image',
//                     args: { file_url: frm.doc.custom_image },
//                     callback: function (r) {
//                         if (r.message.success) {
//                             const { lot_no, reel_size, reel_no , received_qty} = r.message;

//                             // Debugging: log extracted values
//                             console.log("Lot No:", lot_no);
//                             console.log("Reel Size:", reel_size);
//                             console.log("Reel No:", reel_no);
//                             console.log("received_qty", received_qty);
//                             if (lot_no || reel_size || reel_no ||  received_qty) {
//                                 frm.doc.items.forEach(item => {
//                                     if (lot_no) {
//                                         frappe.model.set_value(item.doctype, item.name, 'custom_lot_no', lot_no);
//                                     }
//                                     if (reel_size) {
//                                         frappe.model.set_value(item.doctype, item.name, 'received_qty', parseFloat(reel_size));
//                                     }
//                                     if (reel_no) {
//                                         frappe.model.set_value(item.doctype, item.name, 'custom_reel_size', reel_no);
//                                     }
//                                     if (received_qty) {
//                                         frappe.model.set_value(item.doctype, item.name, 'received_qty', received_qty);
//                                     }
//                                 });

//                                 // Refresh the child table to show changes
//                                 frm.refresh_field('items');

//                                 frappe.msgprint(__('Data extracted and populated successfully!'));
//                             } else {
//                                 frappe.msgprint(__('Could not extract relevant data from the image.'));
//                             }
//                         } else {
//                             frappe.msgprint(__('Error: ' + r.message.error));
//                         }
//                     }
//                 });
//             } else {
//                 frappe.msgprint(__('Please upload an image before extracting data.'));
//             }
//         });
//     }
// });


//all row level
frappe.ui.form.on('Purchase Receipt Item', {
    custom_extract_text_from_sticker: function(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        
        if (!row.custom_sticker_copy) {
            frappe.msgprint(__('Please upload an image before extracting data.'));
            return;
        }

        frappe.call({
            method: 'custom_ocr_app.api.extract_item_level_data',
            args: {
                docname: frm.doc.name,
                item_idx: row.idx
            },
            callback: function(r) {
                if (r.message.success) {
                    frappe.msgprint(__('Data extracted successfully!'));
                    frappe.model.set_value(cdt, cdn, 'custom_lot_no', r.message.lot_no);
                    frappe.model.set_value(cdt, cdn, 'custom_reel_size', r.message.reel_no);
                    frappe.model.set_value(cdt, cdn, 'qty', r.message.qty);


                    // Ensure UI reflects changes in dependent fields
                    frappe.model.set_value(cdt, cdn, 'accepted_qty', r.message.qty);
                    frappe.model.set_value(cdt, cdn, 'rejected_qty', 0);
                } else {
                    frappe.msgprint(__('Error: ' + r.message.error));
                }
            }
        });
    }
});


//item wise row level

// frappe.ui.form.on('Purchase Receipt', {
//     refresh: function (frm) {
//         frm.add_custom_button(__('Extract Data from Image'), function () {
//             // Call server method to process the image for the last row
//             frappe.call({
//                 method: 'custom_ocr_app.api.extract_data_and_update_last_item',
//                 args: { docname: frm.doc.name },
//                 callback: function (r) {
//                     if (r.message.success) {
//                         const { lot_no, reel_no, received_qty } = r.message;

//                         // Log extracted values for debugging
//                         console.log("Lot No:", lot_no);
//                         console.log("Reel No:", reel_no);
//                         console.log("Received Qty:", received_qty);

//                         frappe.msgprint(__('Data extracted and added to the last item successfully!'));

//                         // Refresh the child table to display updated data
//                         frm.refresh_field('items');
//                     } else {
//                         frappe.msgprint(__('Error: ' + r.message.error));
//                     }
//                 }
//             });
//         });
//     }
// });


//check box wise
// frappe.ui.form.on('Purchase Receipt', {
//     refresh: function (frm) {
//         frm.add_custom_button(__('Extract Data from Checked Box'), function () {
//             // Validate: Ensure an image is uploaded
//             if (!frm.doc.custom_image) {
//                 frappe.msgprint(__('Please upload an image first'));
//                 return;
//             }

//             // Find checked items for logging
//             const checkedItems = frm.doc.items.filter(row => row.custom_check);
//             console.log('Checked Items:', checkedItems);

//             frappe.call({
//                 method: 'custom_ocr_app.api.extract_data_for_checked_item',
//                 args: { docname: frm.doc.name },
//                 callback: function (r) {
//                     if (r.message.success) {
//                         const { lot_no, reel_no, received_qty, item_idx } = r.message;
                        
//                         // Find the item by idx and update its fields
//                         const item = frm.doc.items.find(row => row.idx === item_idx);
                        
//                         if (item) {
//                             // Use frappe.model.set_value for each field
//                             if (lot_no) {
//                                 frappe.model.set_value(item.doctype, item.name, 'custom_lot_no', lot_no);
//                             }
//                             if (reel_no) {
//                                 frappe.model.set_value(item.doctype, item.name, 'custom_reel_size', reel_no);
//                             }
//                             if (received_qty) {
//                                 frappe.model.set_value(item.doctype, item.name, 'received_qty', parseFloat(received_qty));
//                             }
                            
//                             // Refresh the form to show updated values
//                             frm.refresh_field('items');
//                             frappe.msgprint(__('Data extracted and populated successfully!'));
                            
//                             // Clear the custom_image field after extraction
//                             frm.set_value('custom_image', null);
//                         } else {
//                             frappe.msgprint(__('Error: Could not find the row to update.'));
//                         }
//                     } else {
//                         frappe.msgprint(__('Error: ' + r.message.error));
//                     }
//                 },
//                 error: function(err) {
//                     console.error('API Call Error:', err);
//                     frappe.msgprint(__('An unexpected error occurred'));
//                 }
//             });
//         });
//     }
// });





