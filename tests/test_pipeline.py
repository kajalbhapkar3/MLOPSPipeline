# import subprocess

# def test_preprocessing():
#     result = subprocess.run(["python", "src/preprocessing/preprocess.py"], capture_output=True)
#     assert result.returncode == 0, f"Preprocessing failed: {result.stderr.decode()}"

# def test_training():
#     result = subprocess.run(["python", "src/training/train_model.py"], capture_output=True)
#     assert result.returncode == 0, f"Training failed: {result.stderr.decode()}"

# def test_retraining():
#     result = subprocess.run(["python", "src/retraining/retrain.py"], capture_output=True)
#     assert result.returncode == 0, f"Retraining failed: {result.stderr.decode()}"
import subprocess

def test_preprocessing():
    result = subprocess.run(["python", "src/preprocessing/preprocess.py"], capture_output=True)
    assert result.returncode == 0, f"Preprocessing failed: {result.stderr.decode()}"


def test_training():
    # Ensure preprocessing is done before training
    test_preprocessing()

    result = subprocess.run(["python", "src/training/train_model.py"], capture_output=True)
    assert result.returncode == 0, f"Training failed: {result.stderr.decode()}"


def test_retraining():
    # Ensure preprocessing is done before retraining
    test_preprocessing()

    result = subprocess.run(["python", "src/retraining/retrain.py"], capture_output=True)
    assert result.returncode == 0, f"Retraining failed: {result.stderr.decode()}"
