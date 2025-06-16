# Helm Deployment Script
import subprocess
import datetime

def deploy_with_helm():
    subprocess.run([
        "helm", "upgrade", "--install", "myapp", "./helm/myapp",
        "--namespace", "production",
        "--set", "image.tag=1.5.3",
        "--atomic", "--timeout", "5m"
    ])

def create_rds_snapshot():
    today = datetime.date.today().isoformat()
    snapshot_id = f"ip-db-prod-snap-{today}"
    subprocess.run([
        "aws", "rds", "create-db-snapshot",
        "--db-instance-identifier", "ip-db-prod",
        "--db-snapshot-identifier", snapshot_id
    ])

def restore_rds_snapshot(snapshot_id, new_instance_id="ip-db-restore"):
    subprocess.run([
        "aws", "rds", "restore-db-instance-from-db-snapshot",
        "--db-instance-identifier", new_instance_id,
        "--db-snapshot-identifier", snapshot_id
    ])

if _name_ == "_main_":
    # Example usage
    deploy_with_helm()
    create_rds_snapshot()
    # restore_rds_snapshot("ip-db-prod-snap-2025-06-16")