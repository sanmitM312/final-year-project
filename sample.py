import argparse
import helper

#hardcoded for 2 nodes only as of now
hp = helper.Helper(2, 100, 1000, 50, 50)
hp.generate_doctor_data()
hp.generate_patient_data()