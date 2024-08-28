import serial
import firebase_admin
from firebase_admin import credentials, firestore
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Serial Communication
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    logging.info("Serial communication initialized successfully.")
except serial.SerialException as e:
    logging.error(f"Failed to initialize serial communication: {e}")
    raise

# Initialize Firebase
try:
    cred = credentials.Certificate('path/to/your/firebase/credentials.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    logging.info("Firebase initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize Firebase: {e}")
    raise

def upload_to_firebase(data: str) -> None:
    """
    Uploads event data to Firebase Firestore.

    :param data: The event data to be uploaded.
    """
    try:
        doc_ref = db.collection(u'security_logs').document()
        doc_ref.set({
            u'event': data,
            u'timestamp': firestore.SERVER_TIMESTAMP
        })
        logging.info(f"Data uploaded to Firebase: {data}")
    except Exception as e:
        logging.error(f"Failed to upload data to Firebase: {e}")

def main() -> None:
    """
    Main function that continuously reads from the serial port
    and uploads data to Firebase Firestore.
    """
    logging.info("Starting main loop. Listening for data...")

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    logging.info(f"Received data: {line}")
                    upload_to_firebase(line)
    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Exiting...")
    except Exception as e:
        logging.error(f"An error occurred in the main loop: {e}")
    finally:
        ser.close()
        logging.info("Serial communication closed.")

if __name__ == '__main__':
    main()
