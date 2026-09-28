"""
Environment and dependency verification test for ComputerVision module.
Verifies that NumPy, OpenCV, Open3D, SciPy, and Matplotlib can be imported.
"""

def test_imports():
    errors = []

    try:
        import numpy as np
        print(f"[OK] numpy: {np.__version__}")
    except Exception as e:
        errors.append(f"numpy import failed: {e}")

    try:
        import cv2
        print(f"[OK] opencv-python (cv2): {cv2.__version__}")
    except Exception as e:
        errors.append(f"opencv-python import failed: {e}")

    try:
        import open3d as o3d
        print(f"[OK] open3d: {o3d.__version__}")
    except Exception as e:
        errors.append(f"open3d import failed: {e}")

    try:
        import scipy
        print(f"[OK] scipy: {scipy.__version__}")
    except Exception as e:
        errors.append(f"scipy import failed: {e}")

    try:
        import matplotlib
        print(f"[OK] matplotlib: {matplotlib.__version__}")
    except Exception as e:
        errors.append(f"matplotlib import failed: {e}")

    if errors:
        print("\nVerification FAILED with the following errors:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\nAll dependencies imported successfully!")
        return True


if __name__ == "__main__":
    success = test_imports()
    if not success:
        exit(1)
