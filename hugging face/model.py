from huggingface_hub import HfApi

api = HfApi()

api.upload_file(
    path_or_fileobj=r"C:\Users\6035s\Desktop\MLOPS\MLOPs-project-\artifact\05_22_2026_13_37_08\model_trainer\trained_model\model.pkl",
    path_in_repo="model.pkl",
    repo_id="yourusername/vehicle-ml-model",
    repo_type="model",
)

print("Upload successful")