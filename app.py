# app.py
import argparse
from engine import run_demo
from upload_webcam import capture_webcam

def main():
    parser = argparse.ArgumentParser(description="TruthMark-Aurion Demo")
    parser.add_argument('--baseline', required=True)
    parser.add_argument('--subject', required=True)
    parser.add_argument('--baseline_txt', required=True)
    parser.add_argument('--subject_txt', required=True)
    parser.add_argument('--webcam', action='store_true')
    args = parser.parse_args()

    if args.webcam:
        capture_webcam("uploads/webcam_input.mp4")

    result = run_demo(args.baseline, args.subject, args.baseline_txt, args.subject_txt)
    print("🔍 Forensic Integrity Assessment:")
    print(result)

if __name__ == "__main__":
    main()
