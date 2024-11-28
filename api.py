
# import frappe
# import pytesseract
# from PIL import Image
# from frappe.utils.file_manager import get_file_path

# @frappe.whitelist()
# def extract_text_from_temp_image(file_url):
#     try:
#         # Get the file path of the uploaded image
#         file_path = get_file_path(file_url)

#         # Open the image and extract text using Tesseract
#         image = Image.open(file_path)
#         extracted_text = pytesseract.image_to_string(image)

#         # Return extracted text without saving it to the document
#         return {"success": True, "text": extracted_text}
#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "OCR Extraction Error")
#         return {"success": False, "error": str(e)}


# import pytesseract
# import re
# import frappe
# from frappe.utils.file_manager import get_file_path

# @frappe.whitelist()
# def extract_text_from_temp_image(file_url):
#     try:
#         # Get the file path
#         file_path = get_file_path(file_url)
        
#         # Extract text using pytesseract
#         extracted_text = pytesseract.image_to_string(file_path)
        
#         # Extract all integer values
#         all_numbers = re.findall(r'\d+', extracted_text)  # Extract all numbers from the text
        
#         # # Assign numbers based on position/order (example logic, can be adjusted)
#         # lot_no = all_numbers[0] if len(all_numbers) > 0 else None  # First number as Lot No.
#         # reel_size = None
#         # weight = None
#          # Extract Lot No. (either 4-digit or 6-digit)
#         lot_no_match = re.search(r"Lot\s*No\.?\s*:\s*(\d{4,6})", extracted_text, re.IGNORECASE)
#         lot_no = lot_no_match.group(1) if lot_no_match else None


#         # Search for reel size in MM format
#         reel_size_match = re.search(r"(\d+)\s*MM", extracted_text, re.IGNORECASE)
#         if reel_size_match:
#             reel_size = reel_size_match.group(1)  # Extract reel size in MM

#         # Assign the last number as weight if it exists
#         if len(all_numbers) > 1:
#             weight = all_numbers[-1]  # Last number as Weight
        
#         return {
#             "success": True,
#             "lot_no": lot_no,
#             "reel_size": reel_size,
#             "weight": weight,
#             "raw_text": extracted_text,  # Include raw text for debugging
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}


#main 
# import pytesseract
# import re
# import frappe
# from frappe.utils.file_manager import get_file_path

# @frappe.whitelist()
# def extract_text_from_temp_image(file_url):
#     try:
#         # Get the file path
#         file_path = get_file_path(file_url)
        
#         # Extract text using pytesseract
#         extracted_text = pytesseract.image_to_string(file_path)

#         # Extract all integer values
#         all_numbers = re.findall(r'\d+', extracted_text)  # Extract all numbers from the text
        
        
#         # Debugging: include raw extracted text
#         raw_text = extracted_text

#         # Extract Lot No. (either 4-digit or 6-digit)
#         lot_no_match = re.search(r"Lot\s*No\.?\s*:\s*(\d{4,6})", extracted_text, re.IGNORECASE)
#         lot_no = lot_no_match.group(1) if lot_no_match else None

#         # Extract Reel Size in MM using "Reel Size" keyword
#         reel_size_match = re.search(r"Reel\s*Size\s*:\s*(\d+)", extracted_text, re.IGNORECASE)
#         reel_size = reel_size_match.group(1) if reel_size_match else None 

#           # Extract Reel No. (including spaces within numbers)
#         reel_no_match = re.search(r"Reel\s*No\.?\s*:\s*([\d\s]+)", extracted_text, re.IGNORECASE)
#         reel_no = reel_no_match.group(1).replace(" ", "") if reel_no_match else None


#          # Assign the last number as weight if it exists
#         if len(all_numbers) > 1:
#             weight = all_numbers[-1]  # Last number as Weight


# # Extract Reel No. (including spaces within numbers)
#         reel_no_match = re.search(r"Reel\s*No\.?\s*:\s*([\d\s]+)", extracted_text, re.IGNORECASE)
#         reel_no = reel_no_match.group(1).replace(" ", "") if reel_no_match else None
#         return {
#             "success": True,
#             "lot_no": lot_no,
#             "reel_size": reel_size,
#             "reel_no": reel_no,
#             "received_qty":weight,
#             "raw_text": raw_text,  # Include raw text for debugging
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}

#all row level
import pytesseract
import re
import frappe
from frappe.utils.file_manager import get_file_path

@frappe.whitelist()
def extract_item_level_data(docname, item_idx):
    try:
        # Fetch the Purchase Receipt document
        doc = frappe.get_doc("Purchase Receipt", docname)
        item = next((i for i in doc.items if i.idx == int(item_idx)), None)
        
        if not item:
            return {"success": False, "error": "Item not found."}

        # Get the file URL for the image
        file_url = item.custom_sticker_copy
        if not file_url:
            return {"success": False, "error": "Please upload an image before extracting data."}

        # Get the file path
        file_path = get_file_path(file_url)
        
        # Extract text using pytesseract
        extracted_text = pytesseract.image_to_string(file_path)
        raw_text = extracted_text

        # Extract Lot No. (either 4-digit or 6-digit)
        lot_no_match = re.search(r"Lot\s*No\.?\s*:\s*(\d{4,6})", extracted_text, re.IGNORECASE)
        lot_no = lot_no_match.group(1) if lot_no_match else None

        # Extract Reel No. (including spaces within numbers)
        reel_no_match = re.search(r"Reel\s*No\.?\s*:\s*([\d\s]+)", extracted_text, re.IGNORECASE)
        reel_no = reel_no_match.group(1).replace(" ", "") if reel_no_match else None
        

        # Extract Weight (Wt in Kgs)
        all_numbers = re.findall(r'\d+', extracted_text)  # Extract all numbers from the text
        if len(all_numbers) > 1:
            weight = all_numbers[-1]  # Last number as Weight

    

        # Update the item fields
        item.custom_lot_no = lot_no
        item.custom_reel_size = reel_no
        item.qty = weight
        
          # Ensure Accepted + Rejected Qty matches Received Qty
        item.received_qty = weight  # Assume full acceptance, adjust as needed
        item.rejected_qty = 0  # No rejection, adjust as needed
        doc.save()
        
        return {
            "success": True,
            "lot_no": lot_no,
            "reel_no": reel_no,
            "qty": weight,
            "raw_text": raw_text,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


# #item wise
# import pytesseract
# import re
# import frappe
# from frappe.utils.file_manager import get_file_path

# @frappe.whitelist()
# def extract_data_and_update_last_item(docname):
#     try:
#         # Fetch the Purchase Receipt document
#         doc = frappe.get_doc("Purchase Receipt", docname)

#         # Ensure there are items in the table
#         if not doc.items:
#             return {"success": False, "error": "No items found in the table."}

#         # Target the last item in the table
#         last_item = doc.items[-1]

#         # Get the file URL for the image
#         file_url = last_item.custom_sticker_copy
#         if not file_url:
#             return {"success": False, "error": "Please upload an image for the last row before extracting data."}

#         # Get the file path
#         file_path = get_file_path(file_url)

#         # Extract text using pytesseract
#         extracted_text = pytesseract.image_to_string(file_path)
#         raw_text = extracted_text

#         # Extract Lot No. (4 or 6 digits)
#         lot_no_match = re.search(r"Lot\s*No\.?\s*:\s*(\d{4,6})", extracted_text, re.IGNORECASE)
#         lot_no = lot_no_match.group(1) if lot_no_match else None

#         # Extract Reel No. (handle spaces in Reel No.)
#         reel_no_match = re.search(r"Reel\s*No\.?\s*:\s*([\d\s]+)", extracted_text, re.IGNORECASE)
#         reel_no = reel_no_match.group(1).replace(" ", "") if reel_no_match else None

#         # Extract Weight (Last number in text)
#         all_numbers = re.findall(r'\d+', extracted_text)  # Extract all numbers
#         weight = all_numbers[-1] if len(all_numbers) > 0 else None  # Last number is Weight

#         # Update the last item row with extracted data
#         last_item.custom_lot_no = lot_no
#         last_item.custom_reel_size = reel_no
#         last_item.received_qty = weight

#         # Clear the image field for the last item
#         last_item.custom_sticker_copy = None

#         # Save the document
#         doc.save()

#         return {
#             "success": True,
#             "lot_no": lot_no,
#             "reel_no": reel_no,
#             "received_qty": weight,
#             "raw_text": raw_text,
#         }
#     except Exception as e:
#         return {"success": False, "error": str(e)}


#check box 

# import os
# import pytesseract
# import re
# import frappe
# from frappe.utils.file_manager import get_file_path

# @frappe.whitelist()
# def extract_data_for_checked_item(docname):
    try:
        # Fetch the Purchase Receipt document
        doc = frappe.get_doc("Purchase Receipt", docname)
        
        # Debug: Log all items and their custom_check status
        for item in doc.items:
            frappe.logger().info(f"Item {item.idx}: custom_check = {item.custom_check}")
        
        # Ensure an image is uploaded at the document level
        file_url = doc.custom_image
        if not file_url:
            return {"success": False, "error": "Please upload an image in the custom_image field before extracting data."}
        
        # Verify the file path
        file_path = get_file_path(file_url)
        if not os.path.exists(file_path):
            return {"success": False, "error": f"File not found at path: {file_path}. Please save the document after uploading the image."}
        
        # Find ALL checked items (in case multiple are checked)
        checked_items = [item for item in doc.items if item.custom_check]
        
        if not checked_items:
            return {"success": False, "error": "No row is checked. Please check a row using the custom checkbox before extracting data."}
        
        # If multiple items are checked, use the first one
        checked_item = checked_items[0]
        
        # Extract text using pytesseract
        extracted_text = pytesseract.image_to_string(file_path)
        raw_text = extracted_text
        
        # More flexible regex for extraction
        lot_no_match = re.search(r"(?:Lot\s*(?:No\.?)?)\s*:?\s*(\d{4,6})", extracted_text, re.IGNORECASE)
        lot_no = lot_no_match.group(1) if lot_no_match else None
        
        reel_no_match = re.search(r"(?:Reel\s*(?:No\.?)?)\s*:?\s*([\d\s]+)", extracted_text, re.IGNORECASE)
        reel_no = reel_no_match.group(1).replace(" ", "") if reel_no_match else None
        
        # More robust weight extraction
        weight_matches = re.findall(r'(\d+(?:\.\d+)?)\s*(?:kg|kgs|kg\.|g|gm)?', extracted_text, re.IGNORECASE)
        weight = weight_matches[-1] if weight_matches else None
        
        # Log extracted data for debugging
        frappe.logger().info(f"Extracted Data: Lot No: {lot_no}, Reel No: {reel_no}, Weight: {weight}")
        
        # Clear the custom_image field after processing
        doc.custom_image = None
        doc.save()
        
        return {
            "success": True,
            "lot_no": lot_no,
            "reel_no": reel_no,
            "received_qty": weight,
            "item_idx": checked_item.idx,
            "raw_text": raw_text,
        }
    except Exception as e:
        frappe.logger().error(f"Error extracting data: {str(e)}")
        return {"success": False, "error": str(e)}